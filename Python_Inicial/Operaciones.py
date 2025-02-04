# Ejercicio 1
from datetime import datetime


def suma(*num):
    print(f"Resultado: {sum(num)}")


# Ejercicio 2
def contar(texto, palabra):
    # Todo a minúsculas
    # Quitamos puntos y comas
    # Con split dividimos en palabras
    # Con palabra en minúscula contamos cuantas son iguales
    palabras = texto.lower().replace('.', '').replace(',', '').split()

    palabra = palabra.lower()
    return palabras.count(palabra)


# Ejercicio 3
def leerArchivo(archivo):
    try:
        with open(archivo, mode="r") as f:
            contenido = f.read()
        print(contenido)
    except Exception as e:
        print(f"Error: {e}")


def escribirArchivo(archivo, texto):
    try:  # con w escribe eliminando y con a añade al final
        with open(archivo, mode="a") as f:
            f.write(texto)
    except Exception as e:
        print(f"Error: {e}")


# Ejercicio 4


def fechaActual():
    return datetime.now().strftime("%d/%m/%Y")


def restarFechas(fecha1, fecha2):
    fecha1 = datetime.strptime(fecha1, "%d/%m/%Y")
    fecha2 = datetime.strptime(fecha2, "%d/%m/%Y")
    resta = fecha1 - fecha2
    print(resta.days)
    
