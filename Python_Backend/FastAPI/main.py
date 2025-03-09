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


from pydantic import BaseModel
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


# La primera siempre será utilizada ya que el path coincide primero. Esta segunda nunca se llega a mostrar
@app.get("/itemInt/{item_id}")
async def leer_item(item_id: int):
    return {"item_id 2": item_id}


# Parámetros de Query
# http://127.0.0.1:8000/items/?skip=0&limit=2
# Resultado: [ {"item_uno": "Uno"}, {"item_dos": "Dos"}]
# Devuelve un slice de la lista. Ee 0 a 10 devuelve los primeros 10
# Lista de diccionarios: [{}, {}, {}]
# Al añadir otro elemento al primer diccionario devuelve esos dos elementos
items_db = [{"item_uno": "Uno", "ola": "adios"},
            {"item_dos": "Dos"}, {"item_Tres": "Tres"}]


@app.get("/items/")
async def buscar_item(skip: int = 0, limit: int = 10):
    return items_db[skip: skip + limit]


# ------------
# Request Body
# ------------
# Cuando necesitas enviar datos desde un cliente (digamos, un navegador) a tu API, los envías como un request body.
# Un request body es un dato enviado por el cliente a tu API. Un response body es el dato que tu API envía al cliente.

# Necesitamos crear nuestro modelo de datos heredando de BaseModel
# Con None marcamos opcionales. El resto son obligatorios
class Producto(BaseModel):
    nombre: str
    descripcion: str | None = None
    precio: float


@app.post("/productos/")
async def crear_producto(producto: Producto):
    producto.nombre = producto.nombre.upper()
    return producto

# Seleccionamos POST con la url: http://127.0.0.1:8000/productos
# En body escribimos:
# {
#   "nombre": "Casco",
#   "precio": 324.56
# }
# y nos devuelve:
#     {
#   "nombre": "CASCO",
#   "descripcion": null,
#   "precio": 324.56
# }
