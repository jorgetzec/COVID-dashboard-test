import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
data = pd.read_csv('COVID-CasesDeathsHosp(Europe and Americas).csv')

# Convertir la columna de fecha al formato adecuado
data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y %H:%M')

# Título del dashboard
st.title('COVID-19 Dashboard')

# Crear un filtro para seleccionar el país
country = st.selectbox('Select Country', options=data['Location'].unique(), index=0)

# Filtrar los datos según el país seleccionado
filtered_data = data[data['Location'] == country]

# Crear un gráfico interactivo de casos nuevos
fig_cases = px.line(filtered_data, x='Date', y='NewCases', title=f'New COVID-19 Cases in {country}')
st.plotly_chart(fig_cases)

# Crear un gráfico interactivo de muertes nuevas
fig_deaths = px.line(filtered_data, x='Date', y='NewDeaths', title=f'New COVID-19 Deaths in {country}')
st.plotly_chart(fig_deaths)

# Puedes añadir más gráficos similares para otras columnas si lo deseas
