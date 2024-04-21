"""
# Importación de librerías
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# **Definición de constantes**

# Ruta del dataset CSV
RUTA_REGISTRADAS = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vR9IGQhDWN0qA-jon8x0cUTap8IxvrdzGjF_kN98upNSQDeDJsI6UkpyGYOtPV18cbSB-rQzU62btO6/pub?gid=446676900&single=true&output=csv'

# **Carga del dataset**

# Se lee el dataset CSV y se guarda en un DataFrame
registradas_df = pd.read_csv(RUTA_REGISTRADAS)

# **Análisis por estado de la empresa**

# Se obtienen los valores únicos de la columna "ESTMATRICULA"
estados = registradas_df['ESTMATRICULA'].value_counts()

# Se imprime la información de las empresas por estado
print("Empresas por estado:")
print(estados.to_string())  # Imprime como string para mejor visualización

# **Análisis por municipio**

# Se obtienen los municipios únicos
municipios = registradas_df.MUNCOMERCIAL.unique()

# Diccionario para almacenar la cantidad de empresas por municipio
empresas_municipio = {}

# Se recorren los municipios
for municipio in municipios:
    # Se filtra el DataFrame por municipio
    empresas_municipio[municipio] = registradas_df[registradas_df["MUNCOMERCIAL"] == municipio].shape[0]

# Se crea un gráfico de barras con la cantidad de empresas por municipio
plt.bar(empresas_municipio.keys(), empresas_municipio.values())
plt.xlabel("Municipio")
plt.ylabel("Número de empresas")
plt.title("Empresas por municipio")
plt.xticks(rotation=90)
plt.show()

print(" ")

# **Análisis por rango de empleados**

# Definición de los rangos de empleados
RANGO_1_5 = 0
RANGO_6_10 = 0
RANGO_11_15 = 0
RANGO_16_20 = 0
RANGO_21_25 = 0
RANGO_26_30 = 0
RANGO_31_35 = 0
RANGO_36_40 = 0
RANGO_41_45 = 0
RANGO_46_50 = 0

# Se recorren las empresas y se actualiza el contador del rango correspondiente
for i in range(registradas_df.shape[0]):
    empleados = registradas_df.loc[i, "Empleados"]
    if empleados <= 5:
        RANGO_1_5 += 1
    elif empleados <= 10:
        RANGO_6_10 += 1
    elif empleados <= 15:
        RANGO_11_15 += 1
    elif empleados <= 20:
        RANGO_16_20 += 1
    elif empleados <= 25:
        RANGO_21_25 += 1
    elif empleados <= 30:
        RANGO_26_30 += 1
    elif empleados <= 35:
        RANGO_31_35 += 1
    elif empleados <= 40:
        RANGO_36_40 += 1
    elif empleados <= 45:
        RANGO_41_45 += 1
    elif empleados <= 50:
        RANGO_46_50 += 1

# Diccionario para almacenar los contadores por rango de empleados
contadores_rango = {
    "1-5":RANGO_1_5,
    "6-10":RANGO_6_10,
    "11-15":RANGO_11_15,
    "16-20":RANGO_16_20,
    "21-25":RANGO_21_25,
    "26-30":RANGO_26_30,
    "31-35":RANGO_31_35,
    "36-40":RANGO_36_40,
    "41-45":RANGO_41_45,
    "46-50":RANGO_46_50,
}

# Convertir el diccionario a un DataFrame
empresas_por_rango_df = pd.DataFrame.from_dict(contadores_rango, orient='index', columns=['Cantidad de empresas'])

# Se crea un gráfico de barras con la cantidad de empresas por rango de empleados
plt.bar(empresas_por_rango_df.index, empresas_por_rango_df['Cantidad de empresas'])
plt.xlabel("Rango de empleados")
plt.ylabel("Cantidad de empresas")
plt.title("Empresas por rango de empleados")
plt.xticks(rotation=45)
plt.show()

# **Análisis de empresas de La Dorada con 0 empleados y Matricula activa**

# Se filtra el DataFrame por La Dorada, 0 empleados y Matricula activa
la_dorada_df = registradas_df[(registradas_df["MUNCOMERCIAL"] == "LA DORADA") & (registradas_df["Empleados"] == 0) & (registradas_df["ESTMATRICULA"] == "Activa")]

# Se obtienen los nombres de las empresas
nombres_empresas = la_dorada_df["RAZON SOCIAL"].tolist()

# Se imprime la información de las empresas
#print("Empresas de La Dorada con 0 empleados y Matricula activa:")
#for nombre in nombres_empresas:
#    print(nombre)