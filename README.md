# Curso de Python 🚀

Este repositorio contiene material educativo para aprender Python desde nivel inicial hasta intermedio, desarrollado siguiendo los videos de MoureDev [Inicial](https://www.youtube.com/watch?v=Kp4Mvapo5kc) y [Intermedio](https://www.youtube.com/watch?v=TbcEqkabAWU). ¡Perfecto para principiantes! 📚

## Estructura del repositorio 📂

El repositorio se divide en las siguientes carpetas:

- **Python_Inicial**: Recursos y ejercicios para principiantes que están comenzando con Python. 🌱
- **Python_Intermedio**: Material para aquellos que desean profundizar en conceptos más avanzados de Python. 🌟

## Contenido de cada carpeta 📖

### Python_Inicial 🌱

En esta carpeta encontrarás:

- **Variables**: Almacena y manipula datos básicos. 🗃️
- **Operadores**: Realiza cálculos y comparaciones. ➕➖✖️➗
- **Strings**: Trabaja con cadenas de texto. ✏️
- **Listas**: Colecciones ordenadas y mutables. 📋
- **Tuplas**: Colecciones ordenadas e inmutables. 🔒
- **Sets**: Colecciones no ordenadas sin duplicados. 🧮
- **Diccionarios**: Pares clave-valor. 🔑
- **Condicionales**: Toma decisiones en el código. ❓
- **Bucles**: Repite acciones automáticamente. 🔄
- **Funciones**: Reutiliza bloques de código. 🔧
- **Clases**: Introduce la programación orientada a objetos. 🏛️
- **Excepciones**: Maneja errores de forma controlada. ⚠️
- **Módulos**: Organiza y reutiliza código en archivos separados. 📦

### Python_Intermedio 🌟

Esta sección incluye:

- **Fechas y horas** (`1_Datetime.py`): Manejo de objetos de fecha y hora en Python. ⏳
- **List Comprehension** (`2_ListComprehension.py`): Crea listas de forma concisa y avanzada. 📏
- **Lambdas y funciones anónimas** (`3_4_Lambdas_FunOrdenSup.py`): Funciones cortas y poderosas. ⚡
- **Ficheros** (`5_Ficheros.py`): Lectura y escritura de archivos. 📜
- **Expresiones regulares** (`6_ExpresionesRegulares.py`) y (`6.1_PatronesRegEx.py`): Manipulación avanzada de cadenas. 🔍
- **Paquetes** (`7_Paquetes.py`): Estructura y uso de paquetes en Python. 📚

## Resumen gráfico: Chuleta de Python 🗺️

### Python Inicial 🌱

| **Concepto**         | **Qué hace**                                   | **Cuándo usarlo**                          | **Ejemplo**                          |
|-----------------------|------------------------------------------------|--------------------------------------------|--------------------------------------|
| **Variables** 🗃️     | Almacena datos (números, texto, etc.)         | Guardar valores para usar después          | `nombre = "Ana", edad = 25`         |
| **Operadores** ➕     | Realiza cálculos o comparaciones              | Matemáticas o lógica                       | `5 + 3` → `8`, `10 > 7` → `True`    |
| **Strings** ✏️       | Maneja texto                                  | Mostrar mensajes o manipular texto         | `"Hola" + " Mundo"` → `"Hola Mundo"`, `"Python".upper()` → `"PYTHON"` |
| **Listas** 📋        | Colección ordenada y mutable                  | Datos que cambian o necesitan orden        | `[1, 2, 3]` → `[1, 2, 3, 4]` (con `.append(4)`), `[0, 1, 2][1]` → `1` |
| **Tuplas** 🔒        | Colección ordenada e inmutable                | Datos fijos que no cambiarán               | `(1, 2, 3)`, `(10, "hola")[0]` → `10` |
| **Sets** 🧮          | Colección no ordenada sin duplicados          | Eliminar repeticiones o buscar elementos   | `{1, 2, 2, 3}` → `{1, 2, 3}`, `3 in {1, 2, 3}` → `True` |
| **Diccionarios** 🔑  | Almacena pares clave-valor                    | Relacionar datos (como un diccionario real)| `{"nombre": "Ana", "edad": 25}`, `d["edad"]` → `25` |
| **Condicionales** ❓  | Toma decisiones según condiciones             | Ejecutar código según casos                | `if edad >= 18: print("Mayor")`, `if 5 > 3 else "No"` → `"Sí"` |
| **Bucles** 🔄        | Repite código automáticamente                 | Iterar listas o repetir tareas            | `for i in range(5): print(i)` → `0 1 2 3 4`, `while x < 3: x += 1` |
| **Funciones** 🔧     | Reutiliza bloques de código                   | Evitar repetir lógica                      | `def suma(a, b): return a + b` → `suma(2, 3)` → `5`, `len("hola")` → `4` |
| **Clases** 🏛️       | Define objetos con propiedades y métodos      | Modelar cosas reales (POO)                 | `class Perro: def ladrar(self): print("Guau")`, `p = Perro(); p.ladrar()` → `"Guau"` |
| **Excepciones** ⚠️   | Maneja errores sin que el programa falle      | Evitar crashes por entradas inesperadas    | `try: 5/0 except: print("Error")` → `"Error"`, `try: int("a") except ValueError: print("No")` → `"No"` |
| **Módulos** 📦       | Organiza código en archivos separados         | Proyectos grandes o reutilización          | `import math; math.pi` → `3.14...`, `from datetime import datetime` |

### Python Intermedio 🌟

| **Concepto**              | **Qué hace**                                   | **Cuándo usarlo**                          | **Ejemplo**                          |
|---------------------------|------------------------------------------------|--------------------------------------------|--------------------------------------|
| **Fechas y horas** ⏳     | Trabaja con fechas y tiempo                   | Calcular diferencias o mostrar fechas      | `datetime.now()` → `2025-03-01`, `datetime(2023, 1, 1).year` → `2023` |
| **List Comprehension** 📏 | Crea listas de forma rápida y elegante        | Simplificar bucles en una línea            | `[x*2 for x in range(5)]` → `[0, 2, 4, 6, 8]`, `[x for x in "hola" if x != "o"]` → `["h", "l", "a"]` |
| **Lambdas** ⚡            | Funciones anónimas cortas                     | Operaciones rápidas sin nombre            | `lambda x: x+1` → `2` (si x=1), `list(map(lambda x: x*2, [1, 2]))` → `[2, 4]` |
| **Ficheros** 📜          | Lee o escribe en archivos (txt, JSON, CSV)    | Guardar o cargar datos                     | `with open("file.txt", "r") as f: f.read()`, `json.dump({"a": 1}, open("data.json", "w"))` |
| **Expresiones regulares** 🔍 | Busca y manipula patrones en texto         | Validar emails, teléfonos, etc.            | `re.findall(r"\d+", "a123b")` → `["123"]`, `re.sub(r"o", "0", "hola")` → `"h0la"` |
| **Paquetes** 📚          | Usa librerías externas como NumPy o Requests  | Proyectos avanzados o APIs                 | `import numpy; numpy.array([1, 2])`, `requests.get("url").json()` |
