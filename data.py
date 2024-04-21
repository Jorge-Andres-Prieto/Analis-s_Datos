import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# **Definición de constantes**

# Ruta del dataset CSV
RUTA_REGISTRADAS = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vR9IGQhDWN0qA-jon8x0cUTap8IxvrdzGjF_kN98upNSQDeDJsI6UkpyGYOtPV18cbSB-rQzU62btO6/pub?gid=446676900&single=true&output=csv'

# **Carga del dataset**

# Se lee el dataset CSV y se guarda en un DataFrame
registradas_df = pd.read_csv(RUTA_REGISTRADAS)

# **Análisis por estado de la empresa**

# Se obtienen los valores únicos de la columna "ESTMATRICULA"
estados = registradas_df['ESTMATRICULA'].value_counts()

# Se muestra la información de las empresas por estado en Streamlit
st.subheader("Empresas por estado:")
st.text(estados.to_string())  # Utiliza st.text para textos largos o st.write para objetos en general

# **Análisis por municipio**

# Se obtienen los municipios únicos
municipios = registradas_df.MUNCOMERCIAL.unique()

# Diccionario para almacenar la cantidad de empresas por municipio
empresas_municipio = {}
for municipio in municipios:
    # Se filtra el DataFrame por municipio
    empresas_municipio[municipio] = registradas_df[registradas_df["MUNCOMERCIAL"] == municipio].shape[0]

# Se crea un gráfico de barras con la cantidad de empresas por municipio
fig, ax = plt.subplots()
ax.bar(empresas_municipio.keys(), empresas_municipio.values())
ax.set_xlabel("Municipio")
ax.set_ylabel("Número de empresas")
ax.set_title("Empresas por municipio")
plt.xticks(rotation=90)
st.pyplot(fig)  # Muestra el gráfico en Streamlit

# **Análisis por rango de empleados**

# Definición de los rangos de empleados
rangos = ["1-5", "6-10", "11-15", "16-20", "21-25", "26-30", "31-35", "36-40", "41-45", "46-50"]
contadores_rango = {rango: 0 for rango in rangos}

# Se recorren las empresas y se actualiza el contador del rango correspondiente
for empleados in registradas_df["Empleados"]:
    for rango in rangos:
        if int(rango.split('-')[0]) <= empleados <= int(rango.split('-')[1]):
            contadores_rango[rango] += 1
            break

# Convertir el diccionario a un DataFrame
empresas_por_rango_df = pd.DataFrame(list(contadores_rango.items()), columns=['Rango de empleados', 'Cantidad de empresas'])

# Se crea un gráfico de barras con la cantidad de empresas por rango de empleados
fig, ax = plt.subplots()
ax.bar(empresas_por_rango_df['Rango de empleados'], empresas_por_rango_df['Cantidad de empresas'])
ax.set_xlabel("Rango de empleados")
ax.set_ylabel("Cantidad de empresas")
ax.set_title("Empresas por rango de empleados")
plt.xticks(rotation=45)
st.pyplot(fig)

# **Análisis de empresas de La Dorada con 0 empleados y Matricula activa**

# Se filtra el DataFrame por La Dorada, 0 empleados y Matricula activa
la_dorada_df = registradas_df[(registradas_df["MUNCOMERCIAL"] == "LA DORADA") & (registradas_df["Empleados"] == 0) & (registradas_df["ESTMATRICULA"] == "Activa")]

# Se obtienen los nombres de las empresas
nombres_empresas = la_dorada_df["RAZON SOCIAL"].tolist()

# Se imprime la información de las empresas en Streamlit
st.subheader("Empresas de La Dorada con 0 empleados y Matricula activa:")
st.write(nombres_empresas)  # Utiliza st.write para listas y objetos
