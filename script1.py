import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import sys
import os

# Configuración de la API de Grobid
GROBID_URL = "http://localhost:8070/api/processFulltextDocument"

def extract_abstract(pdf_path):
    """Extrae el resumen del artículo en PDF usando Grobid."""
    if not os.path.isfile(pdf_path):
        print(f"Error: El archivo {pdf_path} no existe.")
        return None
    
    try:
        with open(pdf_path, "rb") as pdf_file:
            response = requests.post(GROBID_URL, files={'input': pdf_file})
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "xml")
            abstract = soup.find("abstract")
            return abstract.text.strip() if abstract else "No se encontró resumen."
        else:
            print(f"Error en Grobid para {pdf_path}: Código {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión con Grobid: {e}")
        return None

def generate_wordcloud(text):
    """Genera una nube de palabras a partir del resumen extraído."""
    if not text or text == "No se encontró resumen.":
        print("No se pudo generar la nube de palabras porque no se encontró un resumen.")
        return
    
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Nube de Palabras Clave")
    plt.savefig("wordcloud.png")
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python script1.py <ruta_pdf>")
        sys.exit(1)

    pdf_file = sys.argv[1]
    abstract_text = extract_abstract(pdf_file)
    if abstract_text:
        generate_wordcloud(abstract_text)
