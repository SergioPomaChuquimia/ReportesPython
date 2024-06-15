import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

def create_map(csv_file):
    # Cargar datos desde un archivo CSV
    data = pd.read_csv(csv_file)

    # Asegúrate de que el nombre del país en el dataset coincide con el shapefile
    data = data.rename(columns={'Team/NOC': 'name'})

    # Cargar un mapa mundial
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    # Unir el mapa con los datos de las medallas
    merged = world.merge(data, on='name', how="left")

    # Configurar el mapa
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    world.boundary.plot(ax=ax, linewidth=1)
    merged.dropna().plot(ax=ax, column='Total', cmap='OrRd', legend=True,
                         legend_kwds={'label': "Total de Medallas por País"},
                         missing_kwds={'color': 'lightgrey'})

    # Títulos y etiquetas
    plt.title('Total de Medallas en los Juegos Olímpicos de Tokio 2021 por País')
    plt.show()

# Ruta del archivo CSV
csv_file_path = 'Tokyo 2021 dataset v4.csv'  # Ajusta la ruta
create_map(csv_file_path)
