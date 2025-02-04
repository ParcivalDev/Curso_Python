# # Ejercicios curso Python desde cero de https://campus.mouredev.pro/

# # ------------------------------------
# #           HOLA MUNDO
# # ------------------------------------
# # Imprime "¡Hola Mundo!" por consola.
# print("¡Hola Mundo!")
# # print('¡Hola Mundo!')

# # Usa la función type() para imprimir el tipo de dato de una cadena de texto, un número entero y un número decimal
# print(type("Texto"))  # <class 'str'>
# print(type(1))  # <class 'int'>
# print(type(1.2))  # <class 'float'>

# # Imprime el resultado de concatenar dos cadenas de texto, por ejemplo: "Hola" y "Mundo".
# print("Hola" + " Mundo")

# # Crea una variable para almacenar tu nombre, otra para tu edad, e imprime ambas en la misma línea.
# mi_nombre = "Borja"
# edad = 27
# print("Mi nombre es ", mi_nombre, " y tengo ", edad, " años")
# print(f"Mi nombre es {mi_nombre} y tengo {edad} años")

# # Escribe un programa que solicite al usuario su nombre y lo imprima junto con un saludo.
# """
# nombreUsuario = input("Inserte su nombre: ")
# print("Tu nombre es: ", nombreUsuario)
# """


# # ------------------------------------
# #           VARIABLES
# # ------------------------------------
# # Concatenaciójn de variables en un print
# print(mi_nombre, edad)

# # Funciones del sitema
# print(len(mi_nombre))  # 5

# # Variables en una lína
# dia, mes, anho = 30, "Febrero", 1990
# print("Fecha: ", dia, mes, anho)

# # Convierte un número decimal, almacenado en la variable price, a un número entero y luego imprímelo
# precio = 3.14
# precio_entero = int(precio)
# print(precio, " como decimal y ", precio_entero, " como entero")

# # Forzar el tipo de dato no funciona porque Python usa tipado dinámico
# # La anotación de tipo solo le indica al programador lo que se espera
# phone: int = 666666
# print(type(phone))  # <class 'int'>
# phone = "444444"
# print(type(phone))  # <class 'str'>

# # ¿Qué imprime este código? print("Hola", "Python")
# # HolaPython      Hola Python      Hola, Python
# print("Hola", "Python")


# # ------------------------------------
# #           OPERADORES
# # ------------------------------------
# # Aritméticos
# print("\nOPERADORES Aritméticos")
# print(10 + 2)  # 12
# print(10 - 2)  # 8
# print(10 * 2)  # 20
# print(10 ** 2)  # 100 (elevado a)
# print(10 / 2)  # 5.0
# print(10 // 2)  # 5
# print(10 % 3)  # 1 (Sería el resto de la operación)

# print("Hola" + "Python")  # HolaPython
# print("Hola" * 2)  # HolaHola
# print("No se puede mezclar con números sin pasarlos a str: " + str(5))

# # Comparativos
# print("\nOPERADORES Comparativos")
# print(5 < 4)  # False
# print(5 > 4)  # True
# print(5 <= 4)  # False
# print(5 >= 4)  # True
# print(5 == 5)  # True
# print(5 != 5)  # False
# print("adios" >= "bala")  # False (ordenación alfabética)
# print(len("adios") >= len("bala"))  # True (cuenta caracteres)
# print("Hola" == "Hola")  # True

# # Lógicos
# print("\nOPERADORES Lógicos")
# print(5 > 4 and "adios" > "bala")  # True and False -> False
# print(5 > 4 or "adios" > "bala")  # True or False -> True
# print(5 < 4 or "adios" < "bala")  # False or True -> True
# print(not 5 < 4)  # True o print(not (5 < 4))
# print(not not 3 < 2)  # not not False -> not True -> False


# # ------------------------------------
# #           STRINGS
# # ------------------------------------
# print("\nSTRINGS")
# # Salto de línea con \n y tabulación con \t
# print("Mostrar \\t sin tabular")

# # Formateo
# titulo, genero, anho = "Interstellar", "Ciencia ficción", 2014
# print("Mi película favorita es {} que es de {} del año {}".format(titulo, genero, anho))
# print("Mi película favorita es %s que es de %s del año %d" %
#       (titulo, genero, anho))
# print(f"Mi película favorita es {titulo} que es de {genero} del año {anho}")

# # Desempaquetado de caracteres
# lenguaje = "python"
# a, b, c, d, e, f = lenguaje
# print(a)  # P
# print(e)  # o

