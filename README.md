# Aplicación Interactiva con Streamlit

## Descripción
Esta aplicación web creada con Streamlit permite a los usuarios cargar archivos CSV, visualizar datos de manera tabular y generar gráficos interactivos mediante Plotly.

## Características
- **Navegación simple:** Menú lateral para moverse entre la página principal, la sección de visualización de datos y los gráficos interactivos.
- **Visualización de datos:** Permite cargar y mostrar el contenido de archivos CSV junto con estadísticas descriptivas.
- **Gráficos interactivos:** Permite seleccionar columnas de datos para generar gráficos de barras interactivos.

## Requisitos

Antes de ejecutar la aplicación, asegúrate de tener instaladas las siguientes dependencias:

- Python 3.7 o superior
- Streamlit
- Pandas
- Plotly

Para instalarlas, ejecuta:

```bash
pip install streamlit pandas plotly
```

## Ejecución
Para iniciar la aplicación, ejecuta el siguiente comando en tu terminal:

```bash
streamlit run nombre_del_archivo.py
```

Asegúrate de estar en el directorio donde se encuentra el archivo del código.

## Uso

### 1. Navegación
Utiliza la barra lateral para moverte entre las siguientes secciones:

- **Página Principal:** Presenta la introducción de la aplicación.
- **Visualización de Datos:** Permite cargar un archivo CSV para mostrar sus datos y estadísticas.
- **Gráficos Interactivos:** Permite seleccionar columnas del archivo CSV para crear gráficos de barras interactivos.

### 2. Visualización de Datos
- Haz clic en "Elige un archivo CSV" y selecciona un archivo para cargar.
- La aplicación mostrará el contenido del archivo y las estadísticas descriptivas.

### 3. Gráficos Interactivos
- Carga un archivo CSV.
- Selecciona las columnas para el eje X y el eje Y.
- Haz clic en "Crear gráfico" para generar un gráfico de barras interactivo.

## Estructura del Proyecto

```
|-- .idea
|-- main.py
|-- README.md
```

## Contribución
Si deseas contribuir a este proyecto, realiza lo siguiente:
1. Haz un fork del repositorio.
2. Crea una nueva rama para tu funcionalidad (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -m 'Agregar nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia
Este proyecto está bajo la Licencia MIT.

