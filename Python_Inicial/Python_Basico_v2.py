# # ------------------------------------
# #           FUNCIONES
# # ------------------------------------
# # Sin retorno
# def suma_resta(num1, num2, operacion: str):
#     operacion = operacion.lower()
#     # OJO Si no ponemos el tipo (:str) no aparece la ayuda de las funciones disponibles
#     # operacion = str(operacion).lower()
#     if operacion == "suma":
#         print(num1 + num2)
#     elif operacion == "resta":
#         print(num1-num2)
#     else:
#         print("Operación no existente")
# suma_resta(10, 5, "SumA")
# suma_resta(4, 6, "resta")


# # Con retorno
# def suma_v2(num1, num2):
#     return num1 + num2
# suma = suma_v2(10,2)
# print(suma)


# # Cambiar orden de entrada en los parámetros
# def nombre_completo(nombre, apellido):
#     print(f"{nombre} {apellido}")
# nombre_completo(apellido="Mota", nombre="Jose") # Jose Mota


# # Parámetros con valores por defecto
# def nombre_completo(nombre, apellido, alias = "Sin alias"):
#     print(f"{nombre} {apellido} {alias}")
# nombre_completo("Jose", "Mota", "Mota") # Jose Mota Mota
# nombre_completo("Jose", "Mota") # Jose Mota Sin alias

# # Función con un número variable de argumentos agrupados en una tupla
# def print_text(*texto):
#     print(texto)
# print_text("Hola", "que", "tal?") # ('Hola', 'que', 'tal?')

# def print_text(*texto):
#     for text in texto:
#         print(text.upper())
# print_text("Hola", "que", "tal?") # HOLA QUE TAL?


# # Ejercicio
# def nombre(*nom):
#     suma = 0
#     for num in nom:
#         suma += num
#     print(suma)
# nombre(1, 2, 3, 414, 543, 431, 4, 51, 55) # 1504


# # ------------------------------------
# #               CLASES
# # ------------------------------------
# class MiPersona:
#     def __init__(self, nombre, apellido, dni, anho = "2024"):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.lenguaje = "Python"
#         self.anho = anho
#         self.__dni = dni # Privado. No podemos acceder

#     def get_dni(sef):
#         return sef.__dni

#     def estudiar(self):
#         print(f"{self.nombre} está estudiando {self.lenguaje} desde el {self.anho}")


# persona1 = MiPersona("Paco", "Pérez", dni="1111111A")
# print(f"{persona1.nombre} {persona1.apellido}")  # Paco Pérez
# print(persona1.lenguaje) # Python
# persona1.estudiar() # Paco está estudiando Python
# persona2 = MiPersona("Manolo", "Pérez", 2022)
# persona2.estudiar() # Manolo está estudiando Python desde el 2022

# print(persona1.get_dni()) # 1111111A

# #EJERCICIO
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#         self.__speed = 0

#     def acelerate(self):
#         self.__speed += 10
#         return f"Estoy acelerando, voy a {self.__speed}"

#     def brake(self):
#         self.__speed = max(0, self.__speed - 10)
#         return f"Estoy frenando, voy a {self.__speed}"


# coche = Car("audi", "a4")

# print(f"Tengo un {coche.brand} {coche.model}") # Tengo un audi a4

# print(coche.acelerate()) # Estoy acelerando, voy a 10
# print(coche.brake()) # Estoy frenando, voy a 0
# print(coche.brake()) # Estoy frenando, voy a 0


# #EJERCICIO
# # Crea una clase "Estudiante" que tenga como propiedades su nombre, apellido y una lista de notas.
# # Añade un método para calcular y devolver la nota media del estudiante.
# class Estudiante:
#     def __init__(self, nombre, apellido, notas):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.notas = notas

#     def nota_media(self):
#         suma = sum(self.notas)
#         return suma / len(self.notas)


# estudiante = Estudiante("Manolo", "Pérez", [10, 5, 7, 8, 7, 9.5])


