# Reporte de proyecto

## Información de generación

- **Fecha:** 2026-10-05 00:34:53 +0200
- **Usuario:** lucas
- **Equipo:** LUCAS
- **Sistema operativo:** Windows
- **Arquitectura:** x86_64
- **Directorio de ejecución:** `D:/Herramientas/portables/jocarsa-generador-windows-x64`
- **Proyecto documentado:** `D:/Resultados Aprendizaje_DAM1/4-Programación/Unidad 3`
- **HMAC-SHA-256 de autenticidad:** `6b91e93fa53a0b373e9a766a2d8ecb2827fadd8282c3b3bf22edbe04340b7a57`

> El HMAC-SHA-256 se calcula sobre el documento completo usando un secreto incluido en el programa y 64 ceros en el propio campo del HMAC. El secreto no se escribe en el informe. Este mecanismo permite comprobar integridad y que el documento fue generado con el mismo secreto.

## Estructura del proyecto

```
D:/Resultados Aprendizaje_DAM1/4-Programación/Unidad 3
├── 1-Ejercicios
│   ├── 01-Estructuras de selección
│   │   ├── 01-if.py
│   │   ├── 02-else.py
│   │   ├── 03-elif.py
│   │   └── 04-Input.py
│   ├── 02-Estructuras de repetición
│   │   ├── 01-Bucle.py
│   │   ├── 02-Doble bucle.py
│   │   ├── 03-Triple bucle.py
│   │   ├── 04-Bucle while.py
│   │   ├── 05-while controlado.py
│   │   └── 06-import time.py
│   ├── 03-Estructuras de salto
│   │   ├── 01-Bienvenido.py
│   │   ├── 02-Bienvenido.py
│   │   └── 03-Bienvenido.py
│   ├── 04-Control de excepciones
│   │   ├── 01-Un error.py
│   │   ├── 02-try y except.py
│   │   └── 03-Entrada de usuario.py
│   ├── 05-Aserciones
│   │   ├── 01-Asercion.py
│   │   └── 02-assert y except.py
│   ├── 06-Prueba, depuración y documentación de la aplicación
│   │   ├── 01-docstring.py
│   │   ├── 02-Comentarios por seccion.py
│   │   └── 03-Comentarios en la linea.py
│   └── 07-Ejercicio
│       ├── 01-Funcion.py
│       ├── 02-Usar la funcion.py
│       ├── 03-Parametro.py
│       ├── 04-Dos parametros.py
│       ├── 05-Return.py
│       ├── 06-Programa funcion.py
│       ├── 07-Externalizando.py
│       ├── 08-Variable.py
│       ├── 09-Listas.py
│       ├── 10-Operamos con listas.py
│       ├── 11-Ejercicio con lista.py
│       ├── 12-Ajuste estetico.py
│       ├── 13-actualizar y eliminar.py
│       ├── 14-Comentarios.py
│       └── funciones_externas.py
├── 2-Proyecto
│   ├── Proyecto unidad3_programacion.py
│   └── funciones_externas.py
└── 3-Resultado  de aprendizaje
    └── RA3.md
```

## Bases de datos SQLite

Esta sección documenta únicamente el esquema de las bases SQLite detectadas. No se vuelcan registros ni datos de usuario.

No se han encontrado bases SQLite con extensiones .db, .sqlite o .sqlite3.

## Código (intercalado)

