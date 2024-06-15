import streamlit as st
import pandas as pd
import os

# Título de la aplicación
st.title('Análisis de Datos de Tokyo 2021')

# Cargando y mostrando el dataset
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
