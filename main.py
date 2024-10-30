import os
import requests
from fastapi import FastAPI, HTTPException
from bs4 import BeautifulSoup
from urllib.parse import urljoin

app = FastAPI()

def descargar_imagenes(url, carpeta="imagenes_descargadas"):
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="No se pudo acceder a la página")

    soup = BeautifulSoup(response.text, "html.parser")
    imagenes_descargadas = []

    for img_tag in soup.find_all("video"):
        img_url = img_tag.get("src")
        img_url = urljoin(url, img_url)

        try:
            img_response = requests.get(img_url)
            if img_response.status_code == 200:
                img_nombre = os.path.join(carpeta, img_url.split("/")[-1])
                with open(img_nombre, "wb") as img_file:
                    img_file.write(img_response.content)
                imagenes_descargadas.append(img_nombre)
            else:
                print(f"Error al descargar {img_url}")
        except requests.RequestException as e:
            print(f"Error al descargar {img_url}: {e}")

    return imagenes_descargadas

@app.get("/descargar-imagenes")
def descargar_imagenes_api(url: str):
    try:
        imagenes = descargar_imagenes(url)
        return {"mensaje": "Imágenes descargadas con éxito", "imagenes": imagenes}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
