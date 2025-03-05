import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# Proyecto
project = 'Open Science & AI'
copyright = '2024, Tu Nombre'
author = 'Tu Nombre'
release = '1.0'

# Configuración general de Sphinx
extensions = [
    "sphinx_rtd_theme",   # Tema de Read the Docs
    "myst_parser"         # Soporte para Markdown
]

templates_path = ['_templates']
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Configuración del tema
html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']

