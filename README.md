# CV Generator

Generador de currículums basado en FastAPI y Docker.

## Requisitos previos

- [Docker](https://www.docker.com/get-started) y [Docker Compose](https://docs.docker.com/compose/install/) instalados en tu sistema.

## Instrucciones para correr localmente

1. Clona el repositorio y accede a la carpeta del proyecto:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd fastapi_cv_maker
   ```

2. Copia el archivo de variables de entorno de ejemplo:

   ```bash
   cp .env.example .env
   ```

3. Levanta los servicios con Docker Compose:

   ```bash
   docker-compose up -d
   ```

4. Accede a la API en tu navegador o herramienta de pruebas (por defecto en http://localhost:8080/docs).
