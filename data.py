import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def config_page_layout():
    """Configura el layout de Streamlit para utilizar toda la pantalla y
    añade CSS personalizado para ajustar el espaciado entre columnas."""
    st.set_page_config(layout="wide")
    st.markdown("""
        <style>
        .block-container>div {
            padding: 10px;  /* Espacio interno dentro de cada bloque */
        }
        .css-18e3th9 {
            padding-right: 20px;  /* Espacio entre columnas */
        }
        </style>
        """, unsafe_allow_html=True)

def load_data():
    """Carga el dataset desde una URL y retorna un DataFrame."""
    ruta = ('https://docs.google.com/spreadsheets/d/e/2PACX-1vR9IGQhDWN0qA-jon8x0cUTap8IxvrdzGjF_kN98upNSQDeDJsI6UkpyGYOtPV18cbSB-rQzU62btO6/pub?gid=446676900&single=true&output=csv')
    return pd.read_csv(ruta)

def display_company_states(df):
    """Muestra la cantidad de empresas por estado en una columna de Streamlit."""
    estados = df['ESTMATRICULA'].value_counts()
    with state_col:
        st.subheader("Empresas por estado:")
        st.text(estados.to_string())

def plot_companies_by_municipality(df):
    """Genera y muestra un gráfico de barras de empresas por municipio."""
    municipios = df['MUNCOMERCIAL'].unique()
    empresas_municipio = {mun: df[df["MUNCOMERCIAL"] == mun].shape[0] 
                          for mun in municipios}
    fig, ax = plt.subplots()
    ax.bar(empresas_municipio.keys(), empresas_municipio.values())
    ax.set_xlabel("Municipio")
    ax.set_ylabel("Número de empresas")
    ax.set_title("Empresas por municipio")
    plt.xticks(rotation=90)
    st.pyplot(fig)

def plot_companies_by_employee_range(df):
    """Genera y muestra un gráfico de barras de empresas por rango de empleados."""
    rangos = ["0", "1-5", "6-10", "11-15", "16-20", "21-25", 
              "26-30", "31-35", "36-40", "41-45", "46-50"]
    contadores_rango = {rango: 0 for rango in rangos}
    for empleados in df["Empleados"]:
        for rango in rangos:
            if rango == "0" and empleados == 0:
                contadores_rango[rango] += 1
            elif "-" in rango and int(rango.split('-')[0]) <= empleados <= int(rango.split('-')[1]):
                contadores_rango[rango] += 1
                break
    empresas_por_rango_df = pd.DataFrame(list(contadores_rango.items()),
                                         columns=['Rango de empleados', 'Cantidad de empresas'])
    fig, ax = plt.subplots()
    ax.bar(empresas_por_rango_df['Rango de empleados'],
           empresas_por_rango_df['Cantidad de empresas'])
    ax.set_xlabel("Rango de empleados")
    ax.set_ylabel("Cantidad de empresas")
    ax.set_title("Distribución de empresas por rango de empleados")
    plt.xticks(rotation=45)
    st.pyplot(fig)

def main():
    """Función principal que ejecuta todas las funciones configuradas."""
    config_page_layout()
    df = load_data()
    global title_col, state_col
    title_col, state_col = st.columns([3, 2])
    with title_col:
        st.title("Empresas registradas Cámara de Comercio de La Dorada")
    display_company_states(df)
    left_column, right_column = st.columns([1, 1], gap="large")
    with left_column:
        plot_companies_by_municipality(df)
    with right_column:
        plot_companies_by_employee_range(df)
    la_dorada_df = df[(df["MUNCOMERCIAL"] == "LA DORADA") & 
                      (df["Empleados"] == 0) & 
                      (df["ESTMATRICULA"] == "Activa")]
    nombres_empresas = la_dorada_df["RAZON SOCIAL"].tolist()
    st.subheader("Empresas de La Dorada con 0 empleados y Matricula activa")
    st.write(nombres_empresas)

if __name__ == "__main__":
    main()
