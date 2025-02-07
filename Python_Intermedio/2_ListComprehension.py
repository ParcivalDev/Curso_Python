# ------------------------------------
#          List Comprehension
# ------------------------------------

lista_original = [0, 1, 2, 3, 4, 5, 6, 7]
#lista = [i for i in range(0,8)]
lista = [i for i in range(8)] # [0, 1, 2, 3, 4, 5, 6, 7]

print(lista_original)
print(lista)

lista_v2 = [i * 2 for i in lista_original]
print(lista_v2) # [0, 2, 4, 6, 8, 10, 12, 14]