from pelicula import Pelicula
from servicio import Servicio

class Catalogo:

    def __init__(self):
        self.servicio = Servicio()

    def menu(self):
        print("*** Catálogo de películas ***\n")
        while True:
            try:
                print("""Opciones:
                    1. Añadir película
                    2. Listar películas
                    3. Eliminar catálogo
                    4. Salir""")
                opcion = int(input("Selecciona una opción: "))
                if opcion == 1:
                    nombre = input("Indica el nombre de la película: ")
                    pelicula = Pelicula(nombre)
                    self.servicio.agregar(pelicula)
                elif opcion == 2:
                    self.servicio.listar()
                elif opcion == 3:
                    self.servicio.eliminar_archivo()
                elif opcion == 4:
                    print("Saliendo...")
                    break
                else:
                    print("Opción fuera del menú. Introduce un valor entre 1 y 4")
            except ValueError:
                print("Error: Introduce un número válido.")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    app = Catalogo()
    app.menu()