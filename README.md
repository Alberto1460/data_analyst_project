# Análisis de Datos de Vehículos

Esta aplicación web está diseñada para proporcionar un análisis interactivo de un conjunto de datos de anuncios de venta de coches en los Estados Unidos.

## Despliegue en Render

Puedes acceder a la aplicación desplegada en Render a través del siguiente enlace:

[Data Analyst Project en Render](https://data-analyst-project.onrender.com)

## Funcionalidad

La aplicación permite a los usuarios:
- Visualizar los primeros 30 registros del conjunto de datos.
- Construir un histograma del kilometraje de los vehículos.
- Construir un diagrama de dispersión que muestra la relación entre el kilometraje y el precio de los vehículos, coloreado por su condición.

## Cómo Ejecutar la Aplicación

Para ejecutar la aplicación localmente:

1. Clona este repositorio:
   ```sh
   git clone https://github.com/tu-usuario/data_analyst_project.git
   ```
   
2. Navega al directorio del proyecto:
   ```sh
    cd data_analyst_project
    ```

3. Crea y activa un entorno virtual:
   ```sh
    python -m venv vehicles_env
    vehicles_env\Scripts\activate   # En Windows
    source vehicles_env/bin/activate  # En macOS/Linux
    ```

4. Instala las dependencias:
   ```sh
    pip install -r requirements.txt
    ```

5. Ejecuta la aplicación Streamlit:
   ```sh
    streamlit run app.py
    ```