# porcion_lenguaje = lenguaje[1:4]
# print(porcion_lenguaje)  # yth

# porcion_lenguaje = lenguaje[2:]
# print(porcion_lenguaje)  # thon

# porcion_lenguaje = lenguaje[-2:]
# print(porcion_lenguaje)  # on

# porcion_lenguaje = lenguaje[:-3]
# print(porcion_lenguaje)  # Pyt

# # Saltos
# porcion_lenguaje = lenguaje[::2]
# print(porcion_lenguaje)  # Pto Va des 0 hasta : 0 saltando de : 2 en 2

# # Reverse
# reversed_lenguaje = lenguaje[::-1]
# print(reversed_lenguaje)  # nohtyP

# # Funciones
# print("\nFunciones en Strings")
# print(lenguaje.capitalize())  # Pone primera en mayúscula
# print(lenguaje.upper())  # Pone todo en mayúscula
# print(lenguaje.count("t"))  # Cuenta cuantas 't' hay
# print(lenguaje.isnumeric())  # Comprueba si es un número
# print(lenguaje.lower())  # Pone todo en minúsculas
# # Pone todo en mayúsculas y comprueba si está en mayúsculas
# print(lenguaje.upper().isupper())
# print(lenguaje.startswith("py"))  # Sensible a mayúsculas


# # ------------------------------------
# #           LISTAS - Mutables
# # ------------------------------------

# mi_lista = list()
# otra_lista = []

# mi_lista = [0, 1, 2, 3, 4, 3]
# print(mi_lista)  # [0,1,2,3,4,2]
# print(len(mi_lista))  # 6

# # Búsqueda
# print(4 in mi_lista)

# otra_lista = [3, 1.3, "Python"]

# print(otra_lista[2])  # Python o [-1]
# print(mi_lista.count(3))  # 2

# entero, decimal, string = otra_lista  # Desempaquetar en variables
# print(decimal) # 1.3

# # Sumar listas
# print(mi_lista + otra_lista) # [0, 1, 2, 3, 4, 3, 3, 1.3, 'Python']
# # ERROR: print(mi_lista - otra_lista)

# mi_lista.append("Nuevo elemento")
# print(mi_lista)
# mi_lista.insert(0, "Primer elemento") # ['Primer elemento', 0, 1, 2, 3, 4, 3, 'Nuevo elemento']
# print(mi_lista)

# mi_lista.remove(3) # Solo elimina un 3
# print(mi_lista)

# print(mi_lista.pop()) # Nuevo elemento (elimina el último)
# print(mi_lista) # ['Primer elemento', 0, 1, 2, 4, 3]

# # También se puede hacer un pop de una posición concreta pop(2)


# del mi_lista[0:2]
# print(mi_lista) # [1, 2, 4, 3] Elimina desde el primero(0) hasta la posición 2 sin incluírla

# """
# remove() -> busca por valor y elimina la primera coincidencia
# pop() -> elimina por índice y devuelve el elemento eliminado. Si no especificas índice, elimina el último
# del -> elimina por índice o slice (0:2)
# clear() -> elimina toda la lista
# """

# # Cambiar valor elemento de X posición
# mi_lista[0] = "Primer elemento"
# print(mi_lista) # ['Primer elemento', 2, 4, 3]


# mi_lista_dos = mi_lista.copy()
# print(mi_lista_dos)
# mi_lista.remove(3)
# print(mi_lista_dos) # ['Primer elemento', 2, 4, 3]

# """
# Con .copy() creamos una lista independiente con los mismos valores
# Sin .copy() creamos otra referencia a la misma lista  y al borrar un elemento en una se elimina en la otra
# """

# mi_lista_dos.reverse() # Da la vuelta a la lista
# print(mi_lista)
# print(mi_lista_dos) # [3, 4, 2, 'Primer elemento']

# mi_lista_dos.remove("Primer elemento") # Eliminación para evitar error al ordenar strings con ints
# mi_lista_dos.sort()
# print(mi_lista_dos) # [2, 3, 4] Lista ordenada

# sublista = mi_lista[1:]
# print(sublista) # [2, 4] Sublista


# # Ordenar lista todo como strings
# lista_variada = [66, 65, 32, "A", "F", "B"]
# # Se convierte cada elemento a string con key = str
# lista_variada.sort(key=str)
# print(lista_variada)  # [32, 65, 66, 'A', 'B', 'F']


# # ------------------------------------
# #           TUPLAS - Inmutables
# # ------------------------------------
# mi_tupla = tuple()
# otra_tupla = (1000, 3000)  # OJO paréntesis no []

