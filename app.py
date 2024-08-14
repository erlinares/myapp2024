import streamlit as st 
import numpy as np 
import pandas as pd
import plotly.offline as py 
#py.init_notebook_mode(connected=True) # this code, allow us to work with offline plotly version
import plotly.graph_objs as go # it's like "plt" of matplot
import plotly.tools as tls # It's useful to we get some tools of plotly



#writing simple text 

st.title("Credit Card App")

    
# ============ Aplicación Principal  ============
        
# Definir las opciones de página
pages = ["Cargar Datos", "Explorar Datos", "Feature Engineering", "Modelado", "Neural Network", "Prediccion"]


# Mostrar un menú para seleccionar la página
selected_page = st.sidebar.multiselect("Seleccione una página", pages)

# Condicionales para mostrar la página seleccionada
if "Cargar Datos" in selected_page:
    st.write("""
    ## Cargar Datos""")
    # Cargar archivo CSV usando file uploader
    uploaded_file = st.file_uploader("Cargar archivo CSV", type=["csv"])
    # Si el archivo se cargó correctamente
    if uploaded_file is not None:
    # Leer archivo CSV usando Pandas
        dataset = pd.read_csv(uploaded_file)
    # Mostrar datos en una tabla
        st.write(dataset)

if "Explorar Datos" in selected_page:
    st.write("""
    ## Explore Data
    Distributions""")
    if uploaded_file is not None:
        get_eda(dataset)
        
if "Feature Engineering" in selected_page:
    st.write("""
    ## Feature Engineering
    New datset""")

if "Modelado" in selected_page:
    st.write("""
    ## Entrenamiento con diferentes modelos
    Resultados""")

        
if "Neural Network" in selected_page:
    st.write("""
    ## Neural Network
    Resultados""")

        
if "Prediccion" in selected_page:
    st.write("""
    ## Predicción de un Crédito
    Capture los datos""")
 
