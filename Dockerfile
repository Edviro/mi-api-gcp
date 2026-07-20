# 1. Usar una imagen oficial de Python ligera
FROM python:3.10-slim

# 2. Crear una carpeta de trabajo dentro del contenedor
WORKDIR /app

# 3. Instalar las herramientas y librerías necesarias
RUN pip install fastapi uvicorn python-dotenv sqlalchemy psycopg2-binary

# 4. Copiar nuestro código a la caja
COPY main.py .

# 5. El comando para encender la app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]