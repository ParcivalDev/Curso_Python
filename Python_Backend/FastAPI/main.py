""" 
Ejecuta el servidor en vivo: fastapi dev main.py 
"""

""" 
Al construir APIs, normalmente usas estos métodos HTTP específicos para realizar una acción específica.

(CRUD) Normalmente usas:
POST: para crear datos.
GET: para leer datos.
PUT: para actualizar datos.
DELETE: para eliminar datos. """


from fastapi import FastAPI
app = FastAPI()  # crea instancia de FastAPI


@app.get("/saludo")  # http://127.0.0.1:8000/saludo
async def root():  # asíncrono para poder llamar al servidor sin bloquear el resto de la app
    return {"message": "Hola Mundo"}


@app.get("/curso")
async def url():
    return {"url": "https://mouredev.com/python"}


# Puedes declarar "parámetros" o "variables" de path con la misma sintaxis que se usa en los format strings de Python
@app.get("/item/{item_id}")  # 127.0.0.1:8000/item/hola
async def leer_item(item_id):
    return {"item_id": item_id}  # "item_id": "hola" o "item_id": 2


# Si ponemos un valor que no sea un entero saltará un error
# Ej: "hola", 6.8
@app.get("/itemInt/{item_id}") 
async def leer_item(item_id: int):
    return {"item_id": item_id}
