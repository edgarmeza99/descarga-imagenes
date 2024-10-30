
# API de Descarga de Imágenes

Esta es una API desarrollada en Python utilizando FastAPI que permite descargar imágenes de una página web dada su URL. La API extrae todas las imágenes de la página y las guarda en una carpeta local.

## Requisitos

- Python 3.7 o superior
- `fastapi`
- `uvicorn`
- `requests`
- `beautifulsoup4`

## Instalación

1. Clona este repositorio o descarga el código.
2. Asegúrate de tener un entorno virtual (opcional pero recomendado) y actívalo.
3. Instala las dependencias:

   ```bash
   pip install fastapi uvicorn requests beautifulsoup4
   ```

## Uso

1. Guarda el archivo del código como `main.py`.
2. Ejecuta el servidor:

   ```bash
   uvicorn main:app --reload
   ```

3. La API estará disponible en `http://127.0.0.1:8000`.

### Endpoint

- **GET** `/descargar-imagenes`

  Este endpoint descarga todas las imágenes de la página web indicada en la URL.

  #### Parámetros de consulta:
  - `url` (string): La URL de la página de la cual se descargarán las imágenes.

  #### Ejemplo de solicitud:

  ```bash
  curl -X 'GET' \
    'http://127.0.0.1:8000/descargar-imagenes?url=https://ejemplo.com'
  ```

## Notas

- La carpeta `imagenes_descargadas` se crea automáticamente si no existe.
- La API convierte las URLs relativas de las imágenes en URLs absolutas, por lo que no importa si la página usa enlaces relativos para las imágenes.
