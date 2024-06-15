import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def create_heatmap(data):
    # Asegurarse de que las columnas que se van a correlacionar son numéricas
    numeric_cols = data.select_dtypes(include=[np.number]).columns
    data = data[numeric_cols]

    # Calcular la matriz de correlación
    correlation_matrix = data.corr()

    # Configurar el tamaño del gráfico
    plt.figure(figsize=(10, 8))

    # Crear el heatmap con la matriz de correlación
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)

    # Agregar títulos y etiquetas
    plt.title('Heatmap de Correlación')
    plt.xlabel('Variables')
    plt.ylabel('Variables')

    # Mostrar el gráfico
    plt.show()

# Streamlit UI
st.title('Aplicación para Crear Heatmap de Correlación')

# Carga de archivo
uploaded_file = st.file_uploader("Carga tu archivo CSV", type=['csv'])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    create_heatmap(data)
