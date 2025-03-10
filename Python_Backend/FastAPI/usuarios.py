from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Usuario(BaseModel):
    id: int | None = None
    nombre: str
    lenguaje: str
    url_curso: str | None = None
    edad: int


# 📌 LISTA GLOBAL
lista_usuarios = [
    Usuario(id=1, nombre="Carlos", lenguaje="Python",
            url_curso="https://python.org", edad=34),
    Usuario(id=2, nombre="Ana", lenguaje="JavaScript", url_curso=None, edad=28),
    Usuario(id=3, nombre="Antonio", lenguaje="Java",
            url_curso="https://www.java.com/es/", edad=62),
]

# Iniciar el server: fastapi dev usuarios.py
# 127.0.0.1:8000/usuarios


# 📌 GET: Devuelve la lista de usuarios
@app.get("/usuarios")
async def usuarios():
    return lista_usuarios


# 📌 GET: Devuelve el usuario por id desde el path
@app.get("/usuario/{id}")
async def usuario(id: int):  # Poner int para que espere un entero y funcione
    # # Solo devuelve uno
    # for i in lista_usuarios:
    #     if i.id == id:
    #         return i
    # return {"mensaje": "Usuario no encontrado"}

    # Devuelve todos con ese id o si ponemos [0] devolverá el primero
    return buscar_usuario(id)


# 📌 GET: Devuelve el usuario por id desde una query
# 127.0.0.1:8000/usuarioquery/?id=1
# OJO La query es el conjunto de pares clave-valor que van después del ? en una URL, separados por caracteres &.
@app.get("/usuarioquery/")
async def usuario(id: int):
    return buscar_usuario(id)


# Función para buscar usuarios
def buscar_usuario(id: int):
    usuarios = filter(lambda usuario: usuario.id == id, lista_usuarios)
    try:
        return list(usuarios)[0]
    except:
        return {"mensaje": "Usuario no encontrado"}


# 📌 POST: Agrega un nuevo usuario
@app.post("/usuarios/nuevo")
async def crear_usuario(usuario: Usuario):
    # Verificamos si el ID ya existe (solo si se proporcionó un ID)
    if usuario.id is not None:
        resultado = buscar_usuario(usuario.id)
        if not isinstance(resultado, dict):  # Si no es un dict, el ID ya existe
            return {"error": "El ID indicado pertenece a otro usuario"}

    if usuario.id is None:  # Solo asignamos el id si no fue enviado por el cliente
        # Asignamos un id basado en el tamaño de la lista
        usuario.id = len(lista_usuarios) + 1
    lista_usuarios.append(usuario)  # Agregamos el usuario a la lista
    return usuario


# 📌 PUT: Actualiza un usuario
@app.put("/actualizar/{id}")
async def modificar(id: int, usuario_mod: Usuario):
    usuario = buscar_usuario(id)

    if isinstance(usuario, dict):  # Si no se encontró el usuario
        return usuario

# 127.0.0.1:8000/actualizar/1
# {"nombre": "María", "lenguaje": "TypeScript", "edad": 29}
# {"mensaje": "Usuario actualizado con éxito",
#   "usuario": {"id": 1,"nombre": "María","lenguaje": "TypeScript","url_curso": "https://python.org","edad": 29}
# }
    usuario.nombre = usuario_mod.nombre
    usuario.lenguaje = usuario_mod.lenguaje
    usuario.url_curso = usuario_mod.url_curso
    usuario.edad = usuario_mod.edad

    return {
        "mensaje": "Usuario actualizado con éxito",
        "usuario": usuario
    }
