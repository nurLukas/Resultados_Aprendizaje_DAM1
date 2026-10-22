# Consultamos los servicios desde Python.
import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='nurlukas',
    password='tame123',
    database='sturmprojekt'
)

cursor = connection.cursor()

cursor.execute("SELECT nombre, descripcion, precio FROM servicios")
filas = cursor.fetchall()

for fila in filas:
    print(fila)

cursor.close()
connection.close()