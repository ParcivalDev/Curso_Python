# Split para dividir una cadena
cadena = " Ejemplo para split  "
# Divide cadena por los espacios o por ejemplo por comas .split(",")
lista = cadena.split()
print(lista)


# Replace
cadena_nueva = cadena.replace("split", "replace")
print(cadena_nueva)


# Find
cadena_find = cadena.find("split")
print(cadena_find)  # 13 posición


# Strip - Limpiar cadena de espacios al principio y final
print(cadena)
print(cadena.strip())


# Lambda argumentos: expresión
def suma(num1, num2):
    """Comentario interior"""
    return num1 + num2

# resultado = lambda num1, num2: num1 + num2
# print(resultado(5,10))


# Con map y lambda
# Creamos una lista de números
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)  # [1, 4, 9, 16, 25]

# Con filter y lambda
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4]

# sorted() para ordenar elementos en una nueva lista
# sort() para modificar la lista original
num_desordenados = [4, 6, 2, 76, 1, 54, 23]
num_ordenados = sorted(num_desordenados)
print(num_ordenados)  # [1, 2, 4, 6, 23, 54, 76]


# Ordenar un diccionario por clave
empleados_dict = [
    {"nombre": "Manuel", "edad": 33},
    {"nombre": "Sara", "edad": 44},
    {"nombre": "Paula", "edad": 36}
]

empleados_ordenados = sorted(empleados_dict, key=lambda x: x["edad"])
print(empleados_ordenados)


# sum()
resultado = sum(num_desordenados)
print(resultado)  # 166

resultado = sum(num_desordenados, 1000)
print(resultado)  # 1166


# next()
iterador = iter(num_desordenados)
print(next(iterador, "Fin"))



# Sin compresión de listas
cuadrados = []
for x in range(1,6):
    cuadrados.append(x**2)
print(cuadrados) 

# Con compresión de listas
cuadrados = [x**2 for x in range(1,6)]
print(cuadrados)
    
    
    
pares = [x for x in range(1,7) if x % 2 == 0]
print(pares)

clasificacion = [f"par: {x}" if x%2==0 else f"impar: {x}" for x in range(5)]
print(clasificacion)

