from flask import Flask

aplicacion = Flask(__name__)
                                                                    # Guardamos los tres productos en una lista de diccionarios.
productos = [
    {
        "nombre": "Balon de futbol",
        "precio": 24.95,
        "descripcion": "Balón de tamaño reglamentario."
    },
    {
        "nombre": "Raqueta de tenis",
        "precio": 89.50,
        "descripcion": "Raqueta ligera de fibra de carbono."
    },
    {
        "nombre": "Guantes de boxeo",
        "precio": 79.99,
        "descripcion": "Listos para los guantasos."
    }
]
                                                                    # Asociamos la dirección principal con inicio.
@aplicacion.route("/")
def inicio():
    
    salida = ""
                                                                    # Dentro de la función, recorremos los productos.
    for producto in productos:
   
        salida += "<article>"
    
        salida += "<h4>" + producto["nombre"] + "</h4>"
    
        salida += "<p>" + producto["descripcion"] + "</p>"
    
        salida += "<p>" + str(producto["precio"]) + " €</p>"
    
        salida += "</article>"
                                                                    # Fuera del bucle, devolvemos todos los artículos juntos.
    return salida
                                                                    # Arrancamos el servidor.
if __name__ == "__main__":
    aplicacion.run()