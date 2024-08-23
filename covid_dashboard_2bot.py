import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
data = pd.read_csv('COVID-CasesDeathsHosp(Europe and Americas).csv')

# Convertir la columna de fecha al formato adecuado
data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y %H:%M')

# Título del dashboard
st.title('COVID-19 Dashboard')

# Crear dos botones de filtrado en el sidebar
option = st.sidebar.radio(
    "Choose a filter:",
    ('Filter by Country', 'Filter by Date')
)

# Filtro 1: Filtrar por país
if option == 'Filter by Country':
    country = st.selectbox('Select Country', options=data['Location'].unique(), index=0)
    
    # Filtrar los datos según el país seleccionado
    filtered_data_country = data[data['Location'] == country]
    
    # Crear un gráfico interactivo de casos nuevos
    st.subheader(f'New COVID-19 Cases in {country}')
    fig_cases_country = px.line(filtered_data_country, x='Date', y='NewCases', title=f'New Cases in {country}')
    st.plotly_chart(fig_cases_country)
    
# Filtro 2: Filtrar por fecha para todos los países
elif option == 'Filter by Date':
    date = st.date_input('Select Date', value=pd.to_datetime("2020-01-23"), min_value=min(data['Date']), max_value=max(data['Date']))
    
    # Filtrar los datos según la fecha seleccionada
    filtered_data_date = data[data['Date'] == date]
    
    # Crear un gráfico interactivo de muertes nuevas por país en la fecha seleccionada
    st.subheader(f'New COVID-19 Deaths on {date.strftime("%Y-%m-%d")}')
    fig_deaths_date = px.bar(filtered_data_date, x='Location', y='NewDeaths', title=f'New Deaths on {date.strftime("%Y-%m-%d")}')
    st.plotly_chart(fig_deaths_date)
