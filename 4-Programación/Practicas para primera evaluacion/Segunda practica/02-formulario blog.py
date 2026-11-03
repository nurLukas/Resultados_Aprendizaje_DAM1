from flask import Flask

aplicacion = Flask(__name__)

																		# Página principal: muestra el formulario.
@aplicacion.route("/")
def inicio():
    return """
    <form action="/guardar" method="POST">
        <input type="text" name="titulo" placeholder="Título">
        <input type="date" name="fecha">
        <textarea name="texto" placeholder="Texto"></textarea>
        <button type="submit">Guardar</button>
    </form>
    """
	
if __name__ == "__main__":
	aplicacion.run()