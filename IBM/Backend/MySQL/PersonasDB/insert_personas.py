import mysql.connector

personas_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="personas_db"
)


cursor = personas_db.cursor()


nombre = input("Indica tu nombre: ")
apellido = input("Indica tu apellido: ")
edad = int(input("Indica tu edad: "))

# Ejecutamos una consulta SQL para insertar los datos en la tabla 'personas'
cursor.execute("INSERT INTO personas (nombre, apellido, edad) VALUES (%s, %s, %s)",
               (nombre, apellido, edad))  # Pasamos los valores como una tupla

# Confirmamos la transacción para guardar los cambios en la base de datos
personas_db.commit()

cursor.close()
personas_db.close()

# Imprimimos un mensaje de confirmación
print("Datos insertados correctamente.")
