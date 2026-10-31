from flask import Flask

apliacion = Flask(__name__)

@apliacion.route("/")
def inicio():
	return "Hola desde Python"
	
if __name__ == "__main__":
	apliacion.run()