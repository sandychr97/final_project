import streamlit as st
import pandas as pd
import plotly_express as px
vehicle_data = pd.read_csv("vehicles_us.csv")
st.header('Datos de anuncios de vehículos en venta')

build_histogram = st.checkbox('Construir histograma')
if build_histogram:
    st.write('Creación de un histograma para la columna odómetro')
    fig = px.histogram(vehicle_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

graf_button = st.button('Construir gráfico de dispersión')
if graf_button:
    st.write = ('Creación de un gráfico de dispersión ')
    fig_2 = px.scatter(vehicle_data, x='odometer', y='price')
    st.plotly_chart(fig_2, use_container_width=True)
