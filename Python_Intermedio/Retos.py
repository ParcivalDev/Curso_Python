# ------------------------------------
#              Retos
# ------------------------------------

"""
# 1 EL FAMOSO "FIZZ BUZZ"
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""
print("***********************")
print('1 EL FAMOSO "FIZZ BUZZ"')
print("***********************")


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)


fizzbuzz()


"""
# 2 ¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

print("\n***********************")
print('2 ¿ES UN ANAGRAMA?')
print("***********************")


def anagrama(palabra1: str, palabra2: str):
    if palabra1 == palabra2:
        return False
    return sorted((palabra1.lower())) == sorted((palabra2.lower()))


print(anagrama("hola", "hola"))  # False
print(anagrama("hola", "alhO"))  # True
print(anagrama("hola", "adios"))  # False

# def anagrama(palabra1: str, palabra2: str):
#     lista1 = list(palabra1.lower())
#     lista2 = list(palabra2.lower())

#     if lista1 == lista2:
#         return False
#     lista1.sort()
#     lista2.sort()

#     if lista1 == lista2:
#         return True
#     else:
#         return False


# def anagrama2(first_string: str, second_string: str):
#     if first_string == second_string:
#         return False
#     if len(first_string) == len(second_string):

#         for i in first_string:

#             if i not in second_string:

#                 return False

#             else:
#                 return True
#     else:
#         return False


"""
# 3 LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
la que el siguiente siempre es la suma de los dos anteriores.
0, 1, 1, 2, 3, 5, 8, 13...
 """
print("\n***********************")
print('3 LA SUCESIÓN DE FIBONACCI')
print("***********************")
a = 0
b = 1
for i in range(50):
    print(a)
    original = a
    a = b
    b = original + b


"""
# 4 ¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""
print("\n***********************")
print('4 ¿ES UN NÚMERO PRIMO?')
print("***********************")


def primo():
    for num in range(101):
        if num >= 2:
            divisible = False
            for n in range(2, num):
                if num % n == 0:
                    divisible = True
                    break
            if not divisible:
                print(num)


primo()


""" 
# 5 ÁREA DE UN POLÍGONO
Crea una única función (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
- La función recibirá por parámetro sólo UN polígono a la vez.
- Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
- Imprime el cálculo del área de un polígono de cada tipo.
"""
print("\n***********************")
print('5 ÁREA DE UN POLÍGONO')
print("***********************")


def calcularArea(poligono):
    if poligono == "triángulo":
        print("\nÁREA TRIÁNGULO")
        b = int(input("Introduce la base: "))
        a = int(input("Introduce la altura: "))
        return f"El área del triángulo es de {(b*a)/2}"

    elif poligono == "cuadrado":
        print("\nÁREA CUADRADO")
        lado = int(input("Introduce el lado: "))
        return f"El área del cuadrado es de {lado**2}"

    elif poligono == "rectángulo":
        print("\nÁREA RECTÁNGULO")
        an = int(input("Introduce el ancho: "))
        la = int(input("Introduce el largo: "))
        return f"El área del rectángulo es de {an*la}"


# print(calcularArea("triángulo"))
# print(calcularArea("cuadrado"))
# print(calcularArea("rectángulo"))



""" 
# 7 INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""
print("\n***********************")
print('7 INVIRTIENDO CADENAS')
print("***********************")

palabra = "Hola mundo"
palabra2 = ""

# for i in palabra[::-1]:
#     palabra2 += i
    
# print(palabra2)

# len -1 para obtener la última posición
# que pare en el -1 para incluír el índice 0
# los pasos son de -1
for i in range(len(palabra)-1, -1, -1):
    palabra2 += palabra[i]
print(palabra2)

