
"""
    📌 ¿Qué es un decorador?
Un decorador es simplemente una función que recibe otra función y devuelve una función.
"""

# def mi_decorador(func):
#     def wrapper():
#         print("Antes de ejecutar la función")
#         func()
#         print("Después de ejecutar la función")
#     return wrapper

# @mi_decorador
# def saludar():
#     print("¡Hola!")

# saludar()


# def decorador(funcion):
#     def conjunto(*args, **kwargs):
#         print("Bienvenido!")
#         resultado = funcion(*args, **kwargs)
#         print("Hasta pronto!")
#         return resultado
#     return conjunto


# @decorador
# def saludar(nombre):
#     print(f"Hola {nombre}")


# saludar("Pepe")


def requiere_admin(func):
    def wrapper(usuario, *args, **kwargs):
        if usuario != "admin":
            print("Acceso denegado")
            return
        return func(usuario, *args, **kwargs)
    return wrapper


@requiere_admin
def eliminar_usuario(usuario, nombre):
    print(f"{nombre} ha sido eliminado por {usuario}")


print("Intento 1: ", end="")
eliminar_usuario("juan", "Marcos")
print("Intento 2: ", end="")
eliminar_usuario("admin", "Marcos")
