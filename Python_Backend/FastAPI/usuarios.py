from fastapi import FastAPI

app = FastAPI()

# Iniciar el server: fastapi dev usuarios.py

@app.get("/usuarios")
async def usuarios():
    return "Hola usuario"