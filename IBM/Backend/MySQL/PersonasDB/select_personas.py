import mysql.connector

personas_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="personas_db"
)


cursor = personas_db.cursor()
cursor.execute("SELECT * FROM personas")
resultado = cursor.fetchall()

for persona in resultado:
    print(persona)
