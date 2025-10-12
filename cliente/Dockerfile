# Imagen base de Python
#FROM python:3.10-slim

# Crear directorio de trabajo
#WORKDIR /app

# Copiar dependencias
#COPY requirements.txt .

# Instalar dependencias
#RUN pip install --no-cache-dir -r requirements.txt

# Copiar el cliente
#COPY cliente.py .

# Comando por defecto (ejecuta cliente.py)
#CMD ["python", "cliente.py"]

#--------------------------------------

# Imagen base de Python
#FROM python:3.10-slim

# Directorio de trabajo
#WORKDIR /app

# Dependencias
#COPY requirements.txt .
#RUN pip install --no-cache-dir -r requirements.txt

# Copiar el cliente
#COPY cliente.py .

# Comando por defecto (ejecuta cliente.py)
#CMD ["python", "cliente.py"]
#----------------------------------------------
    # Imagen base de Python
# Imagen base
# Imagen base liviana de Python
# Imagen base liviana de Python
FROM python:3.10-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar dependencias e instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código del cliente y archivo JSON
COPY cliente.py .
COPY data.json .

# Configurar variable de entorno para conexión con el servidor
ENV SERVER_HOST=host.docker.internal
ENV SERVER_PORT=5001
ENV API_URL=http://${SERVER_HOST}:${SERVER_PORT}

# Comando por defecto: ejecuta el cliente interactivo
CMD ["python", "cliente.py"]



