FROM python:3.12-slim

# Instala dependencias del sistema necesarias para WeasyPrint
RUN apt-get update && apt-get install -y \
    build-essential \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libcairo2 \
    libffi-dev \
    libxml2 \
    libxslt1.1 \
    libjpeg-dev \
    libpng-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requerimientos e instala dependencias de Python
COPY .requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación
COPY . .

# Expone el puerto 8080
EXPOSE 80

# Comando para ejecutar la app FastAPI con Uvicorn
CMD ["python", "src/main.py"]
