# # Función open()
# # open(nombre_archivo, modo)
# # r (leer), a (añadir), w (escribir), x (crear)
# # r+ (lectura y escritura)
# # w+ (lectura y escritura) Crea o sobreescribe
# # a+ (lectura y añadir)

# # Escritura
# with open("archivo.txt", "w+") as archivo:
#     archivo.write("Prueba")
#     archivo.write("\nnueva linea")
# print("---------------------")  

# # Creación en modo exclusivo
# try:
#     with open("archivo2.txt", "x") as archivo:
#         archivo.write("Prueba2")
#         archivo.write("\nnueva linea")
# except FileExistsError:
#     print(f"El archivo ya existe")
# print("---------------------")

# Lectura
try:
    with open("archivo.txt", "r") as archivo:
        # print(archivo.readlines())
        lista = archivo.readlines()
        for i in lista:
            print(i.strip())
except FileNotFoundError:
    print(f"El archivo no existe")
    
# print("---------------------")
try:
    with open("archivo.txt", "r") as archivo:
        print(archivo.read())
except FileNotFoundError:
    print(f"El archivo no existe")
    

# Añadir al archivo
try:
    with open("archivo.txt", "a") as archivo:
        archivo.write("Añadiendo info\n")
        archivo.write("Añadiendo nueva info\n")
except FileNotFoundError:
    print(f"El archivo no existe")