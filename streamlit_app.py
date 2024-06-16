import pandas as pd
import matplotlib.pyplot as plt

# Carga de datos
data_path = 'athlete_events.csv'
data = pd.read_csv(data_path)

# Filtrar datos para incluir solo Río 2016
rio_data = data[data['Games'] == '2016 Summer']

# Función para crear un gráfico de barras de los países con más medallas
def create_medal_chart(data):
    # Filtrar para incluir solo entradas con medallas
    medal_data = data.dropna(subset=['Medal'])
    medal_counts = medal_data['NOC'].value_counts().head(10)  # Top 10 países
    fig, ax = plt.subplots()
    medal_counts.plot(kind='bar', ax=ax, color='skyblue')
    ax.set_title('Top 10 Países con Más Medallas en Río 2016')
    ax.set_xlabel('País')
    ax.set_ylabel('Número de Medallas')
    plt.show()

# Verificación de que los datos han sido cargados correctamente para la generación del gráfico de barras
if not rio_data.empty:
    create_medal_chart(rio_data)
else:
    print("No se ha cargado el dataset de Río 2016 para la generación del gráfico de barras.")
