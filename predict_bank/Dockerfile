# Imagen base
FROM python:3.11-slim

# Directorio de trabajo
WORKDIR /app

# Instalar utilidades necesarias para Kaggle
RUN apt-get update && apt-get install -y --no-install-recommends \
    unzip curl && \
    rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar la aplicación
COPY app/ ./app


# Copiar credenciales de Kaggle
COPY kaggle.json /root/.kaggle/kaggle.json
RUN chmod 600 /root/.kaggle/kaggle.json

# Crear carpeta de datos
RUN mkdir -p /app/datos
VOLUME ["/app/datos"]

# --- Selecciona el modo de arranque ---
# Modo interactivo (fase 1):
# CMD ["bash"]

# Modo servidor Flask (fase 2):
CMD ["python", "-m", "app.apirest"]