# print(f"El alumno {estudiante.nombre} {estudiante.apellido} tiene las siguientes notas:",
#       *estudiante.notas)  # El alumno Manolo Pérez tiene las siguientes notas: 10 5 7 8 7 9.5

# print(estudiante.nota_media())  # 7.75


# #EJERCICIO
# #Crea una clase "BankAccount" con propiedades como "owner" y "balance". Añade métodos para depositar y retirar dinero, asegurándote de que no se pueda retirar más de lo que hay en la cuenta
# class BackAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance

#     def dep_dinero(self, dinero):
#         self.balance += dinero

#     def quit_dinero(self, dinero):
#         if dinero > self.balance:
#             print("El importe a retirar supera el total")
#         else:
#             self.balance -= dinero

# cuenta = BackAccount("Pepe")
# print(f"Pepe tiene {cuenta.balance}€")  # Pepe tiene 0€
# cuenta.dep_dinero(1000)
# print(f"Pepe tiene {cuenta.balance}€")  # Pepe tiene 1000€
# cuenta.quit_dinero(2000)  # El importe a retirar supera el total
# cuenta.quit_dinero(100)
# print(f"Pepe tiene {cuenta.balance}€")  # Pepe tiene 900€


# # ------------------------------------
# #             EXCEPCIONES
# # ------------------------------------

# import math
# num1, num2 = 1, "2"
# try:
#     print(num1 + num2)
# except:  # Se ejecuta al producirse una excepción
#     print("error")
# else:  # Opcional - Se ejecuta si no se produce una excepción
#     print("Funciona")
# finally:  # Opcional - Se ejecuta siempre
#     print("fin")

# # Excepción por tipo
# try:
#     print(num1 + num2)
# except ValueError:
#     print("Error: ValueError")
# except TypeError:
#     print("Error: TypeError")


# # Captura información del error
# try:
#     print(num1 + num2)
# except TypeError as info_error:
#     print(f"Error: {info_error}")
# # Error: unsupported operand type(s) for +: 'int' and 'str'
# except Exception as info_error:
#     print(f"Error: {info_error}")
# # Para capturar la información de cualquier otro tipo de error
# # Es lo mismo que poner solo except: pero de esta manera obtenemos la información


# # Ejercicio
# # Crea una función que intente dividir dos números
# # proporcionados por el usuario. Usa try-except para
# # capturar cualquier error de división (por ejemplo,
# # división por cero)
# def division(num1, num2):
#     try:
#         print(num1/num2)
#     except ZeroDivisionError:
#         print("Error. No se puede dividir entre 0")
#     except Exception as e:
#         print(f"Error: {e}")


# num1 = int(input("Introduce el número 1: "))
# num2 = int(input("Introduce el número 2: "))

# division(num1, num2)

# # Ejercicio
# # Crea una función que intente convertir una lista de
# # cadenas en enteros. Maneja cualquier error que surja
# # cuando una cadena no pueda convertirse.
# def cadena_entero(lista):
#     enteros = []
#     for e in lista:
#         try:
#             enteros.append(int(e))
#         except Exception as error:
#             print(f"Error: {error}")
#     return enteros

# lista = ["1", "2a", "3", "4", "5"]
# print(lista)  # ['1', '2a', '3', '4', '5']
# # Error: invalid literal for int() with base 10: '2a'
# enteros = cadena_entero(lista)
# print(enteros)  # [1, 3, 4, 5]


# #Crea una función que realice múltiples operaciones
# # (suma, resta, división, multiplicación) con dos números.
# # Usa try-except-else-finally para manejar errores y
# # asegurar que se imprima un mensaje final,
# # independientemente de los errores.
# def operaciones(num1, num2):
#     try:
#         print(f"Suma: {num1 + num2}")
#         print(f"Resta: {num1 - num2}")
#         print(f"Multiplicación: {num1 * num2}")
#         print(f"División: {num1 / num2}")
#     except Exception as e:
#         print(f"Error: {e}")
#     else:
#         print("Operaciones realizadas correctamente")
#     finally:
#         print("Operaciones finalizadas")


