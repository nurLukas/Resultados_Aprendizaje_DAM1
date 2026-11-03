from flask import Flask

aplicacion = Flask (__name__)

productos = ["manzana", "pera", "platano", "fresas"]
                                                                            # Asociamos la dirección principal "/" con la función que viene debajo.
@aplicacion.route("/")
def inicio():
                                                                            # Empezamos con un texto vacío donde iremos guardando el HTML.
    salida = ""
    
                                                                            # Recorremos la lista: en cada vuelta, producto contiene una fruta.
    for producto in productos:
                                                                            # Construimos un artículo HTML con el nombre de esa fruta.
                                                                            # += añade ese artículo al texto que ya contiene salida.
         salida += "<article><h4>" + producto + "</h4></article>"
                                                                            # Enviamos todo el HTML al navegador después de terminar el bucle.
    return salida

                                                                            # Si ejecutamos este archivo directamente, arrancamos el servidor.
if __name__ == "__main__":
    aplicacion.run()