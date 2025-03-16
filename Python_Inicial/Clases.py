# class Coche:
#     def __init__(self):
#         self.largo = 250
#         self.ancho = 120
#         self.ruedas = 4
#         self.peso = 900
#         self.color = "rojo"
#         self.is_enMarcha = False

# Los constructores pueden aceptar parámetros para personalizar la inicialización de objetos
# class Coche:
#     def __init__(self, largo, ancho, ruedas, peso, color, is_enMarcha):
#         self.largo = largo
#         self.ancho = ancho
#         self.ruedas = ruedas
#         self.peso = peso
#         self.color = color
#         self.is_enMarcha = is_enMarcha
# coche_1 = Coche(400, 160, 4, 1200, "amarillo", True)


# DESTRUCTORES
# Un método especial (__del__) que se usa para eliminar un objeto y liberar recursos


# class Vehiculo:
#     def __init__(self, marca, modelo):
#         self.marca = marca
#         self.modelo = modelo
#     # def __del__(self): # Se elimina automáticamente al acabar la ejecución
#     #     print("El objeto acaba de ser eliminado")


# class Coche(Vehiculo):  # Coche hereda de Vehiculo
#     def resumen(self):
#         print(f"Marca: {self.marca}, Modelo: {self.modelo}")


# class Coche2(Coche):
#     pass


# miCoche = Coche("Toyota", "Corolla")
# print(miCoche.marca)  # Salida: Toyota

# coche2 = Coche2("Renault", "Clio")
# coche2.resumen()  # Marca: Renault, Modelo: Clio


class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f"Color: {self.color}, Ruedas: {self.ruedas}"


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__() + f", Velocidad: {self.velocidad} km/h"


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + f", Tipo: {self.tipo}"


vehiculo = Vehiculo("Rojo", 4)
print(vehiculo)  # Color: Rojo, Ruedas: 4

coche = Coche("Azul", 4, 150)
print(coche)  # Color: Azul, Ruedas: 4, Velocidad: 150 km/h

bicicleta = Bicicleta("Blanca", 2, "Urbano")
print(bicicleta)  # Color: Blanca, Ruedas: 2, Tipo: Urbano
