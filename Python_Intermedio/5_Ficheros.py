# ------------------------------------
#             Ficheros
# ------------------------------------

# Ficheros .txt
# archivo_txt = open("Python_Intermedio/Ficheros/archivo.txt", "w+")
# archivo_txt.write("ParcivalDev\nPython\n2025\n")

# # "w+" borra el contenido del archivo inmediatamente al abrirlo. Se usa para sobreescribir
# # "r+" permite leer y escribir sin borrar el contenido
# print("***Lectura***")
# print(archivo_txt.read())

# archivo_txt.write("\nHola")
# archivo_txt.seek(0)  # Movemos el puntero al inicio para volver leer
# print("\n***Nueva lectura***")
# print(archivo_txt.read())

# archivo_txt.seek(0)
# print("\n***Lectura por número de caracteres***")
# print(archivo_txt.read(10)) # ParcivalDe

# archivo_txt.seek(0)
# print("\n***Lectura por línea***")
# print(archivo_txt.readline()) # ParcivalDev
# # print(archivo_txt.readlines()) # Devuelve un array con cada elemento


# archivo_txt.seek(0)
# for i in archivo_txt.readlines():
#     print(i, end="")  # end para evitar saltos de línea debido al readlines

# archivo_txt.seek(0, 2)  # Mover el puntero al final del archivo
# lista = ["Hola", " y ", "adios"]  # Lista de strings
# archivo_txt.writelines(lista)
# archivo_txt.seek(0)  # Mover el puntero al inicio para leer

# print(archivo_txt.read())
# archivo_txt.close()
# # Borrar fichero
# import os
# os.remove("Python_Intermedio/Ficheros/archivo.txt")


# Fichero .json
import json

# Diccionario con datos JSON
ejemplo_json = {
    "nombre": "ParcivalDev",
    "lenguaje": "Python",
    "año": 2025,
    "curso": "Curso de PYTHON desde CERO para PRINCIPIANTES [Intermedio]"
}

# 1️⃣ Escribir en el archivo JSON
with open("Python_Intermedio/Ficheros/archivo.json", "w") as archivo_json:
    # Guardar el diccionario en formato JSON con indentación
    json.dump(ejemplo_json, archivo_json, indent=4)

# 2️⃣ Leer el archivo JSON
with open("Python_Intermedio/Ficheros/archivo.json", "r") as archivo_json:
    # Cargar el JSON desde el archivo y convertirlo a un diccionario
    data = json.load(archivo_json)

# 3️⃣ Imprimir el contenido
print(data)
# {'nombre': 'ParcivalDev', 'lenguaje': 'Python', 'año': 2025, 'curso': 'Curso de PYTHON desde CERO para PRINCIPIANTES [Intermedio]'}

# Segunda opción
# Solo abre el archivo una vez permitiendo que sea más rápido pero si falla la escritura también puede fallar la lectura
# import json

# # Diccionario con estructura JSON
# ejemplo_json = {
#     "nombre": "ParcivalDev",
#     "lenguaje": "Python",
#     "año": 2025,
#     "curso": "Curso de PYTHON desde CERO para PRINCIPIANTES [Intermedio]"
# }

# # Usamos 'with open()' para abrir el archivo en modo escritura y lectura
# with open("Python_Intermedio/Ficheros/archivo.json", "w+") as archivo_json:
#     # Convierte el diccionario a JSON y lo escribe en el archivo
#     json.dump(ejemplo_json, archivo_json, indent=4)  # indent=4 para un formato legible

#     # Mueve el puntero al inicio del archivo para poder leerlo
#     archivo_json.seek(0)

#     # Lee el contenido JSON del archivo y lo carga como un diccionario de Python
#     data = json.load(archivo_json)

# # Imprime el contenido que se leyó del archivo
# print(data)
