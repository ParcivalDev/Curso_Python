# ------------------------------------
#              Paquetes
# ------------------------------------

# pip
# pip list
# pip unistall pandas
# pip show numpy (ver info)
# pip install pip
# Instalar cualquier paquete. Ejemplo numpy
# pip install numpy

import numpy

print(numpy.version.version)

mi_array= numpy.array([10, 20, 30, 50, 40])
print(type(mi_array))
print(mi_array * 2) # [ 20  40  60 100  80]

lista = [10,20,30,50,40]
print(lista * 2) # [10, 20, 30, 50, 40, 10, 20, 30, 50, 40]


import requests

respuesta = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(respuesta)
data = respuesta.json()
for pokemon in data["results"]:
    print(pokemon["name"])
 