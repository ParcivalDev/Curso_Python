import mysql.connector

# Conexión a la base de datos
personas_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="personas_db"
)

# Creamos el cursor para ejecutar consultas
cursor = personas_db.cursor()

# Solicitamos los datos al usuario
cambio = input(
    "Indica el campo que quieres cambiar (nombre, apellido o edad): ").lower()
valor = input("Indica el nuevo valor: ")
id_persona = int(input("Indica el id: "))

# Ejecutamos la consulta SQL según el campo especificado
if cambio == "nombre":
    cursor.execute(
        "UPDATE personas SET nombre = %s WHERE id = %s", (valor, id_persona))
elif cambio == "apellido":
    cursor.execute(
        "UPDATE personas SET apellido = %s WHERE id = %s", (valor, id_persona))
elif cambio == "edad":
    cursor.execute(
        "UPDATE personas SET edad = %s WHERE id = %s", (valor, id_persona))
else:
    # Si el campo no es válido, se muestra un mensaje y se cierra todo
    print("ERROR: Cambio no permitido")
    cursor.close()
    personas_db.close()
    exit()

# Verificamos si la consulta afectó a alguna fila (es decir, si el ID existe)
if cursor.rowcount == 0:
    print("No se encontró ninguna persona con ese ID. No se hizo ningún cambio.")
else:
    # Confirmamos los cambios si hubo modificación
    personas_db.commit()
    print("Datos actualizados correctamente.")

# Cerramos el cursor y la conexión
cursor.close()
personas_db.close()
