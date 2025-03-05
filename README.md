<h1 align="center"> text-extraction-and-analysis </h1> 

[![License](https://img.shields.io/badge/license-GNU-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.12.7-yellow.svg)](https://www.python.org/)

## 📖 Descripción del Proyecto

Este proyecto automatiza el análisis de artículos científicos en PDF utilizando **Grobid**, **Python** y herramientas de procesamiento de datos. Extrae información clave como:
- **Resumen** del artículo y generación de una **nube de palabras clave**.
- **Cantidad de figuras** en el documento.
- **Lista de enlaces externos** presentes en el artículo.

Este sistema está diseñado para apoyar iniciativas de **ciencia abierta** y procesamiento automatizado de literatura científica.

---

## 🚀 Características Principales

✅ **Extracción automática de datos** de artículos científicos.  
✅ **Visualización de palabras clave** con una nube de palabras.  
✅ **Gráficos de análisis** de figuras por artículo.  
✅ **Procesamiento de múltiples documentos en lote**.  
✅ **Entorno reproducible con Docker y Conda**.  

---

## 📦 Instalación y Configuración-Linux

### 🔹 **1. Clonar el Repositorio**
```bash
git clone https://github.com/tu-usuario/text-extraction-and-analysis.git
cd text-extraction-and-analysis
```
### 🔹 **2. Creación y activacion del entorno(Recomendado)**
```bash
conda create --name text-extraction-and-analysis-env python=3.9
conda activate open_science_env
```
### 🔹 **3. Instalación de bibliotecas**
```bash
pip install requests wordcloud matplotlib pandas beautifulsoup4 pytest wordcloud lxml
```
### 🔹 **4. Instalación de docker y grobid**
```bash
sudo apt install docker (para distribuciones no compatibles usar otro gestor de paquetes)
sudo docker pull lfoppiano/grobid:0.7.2
```
### 🔹 **5. Ejecucion de grobid local**
```bash
sudo docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2
```
### 🔹 **6. Ejecucion de scripts**
```bash
python3 script1.py <ruta_al_pdf> (Nube de palabras)
python3 script2.py <ruta_al_pdf> (Conteo de figuras)
python3 script3.py <ruta_al_pdf> (Extracción de enlaces)
```

---

## 📦 Instalación y Configuración (Docker)

### 🔹 **0. Instalar Docker (previo)**
```bash
sudo apt update
sudo apt install docker.io
sudo systemctl enable --now docker
```
#### Instalar desde la web (Todos los SSOO)
#### https://docs.docker.com/desktop/setup/install/windows-install/

### 🔹 **1. Ejecucion de Grobid**
```bash
sudo docker pull lfoppiano/grobid:0.7.2
docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2
```
### 🔹 **2. Construir el contenedor**
```bash
sudo docker build -t teaa .
```
### 🔹 **3. Ejecutar el contenedor**
```bash
sudo docker run --rm -it --network=host teaa
```
### 🔹 **4. Ejecutar scripts dentro del contenedor**
```bash
venv/bin/python3 script1.py <ruta_al_pdf> (Nube de palabras)
venv/bin/python3 script2.py <ruta_al_pdf> (Conteo de figuras)
venv/bin/python3 script3.py <ruta_al_pdf> (Extracción de enlaces)
```
### 🔹 **5. Salir del contenedor**
```bash
exit
```


Si usa este repositorio citenos:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14977143.svg)](https://doi.org/10.5281/zenodo.14977143)

DOI: [10.5281/zenodo.14977143](https://doi.org/10.5281/zenodo.14977143)