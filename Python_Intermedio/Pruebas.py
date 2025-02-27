import random

# Imprimir un valor random de la lista
lista = [10, 30, 40, 502, 203, 44]
print(lista)
print(random.choice(lista))
print(random.shuffle(lista))


# Pedir varios números al usuario
a, b, c = map(int, input("Introduce los números: ").split())
print("Los números son: ", end=" ")
print(a, b, c)

# Pedir nombre y apellidos
nombre, ape1, ape2 = input(
    "Introduce tu nombre y apellidos: ").split()
print("Datos: ", end=" ")
print(nombre, ape1, ape2)

# Versión mejorada
nombre, *apellidos = input("Introduce tu nombre y apellidos: ").split()
print("Datos:", nombre, " ".join(apellidos))
