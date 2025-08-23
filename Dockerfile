FROM python:3.11-slim

# Evitar preguntas interactivas
ENV DEBIAN_FRONTEND=noninteractive

# Instalar ffmpeg y librerías básicas
RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# Crear carpeta de trabajo
WORKDIR /app

# Copiar archivos de la app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py ./ 
COPY templates ./templates
COPY static ./static

# Carpeta donde se guardarán las descargas
VOLUME /downloads

# Exponer puerto
EXPOSE 5000

# Ejecutar la app
CMD ["python", "app.py"]
