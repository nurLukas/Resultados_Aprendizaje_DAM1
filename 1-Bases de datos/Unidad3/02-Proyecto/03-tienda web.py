# Mostramos nuestro catálogo con Flask, HTML y CSS.
from flask import Flask
import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='nurlukas',
    password='tame123',
    database='sturmprojekt'
)

cursor = connection.cursor()

aplicacion = Flask(__name__)


@aplicacion.route("/")
def inicio():

    # Cabecera y estilos básicos.
    cabeza = """
    <!doctype html>
    <html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Servicios Sturmprojekt</title>
        <style>
            body {
                background: grey;
                font-family: sans-serif;
            }
            header, main, footer {
                background: white;
                padding: 20px;
                margin: auto;
                max-width: 800px;
            }
            article {
                padding: 15px;
                border: 1px solid grey;
                margin-bottom: 15px;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Sturmprojekt</h1>
            <p>Catálogo de servicios</p>
        </header>
        <main>
    """

    cuerpo = ""

    # Recuperamos nombre, descripción y precio.
    cursor.execute(
        "SELECT nombre, descripcion, precio FROM servicios"
    )
    filas = cursor.fetchall()

    # Creamos una ficha para cada servicio.
    for fila in filas:
        cuerpo += """
        <article>
            <h2>""" + str(fila[0]) + """</h2>
            <p>""" + str(fila[1]) + """</p>
            <p>Precio: """ + str(fila[2]) + """ €</p>
        </article>
        """

    piedepagina = """
        </main>
        <footer>
            <p>Proyecto final de Bases de Datos — Unidad 3</p>
        </footer>
    </body>
    </html>
    """

    return cabeza + cuerpo + piedepagina


if __name__ == "__main__":
    aplicacion.run()