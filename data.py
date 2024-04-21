import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configurar el layout para que use toda la pantalla
st.set_page_config(layout="wide")

# Título centralizado
st.title("Empresas registradas Cámara de Comercio de La Dorada")

# **Definición de constantes**

# Ruta del dataset CSV
RUTA_REGISTRADAS = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vR9IGQhDWN0qA-jon8x0cUTap8IxvrdzGjF_kN98upNSQDeDJsI6UkpyGYOtPV18cbSB-rQzU62btO6/pub?gid=446676900&single=true&output=csv'

# **Carga del dataset**

# Se lee el dataset CSV y se guarda en un DataFrame
registradas_df = pd.read_csv(RUTA_REGISTRADAS)

# **Análisis por estado de la empresa**

# Se obtienen los valores únicos de la columna "ESTMATRICULA"
estados = registradas_df['ESTMATRICULA'].value_counts()

# Crear columnas para centrar la información de los estados
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.subheader("Empresas por estado:")
    st.text(estados.to_string())

# **Análisis por municipio y por rango de empleados**

# Crear dos columnas para los gráficos de municipio y rango de empleados
left_column, right_column = st.columns(2)

# Gráfico de empresas por municipio
with left_column:
    st.subheader("Empresas por municipio")
    municipios = registradas_df['MUNCOMERCIAL'].unique()
    empresas_municipio = {municipio: registradas_df[registradas_df["MUNCOMERCIAL"] == municipio].shape[0] for municipio in municipios}
    fig, ax = plt.subplots()
    ax.bar(empresas_municipio.keys(), empresas_municipio.values())
    ax.set_xlabel("Municipio")
    ax.set_ylabel("Número de empresas")
    ax.set_title("Empresas por municipio")
    plt.xticks(rotation=90)
    st.pyplot(fig)

# Gráfico de empresas por rango de empleados
with right_column:
    st.subheader("Empresas por rango de empleados")
    # Agregar rango de 0 empleados
    rangos = ["0", "1-5", "6-10", "11-15", "16-20", "21-25", "26-30", "31-35", "36-40", "41-45", "46-50"]
    contadores_rango = {rango: 0 for rango in rangos}
    for empleados in registradas_df["Empleados"]:
        for rango in rangos:
            if rango == "0" and empleados == 0:
                contadores_rango[rango] += 1
            elif "-" in rango and int(rango.split('-')[0]) <= empleados <= int(rango.split('-')[1]):
                contadores_rango[rango] += 1
                break
    empresas_por_rango_df = pd.DataFrame(list(contadores_rango.items()), columns=['Rango de empleados', 'Cantidad de empresas'])
    fig, ax = plt.subplots()
    ax.bar(empresas_por_rango_df['Rango de empleados'], empresas_por_rango_df['Cantidad de empresas'])
    ax.set_xlabel("Rango de empleados")
    ax.set_ylabel("Cantidad de empresas")
    ax.set_title("Distribución de empresas por rango de empleados")
    plt.xticks(rotation=45)
    st.pyplot(fig)

# **Análisis de empresas de La Dorada con 0 empleados y Matricula activa**
la_dorada_df = registradas_df[(registradas_df["MUNCOMERCIAL"] == "LA DORADA") & (registradas_df["Empleados"] == 0) & (registradas_df["ESTMATRICULA"] == "Activa")]
nombres_empresas = la_dorada_df["RAZON SOCIAL"].tolist()
st.subheader("Empresas de La Dorada con 0 empleados y Matricula activa")
st.write(nombres_empresas)
