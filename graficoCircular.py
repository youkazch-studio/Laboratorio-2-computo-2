import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv('datasets/SuperMarket Analysis.csv')

# Agrupar las ventas por ciudad
city_sales = df.groupby('City')['Sales'].sum().reset_index()

# Crear el gráfico circular
plt.figure(figsize=(10, 7))
plt.pie(city_sales['Sales'], labels=city_sales['City'], autopct='%1.1f%%', startangle=140)
plt.title('Distribución de Ventas por Ciudad')
plt.axis('equal')  # Para que el gráfico sea un círculo

# Mostrar gráfico
plt.show()



"""
Análisis del gráfico circular:
Identificación de las ciudades de las sucursales de supermercados más rentables: El gráfico circular permitirá ver rápidamente en qué ciudades se generan más ventas. 
Las porciones más grandes del gráfico representarán las ciudades de las sucursales con mayores ingresos.

Comparación de ventas entre ciudades:  
Mandalay. porcentaje de ventas: 32.9%
Yangon. porcentaje de ventas: 32.9%
Naypyitaw. porsentaje de ventas: 34.2%

Como se puede observar la sucursal del supermercado que mas vende se encuentra en la cuidad de: Naypyitaw.

Esta informacion util para poder implementar estrategias de marketing: Si una ciudad tiene una gran proporción de ventas, puede ser una buena 
oportunidad para lanzar campañas de marketing específicas o promociones para atraer más clientes en esa área.

Tambien se podria análizar el mercado: Este análisis ayudaria a entender el comportamiento del mercado en diferentes ciudades, lo que es útil 
para decisiones estratégicas en términos de expansión o ajuste de productos.


Enlace del Dataset: https://www.kaggle.com/datasets/faresashraf1001/supermarket-sales?resource=download 

"""