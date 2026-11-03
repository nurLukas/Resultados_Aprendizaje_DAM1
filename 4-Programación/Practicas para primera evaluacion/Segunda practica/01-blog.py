                                    # Importamos Flask.
from flask import Flask
                                    # Creamos la aplicación.
aplicacion = Flask(__name__)
                                    # Página principal.
@aplicacion.route("/")
def inicio():
    return "Mi blog"
                                    # Arrancamos el servidor.
if __name__ == "__main__":
    aplicacion.run()
