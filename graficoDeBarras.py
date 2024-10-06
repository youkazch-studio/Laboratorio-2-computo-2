import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv('datasets/Spotify Most Streamed Songs.csv')

# Convertir la columna 'streams' a numérico
df['streams'] = pd.to_numeric(df['streams'], errors='coerce')

# Eliminar filas con valores NaN en 'streams'
df = df.dropna(subset=['streams'])

# Seleccionar las 10 canciones con más streams
top_songs = df.nlargest(10, 'streams')

# Crear el gráfico de barras basado en streams
plt.figure(figsize=(10, 6))

# Definir los datos
canciones = top_songs['track_name']
streams = top_songs['streams']
in_spotify_playlists = top_songs['in_spotify_playlists']
in_spotify_charts = top_songs['in_spotify_charts']

# Crear gráfico de barras para streams
plt.bar(canciones, streams, color='blue', label='Streams')

# Añadir etiquetas
plt.title('Top 10 Canciones más Escuchadas en Spotify')
plt.xlabel('Canciones')
plt.ylabel('Número de reproducciones')
plt.xticks(rotation=45, ha='right')

# Mostrar gráfico
plt.show()


"""
Análisis del gráfico de barras :

A partir del gráfico que se genera con las 10 canciones más populares en Spotify en función de la cantidad de streams o reproducciones, 
podemos realizar las siguientes observaciones:

El número de Streams o reproduccioes : Las canciones más populares en base al numero de reproducciones son las siguientes 10 canciones:
1. Blinding Lights.
2. Shape of You.
3. Someone You Loved.
4. Dance Monkey.
5. Sunflower - Spider-Man: intro the Spider-Verse.
6. One Dance.
7. With Justin Bieber.
8. Believer.
9. Closer.
10. Starboy.

también la relación con Listas y Charts de Spotify : 
Si observamos más datos sobre la columna in_spotify_playlistsy in_spotify_charts, podríamos analizar 
si estas canciones están presentes en listas o charts de Spotify. Esto puede ser importante porque podría haber 
una relación directa entre estar en una lista popular o un chart y el número de streams o reproducciones que obtiene una canción.

Por lo que se puede observar: La cancion Blinding Lights es la mas popular, mientras que la cancion Starboy es la menos escuchada 
dentro del Top 10 de canciones mas populares. 

Enlace del Dataset: https://www.kaggle.com/datasets/abdulszz/spotify-most-streamed-songs

"""