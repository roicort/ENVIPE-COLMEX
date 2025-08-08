# ENVIPE (INEGI)

Este repositorio contiene herramientas y notebooks para el análisis de datos de la Encuesta Nacional de Victimización y Percepción sobre Seguridad Pública (ENVIPE) en México.

## Estructura del repositorio

- `gastoseguridad.ipynb`: Notebook para el análisis de gastos en seguridad.
- `tabuladorpercepcion.ipynb`: Notebook para el análisis de percepción sobre seguridad.
- `transform.py`: Script de transformación y procesamiento de datos.
- `data/`: Carpeta con archivos ZIP de datos ENVIPE por año (2018-2024).
- `pyproject.toml`, `uv.lock`: Archivos de configuración y dependencias del proyecto.

## Requisitos

- Python 3.8+
- Paquetes especificados en `pyproject.toml`

## Instalación

1. Clona el repositorio:
   ```zsh
   git clone https://github.com/tu-usuario/ENVIPE-COLMEX.git
   cd ENVIPE-COLMEX
   ```
2. Usa UV para crear el env

    ```zsh
    uv create
    ```

## Licencia

Este proyecto se distribuye bajo la licencia MIT.
