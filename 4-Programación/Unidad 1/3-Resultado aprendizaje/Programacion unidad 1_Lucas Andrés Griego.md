# Reporte de proyecto

## Información de generación

- **Fecha:** 2026-09-28 17:03:34 +0200
- **Usuario:** lucas
- **Equipo:** LUCAS
- **Sistema operativo:** Windows
- **Arquitectura:** x86_64
- **Directorio de ejecución:** `D:/Ordenar/jocarsa-generador-windows-x64`
- **Proyecto documentado:** `D:/DAM1 Resultados Aprendisaje/4-Programación/Unidad 1`
- **HMAC-SHA-256 de autenticidad:** `d65b1477fd1c2ea7b218dcf1482fcf50b7303745b2f94dcb16121e7c0c73f75c`

> El HMAC-SHA-256 se calcula sobre el documento completo usando un secreto incluido en el programa y 64 ceros en el propio campo del HMAC. El secreto no se escribe en el informe. Este mecanismo permite comprobar integridad y que el documento fue generado con el mismo secreto.

## Estructura del proyecto

```
D:/DAM1 Resultados Aprendisaje/4-Programación/Unidad 1
├── 1-Ejercicios
│   ├── 1-Estructura y bloques fundamentales
│   │   └── Mi primer programa.py
│   ├── 2-Variables
│   │   └── Mi primer programa V0.1.1.py
│   ├── 3-Tipos de datos
│   │   └── Mi primer programa V0.1.2.py
│   ├── 4-Literales
│   │   └── Mi primer programa V0.1.3.py
│   ├── 5-Constantes
│   │   └── Mi primer programa V0.1.4.py
│   └── 6-Operadores y expresiones
│       └── Mi primer programa v0.1.5.py
├── 2-Proyecto
│   └── Mi primer programa v0.1.5.py
└── 3-Resultado aprendisaje
    └── Ra1.md
```

## Bases de datos SQLite

Esta sección documenta únicamente el esquema de las bases SQLite detectadas. No se vuelcan registros ni datos de usuario.

No se han encontrado bases SQLite con extensiones .db, .sqlite o .sqlite3.

## Código (intercalado)

