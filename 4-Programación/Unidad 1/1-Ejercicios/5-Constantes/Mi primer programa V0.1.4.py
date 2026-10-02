print("-" * 70) # Esto es un detalle estético.
VERSION = "0.1.4"  # Esto es una CONSTANTE
print(f"Mi primer programa V{VERSION}")
print("-" * 70)

nombre = "Lucas Ezequiel"     # Aqui la variable tiene un literal str "Lucas Ezequiel"
apellidos = "Andrés Griego"

print("Diseñado por:")
print(nombre, apellidos)

print("-" * 70)

print("¿QUE ESTRUCTURA DEBERIA SEGUIR UN PROGRAMA INFORMÁTICO?")


# Un programa estandar, se ordena de la siguiente forma:

# Primero van las importaciones de librerías

# Luego las declaraciones de las funciones y clases

# A continuación las variables globales

# Y por último la lógica principal del programa

print("¿Cuantos programas informaticos debo desarollar para ser millonario?")

cantidad1 = "100" # Esta variable, a pesar de ser un número, es un str. "100" es in literal str
cantidad2 = "1" # Esta variable tambien tiene un literal un str.

cantidad1int = int(cantidad1) # Aquí la variable str es convertida a literal int.
cantidad2int = int(cantidad2) # Aquí tambien hicimos conversion a literal int.

print("Debo desarollar", cantidad1int+cantidad2int, "programas")

print("-" * 70)

print("Changelog: V0.1.4")
print("* En la cabecera de la app, implementamos por primera vez una constante.")

# En Python existe la convención de escribir las constantes en MAYÚSCULAS, así las diferenciamos facilmente de las "variables".
