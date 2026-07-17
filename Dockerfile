# 1. Usar una imagen oficial de Python ligera
FROM python:3.10-slim

# 2. Crear una carpeta de trabajo dentro del contenedor
WORKDIR /app

# 3. Instalar las herramientas que usamos
RUN pip install fastapi uvicorn

# 4. Copiar nuestro código a la caja
COPY main.py .

# 5. El comando para encender la app (igual que lo hacíamos a mano)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
