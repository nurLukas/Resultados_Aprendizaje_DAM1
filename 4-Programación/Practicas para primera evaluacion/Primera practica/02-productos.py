                                                                                # Importamos Flask, la herramienta que permite crear la aplicación web.
from flask import Flask

                                                                                # Creamos nuestra aplicación.
                                                                                # __name__ permite a Flask identificar el módulo donde la estamos creando
aplicacion = Flask(__name__)

                                                                                # Guardamos una lista de nombres de frutas en la variable productos.
productos = ["mazana", "pera", "platano", "fresas"]

                                                                                # Indicamos qué función debe ejecutarse cuando alguien visita la dirección "/".
                                                                                # "/" es la página principal: http://127.0.0.1:5000/
@aplicacion.route("/")

                                                                                # Definimos esa función y la llamamos inicio.
                                                                                # Las líneas con sangría debajo pertenecen a esta función.
def inicio():
	return productos

                                                                                # Comprobamos si estamos ejecutando este archivo directamente con Python.
if __name__ == "__main__":
	aplicacion.run()