import requests
from bs4 import BeautifulSoup
import sys
import os

# Configuración de la API de Grobid
GROBID_URL = "http://localhost:8070/api/processFulltextDocument"

def count_figures(pdf_path):
    """Cuenta la cantidad de figuras en un artículo en PDF usando Grobid."""
    if not os.path.isfile(pdf_path):
        print(f"Error: El archivo {pdf_path} no existe.")
        return None

    try:
        with open(pdf_path, "rb") as pdf_file:
            response = requests.post(GROBID_URL, files={'input': pdf_file})

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "xml")
            figures = soup.find_all("figure")
            return len(figures)
        else:
            print(f"Error en Grobid para {pdf_path}: Código {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión con Grobid: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python script2.py <ruta_pdf>")
        sys.exit(1)

    pdf_file = sys.argv[1]
    num_figures = count_figures(pdf_file)

    if num_figures is not None:
        print(f"El artículo {pdf_file} contiene {num_figures} figuras.")
    else:
        print("No se pudo contar el número de figuras.")
