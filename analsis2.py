import pandas as pd
import numpy as np  # Asegúrate de que esta línea esté presente
import matplotlib.pyplot as plt
import seaborn as sns

def create_heatmap(csv_file):
    # Cargar datos desde un archivo CSV
    data = pd.read_csv(csv_file)

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

# Ruta del archivo, ajusta según tu sistema de archivos
csv_file_path = 'Tokyo 2021 dataset v4.csv'
create_heatmap(csv_file_path)
