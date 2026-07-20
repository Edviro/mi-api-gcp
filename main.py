import os
from fastapi import FastAPI
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# Carga las variables del archivo .env localmente
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Crea el motor de conexión
engine = create_engine(DATABASE_URL)

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "API funcionando correctamente"}

@app.get("/probar-db")
def probar_db():
    # Intenta hacer una consulta simple a PostgreSQL
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            return {"estado": "Conexión exitosa a Cloud SQL 🚀", "resultado": result.scalar()}
    except Exception as e:
        return {"estado": "Error al conectar", "detalle": str(e)}