import streamlit as st
import pandas as pd
import plotly.express as px

def pagina_principal():
    st.title("VisuHub")
    st.write("Esta aplicación web creada con Streamlit permite a los usuarios cargar archivos CSV, "
             "visualizar datos de manera tabular y generar gráficos interactivos mediante Plotly.")
    st.subheader("Características")
    st.write("**Navegación simple:** Menú lateral para moverse entre la página principal, la sección de visualización de datos y los gráficos interactivos.")
    st.write("**Visualización de datos:** Permite cargar y mostrar el contenido de archivos CSV junto con estadísticas descriptivas.")
    st.write("**Gráficos interactivos:** Permite seleccionar columnas de datos para generar gráficos de barras interactivos.")

def visualizacion_de_datos():
    st.title("Visualizacion de Datos")
    st.write("Carga un archivo CSV para visualizar los datos.")
    archivo_cargado = st.file_uploader("Elige un archivo CSV", type='csv')

    if archivo_cargado is not None:
        df = pd.read_csv(archivo_cargado)
        st.write("Datos del archivo CSV:")
        st.write(df)
        st.write("Estadísticas descriptivas:")
        st.write(df.describe())

def graficos_interactivos():
    st.title("Gráficos interactivos")
    st.write("Carga un archivo CSV para crear gráficos interactivos.")
    archivo_cargado = st.file_uploader("Elige un archivo CSV", type="csv", key="2")

    if archivo_cargado is not None:
        df = pd.read_csv(archivo_cargado)
        st.write("Elige una columna para el eje X:")
        eje_x = st.selectbox("Eje X", df. columns)
        eje_y = st.selectbox("Eje Y", df.columns)

        if st.button("Crear grafico"):
            fig = px.bar(df, x=eje_x, y=eje_y, title=f"{eje_y} por {eje_x}")
            st.plotly_chart(fig)

st.sidebar.title("Navegacion")
pagina = st.sidebar.selectbox("Selecciona una página", ["Página Principal", "Visualizacion de Datos", "Gráficos interactivos"])

if pagina == "Página Principal":
    pagina_principal()
elif pagina == "Visualizacion de Datos":
    visualizacion_de_datos()
elif pagina == "Gráficos interactivos":
    graficos_interactivos()

# Developed by Danny894 