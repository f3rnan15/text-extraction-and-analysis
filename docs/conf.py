import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# Configuración del proyecto
project = 'Open Science & AI'
copyright = '2024, Tu Nombre'
author = 'Tu Nombre'
release = '1.0'

# Extensiones necesarias
extensions = [
    "sphinx_rtd_theme",
    "myst_parser"
]

# Directorios
templates_path = ['_templates']
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Tema de la documentación
html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']

