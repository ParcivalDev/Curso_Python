# ------------------------------------
#               Patrones
#        Expresiones regulares
# ------------------------------------

# # """

# # ────────────────────────────────────────────────────────────────────────────────
# # |  Símbolo  |  Significado                       |  Ejemplo                    |
# # |-----------|---------------------------------|--------------------------------|
# # |  .        | Cualquier carácter (excepto \n) | "a.b" → "acb", "a9b"           |
# # |  ^        | Inicio de la cadena             | "^Hola" → "Hola mundo" ✅      |
# # |  $        | Fin de la cadena                | "mundo$" → "Hola mundo" ✅     |
# # |  \d       | Dígitos (0-9)                   | "\d+" → "2024", "a123b"       |
# # |  \w       | Letras, números o _             | "\w+" → "Python3", "Hola_mundo" |
# # |  \s       | Espacios en blanco              | "\s+" → "  " (espacio/tab)    |
# # |  *        | 0 o más repeticiones            | "ab*c" → "ac", "abc", "abbc"  |
# # |  +        | 1 o más repeticiones            | "ab+c" → "abc", "abbc" (no "ac") |
# # |  ?        | 0 o 1 repetición                | "colou?r" → "color", "colour" |
# # |  {n,m}    | Entre n y m repeticiones        | "\d{2,4}" → "99", "2024"      |
# # |  []       | Conjunto de caracteres          | "[aeiou]" → "a", "e", "o"     |
# # |  |        | Alternativa (OR)                | "Python|Java" → "Python", "Java" |
# # |  ()       | Agrupar subexpresiones          | "(ab)+" → "ab", "abab"        |
# # ──────────────────────────────────────────────────────────────────────────────


import re

texto = "Esta es la lección número 6: Lección llamada Expresiones Regulares"
texto2 = "lección número 6: Lección llamada Expresiones Regulares"

# patron = r"[lL]ección"  # ['lección']
# print(re.match(patron, texto2).group())

# patron = r"[0-9]"  # ['6']
# print(re.findall(patron, texto))

# patron = r"[eE]sta"  # Esta
# print(re.match(patron, texto).group())

# # Detiene la búsqueda en la primera coincidencia de "ón", en lugar de continuar hasta la última posible.
# patron = r"[lL].*?ón"  # ['la lección', 'Lección']
# print(re.findall(patron, texto))

# # Muestra todas las letras sin incluír el número 6.
# # Con \d mostraría solo el 6
# patron = r"\D"  # ['E', 's', 't', 'a', ' ', 'e', 's'....]
# print(re.findall(patron, texto))

# Captura palabras que contengan l o L en cualquier parte
patron = r"\w*[lL]\w*"  # ['la', 'lección', 'Lección', 'llamada', 'Regulares']
print(re.findall(patron, texto))

# Captura solo la l/L y el siguiente caracter
patron = r"[lL]."  # ['la', 'le', 'Le', 'll', 'la']
print(re.findall(patron, texto))





# patron = r"\b\d{9}\b"
# telefono = re.search(patron, texto)
# if telefono:
#     print("Teléfono: ", telefono.group())
# patronMail = r".+@[a-zA-Z]+\.[a-zA-Z]{2,}"
# mail = re.search(patronMail, texto)
# if mail:
#     print("Mail:", mail.group())