# # Búsqueda
# print(1000 in otra_tupla)

# mi_tupla = (32, 1.22, "ParcivalDev", "GitHub", 32)
# print(mi_tupla)  # (32, 1.22, 'ParcivalDev', 'GitHub')
# print(mi_tupla[2])  # ParcivalDev

# print(mi_tupla.count(32))  # 2 Cuenta los 32 en la tupla
# print(mi_tupla.index(32))  # Posición del primer 32 -> 0

# # mi_tupla[0] = 12 Una tupla es INMUTABLE por lo que no podemos ni modificar ni añadir nuevos elementos ni eliminarlos

# # Pero sí que podemos crear una nueva sumando entre ellas
# nueva_tupla = mi_tupla + otra_tupla
# print(nueva_tupla)  # (32, 1.22, 'ParcivalDev', 'GitHub', 32, 1000, 3000)

# # Subtupla
# print(nueva_tupla[1:5])  # (1.22, 'ParcivalDev', 'GitHub', 32)

# # Si necesitamos modificar la tupla podemos pasarla a lista y luego volver pasarla a tupla
# mi_tupla = list(mi_tupla)
# mi_tupla.append("Valor desde Lista")
# mi_tupla = tuple(mi_tupla)
# print(mi_tupla)  # [32, 1.22, 'ParcivalDev', 'GitHub', 32, 'Valor desde Lista']

# del mi_tupla  # Eliminamos para siempre la tupla


# # ------------------------------------
# #    SET - No ordenado / No repetidos
# # ------------------------------------
# mi_set = set()
# otro_set = {"ParcivalDev", "Python", 2025}

# print(len(otro_set))  # 3

# otro_set.add("MoureDev")
# print(otro_set)  # {2025, 'MoureDev', 'Python', 'ParcivalDev'}


# otro_set.add(2025)
# print(otro_set)  # Da el mismo resultado porque no admite repetidos

# # Búsqueda
# print(2025 in otro_set)

# # Eliminar
# otro_set.remove(2025)
# print(otro_set) # {'Python', 'ParcivalDev', 'MoureDev'}
# # Con clear vacía el set dejándo 0 elementos
# # Con del deja de existir el set

# mi_set.add("Curso Python")
# nuevo_set = mi_set.union(otro_set)
# print(nuevo_set) # {'Python', 'Curso Python', 'ParcivalDev', 'MoureDev'}

# nuevo_set = nuevo_set.difference(otro_set)
# print(nuevo_set) # {'Curso Python'}

# # Ejercicio
# mi_set = {1, 2, 3, 4}
# mi_set2 = {3, 4, 5, 6}
# nuevo = mi_set.difference(mi_set2)  # {1, 2}
# # Elementos que están en A o B, pero no en ambos
# nuevo = mi_set.symmetric_difference(mi_set2)
# print(nuevo)  # {1, 2, 5, 6}
# # Elementos que están en ambos conjuntos
# nuevo = mi_set.intersection(mi_set2)
# print(nuevo)  # {3, 4}


# # ------------------------------------
# #    DICCIONARIOS  - Clave/Valor
# # ------------------------------------
# mi_dic = dict()
# otro_dic = {}

# otro_dic = {"Nombre": "ParcivalDev", "Lenguaje": "Python", 2024: "Año"}
# mi_dic = {
#     "Nombre": "ParcivalDev",
#     2024: "Anho",
#     "Lenguajes": {"Python", "Java", "Kotlin"}}  # Contiene un set

# # {'Nombre': 'ParcivalDev', 2024: 'Anho', 'Lenguajes': {'Java', 'Python', 'Kotlin'}}
# print(mi_dic)
# print(mi_dic["Nombre"])  # ParcivalDev
# mi_dic[2024] = "Año pasado"
# print(mi_dic[2024])  # Año pasado

# mi_dic["Mes"] = "Enero"  # Se añade un nuevo campo clave-valor
# # {'Nombre': 'ParcivalDev', 2024: 'Año pasado', 'Lenguajes': {'Python', 'Kotlin', 'Java'}, 'Mes': 'Enero'}
# print(mi_dic)

# del mi_dic["Mes"]  # Elimina solo ese campo
# print(mi_dic)

# print("Nombre" in mi_dic)  # True
# print("ParcivalDev" in mi_dic)  # False porque estamos buscando la clave
# print("ParcivalDev" in mi_dic.values())  # True porque busca por el valor

# print(mi_dic.keys())  # dict_keys(['Nombre', 2024, 'Lenguajes'])

