from flask import Flask, request

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

                                                                            # Recibimos el formulario enviado mediante POST.
@aplicacion.route("/guardar", methods=["POST"])
def guardar():
                                                                            # Leemos los campos usando sus nombres del HTML.
    print("Título:", request.form["titulo"])
    print("Fecha:", request.form["fecha"])
    print("Texto:", request.form["texto"])

                                                                                # Respondemos al navegador.
    return "Datos recibidos"

if __name__ == "__main__":
	aplicacion.run()