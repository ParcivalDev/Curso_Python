# ------------------------------------
#              Lambdas
#         Funciones anónimas
# ------------------------------------
from functools import reduce
print("\n***Lambdas***")
def suma(valor1, valor2): return valor1 + valor2


print(suma(10, 30))  # 40


def multiplicacion(valor1, valor2): return valor1 * valor2 - 10


print(multiplicacion(10, 2))  # 10


def suma_tres_valores(valor):
    return lambda valor1, valor2: valor1 + valor2 + valor


print(suma_tres_valores(10)(4, 1))  # 15


# ------------------------------------
#     Funciones de orden superior
#    Pueden ejecutar otras funciones
# ------------------------------------
print("\n***Funciones de orden superior***")


def suma_uno(valor):
    return valor + 1


def resta_uno(valor):
    return valor - 1


def suma_dos_valores_y_fun(valor1, valor2, f_sum):
    return f_sum(valor1 + valor2)


print(suma_dos_valores_y_fun(5, 2, suma_uno))  # 8
print(suma_dos_valores_y_fun(5, 2, resta_uno))  # 6


# Closures
print("\nClosures")


def suma_diez(original):
    def anhade(value):
        return value + 10 + original
    return anhade


anhade = suma_diez(30)
print(anhade(5))  # 45

print(suma_diez(20)(5))  # 35


# Funciones de orden superior YA EXISTENTES
numeros = [2, 4, 1, 54]


# Map
def multiplica(num):
    return num * 2


# print(list(map(numeros))) ERROR map espera una función y un iterable
print(list(map(multiplica, numeros)))  # [4, 8, 2, 108]
print(list(map(lambda valor: valor * 2, numeros)))  # [4, 8, 2, 108]


# Filter
# Filtramos para obtener los valores mayores de 10
def filtrar(num):
    return num > 10
    # if num > 10:
    #         return True
    #     else:
    #         return False


print(list(filter(filtrar, numeros)))  # [54]
print(list(filter(lambda num: num > 10, numeros)))  # [54]


# Reduce
# Opera con un valor más el acumulado
# de numeros = [2, 4, 1, 54]
# 2 + 4 | 6 + 1 | 7 + 54
def suma_dos_valores(valor1, valor2):
    return valor1 + valor2


print(reduce(suma_dos_valores, numeros))  # 61