# Unidad 1
## 1-Ejercicios
### 1-Estructura y bloques fundamentales
**Mi primer programa.py**
```python
print("-" * 30)

print("Mi primer programa V0.1.0")

print("-" * 30)

print("¿QUE ESTRUCTURA DEBERIA SEGUIR UN PROGRAMA INFORMÁTICO?")


# Un programa estandar, se ordena de la siguiente forma:

# Primero van las importaciones de librerías

# Luego las declaraciones de las funciones y clases

# A continuación las variables globales

# Y por último la lógica principal del programa
```
### 2-Variables
**Mi primer programa V0.1.1.py**
```python
print("-" * 55)

print("Mi primer programa V0.1.1")

nombre = "Lucas Ezequiel"
apellidos = "Andrés Griego"

print("Diseñado por",nombre, apellidos)


print("-" * 55)

print("¿QUE ESTRUCTURA DEBERIA SEGUIR UN PROGRAMA INFORMÁTICO?")


# Un programa estandar, se ordena de la siguiente forma:

# Primero van las importaciones de librerías

# Luego las declaraciones de las funciones y clases

# A continuación las variables globales

# Y por último la lógica principal del programa



print("-" * 55)

print("Changelog: V0.1.1")
print("* Agregamos una variable al programa.")


```
### 3-Tipos de datos
**Mi primer programa V0.1.2.py**
```python
print("-" * 70)

print("Mi primer programa V0.1.2")

nombre = "Lucas Ezequiel"
apellidos = " Andrés Griego"

print("Diseñado por")
print(nombre+apellidos)


print("-" * 70)

print("¿QUE ESTRUCTURA DEBERIA SEGUIR UN PROGRAMA INFORMÁTICO?")


# Un programa estandar, se ordena de la siguiente forma:

# Primero van las importaciones de librerías

# Luego las declaraciones de las funciones y clases

# A continuación las variables globales

# Y por último la lógica principal del programa

print("¿Cuantos programas informaticos debo desarollar para ser millonario?")

cantidad1 = "100"
cantidad2 = "1"

cantidad1int = int(cantidad1)
cantidad2int = int(cantidad2)

print("Debo desarollar", cantidad1int+cantidad2int, "programas")



print("-" * 70)

print("Changelog: V0.1.2")
print("* Encadenamos las variables: nombre y apellidos.")
print("* Ralizamos conversión de variable str a variable int")
```
### 4-Literales
**Mi primer programa V0.1.3.py**
```python
print("-" * 70) # Esto es un detalle estético.

print("Mi primer programa V0.1.3")

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

print("Changelog: V0.1.3")
print("* Agregamos textos literales, para instruir/explicar como funciona nuestro programa, y demás detalles.")
```
### 5-Constantes
**Mi primer programa V0.1.4.py**
```python
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
```
### 6-Operadores y expresiones
**Mi primer programa v0.1.5.py**
```python
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
```
## 2-Proyecto
**Mi primer programa v0.1.5.py**
```python
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
```
## 3-Resultado aprendisaje
**Ra1.md**
```markdown
# Resultado de aprendizaje 1
**Resultado de aprendizaje**
Reconoce la estructura de un programa informático, identificando y relacionando los elementos propios del lenguaje de programación utilizado.

**Criterios de evaluación**
a) Se han identificado los bloques que componen la estructura de un programa informático.
b) Se han creado proyectos de desarrollo de aplicaciones.
c) Se han utilizado entornos integrados de desarrollo.
d) Se han identificado los distintos tipos de variables y la utilidad específica de cada uno.
e) Se ha modificado el código de un programa para crear y utilizar variables.
f) Se han creado y utilizado constantes y literales.
g) Se han clasificado, reconocido y utilizado en expresiones los operadores del lenguaje.
h) Se ha comprobado el funcionamiento de las conversiones de tipo explícitas e implícitas.
i) Se han introducido comentarios en el código.

a) Los bloques los delimitamos esteticamente con ```print("-" * 70)``` Esto genera una linea divisoria haciendo mas entendible el programa, y separando sus bloques.

b) Se creo un proyecto de informático, que consta de un programa, este programa al usuario le sirve para calcular cuantos dias del año le quedan para acabar el mismo, partiendo de una fecha introducida, y a mi como programador me sirvio para implementar conocimientos, practicar, equivocarme, investigar, etc.

c) Mi entorno de desarrollo fue reducido y basico, utilice Notepad++ para programar, y para documentar el RA1. a la vez que el sistema de directorios de windows, para ordenar los archivos de forma correcta. Eh recurrido al chat gpt para depurar mi codigo y pedirle que me explique algun fundamento.

d) Identificamos variables de tipo str, para el nombre, apellido, o para guardar un número con formato de texto, tambien utilice variables int en "cantidad1int", para calculos.

e) Parti de un codigo base de una primera versio de mi programa, este codigo fue ampliandose y modificandose a medida avance en las subunidades, aplicando los nuevos conociemientos de estas al programa.

f) Efectivamente aplique la funcionalidad de las constantes en el versionado del encabezado de mi programa, como tambien a cada mes funciona como constante con un literal int que corresponde a la cantidad de dias del mes.

g) Se utilizaron y reconocieron diferentes operadores del lenguaje, como comparativos, aritmeticos, etc. podemos ver que hay operaciones de comparacion, suma, resta, division, y multriplicacion.

h) El programa realiza operacionns de conversion tanto explícitas como implícitas. 

i) Se han introducido multriples comentarios a lo largo de todo el código, algunos comentarios tenian la funcionalidad de explicar lo que hace cierta seccion del código, y otros comentarios destacaban conversiones, variables, constantes, etc.

Lucas Ezequiel Andrés Griego
DAM1
Programacion unidad 1.
```
