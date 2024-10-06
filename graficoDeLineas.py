import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv('datasets/movie.csv')

# Convertir la columna release_date a datetime
df['release_date'] = pd.to_datetime(df['release_date'])

# Filtrar los últimos 24 años
current_year = pd.to_datetime("today").year
df = df[df['release_date'].dt.year >= current_year - 24]

# Extraer el año de la fecha de lanzamiento
df['release_year'] = df['release_date'].dt.year

# Agrupar por año y calcular la media de popularidad
grouped_data = df.groupby('release_year').agg({
    'popularity': 'mean'
}).reset_index()

# Crear el gráfico de líneas
plt.figure(figsize=(14, 7))

# Gráfico de popularidad promedio
plt.plot(grouped_data['release_year'], grouped_data['popularity'], marker='o', label='Popularidad Promedio', color='orange')

# Añadir etiquetas y título
plt.title('Evolución de la Popularidad Promedio de Películas en los Últimos 24 Años')
plt.xlabel('Año de Estreno')
plt.ylabel('Popularidad')
plt.xticks(grouped_data['release_year'], rotation=45)

# Mostrar título de las películas más populares de cada año
for year in grouped_data['release_year']:
    # Obtener las películas más populares de ese año
    movies_in_year = df[df['release_year'] == year]
    top_movie = movies_in_year.nlargest(1, 'popularity')  # La película más popular
    if not top_movie.empty:
        plt.text(year, grouped_data.loc[grouped_data['release_year'] == year, 'popularity'].values[0],
                 top_movie['title'].values[0], fontsize=8, ha='center', rotation=45)

# Mostrar gráfico
plt.grid()
plt.tight_layout()
plt.legend()
plt.show()






"""
Análisis del gráfico de lineas:

Tendencias a lo largo del tiempo: Se puede observar cómo ha cambiado la popularidad promedio de las películas a lo largo de los ultimos 24 años. 
Un aumento en la línea podría indicar un interés creciente en las películas de parte del publico.

Películas destacadas por año (2000 - 2024): 

2000: The Emperor's New Groove. Popularidad promedio: 26.7
2001: The Lord of the Rings: The Fellowship of the King. Popularidad promedio: 28.9
2002: xxx Popularidad promedio: 31
2003: The Lord of the Rings: The Return of the King. Popularidad promedio: 28
2004: Harry Potter and the Prisoner of Azkaban. Popularidad promedio: 30.1
2005: Popularidad The Chronicles of Namia: The Lion, the Witch and the Wardrobe promedio: 28.6
2006: Pirates of the Caribbean: Dead Man's Chest. Popularidad promedio: 26.46
2007: 30 Days of Night. Popularidad promedio: 27.60
2008: The Dark Knight. Popularidad promedio: 27.85
2009: Coraline. Popularidad promedio: 28.50 
2010: Despicable Me. Popularidad promedio: 26.03 
2011: Harry Potter and the Deathly Hallows: Part 2. Popularidad promedio: 22.93
2012: The Avengers. Popularidad promedio: 25.98
2013: The Conjuring. Popularidad promedio: 25.82 
2014: Interstellar. Popularidad promedio: 29.30 
2015: Inside Out. Popularidad promedio: 26.14
2016: Deadpool. Popularidad promedio: 25.39 
2017: Alien: Covenant. Popularidad promedio: 26.46
2018: Avengers: Infinity War. Popularidad promedio: 24.96
2019: Avengers: Endgame. Popularidad promedio: 25.93
2020: Sonic the Hedgehog. Popularidad promedio: 21.54 
2021: Pleasure. Popularidad promedio: 29.78
2022: Sonic the Hedgehog 2. Popularidad promedio: 36.04 
2023: My Fault. Popularidad promedio: 64.51
2024: Deadpool & Wolverine. Popularidad promedio: 300.36

Como se puede observar la pelicula mas popular fue: Deadpool & Wolverine la cual fue lanzada en el 2024, mientras que la
pelicula Sonic the Hedgehog fue la menos popular la cual fue lanzada en el 2020, de las peliculas que fueron lanzadas en los ultimos 24 años.

Visualización clara: 
Este formato es útil para comparar la popularidad en diferentes años y ver si hay alguna correlación con el lanzamiento de películas específicas.


Enlace del Dataset: https://www.kaggle.com/datasets/ayushi10kumari/top-rated-movie-dataset

"""