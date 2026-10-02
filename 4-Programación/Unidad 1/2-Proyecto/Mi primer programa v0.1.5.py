print("-" * 70) # Esto es un detalle estético.
VERSION = "0.1.5"  # Esto es una CONSTANTE
print(f"Mi primer programa V{VERSION}")
print("-" * 70)

print("Programa calculador de los dias restantes del año")
nombre = "Lucas Ezequiel"     # Aqui la variable tiene un literal str "Lucas Ezequiel"
apellidos = "Andrés Griego"

print("Diseñado por:")
print(nombre, apellidos)

print("-" * 70)

print("¿Cuantos programas informaticos debo desarollar para ser millonario?")

cantidad1 = "100" # Esta variable, a pesar de ser un número, es un str. "100" es in literal str
cantidad2 = "1" # Esta variable tambien tiene un literal un str.

cantidad1int = int(cantidad1) # Aquí la variable str es convertida a literal int.
cantidad2int = int(cantidad2) # Aquí tambien hicimos conversion a literal int.   conversión explícita

print("Debo desarollar", cantidad1int+cantidad2int, "programas")

print("-" * 70)

print("¿CUANTOS DÍAS TE QUEDAN DE ESTE AÑO?")

dia = input("Introduce el día,por ejemplo, 14: ") # agregamos nuestro primer input, a nuestro primer programa, :´)
mes = input("Introduce el mes, por ejemplo, junio: ")
print("Vale, calculamos desde el",dia,"de",mes)

dia = int(dia) # convención del literal str de dia a literal int.


ENERO = 31 # Número de días que tiene cada mes.
FEBRERO = 28
MARZO = 31
ABRIL = 30
MAYO = 31
JUNIO = 30
JULIO = 31
AGOSTO = 31
SEPTIEMBRE = 30
OCTUBRE = 31
NOVIEMBRE = 30
DICIEMBRE = 31

if mes == "enero": # Aqui calculamos los dias transcurridos antes de la fecha introducida, aunque no toca a esta unidad, se tuve que implementar los condicionantes if, y elif.
    dias_anteriores = 0

elif mes == "febrero":
    dias_anteriores = ENERO

elif mes == "marzo":
    dias_anteriores = ENERO + FEBRERO

elif mes == "abril":
    dias_anteriores = ENERO + FEBRERO + MARZO

elif mes == "mayo":
    dias_anteriores = ENERO + FEBRERO + MARZO + ABRIL

elif mes == "junio":
    dias_anteriores = ENERO + FEBRERO + MARZO + ABRIL + MAYO

elif mes == "julio":
    dias_anteriores = ENERO + FEBRERO + MARZO + ABRIL + MAYO + JUNIO

elif mes == "agosto":
    dias_anteriores = ENERO + FEBRERO + MARZO + ABRIL + MAYO + JUNIO + JULIO

elif mes == "septiembre":
    dias_anteriores = ENERO + FEBRERO + MARZO + ABRIL + MAYO + JUNIO + JULIO + AGOSTO

elif mes == "octubre":
    dias_anteriores = ENERO + FEBRERO + MARZO + ABRIL + MAYO + JUNIO + JULIO + AGOSTO + SEPTIEMBRE

elif mes == "noviembre":
    dias_anteriores = ENERO + FEBRERO + MARZO + ABRIL + MAYO + JUNIO + JULIO + AGOSTO + SEPTIEMBRE + OCTUBRE

elif mes == "diciembre":
    dias_anteriores = ENERO + FEBRERO + MARZO + ABRIL + MAYO + JUNIO + JULIO + AGOSTO + SEPTIEMBRE + OCTUBRE + NOVIEMBRE
    
dias_transcurridos = dias_anteriores + dia # Operación aritmetica, es la suma de los dias anteriores mas el dia desde el que parte el calculo.  

dias_restantes = 365 - dias_transcurridos # Operación aritmetica teniendo en cuenta los 365 días del año.

print("-" * 70)

print("Han transcurrido", dias_transcurridos, "días del año.")
print("Quedan", dias_restantes, "días para terminar el año.")

PORCENTAJE = 100.0  # Aqui tenemos un literal float

porcentaje_transcurrido = dias_transcurridos * PORCENTAJE / 365     #Calculo del porcentaje del año que ya transcurrio."dias_transcurridos son un literal int, que se convierte de forma implicita en un float.

print("Ha transcurrido el", porcentaje_transcurrido, "% del año.")  # Python opero un int con un float, dando como resultado un float.

print("-" * 70)

print("Changelog: V0.1.5")
print("*En esta actualizacion aplicamos input, operadores comparativos, booleanos, operaciones aritmeticas, y condicionantes; todo con sus respectivos comentarios, tambien introducimos conversiónes implicitas y explicitas")

print("-" * 70)

print("Tengo mi programa informático listo, ya puedo ser millonario")
print( 101 == 1)   # ESto es una expresion booleana