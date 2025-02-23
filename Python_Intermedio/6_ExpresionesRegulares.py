# ------------------------------------
#         Expresiones regulares
# ------------------------------------
# # Se usan para validar formatos, extraer información o reemplazar caracteres en cadenas de texto.
# # Python proporciona el módulo re para trabajar con expresiones regulares.

# # """
# # 🛠️ Principales funciones del módulo re
# # 1️⃣ re.search(patron, texto) → Busca la primera coincidencia en el texto.

# # texto = "Me gusta programar en Python y también en JavaScript"
# # resultado = re.search(r"Python", texto)
# # if resultado:
# #     print("Coincidencia:", resultado.group())  # ✅ "Python"


# # 2️⃣ re.findall(patron, texto) → Devuelve todas las coincidencias como una lista.

# # texto = "Python es un lenguaje. Python es muy popular."
# # resultado = re.findall(r"Python", texto)
# # print(resultado)  # ✅ ['Python', 'Python']


# # 3️⃣ re.match(patron, texto) → Comprueba si el texto empieza con el patrón.

# # texto = "Python es un lenguaje poderoso"
# # resultado = re.match(r"Python", texto)
# # if resultado:
# #     print("Coincidencia:", resultado.group())  # ✅ "Python"
# # else:
# #     print("No encontrado")

# # resultado = re.match(r"lenguaje", texto)  # ❌ No está al inicio
# # print(resultado)  # None


# # 4️⃣ re.fullmatch(patron, texto) → Comprueba si toda la cadena coincide con el patrón.

# # texto = "Python123"
# # resultado = re.fullmatch(r"[A-Za-z0-9]+", texto)
# # if resultado:
# #     print("Texto válido")  # ✅ "Texto válido"
# # else:
# #     print("Texto inválido")

# # Si ponemos un espacio "Python 123" ya daría error y tendríamos que añadir al patrón \s -> [A-Za-z0-9\s]+

# # 5️⃣ re.sub(patron, reemplazo, texto) → Reemplaza coincidencias en el texto.
# # 6️⃣ re.split(patron, texto) → Divide la cadena usando el patrón como separador.
# # 7️⃣ re.compile(patron) → Compila el patrón para usarlo varias veces de manera eficiente.

import re

texto = "Mi número es 612345678 y mi correo Es ejemplo@email.com"
texto_dos = "Mi número no es 612345678 y mi correo es ejemplo@email.com"

# re.search
print("\n1️⃣  re.search(patron, texto) → Busca la primera coincidencia en el texto.")
# <re.Match object; span=(3, 12), match='número es'>
print(re.search("número es", texto))  # Encuentra la primera coincidencia

# re.findall
print("\n2️⃣  re.findall(patron, texto) → Devuelve todas las coincidencias como una lista.")
# re.I para ignorar mayúsculas y minúsculas
lista = re.findall("es", texto, re.I)
print(lista)  # ['es', 'Es']
print(len(lista))  # 2

# re.match
print("\n3️⃣  re.match(patron, texto) → Comprueba si el texto empieza con el patrón.")
# <re.Match object; span=(0, 12), match='Mi número es'>
print(re.match("Mi número es", texto))
print(re.match("Mi número es", texto_dos))  # None
# None porque match busca desde el principio no como search
print(re.match("número es", texto))

match = re.match("Mi número es", texto)
print(match.group())  # Mi número es
inicio, final = match.span()  # (0, 12) rango donde lo encuentra
print(texto[inicio:final])  # Mi número es

# re.fullmatch
print("\n4️⃣  re.fullmatch(patron, texto) → Comprueba si toda la cadena coincide con el patrón.")
print(re.fullmatch(texto, texto))  # Necesita toda la cadena


# re.sub
print("\n5️⃣  re.sub(patron, reemplazo, texto) → Reemplaza coincidencias en el texto.")
# re.I para que detecte el Mi número es y lo cambie
texto_cambiado = re.sub(
    "mi número es", "Mi número podría ser", texto, flags=re.I)
# Mi número podría ser 612345678 y mi correo Es ejemplo@email.com
print(texto_cambiado)

# Ejemplo cambiando número y correo
# patron = "mi (número|correo) es"
# def reemplazo(match):
#     if match.group(1).lower() == "número":
#         return "Mi número podría ser"
#     else:
#         return "mi correo podría ser"

# texto_cambiado = re.sub(
#     "mi (número|correo) es", reemplazo, texto, flags=re.I)
# # Mi número podría ser 612345678 y mi correo podría ser ejemplo@email.com
# print(texto_cambiado)


# re.split
print("\n6️⃣  re.split(patron, texto) → Divide la cadena usando el patrón como separador.")
# Mi número es 612345678 y mi correo Es ejemplo@email.com
# Devuelve: ['Mi número es 612345678 ', ' mi correo Es ejemplo@email.com']
print(re.split("y", texto))

