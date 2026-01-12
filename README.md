# Proyecto7_tripleten

Este es un proyecto de desarrollo de aplicaciones web donde construyes un panel de control interactivo usando Streamlit y lo despliegas en la nube.

### Objetivo Principal
Crear una aplicación web que permita visualizar y explorar un conjunto de datos de anuncios de venta de coches de manera interactiva.

## Tecnologías Utilizadas
Streamlit: Framework para crear aplicaciones web
Plotly Express: Biblioteca para crear gráficos interactivos
Pandas: Manipulación y análisis de datos
GitHub: Control de versiones y almacenamiento del código
Render: Plataforma para desplegar la aplicación en la nube

## Componentes de la Aplicación
Encabezado: Título descriptivo de la aplicación
Histograma: Visualización de distribución de una variable (ej: kilometraje)
Gráfico de dispersión: Relación entre dos variables (ej: kilometraje vs precio)
Elementos interactivos: Botones o checkboxes para controlar las visualizaciones

## Estructura del Proyecto
├── README.md
├── app.py (aplicación principal)
├── vehicles_us.csv (datos)
├── requirements.txt (dependencias)
└── notebooks/
    └── EDA.ipynb (análisis exploratorio)

## Instalación
1. Clona el repositorio https://github.com/SyTGgreed/Proyecto7_tripleten.git
2. Instala dependencias: `pip install --upgrade pip && pip install -r requirements.txt`
3. Ejecuta: `streamlit run app.py`