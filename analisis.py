from flask import Flask, render_template, send_file
import os
import pandas as pd

# Especificar el backend de Matplotlib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def mostrar_datos():
    ruta_archivo = 'Tokyo 2021 dataset v4.csv'
    data = pd.read_csv(ruta_archivo)

    # Asegurarse de que la carpeta 'static' exista
    if not os.path.exists('static'):
        os.makedirs('static')

    # Crear un gráfico de barras
    plt.figure(figsize=(10, 5))
    data.head(10).plot(kind='bar', x='Team/NOC', y='Total', color='blue')
    plt.title('Total de Medallas Ganadas por los Primeros 10 Equipos')
    plt.xlabel('Equipo/NOC')
    plt.ylabel('Total de Medallas')
    plt.tight_layout()

    # Guardar el gráfico en un archivo de imagen
    img_path = os.path.join('static', 'medallas.png')
    plt.savefig(img_path)
    plt.close()

    # Renderizar la plantilla HTML y pasar la ruta de la imagen
    return render_template('index.html', img_url=img_path)

if __name__ == '__main__':
    app.run(debug=True)
