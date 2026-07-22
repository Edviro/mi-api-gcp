import os
from fastapi import FastAPI, File, UploadFile
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from google.cloud import storage

# Carga las variables del archivo .env localmente
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
NOMBRE_BUCKET = "bucket_de_giles_devs"  # ⚠️ Reemplaza con el nombre exacto de tu bucket

# Crea el motor de conexión
engine = create_engine(DATABASE_URL)

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "API funcionando correctamente"}

@app.get("/probar-db")
def probar_db():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            return {"estado": "Conexión exitosa a Cloud SQL 🚀", "resultado": result.scalar()}
    except Exception as e:
        return {"estado": "Error al conectar", "detalle": str(e)}

@app.post("/subir-archivo")
async def subir_archivo(file: UploadFile = File(...)):
    try:
        # Inicializa el cliente de Cloud Storage
        storage_client = storage.Client()
        bucket = storage_client.bucket(NOMBRE_BUCKET)
        
        # Define el nombre y sube el archivo
        blob = bucket.blob(file.filename)
        blob.upload_from_file(file.file, content_type=file.content_type)
        
        url_publica = f"https://storage.googleapis.com/{NOMBRE_BUCKET}/{file.filename}"
        return {"estado": "Archivo subido con éxito 🚀", "url": url_publica}
    except Exception as e:
        return {"estado": "Error al subir archivo", "detalle": str(e)}
