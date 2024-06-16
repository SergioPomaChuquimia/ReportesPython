import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Título de la aplicación
st.title('Análisis Integral de Datos de Río 2016')

# Subtítulo y carga de datos de Río 2016
st.subheader('Visualización de Datos de Río 2016')
data_path = 'athlete_events.csv'
data = pd.read_csv(data_path)

# Filtramos los datos para incluir solo Río 2016
rio_data = data[data['Games'] == '2016 Summer']
if not rio_data.empty:
    st.write("Aquí se muestra el dataset cargado de Río 2016:")
    st.dataframe(rio_data)
else:
    st.error("No se encontraron datos para Río 2016.")

# Función para crear un gráfico de barras de los países con más medallas
def create_medal_chart(data):
    medal_data = data.dropna(subset=['Medal'])
    medal_counts = medal_data['NOC'].value_counts().head(10)  # Top 10 países
    fig, ax = plt.subplots()
    medal_counts.plot(kind='bar', ax=ax, color='skyblue')
    ax.set_title('Top 10 Países con Más Medallas en Río 2016')
    ax.set_xlabel('País')
    ax.set_ylabel('Número de Medallas')
    st.pyplot(fig)

# Verificación de que los datos han sido cargados correctamente para la generación del gráfico de barras
if 'rio_data' in locals():
    st.subheader('Países con Más Medallas en Río 2016')
    create_medal_chart(rio_data)
else:
    st.error("No se ha cargado el dataset de Río 2016 para la generación del gráfico de barras.")

# Función para crear un heatmap de correlación
# Función para crear un heatmap de correlación
# Función para crear un heatmap de correlación
def create_heatmap(data):
    numeric_cols = data.select_dtypes(include=[np.number]).columns
    # Filtrar los datos para incluir sólo las columnas numéricas
    data = data[numeric_cols]  # Usar 'numeric_cols' en lugar de 'numeric_data'
    correlation_matrix = data.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5, ax=ax)
    ax.set_title('Heatmap de Correlación')
    ax.set_xlabel('Variables')
    ax.set_ylabel('Variables')
    st.pyplot(fig)



# Verificación de que los datos han sido cargados correctamente para la generación del heatmap
if 'rio_data' in locals():
    st.subheader('Heatmap de Correlación')
    create_heatmap(rio_data)
else:
    st.error("No se ha cargado el dataset de Río 2016 para la generación de heatmap.")
