# import random

# # Imprimir un valor random de la lista
# lista = [10, 30, 40, 502, 203, 44]
# print(lista)
# print(random.choice(lista))
# print(random.shuffle(lista))


# # Pedir varios números al usuario
# a, b, c = map(int, input("Introduce los números: ").split())
# print("Los números son: ", end=" ")
# print(a, b, c)

# # Pedir nombre y apellidos
# nombre, ape1, ape2 = input(
#     "Introduce tu nombre y apellidos: ").split()
# print("Datos: ", end=" ")
# print(nombre, ape1, ape2)

# # Versión mejorada
# nombre, *apellidos = input("Introduce tu nombre y apellidos: ").split()
# print("Datos:", nombre, " ".join(apellidos))


# # Saber si un número introducido es número o no
# num = input("Introduce un número: ")
# lista = list()
# if num.isdigit():
#     num = int(num)
#     lista.append(num)
#     print(f"Número {num} añadido a la lista")
# else:
#     print("No es número")


# # Ejercicio registar/modificar o consultar DNI
# registro = {"123456789L": 21, "863417311A": 41}
# print("1. Añadir o modificar un DNI \n2. Consultar edad")
# try:
#     accion = int(input("\tSelecciona una opción: "))
#     if accion == 1:
#         dni = input("Escribe el DNI: ").strip()
#         try:
#             edad = int(input("Escribe la edad: "))
#             registro[dni] = edad
#             print("DNI agregado/modificado correctamente.")
#         except ValueError:
#             print("Error: La edad debe ser un número entero.")
#     elif accion == 2:
#         dni = input("Escribe el DNI: ").strip()
#         if dni in registro:
#             print(f"La edad de {dni} es {registro[dni]}")
#         else:
#             print("Ese DNI no existe en el registro.")
#     else:
#         print("Opción fuera del menú!")
# except ValueError:
#     print("Error: Debes introducir un número válido.")
# print("Registro actualizado:", registro)

# # Recorrer un diccionario
# dicc = {"uno": 1, "dos": 2, "tres": 3}
# for x in dicc.values():
#     print(x) # 1 2 3

# for x in dicc:
#     print(x) # uno dos tres

# for x in dicc:
#     print(dicc[x]) # 1 2 3
    
# for x in dicc.items():
#     print(x) # ('uno', 1) ('dos', 2) ('tres', 3)