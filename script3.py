import requests
from bs4 import BeautifulSoup
import sys
import os
import re

# URL de la API de Grobid
GROBID_URL = "http://localhost:8070/api/processFulltextDocument"

def extract_links_from_grobid(pdf_path):
    """Extrae todos los enlaces externos de un PDF usando Grobid."""
    if not os.path.isfile(pdf_path):
        print(f" Error: El archivo {pdf_path} no existe.")
        return None

    try:
        with open(pdf_path, "rb") as pdf_file:
            response = requests.post(GROBID_URL, files={'input': pdf_file})

        if response.status_code != 200:
            print(f" Error en Grobid para {pdf_path}: Código {response.status_code}")
            return None

        # Parsear la salida XML de Grobid
        soup = BeautifulSoup(response.text, "xml")

        # Opcional: Guardar el XML de salida para depuración
        with open("grobid_output3.xml", "w", encoding="utf-8") as f:
            f.write(soup.prettify())

        links = set()

        for doi in soup.find_all("idno", {"type": "DOI"}):
            links.add(f"https://doi.org/{doi.text.strip()}")

        for ref in soup.find_all("ref", target=True):
            link = ref["target"]
            if link and re.match(r"^(https?://|www\.)", link):
                links.add(link.strip())

        for ptr in soup.find_all("ptr", target=True):
            link = ptr["target"]
            if link and re.match(r"^(https?://|www\.)", link):
                links.add(link.strip())

        for note in soup.find_all("note"):
            note_text = note.text.strip() if note.text else ""
            urls = re.findall(r"https?://[^\s]+", note_text)
            links.update(urls)

        return list(links) if links else None

    except requests.exceptions.RequestException as e:
        print(f" Error de conexión con Grobid: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python script3.py <ruta_pdf>")
        sys.exit(1)

    pdf_file = sys.argv[1]
    links = extract_links_from_grobid(pdf_file)

    if links:
        print(f"🔗 Enlaces externos encontrados en {pdf_file}:")
        for link in links:
            print(link)
    else:
        print(f" No se encontraron enlaces externos en {pdf_file}.")
