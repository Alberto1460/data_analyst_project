import pandas as pd
import streamlit as st
import plotly.express as px


# Configurar el tema claro
st.set_page_config(
    page_title="Análisis de datos de Vehículos",
    page_icon="🚗",
    layout="centered",
    initial_sidebar_state="auto",
)

# Encabezado de la aplicación
st.header('Análisis de datos de Vehículos')

# Cargar los datos desde el directorio
car_data = pd.read_csv('C:/Users/Albert/Desktop/data_analyst_project/vehicles_us.csv')

# Mostrar los primeros 30 datos del conjunto de datos
st.subheader('Primeros 30 datos del conjunto de datos')
st.write(car_data.head(30))

# Crear casillas de verificación
build_histogram = st.checkbox('Construir un histograma')
buil_scatter = st.checkbox('Contruir un diagrama de dispersión')

# Acciones al seleccionar la casilla de construir un histograma
if build_histogram:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches\n'
            'en base a su kilometraje')
    # Crear histograma
    fig = px.histogram(car_data, x='odometer')
    # Mostrar gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Acciones al seleccionar la casilla de diagrama de dispersión
if buil_scatter:
    st.write('Construcción de un diagrama de dispersión en base a las columnas\n'
             '`kilometraje` y `precio`')
    # Crear un diagrama de dispersión
    fig = px.scatter(car_data, x='odometer', y='price', color='condition')
    # Mostrar gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


