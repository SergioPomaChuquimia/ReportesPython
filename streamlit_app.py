import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import geopandas as gpd

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
# Mostrando una imagen estática
image_path = os.path.join('static', 'medallas.png')
if os.tru(image_path):
    st.image(image_path, caption='Medallas en Tokyo 2021')  # Aquí se cambia `image_file` por `image_path`
else:
    st.error(f"La imagen {image_path} no se encontró. Asegúrate de que esté en la ubicación correcta.")

# Función para crear un heatmap de correlación
def create_heatmap(data):
    numeric_cols = data.select_dtypes(include=[np.number]).columns
    correlation_matrix = data[numeric_cols].corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5, ax=ax)
    ax.set_title('Heatmap de Correlación')
    ax.set_xlabel('Variables')
    ax.set_ylabel('Variables')
    st.pyplot(fig)

# Verificación de que los datos han sido cargados correctamente para la generación del heatmap
if 'data' in locals():
    st.subheader('Heatmap de Correlación')
    create_heatmap(data)

# Función para crear un mapa
def create_map(csv_file):
    data = pd.read_csv(csv_file)
    data = data.rename(columns={'Team/NOC': 'name'})
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    merged = world.merge(data, on='name', how="left")
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    world.boundary.plot(ax=ax, linewidth=1)
    merged.dropna().plot(ax=ax, column='Total', cmap='OrRd', legend=True,
                         legend_kwds={'label': "Total de Medallas por País"},
                         missing_kwds={'color': 'lightgrey'})
    plt.title('Total de Medallas en los Juegos Olímpicos de Tokio 2021 por País')
    st.pyplot(fig)

# Verificación de que el archivo CSV existe para la generación del mapa
if os.path.exists(data_path):
    st.subheader('Mapa de Distribución de Medallas')
    create_map(data_path)
else:
    st.error(f"No se ha cargado el dataset de Tokyo 2021 para la generación del mapa.")
