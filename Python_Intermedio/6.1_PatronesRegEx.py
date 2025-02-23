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





# patron = r"\b\d{9}\b"
# telefono = re.search(patron, texto)
# if telefono:
#     print("Teléfono: ", telefono.group())
# patronMail = r".+@[a-zA-Z]+\.[a-zA-Z]{2,}"
# mail = re.search(patronMail, texto)
# if mail:
#     print("Mail:", mail.group())
