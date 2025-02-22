# ------------------------------------
#         Expresiones regulares
# ------------------------------------
# Se usan para validar formatos, extraer información o reemplazar caracteres en cadenas de texto.
# Python proporciona el módulo re para trabajar con expresiones regulares.

# """
# 🛠️ Principales funciones del módulo re
# 1️⃣ re.search(patron, texto) → Busca la primera coincidencia en el texto.

# texto = "Me gusta programar en Python y también en JavaScript"
# resultado = re.search(r"Python", texto)
# if resultado:
#     print("Coincidencia:", resultado.group())  # ✅ "Python"


# 2️⃣ re.findall(patron, texto) → Devuelve todas las coincidencias como una lista.

# texto = "Python es un lenguaje. Python es muy popular."
# resultado = re.findall(r"Python", texto)
# print(resultado)  # ✅ ['Python', 'Python']


# 3️⃣ re.match(patron, texto) → Comprueba si el texto empieza con el patrón.

# texto = "Python es un lenguaje poderoso"
# resultado = re.match(r"Python", texto)
# if resultado:
#     print("Coincidencia:", resultado.group())  # ✅ "Python"
# else:
#     print("No encontrado")

# resultado = re.match(r"lenguaje", texto)  # ❌ No está al inicio
# print(resultado)  # None


# 4️⃣ re.fullmatch(patron, texto) → Comprueba si toda la cadena coincide con el patrón.

# texto = "Python123"
# resultado = re.fullmatch(r"[A-Za-z0-9]+", texto)
# if resultado:
#     print("Texto válido")  # ✅ "Texto válido"
# else:
#     print("Texto inválido")

# Si ponemos un espacio "Python 123" ya daría error y tendríamos que añadir al patrón \s -> [A-Za-z0-9\s]+

# 5️⃣ re.sub(patron, reemplazo, texto) → Reemplaza coincidencias en el texto.
# 6️⃣ re.split(patron, texto) → Divide la cadena usando el patrón como separador.
# 7️⃣ re.compile(patron) → Compila el patrón para usarlo varias veces de manera eficiente.


# """

# ────────────────────────────────────────────────────────────────────────────────
# |  Símbolo  |  Significado                       |  Ejemplo                    |
# |-----------|---------------------------------|--------------------------------|
# |  .        | Cualquier carácter (excepto \n) | "a.b" → "acb", "a9b"           |
# |  ^        | Inicio de la cadena             | "^Hola" → "Hola mundo" ✅      |
# |  $        | Fin de la cadena                | "mundo$" → "Hola mundo" ✅     |
# |  \d       | Dígitos (0-9)                   | "\d+" → "2024", "a123b"       |
# |  \w       | Letras, números o _             | "\w+" → "Python3", "Hola_mundo" |
# |  \s       | Espacios en blanco              | "\s+" → "  " (espacio/tab)    |
# |  *        | 0 o más repeticiones            | "ab*c" → "ac", "abc", "abbc"  |
# |  +        | 1 o más repeticiones            | "ab+c" → "abc", "abbc" (no "ac") |
# |  ?        | 0 o 1 repetición                | "colou?r" → "color", "colour" |
# |  {n,m}    | Entre n y m repeticiones        | "\d{2,4}" → "99", "2024"      |
# |  []       | Conjunto de caracteres          | "[aeiou]" → "a", "e", "o"     |
# |  |        | Alternativa (OR)                | "Python|Java" → "Python", "Java" |
# |  ()       | Agrupar subexpresiones          | "(ab)+" → "ab", "abab"        |
# ──────────────────────────────────────────────────────────────────────────────


import re

texto = "Mi número es 612345678 y mi correo es ejemplo@email.com"

texto_dos = "Mi número no es 612345678 y mi correo es ejemplo@email.com"

# # <re.Match object; span=(0, 12), match='Mi número es'>
# print(re.match("Mi número es", texto))
# print(re.match("Mi número es", texto_dos))  # None
# # None porque match busca desde el principio
# print(re.match("número es", texto))
# print(re.search("número es", texto))  # Encuentra la primera coincidencia
# print(re.fullmatch(texto, texto))  # Necesita toda la cadena

# match = re.match("Mi número es", texto)
# print(match.group())  # Mi número es


# inicio, final = match.span()  # (0, 12) rango donde lo encuentra
# print(texto[inicio:final])  # Mi número es





# patron = r"\b\d{9}\b"

# telefono = re.search(patron, texto)

# if telefono:
#     print("Teléfono: ", telefono.group())


# patronMail = r".+@[a-zA-Z]+\.[a-zA-Z]{2,}"

# mail = re.search(patronMail, texto)

# if mail:
#     print("Mail:", mail.group())
