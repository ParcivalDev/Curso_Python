# ------------------------------------
#              Lambdas
#         Funciones anónimas
# ------------------------------------

suma = lambda valor1, valor2: valor1 + valor2
print(suma(10,30)) # 40


multiplicacion = lambda valor1, valor2: valor1 * valor2 - 10
print(multiplicacion(10,2)) # 10


def suma_tres_valores(valor):
    return lambda valor1, valor2: valor1 + valor2 + valor
print(suma_tres_valores(10)(4,1)) # 15