# operaciones(3, 4)
# print("___________________________________")
# operaciones(-3, 4)
# print("___________________________________")
# operaciones(0, 4)
# print("___________________________________")
# operaciones(3, 0)


# # OJO   <-------------------
# # Crea una función que simule una transacción. Lanza una
# # excepción personalizada llamada InsufficientFundsError
# # si el saldo es menor que la cantidad a retirar.
# class DineroInsuficienteError(Exception):
#     pass


# def transacion(cuenta, retiro):
#     try:
#         if cuenta < retiro:
#             raise DineroInsuficienteError("Saldo insuficiente")
#         cuenta -= retiro
#         print(f"Transacción realizada. Nuevo saldo: {cuenta}")

#     except DineroInsuficienteError as e:
#         print(f"Error: {e}")


# # Crea una función que le pida al usuario su edad y lance
# # un ValueError si la entrada no es un número entero
# # positivo. Usa el manejo de excepciones para gestionar la
# # entrada y lanzar excepciones personalizadas cuando sea
# # necesario
# def edad():
#     try:
#         edad = int(input("Introduce tu edad: "))
#         if edad <= 0:
#             raise ValueError("Error, tu edad no puede ser menos de 1 año")
#     except ValueError as e:
#         print(f"Error: {e}") # Error: Error, tu edad no puede ser menos de 1 año
# edad()


# # Crea una función que abra un archivo, lea su contenido y
# # maneje posibles errores (por ejemplo, archivo no
# # encontrado). Usa try-except para gestionar las
# # operaciones de archivos de forma segura
# def abrirArchivo(archivo):
#     try:
#         with open(archivo, mode="r") as f:
#             contenido = f.read()
#             print(contenido)
#     except FileNotFoundError:
#         print("Error: Fichero no encontrado.")

# abrirArchivo("hola.txt")


# # ------------------------------------
# #              MÓDULOS
# # ------------------------------------
# import math  # Importar todo el módulo
# from math import pi as PI_VALUE  # Importar solo pi dándole un nuevo nombre
# from Funcion import suma

# suma(10, 4)  # Esto es una función que está en el archivo Funcion.py


# print(PI_VALUE)  # 3.14...
# print(math.pow(2, 3))  # 8.0


# # Ejercicio 1
# # Escribe un módulo que contenga una función que acepte
# # cualquier número de argumentos y devuelva su suma. Importa
# # y usa la función en otro archivo.

# from Operaciones import suma

# suma(6, 2, 9, 10) # Resultado: 27


# # Ejercicio 2
# # Crea un módulo que contenga una función para contar
# # cuántas veces aparece una palabra en un texto. Escribe un
# # programa que importe el módulo y lo use para contar
# # palabras en una cadena.
# from Operaciones import contar
# texto = "Hola, qué tal? Probando un ejercicio de Python de Mouredev"
# print(contar(texto, "de"))  # 2


# # Ejercicio 3
# # Escribe un módulo que contenga funciones para leer y
# # escribir en archivos de texto. Crea un programa que use
# # estas funciones para escribir y leer datos.
# from Operaciones import leerArchivo, escribirArchivo
# leerArchivo("Prueba.txt")  # Hola Mundo!
# escribirArchivo("Prueba.txt", "Hola Mundo!")
# leerArchivo("Prueba.txt")  # Hola Mundo!Hola Mundo!


# # Ejercicio 4
# # Crea un módulo llamado "dates" que contenga funciones
# # para obtener la fecha actual y calcular la diferencia
# # entre dos fechas. Usa este módulo en un programa para
# # mostrar la fecha actual y la diferencia entre dos fechas
# # específicas

# from Operaciones import fechaActual, restarFechas
# print(fechaActual())  # 26/01/2025
# restarFechas(fechaActual(), "25/01/2025")  # 1

## OJO
# # strptime -> Convertir una cadena en un objeto datetime.	"25/01/2025" a datetime(2025, 1, 25)
# # strftime -> Convertir un objeto datetime en una cadena.	datetime(2025, 1, 25)	"25/01/2025"


# Es True ya que la P está más lejos que la J
#print("Python">"Java")

