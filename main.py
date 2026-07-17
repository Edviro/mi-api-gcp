from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "online", "mensaje": "¡Hola versión 2.0 automatizada desde GitHub Actions! 🚀",}

@app.get("/usuarios")
def get_usuarios():
    return [{"id": 1, "nombre": "Edu"}, {"id": 2, "nombre": "Admin"}]