# Unidad 3
## 1-Ejercicios
### 01-Estructuras de selección
**01-if.py**
```python
temperatura = 27 

if temperatura > 26:
    print("Hace calor.")
```
**02-else.py**
```python
temperatura = 27 

if temperatura > 26:                      # Caso verdadero.
    print("Hace calor.")
else:
	print("Esta fresco, que placer!")     # Caso falso.
```
**03-elif.py**
```python
temperatura = 26

if temperatura <= 20:
    print("Que fresquito, así da gusto.")
elif temperatura <= 25:
    print("Aún se esta bien")
elif temperatura > 25 < 31:
    print("Está comenzando a hacer calor")
elif temperatura >= 31 < 36:
    print("Que calor hace!")
else:
	print("¡Esto parace un infierno!")
```
**04-Input.py**
```python
temperatura = input("Dime la temperatura, del entorno de trabajo: ")   # Aplicamos por primera vez un input

temperatura = int(temperatura)                                     # Conversión explícita.--> input() siempre devuelve un str, entonces con este movimiento transformamos la información de srt a int.

if temperatura <= 20:
    print("Que fresquito, así da gusto.")
elif temperatura <= 25 and temperatura:
    print("Aún se esta bien")
elif temperatura > 25 and temperatura < 31:
    print("Está comenzando a hacer calor")
elif temperatura >= 31 and temperatura < 36:
    print("Que calor hace!")
else:
	print("¡Esto parace un infierno!")
```
### 02-Estructuras de repetición
**01-Bucle.py**
```python
for espacioEnAlmacenamiento in range(2,950):
	print("Estas ocupando",espacioEnAlmacenamiento,"Gb de alamacenamiento")
if espacioEnAlmacenamiento == 949:
    print("Casi no tienes almacenamiento libre")
```
**02-Doble bucle.py**
```python
for disco in range(1,5):
    print("disco ",disco)
    for carpeta in range(1,5):
        print("carpeta numero ",carpeta)
```
**03-Triple bucle.py**
```python
for disco in range(1,5):
    print("Disco número ",disco)
    for carpeta in range(1,5):
        print("Carpeta número ",carpeta)
        for archivo in range(1,5):
            print("Archivo número ",archivo)
```
**04-Bucle while.py**
```python
archivo = 2

while archivo < 20:            # El valor actual de archivo es 2, por ende el bucle se ejectuara infinitamente 
    print("Creo archivos")
```
**05-while controlado.py**
```python
archivo = 2

while archivo < 20:            # El bucle continua hasta el último número menor a 20
    print("Creo archivos")
    archivo = archivo + 1
```
**06-import time.py**
```python
import time        # importa el módulo time, que permite trabajar con pausas y tiempo en Python.

while True:        # while significa “mientras”. Como la condición es True, que siempre es verdadera, el bucle nunca termina por sí solo.
  print("Dime si te canso, con esta serenata")
  time.sleep(1)    # hace que el programa se pause durante 1 segundo antes de continuar imprimiendo "Dime si te canso, con esta serenata"
```
### 03-Estructuras de salto
**01-Bienvenido.py**
```python
# Cabecera de presentación
print("-"*42)
print("Programa gestor de proyectos v0.1")
print("por Lucas Andrés Griego")
print("¡Bienvenido!")
print("-"*42)
```
**02-Bienvenido.py**
```python
# Cabecera de presentación
print("-"*42)
print("Programa gestor de proyectos v0.1")
print("por Lucas Andrés Griego")
print("¡Bienvenido!")
print("-"*42)

# Bucle infinito con el CRUD
print("-"*42)
while True:
    print("Tienes las siguientes opciones:")
    print("1- Crear proyecto")
    print("2- Listar proyectos")
    print("3- Actualizar/editar proyecto")
    print("4- Eliminar proyecto")
    print("-"*42)
    opcion = input("Selecciona y escribe la opción deseada: ")
    print("-"*42)
```
**03-Bienvenido.py**
```python
# Cabecera de presentación
print("-"*42)
print("Programa gestor de proyectos v0.1")
print("Diseñado por Sturmprojekt")
print("¡Bienvenido!")
print("-"*42)

# Bucle infinito con el CRUD
print("-"*42)
while True:
    print("Tienes las siguientes opciones:")
    print("1- Crear proyecto")
    print("2- Listar proyectos")
    print("3- Actualizar/editar proyecto")
    print("4- Eliminar proyecto")
    print("5- Salir del programa")
    print("-"*42)
    opcion = input("Selecciona y escribe la opción deseada: ")
    print("-"*42)
    
# Tratamiento de las opciones seleccionadas
    if opcion == "1":
        print("Vamos a crear el proyecto")
    if opcion == "2":
        print("Te listo los proyectos")
    if opcion == "3":
        print("Selecciona el proyecto que quieres actualizar")
    if opcion == "4":
        print("Selecciona el proyecto que quieres eliminar")
    if opcion == "5":
        print("Cerrando el gestor")
        break
        
# "Estructuras de salto". Es este programa gestor, se demuestra como saltamos de bloque en bloque, dentro de su estructura.
```
### 04-Control de excepciones
**01-Un error.py**
```python
division = 10/0     # En matemáticas no se puede dividir entre cero, y Python lanza un error llamado: ZeroDivisionError, terminando el progama.
print(division)     # Por eso nunca llega a ejecutar el último print()

print("Pero es que yo quiero que mi programa siga funcionando")
```
**02-try y except.py**
```python
try:                             # Significa aproximadamente: “Intenta ejecutar este código.”
  division = 10/0                # Dentro del try, tenemos esta división que puede provocar el error.
  print(division)
except Exception as e:           # Significa: “Si ocurre un error, en lugar de detener el programa, entra aquí.”
  print("Ha ocurrido un error pero continuamos:", e)       # La variable e guarda información sobre el error que ha ocurrido.

print("Pero es que yo quiero que mi programa siga funcionando")        # Lo importante es que el programa no termina ahí. Después continúa y ejecuta el último print.
```
**03-Entrada de usuario.py**
```python
try:
    # Pedimos los datos al usuario
    dividendo = int(input("Introduce el dividendo: "))
    divisor = int(input("Introduce el divisor: "))

    # Calculamos y mostramos la división
    division = dividendo / divisor
    print(division)

except Exception as e:
    # Capturamos el error para que el programa no se cierre
    print("Ha ocurrido un error pero continuamos:", e)

# El programa sigue ejecutándose después del try/except
print("El programa continúa")
```
### 05-Aserciones
**01-Asercion.py**
```python
edad = 18                                                     # Primero se guarda 18 en la variable edad

assert edad > 17                                              # assert sirve para comprobar que una condición sea verdadera. Como 18 > 17 es True y el programa continua al print

print:("Eres mayor de edad, puedes acceder al contenido")
```
**02-assert y except.py**
```python
# Aquí el código cambia porque el assert está dentro de un try
try:
	edad = 16
	assert edad > 17, "Debes ser mayor de edad"       # Python comprueba: 16 > 17, eso es False, así que assert genera un AssertionError.
except Exception as e:                                # El except captura la excepción en la variable "e" producida. Entonces se ejecutan las siguientes instrucciones.
	print("No puedes acceder al contenido, eres menor de edad.")
	print(e)                                          # Imprime el texto contenido en esa excepción.
	
print("Buscate algo adecuado a tu edad.")
```
### 06-Prueba, depuración y documentación de la aplicación
**01-docstring.py**
```python
'''
    Programa gestor basico 
    Diseñado por nurLukas de Sturmprojekt
    v 0.2
    Changelog:
    0.1 - CRUD básico con menú
    0.2 - Añadido funcionalidad a las opciones del if
    Entrada: usuario mediante input en consola
    Salida: print mediante consola
'''

print("-"*42)
print("Programa gestor de proyectos v0.2")
print("Diseñado por Sturmprojekt")
print("¡Bienvenido!")
print("-"*42)

print("-"*42)
while True:
    print("Tienes las siguientes opciones:")
    print("1- Crear proyecto")
    print("2- Listar proyectos")
    print("3- Actualizar/editar proyecto")
    print("4- Eliminar proyecto")
    print("5- Salir del programa")
    print("-"*42)
    opcion = input("Selecciona y escribe la opción deseada: ")
    print("-"*42)
    
    if opcion == "1":
        print("Vamos a crear el proyecto")
    if opcion == "2":
        print("Te listo los proyectos")
    if opcion == "3":
        print("Selecciona el proyecto que quieres actualizar")
    if opcion == "4":
        print("Selecciona el proyecto que quieres eliminar")
    if opcion == "5":
        print("Cerrando el gestor")
        break
```
**02-Comentarios por seccion.py**
```python
'''
    Programa gestor basico 
    Diseñado por nurLukas de Sturmprojekt
    v 0.2
    Changelog:
    0.1 - CRUD básico con menú
    0.2 - Añadido funcionalidad a las opciones del if
    Entrada: usuario mediante input en consola
    Salida: print mediante consola
'''

# Saludo - Antes de comenzar, introduzco un print de bievenida, con informacion de versionado y autor.
print("-"*42)
print("Programa gestor de proyectos v0.2")
print("Diseñado por Sturmprojekt")
print("¡Bienvenido!")
print("-"*42)

# Ahora entramos en un menu infinito de tal forma que la aplicación repite su ejecución
print("-"*42)
while True:
    print("Tienes las siguientes opciones:")
    print("1- Crear proyecto")
    print("2- Listar proyectos")
    print("3- Actualizar/editar proyecto")
    print("4- Eliminar proyecto")
    print("5- Salir del programa")
    print("-"*42)
    opcion = input("Selecciona y escribe la opción deseada: ")
    print("-"*42)

# Tratamiento de las opciones   
    if opcion == "1":
        print("Vamos a crear el proyecto")
    if opcion == "2":
        print("Te listo los proyectos")
    if opcion == "3":
        print("Selecciona el proyecto que quieres actualizar")
    if opcion == "4":
        print("Selecciona el proyecto que quieres eliminar")
    if opcion == "5":
        print("Cerrando el gestor")
        break
```
**03-Comentarios en la linea.py**
```python
'''
    Programa gestor basico 
    Diseñado por nurLukas de Sturmprojekt
    v 0.2
    Changelog:
    0.1 - CRUD básico con menú
    0.2 - Añadido funcionalidad a las opciones del if
    Entrada: usuario mediante input en consola
    Salida: print mediante consola
'''

# Saludo - Antes de comenzar, introduzco un print de bievenida, con informacion de versionado y autor.
print("-"*42)
print("Programa gestor de proyectos v0.2")
print("Diseñado por Sturmprojekt")
print("¡Bienvenido!")
print("-"*42)

# Ahora entramos en un menu infinito de tal forma que la aplicación repite su ejecución
print("-"*42)
while True:
    print("Tienes las siguientes opciones:")
    print("1- Crear proyecto")
    print("2- Listar proyectos")
    print("3- Actualizar/editar proyecto")
    print("4- Eliminar proyecto")
    print("5- Salir del programa")
    print("-"*42)
    opcion = input("Selecciona y escribe la opción deseada: ")
    print("-"*42)

# Tratamiento de las opciones   
    if opcion == "1":                                           # Esto es lo que va a ocurrir cuando el usuario use la opción 1                                         
        print("Vamos a crear el proyecto")
    if opcion == "2":                                           # Esto es lo que va a ocurrir cuando el usuario use la opción 2
        print("Te listo los proyectos")
    if opcion == "3":                                           # Esto es lo que va a ocurrir cuando el usuario use la opción 3
        print("Selecciona el proyecto que quieres actualizar")
    if opcion == "4":                                           # Esto es lo que va a ocurrir cuando el usuario use la opción 4
        print("Selecciona el proyecto que quieres eliminar")
    if opcion == "5":                                           # Esto es lo que va a ocurrir cuando el usuario use la opción 5
        print("Cerrando el gestor")
        break
```
### 07-Ejercicio
**01-Funcion.py**
```python
'''
"def" sirve para definir una función.
'''

def programando():                               # def programando(): significa: “crea una función llamada programando”.    Esto es una función, por si sola no hace nada.
	print("Hola, estoy ocupado programando")
```
**02-Usar la funcion.py**
```python
def programando():                               # Esto es una función, por si sola no hace nada.
	print("Hola, estoy ocupado programando.")
programando()                                    # Esto "llama" a la función "programando"

```
**03-Parametro.py**
```python
def programando(nombre):                               # Esto es una función, contiene un parametro (nombre), Es como una variable que la función recibe desde fuera.
	print("Hola, somos",nombre,"y estamos programando una nueva plataforma.")
programando("Sturmprojekt")                             # Esto llama a la función, contiene informacion para el parametro

```
**04-Dos parametros.py**
```python
def programando(empresa,operario):                               
	print("Hola, soy",operario,"de la empresa",empresa,"y estamos programando una nueva plataforma para el ayuntamiento de Canals.")
programando("Sturmprojekt","nurLukas")                            
```
**05-Return.py**
```python
def programando(empresa,operario):                               
	return "Hola, soy "+operario+", de la empresa "+empresa+",estamos trabajando en una plataforma para el ayuntamiento de Canals." # return significa devolver un resultado.

print(programando("Sturmprojekt","nurLukas"))        # Primero se ejecuta lo de dentro,"programando("Sturmprojekt","nurLukas")" Después, ese resultado pasa al print().        


# print()  → muestra algo en pantalla
# return   → devuelve algo al lugar donde llamaste la función
```
**06-Programa funcion.py**
```python
'''
    Programa gestor basico de proyectos 
    Diseñado por nurLukas de Sturmprojekt
    v 0.3
'''

def cabeceraBienvenida():
    print("-"*42)
    print("Programa gestor de proyectos v0.2")
    print("Diseñado por Sturmprojekt")
    print("¡Bienvenido!")
    print("-"*42)

def muestraMenu():
        print("-"*42)
        print("Tienes las siguientes opciones:")
        print("1- Crear proyecto")
        print("2- Listar proyectos")
        print("3- Actualizar/editar proyecto")
        print("4- Eliminar proyecto")
        print("5- Salir del programa")
        print("-"*42)
 
def listarProyecto():
    print("Vamos a listar los proyectos")
    print(nombreProyecto)
    
cabeceraBienvenida()
nombreProyecto = ""
while True:
    muestraMenu()
    print("-"*42)
    opcion = input("Selecciona y escribe la opción deseada: ")
    print("-"*42)
    if opcion == "2":
        listarProyecto()
    

```
**07-Externalizando.py**
```python
'''
    Programa gestor basico de proyectos 
    Diseñado por nurLukas de Sturmprojekt
    v 0.3
'''
from funciones_externas import *
 
def listarProyecto():
    print("Vamos a listar los proyectos: ")
    print(nombreProyecto)
    
cabeceraBienvenida()
nombreProyecto = ""
while True:
    muestraMenu()
    print("-"*42)
    opcion = input("Selecciona y escribe la opción deseada: ")
    print("-"*42)
    if opcion == "2":
        listarProyecto()
    

```
**08-Variable.py**
```python
# Cada variable almacena un dato:

edad = 31                     # Una variable
nombre = "Lucas Ezequiel"     # Otra variable
```
**09-Listas.py**
```python
lista_de_la_compra = ["manzanas","peras","platanos"] # "lista_de_la_compra" es una variable de tipo "lista"
print(lista_de_la_compra)
lista_de_la_compra.append("naranjas")                # append() añade un elemento al final:
print(lista_de_la_compra)
lista_de_la_compra.pop()                             # Como pop() no recibe ningún índice, elimina el último elemento, "naranjas"
print(lista_de_la_compra)


# append()  significa aproximadamente añadir

# pop() significa aproximadamente extraer/eliminar.
```
**10-Operamos con listas.py**
```python
clientes = []                           # Variable de tipo "lista", vacia.

clientes.append("Juan") # 0             # Insertamos - la clave es append
clientes.append("Jorge") # 1            # Insertamos - la clave es append

# Ahora Los índices son: [0] Juan
#                        [1] Jorge


print(clientes)                         # Leemos - Seleccionamos - la clave es print

clientes[1] = "Jaime"                   # Actualizamos - Update, (En la posición 1, reemplaza el valor actual por "Jaime".)

# Ahora Los índices son: [0] Juan
#                        [1] Jaime


print(clientes)


clientes.pop(1)                                                   # Elimina el elemento que está en la posición "1"  (Jaime)

# clientes.remove("Jaime") ---> alternativa a clientes.pop(1), ---> Elimina buscando el valor "Jaime"

print(clientes)
```
**11-Ejercicio con lista.py**
```python
from funciones_externas import *

cabeceraBienvenida()

proyectos = []

while True:
    muestraMenu()
    opcion = input("Introduce tu opción: ")

    if opcion == "1":
        nuevoregistro = input("Introduce un nuevo proyecto: ")
        proyectos = crearRegistro(proyectos, nuevoregistro)

    elif opcion == "2":
        listarRegistros(proyectos)

    elif opcion == "3":
        indice = int(input("Introduce el índice a modificar: "))
        valor = input("Introduce el nuevo valor: ")
        proyectos = actualizarRegistro(proyectos, indice, valor)

    elif opcion == "4":
        indice = int(input("Introduce el índice a eliminar: "))
        proyectos = eliminarRegistro(proyectos, indice)

    elif opcion == "5":
        break
```
**12-Ajuste estetico.py**
```python
from funciones_externas import *

cabeceraBienvenida()

proyectos = []

while True:
    muestraMenu()
    opcion = input("Introduce tu opción: ")

    if opcion == "1":
        nuevoregistro = input("Introduce un nuevo proyecto: ")
        proyectos = crearRegistro(proyectos, nuevoregistro)

    elif opcion == "2":
        listarRegistros(proyectos)

    elif opcion == "3":
        indice = int(input("Introduce el indice a modificar: "))
        valor = input("Introduce el nuevo valor: ")
        proyectos = actualizarRegistro(proyectos, indice, valor)

    elif opcion == "4":
        indice = int(input("Introduce el indice a eliminar: "))
        proyectos = eliminarRegistro(proyectos, indice)

    elif opcion == "5":
        print("Estas saliendo del programa gestor, adios.")
        break
```
**13-actualizar y eliminar.py**
```python
from funciones_externas import *              

cabeceraBienvenida()

proyectos = []

while True:
    muestraMenu()
    opcion = input("Introduce tu opción: ")

    if opcion == "1":
        nuevoregistro = input("Introduce un nuevo proyecto: ")
        proyectos = crearRegistro(proyectos, nuevoregistro)

    elif opcion == "2":
        listarRegistros(proyectos)

    elif opcion == "3":
        indice = int(input("Introduce el indice a modificar: "))
        valor = input("Introduce el valor a insertar: ")
        proyectos = actualizarRegistro(proyectos, indice, valor)

    elif opcion == "4":
        indice = int(input("Introduce el indice a eliminar: "))
        proyectos = eliminarRegistro(proyectos, indice)

    elif opcion == "5":
        print("Estas saliendo, adios.")
        break

    print("-"*30)
    
    
```
**14-Comentarios.py**
```python
'''
    Programa gestor de proyectos.
    Desarrollado po nurLukas de Sturmprojekt
'''
from funciones_externas import *                                   # Importo de archivo externo, funciones, y alguna cualidad estetica.

cabeceraBienvenida()                                               # Llamo a la función

proyectos = []                                                     # Creo lista "proyectos"

while True:                                                        # Bucle del menú
    muestraMenu()
    opcion = input("Introduce tu opción: ")                        # input para la selccion de opcions del usuario

    if opcion == "1":
        nuevoregistro = input("Introduce un nuevo proyecto: ")     # Se solicita al usuario la informacion necesaria, y se le brinda la posibilidad de introducir informacion
        proyectos = crearRegistro(proyectos, nuevoregistro)

    elif opcion == "2":                                            # Se genera una lista ordenada de los proyectos
        listarRegistros(proyectos)

    elif opcion == "3":                                            # Utilidad Update del CRUD, con instrucciones de uso. 
        indice = int(input("Introduce el indice a modificar: "))
        valor = input("Introduce el valor a insertar: ")
        proyectos = actualizarRegistro(proyectos, indice, valor)

    elif opcion == "4":                                            #Utilidad Delete, con instrucciones de uso
        indice = int(input("Introduce el indice a eliminar: "))
        proyectos = eliminarRegistro(proyectos, indice)

    elif opcion == "5":
        print("Estas saliendo, adios.")
        break                                                      # Cierre del programa

    print("-"*30)                                                  # Detalle estetico
    
    
```
**funciones_externas.py**
```python
'''
    Archivo de almacenamiento de funciones.
    Funciones listas para externalizar con exito.
'''
def cabeceraBienvenida():
    print("-"*42)
    print("Programa gestor de proyectos v0.2")
    print("Diseñado por Sturmprojekt")
    print("¡Bienvenido!")
    print("-"*42)
    
def muestraMenu():
        print("-"*42)
        print("Tienes las siguientes opciones:")
        print("1- Crear proyecto")
        print("2- Listar proyectos")
        print("3- Actualizar/editar proyecto")
        print("4- Eliminar proyecto")
        print("5- Salir del programa")
        print("-"*42)
        
def listarRegistros(proyectos):
    print("Vamos a listar los proyectos")
    print(proyectos)

def crearRegistro(proyectos,registro):
    proyectos.append(registro)
    return proyectos

def actualizarRegistro(proyectos,indice,valor):
    proyectos[indice] = valor
    return proyectos

def eliminarRegistro(proyectos,indice):
    proyectos.pop(indice)
    return proyectos
```
## 2-Proyecto
**Proyecto unidad3_programacion.py**
```python
'''
    Programa gestor de proyectos.
    Desarrollado po nurLukas de Sturmprojekt
'''
from funciones_externas import *                                   # Importo de archivo externo, funciones, y alguna cualidad estetica.

cabeceraBienvenida()                                               # Llamo a la función

proyectos = []                                                     # Creo lista "proyectos"

while True:                                                        # Bucle del menú
    muestraMenu()
    opcion = input("Introduce tu opción: ")                        # input para la selccion de opcions del usuario

    if opcion == "1":
        nuevoregistro = input("Introduce un nuevo proyecto: ")     # Se solicita al usuario la informacion necesaria, y se le brinda la posibilidad de introducir informacion
        proyectos = crearRegistro(proyectos, nuevoregistro)

    elif opcion == "2":                                            # Se genera una lista ordenada de los proyectos
        listarRegistros(proyectos)

    elif opcion == "3":                                            # Utilidad Update del CRUD, con instrucciones de uso. 
        indice = int(input("Introduce el indice a modificar: "))
        valor = input("Introduce el valor a insertar: ")
        proyectos = actualizarRegistro(proyectos, indice, valor)

    elif opcion == "4":                                            #Utilidad Delete, con instrucciones de uso
        indice = int(input("Introduce el indice a eliminar: "))
        proyectos = eliminarRegistro(proyectos, indice)

    elif opcion == "5":
        print("Estas saliendo, adios.")
        break                                                      # Cierre del programa

    print("-"*30)                                                  # Detalle estetico
    
    
```
**funciones_externas.py**
```python
'''
    Archivo de almacenamiento de funciones.
    Funciones listas para externalizar con exito.
'''
def cabeceraBienvenida():
    print("-"*42)
    print("Programa gestor de proyectos v0.2")
    print("Diseñado por Sturmprojekt")
    print("¡Bienvenido!")
    print("-"*42)
    
def muestraMenu():
        print("-"*42)
        print("Tienes las siguientes opciones:")
        print("1- Crear proyecto")
        print("2- Listar proyectos")
        print("3- Actualizar/editar proyecto")
        print("4- Eliminar proyecto")
        print("5- Salir del programa")
        print("-"*42)
        
def listarRegistros(proyectos):
    print("Vamos a listar los proyectos")
    print(proyectos)

def crearRegistro(proyectos,registro):
    proyectos.append(registro)
    return proyectos

def actualizarRegistro(proyectos,indice,valor):
    proyectos[indice] = valor
    return proyectos

def eliminarRegistro(proyectos,indice):
    proyectos.pop(indice)
    return proyectos
```
## 3-Resultado  de aprendizaje
**RA3.md**
```markdown
# Resultado de aprendizaje 3
Resultado de aprendizaje
Escribe y depura código, analizando y utilizando las estructuras de control del lenguaje.

**Criterios de evaluación**
a) Se ha escrito y probado código que haga uso de estructuras de selección.
a) El aprendizaje de esta unidad, inicio efectivamente con la subunidad de estructuras de selección,
analizando con detalle if, else, elif e input.
Dichas estructuras se aplicaron a los ejercicios y proyecto correspondientes a esta unidad.

b) Se han utilizado estructuras de repetición.
b) Profundizamos conocimientos con estructuras de repetición tipo bucle "while" y tambien bucles "for.. in range.." 
Probando bucles simples, dobles y hasta triples. controlados o sin control, (infinitos)
Concluí que es muy importante un bucle while True para un menu CRUD

c) Se han reconocido las posibilidades de las sentencias de salto.
c) Gracias a las sentencias de salto, tenemos la posibilidad y la capacidad de estructurar bien el codigo desarollado, y poder saltar efectivamente de un bloque de codigo al siguien.

d) Se ha escrito código utilizando control de excepciones.
d) Gracias a try y except, podemos pasar por alto ciertos errores de nuestras aplicaciones, sin que esta colapse y se cierre o de error. pasando asi a otra estructura de codigo siguiente.

e) Se han creado programas ejecutables utilizando diferentes estructuras de control.
e) Utilice Usas while True, if, elif y break en el gestor de proyectos, y los ejercicios de las subunidades.


f) Se han probado y depurado los programas.
f) A  prueba y error, se depuro efectivamente el codigo, y tambien recurrí al código de mi profesor como referencia, tambien se utilizo la IA para momentos de estancamiento.


g) Se ha comentado y documentado el código.
g) A lo largo de la unidad en los ejercicios se aplicaros docstrings y lineas de comentarios, con instrucciones de uso, para el usuario y para el tecnico que revise el codigo.


h) Se han creado excepciones.
h) se han  creado con try, except en los ejercicios


i) Se han utilizado aserciones para la detección y corrección de errores durante la fase de desarrollo.
i) Hemos utilizado assert en ejercicios de la subunidad correspondiente, y el repaso general.
```
