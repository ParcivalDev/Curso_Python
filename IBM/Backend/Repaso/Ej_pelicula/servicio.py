import os


class Servicio:

    def __init__(self):
        self.nombre_archivo = "peliculas.txt"

    def agregar(self, pelicula):
        with open(self.nombre_archivo, "a", encoding="utf8") as archivo:
            archivo.write(f"{pelicula.nombre}\n")

    def listar(self):
        try:
            with open(self.nombre_archivo, "r", encoding="utf8") as archivo:
                print("---Listado de películas---")
                print(archivo.read())  # Leer todo el archivo
        except FileNotFoundError:
            print("Error: El catálogo todavía no existe")

    def eliminar_archivo(self):
        try:
            os.remove(self.nombre_archivo)
            print(f"Archivo eliminado: {self.nombre_archivo}")
        except FileNotFoundError:
            print("Error: El catálogo todavía no existe")
