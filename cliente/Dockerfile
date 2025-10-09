# Imagen base de Python
FROM python:3.10-slim

# Crear directorio de trabajo
WORKDIR /app

# Copiar dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el cliente
COPY cliente.py .

# Comando por defecto (ejecuta cliente.py)
CMD ["python", "cliente.py"]
