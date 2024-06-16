import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Título de la aplicación
st.title('Análisis Integral de Datos de Tokyo 2021')

# Subtítulo y carga de datos de Tokyo
st.subheader('Visualización de Datos de Tokyo 2021')
data_path = os.path.join('Tokyo 2021 dataset v4.csv')
if os.path.exists(data_path):
    data = pd.read_csv(data_path)
    st.write("Aquí se muestra el dataset cargado:")
    st.dataframe(data)
else:
    st.error(f"El archivo {data_path} no se encontró. Asegúrate de que esté en la ubicación correcta.")

# Mostrando una imagen estática
image_path = os.path.join('static', 'medallas.png')
if os.path.exists(image_path):
    st.image(image_path, caption='Medallas en Tokyo 2021')
else:
    st.error(f"La imagen {image_path} no se encontró. Asegúrate de que esté en la ubicación correcta.")

# Función para crear un heatmap de correlación
def create_heatmap(data):
    numeric_cols = data.select_dtypes(include=[np.number]).columns
    data = data[numeric_cols]
    correlation_matrix = data.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
    plt.title('Heatmap de Correlación')
    plt.xlabel('Variables')
    plt.ylabel('Variables')
    st.pyplot()  # Usando st.pyplot() para mostrar el gráfico en Streamlit

# UI para heatmap de correlación
st.subheader('Crea un Heatmap de Correlación')
uploaded_file = st.file_uploader("Carga tu archivo CSV para análisis de correlación:", type=['csv'])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    create_heatmap(data)
