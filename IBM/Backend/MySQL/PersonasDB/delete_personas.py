import mysql.connector

# Conexión a la base de datos
personas_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="personas_db"
)

# Creamos el cursor
cursor = personas_db.cursor()

# Sentencia SQL para borrar registros por nombre
sentencia_sql = "DELETE FROM personas WHERE nombre = %s"
valor = ("uno",)  # Tupla con un solo elemento

# Ejecutamos la sentencia
cursor.execute(sentencia_sql, valor)
personas_db.commit()

# Confirmamos cuántas filas se eliminaron
print(f"Se eliminaron {cursor.rowcount} fila(s).")

# Cerramos conexiones
cursor.close()
personas_db.close()
