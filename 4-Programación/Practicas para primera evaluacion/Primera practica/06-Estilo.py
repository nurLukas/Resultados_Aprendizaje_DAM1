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
                                                                    # Asociamos la página principal con la función inicio.
@aplicacion.route("/")
def inicio():
                                                                    # Guardamos el principio de la página.
                                                                        # Las triples comillas permiten escribir un texto en varias líneas.
    principio = """
    <!doctype html>
    <html lang="es">
      <head>
        <meta charset="utf-8">
        <title>Tienda de deportes</title>

        <style>
          /* Aspecto general de la página. */
          body {
            background: grey;          /* Fondo gris. */
            font-family: Arial;        /* Tipo de letra. */
          }

          /* Aplicamos las mismas reglas a estas tres zonas. */
          header, main, footer {
            background: white;         /* Fondo blanco. */
            width: 800px;              /* Ancho de cada zona. */
            padding: 20px;             /* Espacio interior entre el borde y el contenido. */
            margin: auto;              /* Centra las zonas horizontalmente. */
            text-align: center;        /* Centra el texto. */
          }

          /* Organizamos los productos en columnas. */
          section {
            display: grid;                        /* Activa una cuadrícula. */
            grid-template-columns: repeat(3, 1fr); /* Crea tres columnas iguales. */
            gap: 20px;                            /* Separa los productos. */
          }

          /* Aspecto de cada producto. */
          article {
            border: 1px solid lightgrey; /* Borde fino gris claro. */
            padding: 15px;               /* Espacio interior. */
          }
        </style>

      </head>
        
      <body>
        <header>
          <h1>Tienda de deportes</h1>
        </header>
        <main>
          <h2>Catálogo de productos</h2>
          <section>
    """

                                                                        # Preparamos el texto donde guardaremos los productos.
    medio = ""

                                                                            # Recorremos los productos, igual que en el ejercicio anterior.
    for producto in productos:
                                                                                # Añadimos un artículo con nombre, descripción y precio.
        medio += "<article>"
        medio += "<h4>" + producto["nombre"] + "</h4>"
        medio += "<p>" + producto["descripcion"] + "</p>"
        medio += "<p>" + str(producto["precio"]) + " €</p>"
        medio += "</article>"

                                                                                    # Cerramos la zona de productos y añadimos el pie de página.
    final = """
          </section>
        </main>
        <footer>
          <p>Tienda de deportes — 2026</p>
        </footer>
      </body>
    </html>
    """

                                                                                            # Unimos las tres partes y enviamos la página completa al navegador.
    return principio + medio + final

                                                                                                        # Arrancamos el servidor al ejecutar este archivo directamente.
if __name__ == "__main__":
    aplicacion.run()