# nuevo_dic = mi_dic.fromkeys(("Uno", 2, "Nombre"))
# print(nuevo_dic) # {'Uno': None, 2: None, 'Nombre': None}

# # Ejercicios
# # Crea un diccionario donde las claves sean números del 1 al 5 y los valores sean sus cuadrados (ejemplo: 1: 1, 2: 4, ...).
# squares = {x: x**2 for x in range(1, 6)}
# print(squares)


# # Crea un nuevo diccionario a partir de una lista de claves ["name", "age", "job"] usando fromkeys(), asignando a todas las claves el valor "Desconocido".
# my_keys = ["name", "age", "job"]
# my_new_dict = dict.fromkeys(my_keys, "Desconocido")
# print(my_new_dict)


# # ------------------------------------
# #     CONDICIONALES - if/elif/else
# # ------------------------------------
# condicion = 5

# if condicion >= 6 and condicion <= 10:
#     print("Está entre 6 y 10")

# elif not condicion > 6:
#     print("Es menor que 6")
# else:
#     print("Es mayor que 10")

# print("Continúa")

# # Comprobar si es mayor o menor de edad. OJO al int()
# edad = int(input("edad:"))
# if edad >= 18:
#     print("mayor de edad")
# else:
#     print("menor de edad")

# # Escribe un programa que verifique si un número es divisible por 3 y por 5 al mismo tiempo.
# number = int(input("Introduce un número: "))
# if number % 3 == 0 and number % 5 == 0:
#     print(f"{number} es divisible por 3 y por 5")
# else:
#     print(f"{number} no es divisible por 3 y 5 al mismo tiempo")


# # ------------------------------------
# #        BUCLES - while / for
# # ------------------------------------
# # WHILE
# Ejecuta código mientras una condición sea verdadera.
# num = 0

# while num < 10:
#     # end tiene valor predeterminado \n pero podemos ponerle un espacio para que se muestre todo en la misma línea
#     print(num, end=" ")  # 0 2 4 6 8
#     num += 2
# else:
#     print("Fin del bucle")
# print("Continúa")


# while num < 20:
#     num += 1
#     if num == 15:
#         print("Mi número es igual a 15")
#         break # Salimos del bucle cuando el valor es 15
#     print(num)
# print("Continúa")

# # FOR
# # Se suele usar para iterar colecciones, listas, tuplas, sets y diccionarios.
# lista = [10, 23, 454, 12, 4]
# diccionario = {"Nombre": "ParcivalDev", "Curso": "Python", "Fecha": 2024}

# # Iterar lista
# for x in lista:
#     print(x)  # 10 23 454...

# # Iterar diccionario
# for x in diccionario:
#     print(x)  # Nombre Curso
#     if x == "Curso":
#         print(f"Hay una clave que es curso con valor {diccionario[x]}")
#         # Continúa el bucle pero saltando el print siguiente. Salta a la siguiente iteracción.
#         continue
#     print("-> Continúa iterando")
# else:
#     print("El bucle de diccionarios ha finalizado")


# # Iterar valores
# for valor in diccionario.values():
#     print(valor)

# # Iterar ambos
# for clave, valor in diccionario.items():
#     print(f"Clave: {clave}, Valor: {valor}")
#     # Clave: Nombre, Valor: ParcivalDev
#     # Clave: Curso, Valor: Python

# # Escribe un programa que use un bucle while para sumar
# # los números del 1 al 100 e imprime el resultado
# num = 1  # Inicializamos la variable en 1
# suma = 0  # Variable para almacenar la suma

# while num <= 100:  # Mientras el número sea menor o igual a 100
#     suma += num  # Añadimos el número actual a la suma
#     num += 1  # Incrementamos el número en 1

# print(f"La suma de los números del 1 al 100 es: {suma}")


# # Escribe un bucle for que imprima cada carácter de la cadena “Python”
# cadena = "Python"
# for c in cadena:
#     print(c)

# # Usa un bucle while para encontrar el primer número divisible por 7 entre 1 y 50.
# num = 1
# while num <= 50:
#     if num % 7 == 0:
#         print(f"El número {num} es divisible entre 7")
#         break
#     else:
#         print(f"El número {num} no es divisible entre 7")
#     num += 1


# # Usa un bucle for con la función range() para imprimir los números del 1 al 10 en orden inverso
# for x in range(10, 0, -1):
#     # Desde el 10 hasta el 1(no incluído) con paso de -1
#     print(x, end=" ") # 10 9 8 7 6 5 4 3 2 1 


# for i in range(3):
#     print(i) # 0 1 2