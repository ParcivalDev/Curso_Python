from fastapi import FastAPI

app = FastAPI()


# Iniciar el server: fastapi dev usuarios.py
# 127.0.0.1:8000/usuarios
@app.get("/usuarios")
async def usuarios():
    return "Hola usuario"



