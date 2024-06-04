# my_api_project
# Proyecto API con FastAPI y Docker

Este proyecto implementa una API utilizando FastAPI y Docker, conectada a una base de datos PostgreSQL.

## Requisitos

- Docker y Docker Compose
- Git

## Instalación y Ejecución

1. Clona el repositorio:
    ```bash
    git clone https://github.com/<tu-usuario>/my_api_project.git
    cd my_api_project
    ```

2. Construye y levanta los contenedores:
    ```bash
    docker-compose up --build
    ```

3. La API estará disponible en `http://localhost:8000`.

## Endpoints

- `GET /movies/` - Obtener todos los registros
- `GET /movies/{id}` - Obtener un registro específico
- `POST /movies/` - Crear un nuevo registro
- `PUT /movies/{id}` - Actualizar un registro
- `DELETE /movies/{id}` - Eliminar un registro

## Uso de Postman

Se incluyen capturas de las pruebas realizadas con Postman en la carpeta `screenshots/`.

## Estructura del Proyecto

- `main.py` - Inicializador de la aplicación FastAPI.
- `models/` - Definición de los modelos de datos.
- `controllers/` - Lógica de negocio.
- `routes.py` - Definición de los endpoints.
- `Dockerfile` - Configuración de Docker para la API.
- `docker-compose.yml` - Configuración de Docker Compose.
- `requirements.txt` - Dependencias del proyecto.
