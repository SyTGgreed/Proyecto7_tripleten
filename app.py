import pandas as pd
import plotly.express as px
import streamlit as st
     
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_checkbox = st.checkbox('Construir histograma') # crear casilla para histograma
scatter_checkbox = st.checkbox('Construir grafico de dispersion') # crear casilla para grafico de dispersion

if hist_checkbox: # mostrar histograma si esta marcado
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if scatter_checkbox: # mostrar grafico de dispersion si esta marcado
    st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')
         
    # crear un histograma
    fig = px.scatter(car_data, x="odometer")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)