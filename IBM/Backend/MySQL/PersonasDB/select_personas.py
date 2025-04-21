import mysql.connector  # Importamos el conector de MySQL para conectar Python con la base de datos

# Establecemos la conexión a la base de datos
personas_db = mysql.connector.connect(
    host="localhost",        # Dirección del servidor de la base de datos
    user="root",             # Usuario para autenticarte en MySQL
    password="1234",         # Contraseña del usuario
    database="personas_db"  # Nombre de la base de datos con la que queremos interactuar
)

# Creamos un cursor para ejecutar consultas en la base de datos
cursor = personas_db.cursor()

# Ejecutamos una consulta SQL para seleccionar todos los registros de la tabla 'personas'
cursor.execute("SELECT * FROM personas")

# Obtenemos todos los resultados de la consulta (todos los registros)
resultado = cursor.fetchall()

# Recorremos los resultados y los imprimimos
for persona in resultado:
    print(persona)

# Cerramos el cursor para liberar recursos
cursor.close()

# Cerramos la conexión con la base de datos
personas_db.close()

