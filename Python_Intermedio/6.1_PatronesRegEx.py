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

patron = r"[lL]ección"  # ['lección']
print(re.match(patron, texto2).group())

patron = r"[0-9]"  # ['6']
print(re.findall(patron, texto))

patron = r"[eE]sta"  # Esta
print(re.match(patron, texto).group())

# Detiene la búsqueda en la primera coincidencia de "ón", en lugar de continuar hasta la última posible.
patron = r"[lL].*?ón"  # ['la lección', 'Lección']
print(re.findall(patron, texto))

# Muestra todas las letras sin incluír el número 6.
# Con \d mostraría solo el 6
patron = r"\D"  # ['E', 's', 't', 'a', ' ', 'e', 's'....]
print(re.findall(patron, texto))

# Captura palabras que contengan l o L en cualquier parte
patron = r"\w*[lL]\w*"  # ['la', 'lección', 'Lección', 'llamada', 'Regulares']
print(re.findall(patron, texto))

# Captura solo la l/L y el siguiente caracter
patron = r"[lL]."  # ['la', 'le', 'Le', 'll', 'la']
print(re.findall(patron, texto))


"""
^[a-zA-Z0-9]+ → La parte del usuario debe comenzar con una letra o número.
[_.+-]* → Permite caracteres especiales (_ . + -) después de la primera letra o número.
@[a-zA-Z0-9-]+ → La parte del dominio permite letras, números y -
\.[a-zA-Z]{2,}$ → Asegura que el TLD (.com, .org, etc.) tenga al menos 2 letras.
"""
patronMail = r"^[a-zA-Z0-9]+[_.+-]*@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"

print(re.match(patronMail, "usuario@dominio.com"))


"""
\b → Límite de palabra: Asegura que el número no esté dentro de otra palabra.
\d{9} → Nueve dígitos seguidos (\d significa "cualquier número" y {9} indica que deben ser exactamente 9).
\b → Límite de palabra: Evita que detecte parte de un número más largo.
re.search(patron, texto) → Busca el primer número de 9 dígitos seguidos en el texto.
"""
texto = "Mi número es 609318531"
patron = r"\b\d{9}\b"
telefono = re.search(patron, texto)
if telefono:
    print("Teléfono: ", telefono.group())
