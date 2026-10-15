# Reporte de proyecto

## Información de generación

- **Fecha:** 2026-10-12 04:32:43 +0200
- **Usuario:** lucas
- **Equipo:** LUCAS
- **Sistema operativo:** Windows
- **Arquitectura:** x86_64
- **Directorio de ejecución:** `D:/Herramientas/portables/jocarsa-generador-windows-x64`
- **Proyecto documentado:** `D:/Resultados Aprendizaje_DAM1/4-Programación/Unidad 5`
- **HMAC-SHA-256 de autenticidad:** `5d7c6220c2069ef4c8134102e277c331a4cb649194917bab9788559813f5430e`

> El HMAC-SHA-256 se calcula sobre el documento completo usando un secreto incluido en el programa y 64 ceros en el propio campo del HMAC. El secreto no se escribe en el informe. Este mecanismo permite comprobar integridad y que el documento fue generado con el mismo secreto.

## Estructura del proyecto

```
D:/Resultados Aprendizaje_DAM1/4-Programación/Unidad 5
├── 1-Ejercicios
│   ├── 01-Flujos. Tipos bytes y caracteres. Clases relacionadas
│   │   ├── 01-Escribir.py
│   │   ├── 02-Leer archivos.py
│   │   ├── 03-Gestor de proyectos.py
│   │   ├── 04-Leer registro.py
│   │   ├── 05-Gestor completo.py
│   │   ├── registro_proyectos.txt
│   │   └── test.txt
│   ├── 02-Ficheros de datos. Registros
│   │   ├── 01-Lectura basica.py
│   │   ├── 02-split de linea.py
│   │   ├── 03-Repaso de listas.py
│   │   ├── 04-Diccionario.py
│   │   ├── 05-csv a diccionario.py
│   │   ├── 06-leer json.py
│   │   ├── misdatos.json
│   │   └── proyectos.csv
│   ├── 03-Apertura y cierre de ficheros. Modos de acceso. Escritura y lectura de información en ficheros
│   │   ├── 01-apertura.py
│   │   ├── 02-Cierre de archivos.py
│   │   ├── 03-pickle.py
│   │   ├── 04-pickle ahora si.py
│   │   ├── 05-pickle devolver.py
│   │   └── frutas.txt
│   ├── 04-Utilización de los sistemas de ficheros
│   │   ├── 01-Crear nueva carpeta.py
│   │   ├── 02-Eliminar carpeta.py
│   │   ├── 03-Crear archivo.py
│   │   ├── 04-Eliminar archivo.py
│   │   ├── 05-Caminar.py
│   │   ├── 06-Recorrer arbol win11.py
│   │   ├── 06-Recorrer arbol.py
│   │   ├── 07-Guardar en archivo win11.py
│   │   ├── 07-Guardar en archivo.py
│   │   └── arbol.txt
│   ├── 06-Entrada desde teclado. Salida a pantalla. Formatos de visualización
│   │   ├── 01-Comenzamos programa.py
│   │   ├── 02-Cabecera de bienvenida.py
│   │   ├── 03-while True.py
│   │   ├── 04-Seleccion.py
│   │   ├── 05-Insertamos registro.py
│   │   ├── 06-Listado de proyectos.py
│   │   ├── 07-Listado de proyectos formateado.py
│   │   ├── 08-Listado de proyectos con cabeceras.py
│   │   └── proyectos.csv
│   ├── 07-Interfaces gráficas
│   │   ├── 01-tkinter.py
│   │   ├── 02-nueva ventana.py
│   │   ├── 03-Pongo texto.py
│   │   ├── 04-Tamaño del texto.py
│   │   ├── 05-Creamos botones.py
│   │   ├── 06-Padding.py
│   │   ├── 07-Comando en el boton.py
│   │   ├── 08-Escribir en la interfaz.py
│   │   ├── 09-Entrada.py
│   │   └── 10-calculadora de IVA.py
│   ├── 08-Concepto de evento
│   │   ├── 01-Agenda tkinter.py
│   │   ├── 02-Entradas.py
│   │   ├── 03-Labels.py
│   │   ├── 04-Guardar.py
│   │   ├── 05-Area de texto.py
│   │   └── 06-Escribir dentro del area.py
│   └── 09-Creación de controladores de eventos
│       ├── 01-Grid.py
│       ├── 02-Panel.py
│       ├── 03-Controles.py
│       ├── 04-Escribir.py
│       └── agenda.csv
├── 2-Proyecto
│   ├── final
│   │   ├── 01-mantenimiento.py
│   │   ├── 02-Entradas.py
│   │   ├── 03-Boton guardar.py
│   │   ├── 04-Listar.py
│   │   ├── 05-Programa completo.py
│   │   └── mantenimiento.csv
│   ├── sub1
│   │   ├── 01-Escribir.py
│   │   ├── 02-Leer.py
│   │   ├── 03-Anadir.py
│   │   ├── 04-Listar.py
│   │   ├── 05-Menu.py
│   │   └── mantenimiento.txt
│   ├── sub2
│   │   ├── 06-Registros.py
│   │   ├── 07-Leer registros.py
│   │   ├── 08-Diccionario.py
│   │   ├── 09-Leer JSON.py
│   │   ├── coche.json
│   │   └── mantenimiento.csv
│   └── sub3
│       ├── 10-Guardar copia.py
│       ├── 11-Leer copia.py
│       └── copia.dat
└── 3-Resultado  de aprendizaje
    ├── Programacion Unidad 5_Lucas Andrés Griego.md
    └── RA5.md
```

## Bases de datos SQLite

Esta sección documenta únicamente el esquema de las bases SQLite detectadas. No se vuelcan registros ni datos de usuario.

No se han encontrado bases SQLite con extensiones .db, .sqlite o .sqlite3.

## Código (intercalado)

# Unidad 5
## 1-Ejercicios
### 01-Flujos. Tipos bytes y caracteres. Clases relacionadas
**01-Escribir.py**
```python
archivo = open("test.txt",'w')                                # 'w' Indica que a abrimos el archivo especificado, en modo escritura
archivo.write("El contenido de esta unidad, esta muy guay")   # Esto es lo que escribimos en el archivo externo abierto previamente
archivo.close()                                               # Cerrar el arcvhi es una buena practica que debemos tener siempre
```
**02-Leer archivos.py**
```python
archivo = open("test.txt",'r')      # Abrimos el archivo en modo lectura
lector = archivo.readlines()        # guarda todas sus líneas en una lista con readlines()
print(lector)                       # muestra esa lista
archivo.close()                     # Cerramos el archivo
```
**03-Gestor de proyectos.py**
```python
'''
    Implementacion de escritura tipo append
'''

print("-"*45)                                                  # Detalle estetico
print("Programa gestor de proyectos v0.1")                     # Cabecera de presentación
print("Desarrollado por nurLukas de Sturmprojekt")             # Cabecera de presentación
print("-"*45)                                                  # Detalle estetico

while True:                                                    # Bucle del menú
    nombre = input("Introduce el nombre del proyecto: ")       # input con indicaciones
    archivo = open("registro_proyectos.txt",'a')               # "a" significa append, es decir, añadir al final. A diferencia de "w", no borra lo que ya existe.
    archivo.write(nombre+"\n")                                 # "\n" significa salto de línea, así que cada contacto queda en una línea diferente.
    archivo.close()                                            # cerramos el archivo abierto previamente.
    
    
    
    
    
   
```
**04-Leer registro.py**
```python
'''
    Implementacion de lectura tipo "read".
'''

print("-"*45)                                          # Detalle estetico.
print("Programa gestor de proyectos v0.1")             # Cabecera de presentación.
print("Desarrollado por nurLukas de Sturmprojekt")     # Cabecera de presentación.
print("-"*45)                                          # Detalle estetico.


archivo = open("registro_proyectos.txt",'r')           # Apertura del archivo, en modo lectura
lineas = archivo.readlines()                           # crea una lista parecida a: ["Ruffoo\n", "zandtvoort\n", "Corcobo\n"].
for linea in lineas:                                   # Para cada elemento que haya dentro de lineas, guárdalo temporalmente en la variable linea.
    print(linea)                                       # imprime cada nombre.
archivo.close()                                        # Cierra el archivo.
```
**05-Gestor completo.py**
```python
'''
    Implementacion de lectura y escritura.
'''

print("-"*45)                                              # Detalle estetico.
print("Programa gestor de proyectos v0.2")                 # Cabecera de presentación.
print("Desarrollado por nurLukas de Sturmprojekt")         # Cabecera de presentación.
print("-"*45)                                              # Detalle estetico

while True:                                                # Bucle infinito,  mantiene el menú activo hasta que el usuario elige salir.
    print("-"*35)                                          # Detalle estetico
    print("Selecciona una opcion")
    print("1.-Introduce un proyecto")
    print("2.-Selecciona los proyectos")
    print("3.-Salir del gestor")
    opcion = input("Escoge una opción: ")                  # input: Lee la opción introducida por el usuario.
    print("-"*35)                                          # Detalle estetico
    if opcion == "1":
        archivo = open("registro_proyectos.txt",'a')       # # Apertura del archivo, en modo append
        nombre = input("Ahora introduce el nombre del nuevo proyecto: ")
        archivo.write(nombre+"\n")
        archivo.close()                                    # Cierra el archivo.
    elif opcion == "2":
        archivo = open("registro_proyectos.txt",'r')       # Apertura del archivo, en modo lectura
        lineas = archivo.readlines()                       # Guarda todas las líneas del archivo en una lista.
        for linea in lineas:                               # Recorre cada línea almacenada en la lista.
            print(linea)                                   # imprime cada nombre.
            archivo.close()                                # Cierra el archivo.
    elif opcion == "3":
        print("Saliendo del gestor, adios")
        break                                              # Se cierra el programa
    else:
        print("Opción incorrecta")
    
```
### 02-Ficheros de datos. Registros
**01-Lectura basica.py**
```python
archivo = open('proyectos.csv','r')   # Aquí se abre el archivo proyectos.csv en modo lectura
lineas = archivo.readlines()          # se pretende leer todas las líneas del archivo y guardarlas en una lista llamada lineas
for linea in lineas:                  # Esto recorre la lista lineas          
    print(lineas)
```
**02-split de linea.py**
```python
'''
    split() significa dividir o separar un texto.
'''
archivo = open('proyectos.csv','r')    # Abre el archivo proyectos.csv en modo lectura ('r')
lineas = archivo.readlines()           # Lee todas las líneas del archivo y las guarda en una lista llamada lineas
for linea in lineas:                   # Recorre una por una todas las líneas guardadas en la lista
	partido = linea.split("|")         # Divide la línea cada vez que encuentra el símbolo |   # El resultado se guarda en una lista llamada partido
	print(partido)                     # # Muestra en pantalla la lista resultante
```
**03-Repaso de listas.py**
```python
lista = ['Ignacio Emanuel', 'Andrés Lago', 'nacho.kapo@ejemplo.com', 'carrer el wachin 28', 'Valencia', '612345678\n']  # Crea una lista llamada "lista" con varios elementos de texto


print(lista)         # Muestra la lista completa
print(lista[0])      # Muestra el primer elemento de la lista
print(lista[1])      # Muestra el segundo elemento de la lista
print(lista[2])      # Muestra el tercer elemento de la lista


# \n es un carácter especial que significa “salta a la siguiente línea”.

# Suele aparecer mucho cuando lees líneas de un archivo con readlines(), porque cada línea del archivo normalmente termina con \n.
```
**04-Diccionario.py**
```python
diccionario = {                              # Crea un diccionario llamado "diccionario"
  'nombre':'Ana',                            # "nombre" es la clave y "Ana" es su valor
  'apellidos':'García López', 
  'email':'ana.garcia@example.com',          # Guarda un email asociado a la clave "email"
  'direccion':'Calle Colón 24, Valencia', 
  'telefono':'612345678'                     # Guarda un teléfono asociado a la clave "telefono"
}

print(diccionario)                           # Muestra el diccionario completo
print(diccionario['nombre'])                 # Muestra solamente el valor asociado a la clave "nombre"


# Un diccionario funciona con parejas de clave : valor. Por ejemplo: 'nombre': 'Ana'
```
**05-csv a diccionario.py**
```python
# Primero abrimos
archivo = open('proyectos.csv','r')
# Solo leemos la primera linea
cabecera = archivo.readline()  # Singular
# Partimos la primera linea en una lista de cabeceras de columna
cabeceras = cabecera.split("|")
# Ahora sí ya lo leemos todo
lineas = archivo.readlines()  # Plural
# Recorro todas las lineas
for linea in lineas:
    # Parto una linea completa en campos individuales
    datos = linea.split("|")
    for i in range(0, len(datos)):
        print(cabeceras[i], ":", datos[i])
```
**06-leer json.py**
```python
import json

archivo = open("misdatos.json", 'r')
contenido = json.load(archivo)
#print(contenido)
print(contenido['nombre'])
archivo.close()
```
**misdatos.json**
```json
{
  "nombre": "Lucas Andrés Griego",
  "marca": "STURMPROJEKT",
  "nacimiento": "1995-10-06",
  "ciudad": "Valencia",
  "pais": "España",
  "profesion": "Desarrollador informatico",
  "especialidad": "Programación e Inteligencia Artificial",
  "experiencia_desde": 2025,
  "tecnologias": [
    "Python",
    "PHP",
    "JavaScript",
    "C++",
    "SQL",
    "Linux",
    "IA"
  ],
  "web": "https://sturmprojekt.es"
}
```
### 03-Apertura y cierre de ficheros. Modos de acceso. Escritura y lectura de información en ficheros
**01-apertura.py**
```python
archivo = open('archivo.txt','w')

# archivo: es una variable donde guardamos la referencia al archivo abierto.
# open(): es una función de Python que sirve para abrir archivos.
# 'archivo.txt': es el nombre del archivo que queremos abrir.
# 'w': indica que queremos abrirlo en modo escritura (write).


'''
    Modo	Significado	    Qué hace
    'w'	    Write	        Escribe, borrando lo anterior
    'r'	    Read	        Lee un archivo existente
    'a'	    Append	        Añade contenido al final
    'wb'	Write binary	Escribe datos binarios
    'rb'	Read binary	    Lee datos binarios
'''
```
**02-Cierre de archivos.py**
```python
archivo = open('archivo.txt','w')
archivo.close  #Cuando abres un archivo, Python utiliza recursos del sistema para trabajar con él. Cuando terminas, debes cerrarlo para liberar esos recursos y asegurar que se completen las escrituras pendientes.
```
**03-pickle.py**
```python
frutas = ['manzana','pera','platano']    # Creamos una lista llamada frutas con tres elementos.

archivo = open("frutas.txt",'w')         # Creamos o abrimos un archivo de texto llamado frutas.txt para escribir información.
archivo.write(str(frutas))
archivo.close()

'''
    str(frutas) convierte la lista en una cadena de texto.
    Pero hay un inconveniente: cuando recuperes la información, será texto, no una lista de Python.
    Y precisamente para solucionar esto aparece pickle.
'''
```
**04-pickle ahora si.py**
```python
import pickle                             # Esto permite utilizar las funciones de pickle.

frutas = ['manzana', 'pera', 'platano']   # Creamos la lista

archivo = open('frutas.dat', 'wb')        # Abrimos un archivo binario
pickle.dump(frutas, archivo)              # Guardamos la lista


'''
    ¿Qué es pickle?
    pickle es un módulo de Python que permite guardar objetos de Python en archivos y recuperarlos posteriormente.
    Por ejemplo, puedes guardar listas, diccionarios y otros objetos compatibles.
'''
```
**05-pickle devolver.py**
```python
import pickle                        # Importamos pickle

frutas = []                          # Creamos una lista vacía

archivo = open('frutas.dat', 'rb')   # Abrimos el archivo para leer
frutas = pickle.load(archivo)        # Recuperamos los datos
print(frutas)                        # Mostramos el resultado
archivo.close()                      # Cerramos el archivo


'''
    Diferencia entre dump() y load()
    pickle.dump()	Guarda	Pasar un objeto de Python a un archivo
    pickle.load()	Recupera	Pasar los datos del archivo a un objeto de Python
'''
```
### 04-Utilización de los sistemas de ficheros
**01-Crear nueva carpeta.py**
```python
import os                    # Importa el módulo os de Python, que permite interactuar con el sistema operativo y realizar operaciones con archivos y carpetas.

os.mkdir("documentos")


'''
    os.mkdir("documentos")
    - os: módulo del sistema operativo.
    - mkdir: significa make directory (crear directorio).
    - "documentos": nombre de la carpeta que queremos crear.
'''
```
**02-Eliminar carpeta.py**
```python
import os

os.rmdir("documentos")     # os.rmdir() significa remove directory (eliminar directorio).

'''
    Pero tiene una condición muy importante: la carpeta debe estar vacía.
    Por ejemplo:
    - Si documentos está vacía → se elimina.
    - Si contiene apuntes.txt → da un error.
    - Si no existe → da un error.
'''
```
**03-Crear archivo.py**
```python
'''
    Este programa crea un archivo llamado archivo.txt.
'''
archivo = open("archivo.txt",'w') # open() abre un archivo., "archivo.txt" indica el archivo que queremos utilizar, 'w' indica que queremos abrirlo en modo escritura (write).
archivo.close()                   # Cierra el archivo después de abrirlo.
```
**04-Eliminar archivo.py**
```python
'''
    Elimina el archivo archivo.txt del directorio de trabajo actual.
'''
import os
os.remove("archivo.txt")     # os.remove() se utiliza para eliminar archivos, no carpetas.
```
**05-Caminar.py**
```python
import os

arbol = os.walk("/var/www/html/tame2627dam1")   # os.walk() Permite recorrer la estructura de directorios, incluyendo carpetas, subcarpetas y archivos.
print(arbol)                                    # No muestra las carpetas ni los archivos. Muestra una representación del objeto iterador

'''
    os.walk() prepara un recorrido del árbol de directorios.
    "/var/www/html/tame2627dam1" es la ruta desde la que empezará.
    arbol guarda el iterador generado.
'''


'''
    En windows11:
   
   import os

    arbol = os.walk(r"D:\2627_DAM1\4-Programación\05-Lectura y escritura de información\04-Utilización de los sistemas de ficheros")
    print(arbol)

    ¿Qué hemos cambiado?
    Únicamente dos cosas en la ruta:
    1. Hemos sustituido /var/www/html/tame2627dam1 por tu ruta de Windows.
    2. Hemos añadido una r delante de las comillas para que Python interprete correctamente las barras invertidas \.
'''
```
**06-Recorrer arbol win11.py**
```python

import os

arbol = os.walk(r"D:\2627_DAM1\4-Programación\05-Lectura y escritura de información\04-Utilización de los sistemas de ficheros")

for carpeta, carpetas, archivos in arbol:
    print("Carpeta actual:", carpeta)

    print("Subcarpetas:")
    for subcarpeta in carpetas:
        print("  📁", subcarpeta)

    print("Archivos:")
    for archivo in archivos:
        print("  📄", archivo)

    print()
```
**06-Recorrer arbol.py**
```python
'''
    Este es uno de los ejercicios más importantes, porque combina os.walk() con varios bucles for.
    ¿Qué hace este programa?
    Recorre una carpeta y todas sus subcarpetas para mostrar:
    - La carpeta que está examinando.
    - Las subcarpetas que contiene.
    - Los archivos que contiene.
    No crea, modifica ni elimina archivos. Solo consulta y muestra información.
'''
import os                                          # Importar el módulo os

arbol = os.walk("/var/www/html/tame2627dam1")      # Preparar el recorrido

for carpeta, carpetas, archivos in arbol:          # Bucle for principal
    print("Carpeta actual:", carpeta)

    print("Subcarpetas:")
    for subcarpeta in carpetas:
        print("  📁", subcarpeta)

    print("Archivos:")
    for archivo in archivos:
        print("  📄", archivo)

    print()
    
'''
    os.walk() recorre los directorios y, en cada vuelta, nos da tres cosas: 
    la ruta actual, 
    sus subcarpetas 
    y sus archivos. 
    El for principal avanza por los directorios 
    y los otros dos for muestran lo que hay dentro de cada uno.
'''
```
**07-Guardar en archivo win11.py**
```python

import os

ruta = r"D:\2627_DAM1\4-Programación\05-Lectura y escritura de información\04-Utilización de los sistemas de ficheros"

with open("arbol.txt", "w") as salida:

    for carpeta, carpetas, archivos in os.walk(ruta):
        salida.write(carpeta + "\n")

        for archivo in archivos:
            salida.write("  - " + archivo + "\n")

print("Tree saved to arbol.txt")
```
**07-Guardar en archivo.py**
```python
'''
    Este programa Recorre una carpeta y todas sus subcarpetas. 
    Después guarda sus rutas y los nombres de los archivos encontrados en un documento de texto llamado arbol.txt.
'''
import os                                                 # Importamos el módulo os, permite a Python interactuar con el sistema operativo.

ruta = "/var/www/html/tame2627dam1"                       # Indicamos la ruta que queremos recorrer, Aquí creamos una variable llamada ruta. Dentro guardamos la dirección de la carpeta que queremos analizar.

with open("arbol.txt", "w") as salida:                    # Abrimos un archivo para escribir

    for carpeta, carpetas, archivos in os.walk(ruta):     # Recorremos los directorios
        salida.write(carpeta + "\n")

        for archivo in archivos:
            salida.write("  - " + archivo + "\n")         # Guardamos la ruta de la carpeta

print("Tree saved to arbol.txt")                          # Mostramos un mensaje final
```
### 06-Entrada desde teclado. Salida a pantalla. Formatos de visualización
**01-Comenzamos programa.py**
```python
'''
    Programa gestor de proyectos v0.3
    Lucas Andrés Griego
  
    Proyecto
    -nombre del proyecto
    -cliente
    -email
    -telefono
'''
```
**02-Cabecera de bienvenida.py**
```python
'''
    Programa gestor de proyectos v0.3
    Lucas Andrés Griego
  
    Proyecto
    -nombre del proyecto
    -cliente
    -email
    -telefono
'''

print("Programa gestor de proyectos")
print("v0.3 Lucas Andrés Griego")
```
**03-while True.py**
```python
'''
    Programa gestor de proyectos v0.3
    Lucas Andrés Griego
  
    Proyecto
    -nombre del proyecto
    -cliente
    -email
    -telefono
'''

print("Programa gestor de proyectos")
print("v0.3 Lucas Andrés Griego")

while True:
	print("Selecciona una opción")
	print("1.-Agregar un proyecto")
	print("2.-Listar proyectos")
```
**04-Seleccion.py**
```python
'''
    Programa gestor de proyectos v0.3
    Lucas Andrés Griego
  
    Proyecto
    -nombreProyecto
    -descripcion
    -cliente
    -telefono
'''

print("Programa gestor de proyectos")
print("v0.3 Lucas Andrés Griego")

while True:
	print("Selecciona una opción")
	print("1.-Agregar un proyecto")
	print("2.-Listar proyectos")
	opcion = input("Selecciona una opcion: ")
	if opcion == "1":
		
    elif opcion == "2":
```
**05-Insertamos registro.py**
```python
'''
    Programa gestor de proyectos v0.3
    Lucas Andrés Griego
  
    Proyecto
    -nombreProyecto
    -descripcion
    -cliente
    -telefono
'''

print("Programa gestor de proyectos")
print("v0.3 Lucas Andrés Griego")

while True:
    print("Selecciona una opción")
	print("1.-Agregar un proyecto")
    print("2.-Listar proyectos")
	
    opcion = input("Selecciona una opcion: ")
	
	if opcion == "1":
        nombreProyecto = input("Introduce el nombre del nuevo proyecto: ") 
        descripcion = input("Introduce una breve descripcion del proyecto: ") 
        cliente = input("Introduce nombre y apellidos del cliente: ") 
        telefono = input("Introduce telefono del cliente: ") 
        
        archivo = open("proyectos.csv", "a")
        archivo.write(nombreProyecto + "|" + descripcion + "|" + cliente + "|" + telefono + "\n")
        archivo.close()

        print("Tu proyecto ha sido guardado")
        archivo.close()
		
    elif opcion == "2":
        pass
```
**06-Listado de proyectos.py**
```python
'''
    Programa gestor de proyectos v0.3
    Lucas Andrés Griego
  
    Proyecto
    -nombreProyecto
    -descripcion
    -cliente
    -telefono
'''

print("Programa gestor de proyectos")
print("v0.3 Lucas Andrés Griego")
print("+ Proyectos = + Euros")

while True:
    print("Selecciona una opción")
	print("1.-Agregar un proyecto")
    print("2.-Listar proyectos")
	
    opcion = input("Selecciona una opcion: ")
	
	if opcion == "1":
        nombreProyecto = input("Introduce el nombre del nuevo proyecto: ") 
        descripcion = input("Introduce una breve descripcion del proyecto: ") 
        cliente = input("Introduce nombre y apellidos del cliente: ") 
        telefono = input("Introduce telefono del cliente: ") 
        
        archivo = open("proyectos.csv", "a")
        archivo.write(nombreProyecto + "|" + descripcion + "|" + cliente + "|" + telefono + "\n")
        archivo.close()

        print("Tu proyecto ha sido guardado")
        archivo.close()
		
    elif opcion == "2":
        archivo = open("proyectos.csv", "r")
        lineas = archivo.readlines()
        print(lineas)
        archivo.close()
```
**07-Listado de proyectos formateado.py**
```python
''' 
    Programa gestor de proyectos v0.3
    Lucas Andrés Griego
  
    Proyecto
    -nombreProyecto
    -descripcion
    -cliente
    -telefono
'''

print("Programa gestor de proyectos")
print("v0.3 Lucas Andrés Griego")
print("+ Proyectos = + Euros")

while True:
    print("Selecciona una opción")
	print("1.-Agregar un proyecto")
    print("2.-Listar proyectos")
	print("3.-Salir del programa")
	
    opcion = input("Selecciona una opcion: ")
	
	if opcion == "1":
        nombreProyecto = input("Introduce el nombre del nuevo proyecto: ") 
        descripcion = input("Introduce una breve descripcion del proyecto: ") 
        cliente = input("Introduce nombre y apellidos del cliente: ") 
        telefono = input("Introduce telefono del cliente: ") 
        
        archivo = open("proyectos.csv", "a")
        archivo.write(
            nombreProyecto + "|" + 
            descripcion + "|" + 
            cliente + "|" + 
            telefono + "\n"
        )
        archivo.close()

        print("Tu proyecto ha sido guardado")
        archivo.close()
		
    elif opcion == "2":
        archivo = open("proyectos.csv", "r")
        lineas = archivo.readlines()
        cabeceras = [
            "nombreProyecto",
            "descripcion",
            "cliente",
            "telefono"
        ]
        
        for linea in lineas:
            datos = linea.strip().split("|")
            print("\n------------------------------")
            for i in range(0, len(datos)):
                print(cabeceras[i], ":", datos[i])
        archivo.close()
        print("------------------------------")

	elif opcion == "3":
		print("Estas cerrando el programa, adios")
		break
```
**08-Listado de proyectos con cabeceras.py**
```python
''' 
    Programa gestor de proyectos v0.3
    Lucas Andrés Griego
  
    Proyecto
    -nombreProyecto
    -descripcion
    -cliente
    -telefono
'''
print("-"*30)
print("Programa gestor de proyectos")
print("v0.3 Lucas Andrés Griego")
print("+ Proyectos = + Euros")
print("-"*30)

while True:
    print("Selecciona una opción")
    print("1.-Agregar un proyecto")
    print("2.-Listar proyectos")
    print("3.-Salir del programa")
	
    opcion = input("Selecciona una opcion: ")
	
    if opcion == "1":
        nombreProyecto = input("Introduce el nombre del nuevo proyecto: ") 
        descripcion = input("Introduce una breve descripcion del proyecto: ") 
        cliente = input("Introduce nombre y apellidos del cliente: ") 
        telefono = input("Introduce telefono del cliente: ") 
        
        archivo = open("proyectos.csv", "a")
        archivo.write(
            nombreProyecto + "|" + 
            descripcion + "|" + 
            cliente + "|" + 
            telefono + "\n"
        )

        print("Tu proyecto ha sido guardado")
        archivo.close()
		
    elif opcion == "2":
        archivo = open("proyectos.csv", "r")
        # Leo la primera línea, que contiene las cabeceras
        cabecera = archivo.readline()
        # Separo las cabeceras
        cabeceras = cabecera.strip().split("|")
        # Leo el resto de líneas
        lineas = archivo.readlines()
        # Recorro todos los registros
        for linea in lineas:
            # Separo los campos del registro
            datos = linea.strip().split("|")
            print("------------------------------")
            # Muestro cabecera : valor
            for i in range(0, len(datos)):
                print(cabeceras[i], ":", datos[i])
        print("------------------------------")
        archivo.close()

    elif opcion == "3":
        print("Estas cerrando el programa, adios")
        break
```
### 07-Interfaces gráficas
**01-tkinter.py**
```python
import tkinter as tk     # Importa la biblioteca tkinter, que permite crear interfaces gráficas.

'''
    import: importa una biblioteca.
    tkinter: biblioteca de interfaces gráficas.
    as tk: le asigna un nombre más corto.
'''
```
**02-nueva ventana.py**
```python
import tkinter as tk

raiz = tk.Tk()     # Crea la ventana principal del programa y la guarda en la variable raiz.
raiz.mainloop()    # Inicia el bucle de eventos de Tkinter. Mientras está funcionando, la ventana puede responder a clics, teclas y otras acciones del usuario.
                   # Sin mainloop(), el programa normalmente terminaría sin mantener abierta la ventana.
```
**03-Pongo texto.py**
```python
import tkinter as tk

raiz = tk.Tk()

# Agregar texto a la ventana
etiqueta = tk.Label(raiz, text="¡Hola mundo!")
etiqueta.pack()

raiz.mainloop() # no te salgas del bucle

'''
    tk.Label() crea una etiqueta para mostrar información.
    - raiz: indica la ventana donde estará.
    - text="¡Hola mundo!": define su contenido.
    - .pack(): coloca el elemento dentro de la ventana.
'''
```
**04-Tamaño del texto.py**
```python
import tkinter as tk

raiz = tk.Tk()

# Agregar texto a la ventana
etiqueta = tk.Label(raiz, text="¡Hola mundo!", font=("Arial", 24)) # Aumenta el tamaño del texto
etiqueta.pack()

raiz.mainloop() # no te salgas del bucle


'''
    "Arial": tipo de letra.
    24: tamaño de la letra.
'''
```
**05-Creamos botones.py**
```python
'''
    En este archivo estás aprendiendo a crear botones en una ventana de Python utilizando Tkinter.
'''
import tkinter as tk     # Importar Tkinter

raiz = tk.Tk()           # Crear la ventana

# Agregar texto a la ventana
etiqueta = tk.Label(raiz, text="¡Hola mundo!", font=("Arial", 24)) # Aumenta el tamaño del texto
etiqueta.pack()          # Mostrar la etiqueta

boton = tk.Button(raiz,text="Pulsame si te atreves")
boton.pack()             # Colocar el botón

raiz.mainloop() # no te salgas del bucle
```
**06-Padding.py**
```python
'''
    ¿Qué significa Padding?
    En programación de interfaces, padding significa espacio de relleno.
    En tu código utilizas dos parámetros:
    - padx: espacio horizontal (izquierda y derecha).
    - pady: espacio vertical (arriba y abajo).
'''
import tkinter as tk    # importamos Tkinter

raiz = tk.Tk()          # creamos la ventana

# Agregar texto a la ventana
etiqueta = tk.Label(raiz, text="¡Hola mundo!", font=("Arial", 24)) # Aumenta el tamaño del texto (creamos la etiqueta)
etiqueta.pack(padx=20,pady=20)        # colocamos la etiqueta con espacio

boton = tk.Button(raiz,text="Pulsame si te atreves")   # creamos el botón
boton.pack(padx=20,pady=20)                            # colocamos el botón con espacio

raiz.mainloop() # no te salgas del bucle
```
**07-Comando en el boton.py**
```python
import tkinter as tk                    # Importamos Tkinter

def pulsaBoton():                       # Definimos una función
    print("Hola que tal, como estas")   # Instrucción dentro de la función

raiz = tk.Tk()                          # Creamos la ventana

# Agregar texto a la ventana
etiqueta = tk.Label(raiz, text="¡Hola mundo!", font=("Arial", 24)) # Aumenta el tamaño del texto (Creamos una etiquet)
etiqueta.pack(padx=20,pady=20)          # Colocamos la etiqueta

boton = tk.Button(raiz,text="Pulsame si te atreves",command=pulsaBoton)
boton.pack(padx=20,pady=20)             # Colocamos el botón

raiz.mainloop()                         # no te salgas del bucle (Mantenemos la ventana abierta)
```
**08-Escribir en la interfaz.py**
```python
import tkinter as tk

def pulsaBoton():                            # Definimos una función
    print("Hola que tal, como estas")        # Mostramos un mensaje en la consola
    resultado.config(text="prueba superada") # Del resultado, configuro que su texto es X o lo que yo quiera ej: "prueba superada"

raiz = tk.Tk()                               #Creamos la ventana

# Agregar texto a la ventana
etiqueta = tk.Label(raiz, text="¡Hola mundo!", font=("Arial", 24))        # Aumenta el tamaño del texto. Creamos la primera etiqueta
etiqueta.pack(padx=20,pady=20)                                            # Colocamos la etiqueta

boton = tk.Button(raiz,text="Pulsame si te atreves",command=pulsaBoton)   # Creamos el botón
boton.pack(padx=20,pady=20)                                               # Colocamos el botón

resultado = tk.Label(raiz, text="x", font=("Arial", 24))                  # Creamos la etiqueta del resultado
resultado.pack(padx=20,pady=20)                                           # Colocamos la etiqueta del resultado

raiz.mainloop() # no te salgas del bucle
```
**09-Entrada.py**
```python
import tkinter as tk

raiz = tk.Tk()                  # Creamos la ventana principal

entrada = tk.Entry(raiz)        # Creamos un campo de entrada
entrada.pack(padx=20,pady=20)   # Colocamos el campo en la ventana

raiz.mainloop()                 # no te salgas del bucle
```
**10-calculadora de IVA.py**
```python
'''
    Hasta ahora hemos aprendido a crear ventanas, mostrar textos, añadir botones, ejecutar funciones y recoger información con Entry.
    En este archivo vamos a juntar todos esos conocimientos para crear una calculadora de IVA del 21 %.
'''
import tkinter as tk

def calculaIVA():                     # Creamos una función
  basenumero = base.get()             # Obtenemos el número escrito por el usuario
  basenumero = float(basenumero)      # Convertimos el texto en número
  iva = basenumero*0.21               # Calculamos el IVA
  resultado.config(text=iva)          # Mostramos el resultado en la ventana

ventana = tk.Tk()                     # Creamos la ventana

base = tk.Entry(ventana)              # Creamos el campo para introducir números
base.pack(padx=20,pady=20)            # Colocamos el campo

boton_calcula = tk.Button(ventana,text="Calcula!",command=calculaIVA)    # Creamos el botón de calcular
boton_calcula.pack(padx=20,pady=20)                                      # Colocamos el botón

resultado = tk.Label(ventana,text="resultado")                           # Creamos la etiqueta para mostrar el resultado
resultado.pack(padx=20,pady=20)                                          # Colocamos la etiqueta

ventana.mainloop()                                                       # Mantenemos la ventana abierta
```
### 08-Concepto de evento
**01-Agenda tkinter.py**
```python
import tkinter as tk    # Importa la biblioteca Tkinter y le asigna el alias tk, para que podamos utilizar sus funciones de forma abreviada.

ventana = tk.Tk()       # Crea la ventana principal de nuestra aplicación.

ventana.mainloop()      # Inicia el bucle de eventos de Tkinter. Gracias a él, la ventana permanece abierta y puede responder a acciones como hacer clic, escribir o cerrarla.
```
**02-Entradas.py**
```python
'''
    En lugar de mostrar una ventana vacía, presenta tres campos de entrada y un botón.
'''
import tkinter as tk

ventana = tk.Tk()

nombre = tk.Entry(ventana)                            # tk.Entry() crea una caja donde el usuario puede escribir texto en una sola línea.
nombre.pack(padx=20,pady=20)

apellidos = tk.Entry(ventana)
apellidos.pack(padx=20,pady=20)

email = tk.Entry(ventana)
email.pack(padx=20,pady=20)

boton = tk.Button(ventana,text="Guardar proyecto")    # Crea un botón con el texto «Guardar proyecto».
boton.pack(padx=20,pady=20)

ventana.mainloop()
```
**03-Labels.py**
```python
'''
    Este archivo mejora la interfaz anterior utilizando Label.
'''
import tkinter as tk

ventana = tk.Tk()

tk.Label(ventana, text="Nombre del proyecto").pack()       # tk.Label() crea una etiqueta que muestra información en pantalla.
nombre = tk.Entry(ventana)
nombre.pack(padx=20, pady=20)

tk.Label(ventana, text="Descripcion").pack()
apellidos = tk.Entry(ventana)
apellidos.pack(padx=20, pady=20)

tk.Label(ventana, text="Cliente").pack()
email = tk.Entry(ventana)
email.pack(padx=20, pady=20)

boton = tk.Button(ventana, text="Guardar proyecto")
boton.pack(padx=20, pady=20)

ventana.mainloop()


'''
    una interfaz gráfica no consiste únicamente en introducir información, sino también en indicar claramente qué debe escribir el usuario en cada campo.
    Componente	Función
    Label	    Mostrar texto informativo
    Entry	    Permitir escribir texto
    Button	    Ejecutar una acción cuando se pulsa, si tiene una función asociada
    El archivo utiliza tres etiquetas: Nombre, Apellidos y Email.
'''
```
**04-Guardar.py**
```python
'''
    Este es el archivo introduce una función que permite guardar la información de los proyectos.
'''
import tkinter as tk

ventana = tk.Tk()

def guardar():                                                            # Definimos función guardar
    archivo = open("proyectos.csv",'a')                                   # Abrir el archivo en modo append
    texto = nombre.get()+","+apellidos.get()+","+email.get()+"\n"         # Recuperar lo que ha escrito el usuario
    archivo.write(texto)
    archivo.close()                                                       # Cerrar el archivo

tk.Label(ventana, text="Nombre del proyecto").pack()
nombre = tk.Entry(ventana)
nombre.pack(padx=20, pady=20)

tk.Label(ventana, text="Descripcion").pack()
apellidos = tk.Entry(ventana)
apellidos.pack(padx=20, pady=20)

tk.Label(ventana, text="Cliente").pack()
email = tk.Entry(ventana)
email.pack(padx=20, pady=20)

boton = tk.Button(ventana, text="Guardar proyecto",command=guardar)
boton.pack(padx=20, pady=20)

ventana.mainloop()
```
**05-Area de texto.py**
```python
import tkinter as tk

ventana = tk.Tk()

area = tk.Text(ventana)           # Text crea un espacio para escribir textos de varias líneas.
area.pack(padx=20,pady=20)

ventana.mainloop()


'''
    La diferencia fundamental entre Entry y Text es que Entry está pensado para datos cortos de una sola línea, mientras que Text permite introducir párrafos enteros.
'''
```
**06-Escribir dentro del area.py**
```python
import tkinter as tk

ventana = tk.Tk()

area = tk.Text(ventana)
area.pack(padx=20,pady=20)

area.insert("1.0", "Hola que tal")   # .insert()  Se utiliza para introducir texto en una posición concreta
                                     # "1.0"  En un componente Text, las posiciones pueden expresarse como línea.columna. Las líneas empiezan en 1 y las columnas en 0.
ventana.mainloop()


'''
    Estos seis archivos introducen varias instrucciones que aparecen continuamente en aplicaciones desarrolladas con Tkinter.
    Instrucción	    ¿Para qué sirve?
    tk.Tk()	        Crear la ventana principal
    tk.Label()	    Mostrar etiquetas
    tk.Entry()	    Crear entradas de una línea
    tk.Button()	    Crear botones
    tk.Text()	    Crear áreas de texto multilínea
    .pack()	        Colocar elementos en la ventana
    .get()	        Leer el contenido de un Entry
    .insert()	    Insertar contenido en una posición
    command=	    Asociar una función a un botón
    open()	        Abrir o crear un archivo
    .write()	    Escribir en un archivo
    .close()	    Cerrar el archivo
    .mainloop()	    Mantener activa la interfaz gráfica
'''
```
### 09-Creación de controladores de eventos
**01-Grid.py**
```python
'''
    objetivo es enseñarte a crear una ventana y colocar elementos utilizando el sistema de cuadrícula de Tkinter.
'''
import tkinter as tk                                       # Importa la biblioteca tkinter, que permite crear interfaces gráficas con Python.

ventana = tk.Tk()                                          # Crea la ventana principal de la aplicación.

tk.Label(ventana, text="Insertar").grid(row=0,column=0)    # Esta línea hace dos cosas: crea una etiqueta y la coloca dentro de la ventana.

tk.Label(ventana, text="Leer").grid(row=0,column=1)        # Hace exactamente lo mismo que la línea anterior, pero con dos diferencias: - El texto será "Leer". - Se coloca en la columna 1.

ventana.mainloop()                                         # Inicia el bucle principal de eventos de la aplicación.
```
**02-Panel.py**
```python
'''
    Este archivo añade un concepto muy importante: los contenedores Frame.
    En lugar de colocar todos los elementos directamente sobre la ventana, podemos organizarla en diferentes secciones.
'''
import tkinter as tk

ventana = tk.Tk()

insertar = tk.Frame(ventana)       # Crea un contenedor llamado insertar. Un Frame es una zona de la interfaz que permite agrupar elementos gráficos.
insertar.grid(row=0,column=0)      # Coloca el panel insertar en la primera fila y primera columna de la ventana.
leer = tk.Frame(ventana)           # Crea un segundo contenedor llamado leer.
leer.grid(row=0,column=1)          # Coloca el panel leer en la primera fila y segunda columna.

tk.Label(insertar,text="Insertar").pack(padx=20,pady=20)    # Crea una etiqueta dentro del panel insertar.
tk.Label(leer,text="Leer").pack(padx=20,pady=20)            # Crea una etiqueta con el texto "Leer" dentro del segundo panel

ventana.mainloop()                                          # Inicia el bucle principal de eventos, manteniendo la ventana abierta y respondiendo a las interacciones.
```
**03-Controles.py**
```python
'''
    Ahora no solamente tenemos dos paneles, sino que incorporamos un formulario en el que el usuario puede escribir información.
'''
import tkinter as tk                                        # Importa Tkinter.

ventana = tk.Tk()                                           # Crea la ventana principal.

insertar = tk.Frame(ventana)                                # Crea el panel izquierdo.
insertar.grid(row=0,column=0)                               # Lo coloca en la columna 0.
leer = tk.Frame(ventana)                                    # Crea el panel derecho.
leer.grid(row=0,column=1)                                   # Lo coloca en la columna 1.

tk.Label(insertar,text="Insertar").pack(padx=20,pady=20)    # Crea el título "Insertar" dentro del panel izquierdo, con un espacio exterior de 20 píxeles alrededor.

tk.Label(insertar, text="Nombre").pack()                    # Crea una etiqueta con el texto "Nombre".
nombre = tk.Entry(insertar)                                 # Entry es un cuadro de texto de una sola línea.   # Permite al usuario escribir un nombre, un apellido, un correo electrónico u otro valor.
nombre.pack(padx=20, pady=20)                               

tk.Label(insertar, text="Apellidos").pack()
apellidos = tk.Entry(insertar)
apellidos.pack(padx=20, pady=20)

tk.Label(insertar, text="Email").pack()
email = tk.Entry(insertar)
email.pack(padx=20, pady=20)

boton = tk.Button(insertar, text="Guardar contacto")
boton.pack(padx=20, pady=20)

tk.Label(leer,text="Leer").pack(padx=20,pady=20)

area = tk.Text(leer)
area.pack(padx=20,pady=20)

ventana.mainloop()
```
**04-Escribir.py**
```python
'''
    Este archivo introduce las funciones y la escritura de archivos.
    Ahora el botón "Guardar contacto" sí realizará una acción.
'''
import tkinter as tk

def guardar():                                                        # Define una función llamada guardar
    archivo = open("agenda.csv",'a')                                  # Abre un archivo llamado agenda.csv en modo añadir.
    texto = nombre.get()+","+apellidos.get()+","+email.get()+"\n"
    archivo.write(texto)
    archivo.close()

ventana = tk.Tk()

insertar = tk.Frame(ventana)
insertar.grid(row=0,column=0)
leer = tk.Frame(ventana)
leer.grid(row=0,column=1)

tk.Label(insertar,text="Insertar").pack(padx=20,pady=20)

tk.Label(insertar, text="Nombre").pack()
nombre = tk.Entry(insertar)
nombre.pack(padx=20, pady=20)

tk.Label(insertar, text="Apellidos").pack()
apellidos = tk.Entry(insertar)
apellidos.pack(padx=20, pady=20)

tk.Label(insertar, text="Email").pack()
email = tk.Entry(insertar)
email.pack(padx=20, pady=20)

boton = tk.Button(insertar, text="Guardar contacto",command=guardar)
boton.pack(padx=20, pady=20)

tk.Label(leer,text="Leer").pack(padx=20,pady=20)

area = tk.Text(leer)
area.pack(padx=20,pady=20)

ventana.mainloop()
```
## 2-Proyecto
### final
**01-mantenimiento.py**
```python
import tkinter as tk

ventana = tk.Tk()
ventana.title("Mantenimiento de mi coche")

titulo = tk.Label(
    ventana,
    text="Registro de mantenimiento",
    font=("Arial", 18)
)
titulo.pack(padx=20, pady=20)

ventana.mainloop()
```
**02-Entradas.py**
```python
import tkinter as tk

ventana = tk.Tk()
ventana.title("Mantenimiento de mi coche")

titulo = tk.Label(
    ventana,
    text="Registro de mantenimiento",
    font=("Arial", 18)
)
titulo.pack(padx=20, pady=20)

tk.Label(ventana, text="Fecha").pack()
fecha = tk.Entry(ventana)
fecha.pack(padx=20, pady=5)

tk.Label(ventana, text="Kilometraje").pack()
kilometraje = tk.Entry(ventana)
kilometraje.pack(padx=20, pady=5)

tk.Label(ventana, text="Detalle del mantenimiento").pack()
detalle = tk.Entry(ventana)
detalle.pack(padx=20, pady=5)

tk.Label(ventana, text="Coste").pack()
coste = tk.Entry(ventana)
coste.pack(padx=20, pady=5)

ventana.mainloop()

```
**03-Boton guardar.py**
```python
import tkinter as tk

def guardar():
    archivo = open("mantenimiento.csv", "a")
    texto = fecha.get() + "|" + kilometraje.get() + "|" + detalle.get() + "|" + coste.get() + "\n"
    archivo.write(texto)
    archivo.close()

    resultado.config(text="Mantenimiento guardado")

ventana = tk.Tk()
ventana.title("Mantenimiento de mi coche")

titulo = tk.Label(
    ventana,
    text="Registro de mantenimiento",
    font=("Arial", 18)
)
titulo.pack(padx=20, pady=20)

tk.Label(ventana, text="Fecha").pack()
fecha = tk.Entry(ventana)
fecha.pack(padx=20, pady=5)

tk.Label(ventana, text="Kilometraje").pack()
kilometraje = tk.Entry(ventana)
kilometraje.pack(padx=20, pady=5)

tk.Label(ventana, text="Detalle del mantenimiento").pack()
detalle = tk.Entry(ventana)
detalle.pack(padx=20, pady=5)

tk.Label(ventana, text="Coste").pack()
coste = tk.Entry(ventana)
coste.pack(padx=20, pady=5)

# Boton guardar
boton_guardar = tk.Button(
    ventana,
    text="Guardar mantenimiento",
    command=guardar
)
boton_guardar.pack(padx=20, pady=10)

resultado = tk.Label(ventana, text="")
resultado.pack(padx=20, pady=5)

ventana.mainloop()

```
**04-Listar.py**
```python
import tkinter as tk

def guardar():
    archivo = open("mantenimiento.csv", "a")
    texto = fecha.get() + "|" + kilometraje.get() + "|" + detalle.get() + "|" + coste.get() + "\n"
    archivo.write(texto)
    archivo.close()

    resultado.config(text="Mantenimiento guardado")
    
def listar():
    archivo = open("mantenimiento.csv", "r")
    lineas = archivo.readlines()
    archivo.close()

    area.delete("1.0", tk.END)

    for linea in lineas:
        datos = linea.strip().split("|")

        area.insert(tk.END, "Fecha: " + datos[0] + "\n")
        area.insert(tk.END, "Kilometraje: " + datos[1] + "\n")
        area.insert(tk.END, "Detalle: " + datos[2] + "\n")
        area.insert(tk.END, "Coste: " + datos[3] + "\n")
        area.insert(tk.END, "------------------------------\n")

ventana = tk.Tk()
ventana.title("Mantenimiento de mi coche")

titulo = tk.Label(
    ventana,
    text="Registro de mantenimiento",
    font=("Arial", 18)
)
titulo.pack(padx=20, pady=20)

tk.Label(ventana, text="Fecha").pack()
fecha = tk.Entry(ventana)
fecha.pack(padx=20, pady=5)

tk.Label(ventana, text="Kilometraje").pack()
kilometraje = tk.Entry(ventana)
kilometraje.pack(padx=20, pady=5)

tk.Label(ventana, text="Detalle del mantenimiento").pack()
detalle = tk.Entry(ventana)
detalle.pack(padx=20, pady=5)

tk.Label(ventana, text="Coste").pack()
coste = tk.Entry(ventana)
coste.pack(padx=20, pady=5)

# Boton guardar
boton_guardar = tk.Button(
    ventana,
    text="Guardar mantenimiento",
    command=guardar
)
boton_guardar.pack(padx=20, pady=10)

resultado = tk.Label(ventana, text="")
resultado.pack(padx=20, pady=5)

boton_listar = tk.Button(
    ventana,
    text="Listar mantenimientos",                 # Pulsa Listar dos veces: el contenido no debe duplicarse, porque primero vaciamos el area.
    command=listar
)
boton_listar.pack(padx=20, pady=10)

area = tk.Text(ventana, width=55, height=12)
area.pack(padx=20, pady=10)

ventana.mainloop()

```
**05-Programa completo.py**
```python
'''
    Programa para documentación y registro detallado del mantenimiento del coche.
    Permite introducir fecha, kilometraje, detalle y coste, guardar cada mantenimiento en un CSV y consultar los registros desde una ventana.
'''
print("-"*45)
print("Programa para documentación y registro")
print("del mantenimiento de tu coche")
print("Desarrollado por nurLukas de Sturmprojekt")
print("Poder en cada proyecto!")
print("-"*45)

import tkinter as tk

archivo = open("mantenimiento.csv", "a")
archivo.close()

def guardar():
    archivo = open("mantenimiento.csv", "a")
    texto = fecha.get() + "|" + kilometraje.get() + "|" + detalle.get() + "|" + coste.get() + "\n"
    archivo.write(texto)
    archivo.close()

    resultado.config(text="Mantenimiento guardado")
    
def listar():
    archivo = open("mantenimiento.csv", "r")
    lineas = archivo.readlines()
    archivo.close()

    area.delete("1.0", tk.END)

    for linea in lineas:
        datos = linea.strip().split("|")

        area.insert(tk.END, "Fecha: " + datos[0] + "\n")
        area.insert(tk.END, "Kilometraje: " + datos[1] + "\n")
        area.insert(tk.END, "Detalle: " + datos[2] + "\n")
        area.insert(tk.END, "Coste: " + datos[3] + "\n")
        area.insert(tk.END, "------------------------------\n")

ventana = tk.Tk()
ventana.title("Mantenimiento de mi coche")

formulario = tk.Frame(ventana)
formulario.grid(row=0, column=0, padx=20, pady=20)

listado = tk.Frame(ventana)
listado.grid(row=0, column=1, padx=20, pady=20)

titulo = tk.Label(
    formulario,
    text="Registro de mantenimiento",
    font=("Arial", 18)
)
titulo.pack(padx=20, pady=20)

tk.Label(formulario, text="Fecha").pack()
fecha = tk.Entry(formulario)
fecha.pack(padx=20, pady=5)

tk.Label(formulario, text="Kilometraje").pack()
kilometraje = tk.Entry(formulario)
kilometraje.pack(padx=20, pady=5)

tk.Label(formulario, text="Detalle del mantenimiento").pack()
detalle = tk.Entry(formulario)
detalle.pack(padx=20, pady=5)

tk.Label(formulario, text="Coste").pack()
coste = tk.Entry(formulario)
coste.pack(padx=20, pady=5)

boton_guardar = tk.Button(
    formulario,
    text="Guardar mantenimiento",
    command=guardar
)
boton_guardar.pack(padx=20, pady=10)

resultado = tk.Label(formulario, text="")
resultado.pack(padx=20, pady=5)

boton_listar = tk.Button(
    listado,
    text="Listar mantenimientos",
    command=listar
)
boton_listar.pack(padx=20, pady=10)

area = tk.Text(listado, width=55, height=12)
area.pack(padx=20, pady=10)

ventana.mainloop()
```
### sub1
**01-Escribir.py**
```python
'''
    Programa para documentación y registro detallado del mantenimiento del coche.
'''
print("-"*45)
print("Programa para documentación y registro")
print("del mantenimiento de tu coche")
print("Desarrollado por nurLukas de Sturmprojekt")
print("Poder en cada proyecto!")
print("-"*45)

archivo = open("mantenimiento.txt", "w")      # Abre mantenimiento.txt. El modo "w" lo crea si no existe; si existe, borra su contenido. 
archivo.write("Cambio de aceite.")             # Escribe el texto.
archivo.close()                                 # Cierra el archivo.

# Archivo es la variable que utilizamos para trabajar con el fichero abierto.
```
**02-Leer.py**
```python
'''
    Programa para documentación y registro detallado del mantenimiento del coche.
'''
print("-"*45)
print("Programa para documentación y registro")
print("del mantenimiento de tu coche")
print("Desarrollado por nurLukas de Sturmprojekt")
print("Poder en cada proyecto!")
print("-"*45)

archivo = open("mantenimiento.txt", "r")   # "r" abre el archivo para leerlo, sin modificarlo.
lineas = archivo.readlines()               # readlines() lee sus líneas y las devuelve en una lista. --> ['Cambio de aceite'], # lineas guarda esa lista.
print(lineas)                              # La muestra en la terminal.
archivo.close()                              # Cerramos el archivo.
```
**03-Anadir.py**
```python
'''
    Programa para documentación y registro detallado del mantenimiento del coche.
'''
print("-"*45)
print("Programa para documentación y registro")
print("del mantenimiento de tu coche")
print("Desarrollado por nurLukas de Sturmprojekt")
print("Poder en cada proyecto!")
print("-"*45)

detalle = input("Introduce el mantenimiento realizado: ")   # input() pide un texto y lo guarda en detalle.

archivo = open("mantenimiento.txt", "a")                    # "a" añade al final del archivo sin borrar lo anterior.
archivo.write(detalle + "\n")                               # "\n" escribe un salto de línea para separar los mantenimientos.
archivo.close()                                               # Cerramos el archivo.
```
**04-Listar.py**
```python
'''
    Programa para documentación y registro detallado del mantenimiento del coche.
'''
print("-"*45)
print("Programa para documentación y registro")
print("del mantenimiento de tu coche")
print("Desarrollado por nurLukas de Sturmprojekt")
print("Poder en cada proyecto!")
print("-"*45)

print("-"*45)
print("Mantenimientos realizados:")
archivo = open("mantenimiento.txt", "r")
lineas = archivo.readlines()  # Lee todas las líneas restantes del archivo y las guarda en una lista llamada lineas.

for linea in lineas:          # Recorre la lista, tomando una línea en cada repetición.
    print(linea.strip())      # Quita los espacios y saltos de línea de los extremos. Así evitamos líneas vacías entre los mantenimientos al imprimir.
    
archivo.close()

```
**05-Menu.py**
```python
'''
    Programa para documentación y registro detallado del mantenimiento del coche.
'''
print("-"*45)
print("Programa para documentación y registro")
print("del mantenimiento de tu coche")
print("Desarrollado por nurLukas de Sturmprojekt")
print("Poder en cada proyecto!")
print("-"*45)

print("Registro de mantenimientos realizados")

while True:
    print("-"*45)
    print("1.- Agregar mantenimiento realizado")
    print("2.- Listar mantenimientos")
    print("0.- Salir del programa")
    print("-"*45)
    
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        detalle = input("Introduce el mantenimiento realizado: ")
        archivo = open("mantenimiento.txt", "a")
        archivo.write("- " + detalle + "\n")
        archivo.close()
    
    elif opcion == "2":
        print("Mantenimientos realizados:")
        archivo = open("mantenimiento.txt", "r")
        lineas = archivo.readlines()
        
        for linea in lineas:
            print(linea.strip())
        archivo.close()
    
    elif opcion == "0": 
        print("Esta saliendo del programa, adios")
        break
    else:
        print("Opción incorrecta")
```
### sub2
**06-Registros.py**
```python
'''
    ( El contenido de este programa, corresponde a la subunidad 02: "ficheros de datos y registros". 
    Primero guardaremos un mantenimiento con sus cuatro campos. Después aprenderemos a separarlos al leer.
    Programa para documentación y registro detallado del mantenimiento del coche.
'''
print("-"*45)
print("Programa para documentación y registro")
print("del mantenimiento de tu coche")
print("Desarrollado por nurLukas de Sturmprojekt")
print("Poder en cada proyecto!")
print("-"*45)

print("Registrar mantenimiento")
print("-"*45)

fecha = input("Fecha del mantenimiento: ")
kilometraje = input("Kilometraje del coche: ")
detalle = input("Mantenimiento realizado: ")
coste = input("Coste del mantenimiento: ")

archivo = open("mantenimiento.csv", "a")
archivo.write(fecha + "|" + kilometraje + "|" + detalle + "|" + coste + "\n")
archivo.close()

print("Mantenimientos guardados")
archivo = open("mantenimiento.csv", "r")
lineas = archivo.readlines()

for linea in lineas:
    datos = linea.strip().split("|")
    print(datos)
    
archivo.close()
```
**07-Leer registros.py**
```python
'''
    ( El contenido de este programa, corresponde a la subunidad 02: "ficheros de datos y registros". 
    Programa para documentación y registro detallado del mantenimiento del coche.
'''
print("-"*45)
print("Programa para documentación y registro")
print("del mantenimiento de tu coche")
print("Desarrollado por nurLukas de Sturmprojekt")
print("Poder en cada proyecto!")
print("-"*45)

print("Mantenimientos guardados:")
print("-"*45)

archivo = open("mantenimiento.csv", "r")
lineas = archivo.readlines()

for linea in lineas:
    datos = linea.strip().split("|")

    print("------------------------------")
    print("Fecha:", datos[0])
    print("Kilometraje:", datos[1])
    print("Detalle:", datos[2])
    print("Coste:", datos[3])

archivo.close()
```
**08-Diccionario.py**
```python
'''
    ( El contenido de este programa, corresponde a la subunidad 02: "ficheros de datos y registros". 
    Programa para documentación y registro detallado del mantenimiento del coche.
'''
print("-"*45)
print("Programa para documentación y registro")
print("del mantenimiento de tu coche")
print("Desarrollado por nurLukas de Sturmprojekt")
print("Poder en cada proyecto!")
print("-"*45)

print("Mantenimientos guardados:")
print("-"*45)

archivo = open("mantenimiento.csv", "r")
lineas = archivo.readlines()

for linea in lineas:
    datos = linea.strip().split("|")

    mantenimiento = {
        "fecha": datos[0],
        "kilometraje": datos[1],
        "detalle": datos[2],
        "coste": datos[3]
    }

    print("------------------------------")
    print("Fecha:", mantenimiento["fecha"])
    print("Kilometraje:", mantenimiento["kilometraje"])
    print("Detalle:", mantenimiento["detalle"])
    print("Coste:", mantenimiento["coste"])
    
archivo.close()


'''
    datos[0]                 # Lista: accedemos por posición
    mantenimiento["fecha"]   # Diccionario: accedemos por clave
    
    En el diccionario, cada pareja tiene una clave y un valor. Por ejemplo:
    "fecha": datos[0]
'''
```
**09-Leer JSON.py**
```python
import json

print("Datos de mi coche")

archivo = open("coche.json", "r")
coche = json.load(archivo)
archivo.close()

print("Marca:", coche["marca"])
print("Modelo:", coche["modelo"])
print("Matrícula:", coche["matricula"])

'''
    Aquí no usamos split(): json.load() interpreta la estructura del archivo por nosotros.
'''
```
**coche.json**
```json
{
    "marca": "Seat",
    "modelo": "Ibiza",
    "matricula": "1234ABC"
}
```
### sub3
**10-Guardar copia.py**
```python
'''
	Guardaremos una lista en formato binario con pickle
'''

import pickle                            # permite guardar y recuperar objetos de Python, como listas.

mantenimiento = ["2026-10-12", "125000", "Cambio de aceite", "85.50"]

archivo = open("copia.dat", "wb")       # "wb" significa escribir (w) en formato binario (b). Si el archivo existe, sobrescribe su contenido.
pickle.dump(mantenimiento, archivo)     # pickle.dump(mantenimiento, archivo) guarda la lista en el archivo.
archivo.close()

print("Copia guardada")
```
**11-Leer copia.py**
```python
import pickle

archivo = open("copia.dat", "rb")       # "rb" abre el archivo para leer (r) en formato binario (b).
mantenimiento = pickle.load(archivo)    # pickle.load(archivo) recupera el objeto guardado.  mantenimiento recibe la lista recuperada.
archivo.close()

print(mantenimiento)
```
## 3-Resultado  de aprendizaje
**Programacion Unidad 5_Lucas Andrés Griego.md**
```markdown
# Reporte de proyecto

## Información de generación

- **Fecha:** 2026-10-12 04:30:28 +0200
- **Usuario:** lucas
- **Equipo:** LUCAS
- **Sistema operativo:** Windows
- **Arquitectura:** x86_64
- **Directorio de ejecución:** `D:/Herramientas/portables/jocarsa-generador-windows-x64`
- **Proyecto documentado:** `D:/Resultados Aprendizaje_DAM1/4-Programación/Unidad 5`
- **HMAC-SHA-256 de autenticidad:** `226dc7c0c189b30858c26ab78bd03b63af0cdd106f8d685555b66ea170dad621`

> El HMAC-SHA-256 se calcula sobre el documento completo usando un secreto incluido en el programa y 64 ceros en el propio campo del HMAC. El secreto no se escribe en el informe. Este mecanismo permite comprobar integridad y que el documento fue generado con el mismo secreto.

## Estructura del proyecto

```
D:/Resultados Aprendizaje_DAM1/4-Programación/Unidad 5
├── 1-Ejercicios
│   ├── 01-Flujos. Tipos bytes y caracteres. Clases relacionadas
│   │   ├── 01-Escribir.py
│   │   ├── 02-Leer archivos.py
│   │   ├── 03-Gestor de proyectos.py
│   │   ├── 04-Leer registro.py
│   │   ├── 05-Gestor completo.py
│   │   ├── registro_proyectos.txt
│   │   └── test.txt
│   ├── 02-Ficheros de datos. Registros
│   │   ├── 01-Lectura basica.py
│   │   ├── 02-split de linea.py
│   │   ├── 03-Repaso de listas.py
│   │   ├── 04-Diccionario.py
│   │   ├── 05-csv a diccionario.py
│   │   ├── 06-leer json.py
│   │   ├── misdatos.json
│   │   └── proyectos.csv
│   ├── 03-Apertura y cierre de ficheros. Modos de acceso. Escritura y lectura de información en ficheros
│   │   ├── 01-apertura.py
│   │   ├── 02-Cierre de archivos.py
│   │   ├── 03-pickle.py
│   │   ├── 04-pickle ahora si.py
│   │   ├── 05-pickle devolver.py
│   │   └── frutas.txt
│   ├── 04-Utilización de los sistemas de ficheros
│   │   ├── 01-Crear nueva carpeta.py
│   │   ├── 02-Eliminar carpeta.py
│   │   ├── 03-Crear archivo.py
│   │   ├── 04-Eliminar archivo.py
│   │   ├── 05-Caminar.py
│   │   ├── 06-Recorrer arbol win11.py
│   │   ├── 06-Recorrer arbol.py
│   │   ├── 07-Guardar en archivo win11.py
│   │   ├── 07-Guardar en archivo.py
│   │   └── arbol.txt
│   ├── 06-Entrada desde teclado. Salida a pantalla. Formatos de visualización
│   │   ├── 01-Comenzamos programa.py
│   │   ├── 02-Cabecera de bienvenida.py
│   │   ├── 03-while True.py
│   │   ├── 04-Seleccion.py
│   │   ├── 05-Insertamos registro.py
│   │   ├── 06-Listado de proyectos.py
│   │   ├── 07-Listado de proyectos formateado.py
│   │   ├── 08-Listado de proyectos con cabeceras.py
│   │   └── proyectos.csv
│   ├── 07-Interfaces gráficas
│   │   ├── 01-tkinter.py
│   │   ├── 02-nueva ventana.py
│   │   ├── 03-Pongo texto.py
│   │   ├── 04-Tamaño del texto.py
│   │   ├── 05-Creamos botones.py
│   │   ├── 06-Padding.py
│   │   ├── 07-Comando en el boton.py
│   │   ├── 08-Escribir en la interfaz.py
│   │   ├── 09-Entrada.py
│   │   ├── 10-calculadora de IVA.py
│   │   └── 11-ia.py
│   ├── 08-Concepto de evento
│   │   ├── 01-Agenda tkinter.py
│   │   ├── 02-Entradas.py
│   │   ├── 03-Labels.py
│   │   ├── 04-Guardar.py
│   │   ├── 05-Area de texto.py
│   │   └── 06-Escribir dentro del area.py
│   └── 09-Creación de controladores de eventos
│       ├── 01-Grid.py
│       ├── 02-Panel.py
│       ├── 03-Controles.py
│       ├── 04-Escribir.py
│       ├── 05-IA.py
│       └── agenda.csv
├── 2-Proyecto
│   ├── final
│   │   ├── 01-mantenimiento.py
│   │   ├── 02-Entradas.py
│   │   ├── 03-Boton guardar.py
│   │   ├── 04-Listar.py
│   │   ├── 05-Programa completo.py
│   │   └── mantenimiento.csv
│   ├── sub1
│   │   ├── 01-Escribir.py
│   │   ├── 02-Leer.py
│   │   ├── 03-Anadir.py
│   │   ├── 04-Listar.py
│   │   ├── 05-Menu.py
│   │   └── mantenimiento.txt
│   ├── sub2
│   │   ├── 06-Registros.py
│   │   ├── 07-Leer registros.py
│   │   ├── 08-Diccionario.py
│   │   ├── 09-Leer JSON.py
│   │   ├── coche.json
│   │   └── mantenimiento.csv
│   └── sub3
│       ├── 10-Guardar copia.py
│       ├── 11-Leer copia.py
│       └── copia.dat
└── 3-Resultado  de aprendizaje
    └── RA5.md
```

## Bases de datos SQLite

Esta sección documenta únicamente el esquema de las bases SQLite detectadas. No se vuelcan registros ni datos de usuario.

No se han encontrado bases SQLite con extensiones .db, .sqlite o .sqlite3.

## Código (intercalado)

# Unidad 5
## 1-Ejercicios
### 01-Flujos. Tipos bytes y caracteres. Clases relacionadas
**01-Escribir.py**
```python
archivo = open("test.txt",'w')                                # 'w' Indica que a abrimos el archivo especificado, en modo escritura
archivo.write("El contenido de esta unidad, esta muy guay")   # Esto es lo que escribimos en el archivo externo abierto previamente
archivo.close()                                               # Cerrar el arcvhi es una buena practica que debemos tener siempre
```
**02-Leer archivos.py**
```python
archivo = open("test.txt",'r')      # Abrimos el archivo en modo lectura
lector = archivo.readlines()        # guarda todas sus líneas en una lista con readlines()
print(lector)                       # muestra esa lista
archivo.close()                     # Cerramos el archivo
```
**03-Gestor de proyectos.py**
```python
'''
    Implementacion de escritura tipo append
'''

print("-"*45)                                                  # Detalle estetico
print("Programa gestor de proyectos v0.1")                     # Cabecera de presentación
print("Desarrollado por nurLukas de Sturmprojekt")             # Cabecera de presentación
print("-"*45)                                                  # Detalle estetico

while True:                                                    # Bucle del menú
    nombre = input("Introduce el nombre del proyecto: ")       # input con indicaciones
    archivo = open("registro_proyectos.txt",'a')               # "a" significa append, es decir, añadir al final. A diferencia de "w", no borra lo que ya existe.
    archivo.write(nombre+"\n")                                 # "\n" significa salto de línea, así que cada contacto queda en una línea diferente.
    archivo.close()                                            # cerramos el archivo abierto previamente.
    
    
    
    
    
   
```
**04-Leer registro.py**
```python
'''
    Implementacion de lectura tipo "read".
'''

print("-"*45)                                          # Detalle estetico.
print("Programa gestor de proyectos v0.1")             # Cabecera de presentación.
print("Desarrollado por nurLukas de Sturmprojekt")     # Cabecera de presentación.
print("-"*45)                                          # Detalle estetico.


archivo = open("registro_proyectos.txt",'r')           # Apertura del archivo, en modo lectura
lineas = archivo.readlines()                           # crea una lista parecida a: ["Ruffoo\n", "zandtvoort\n", "Corcobo\n"].
for linea in lineas:                                   # Para cada elemento que haya dentro de lineas, guárdalo temporalmente en la variable linea.
    print(linea)                                       # imprime cada nombre.
archivo.close()                                        # Cierra el archivo.
```
**05-Gestor completo.py**
```python
'''
    Implementacion de lectura y escritura.
'''

print("-"*45)                                              # Detalle estetico.
print("Programa gestor de proyectos v0.2")                 # Cabecera de presentación.
print("Desarrollado por nurLukas de Sturmprojekt")         # Cabecera de presentación.
print("-"*45)                                              # Detalle estetico

while True:                                                # Bucle infinito,  mantiene el menú activo hasta que el usuario elige salir.
    print("-"*35)                                          # Detalle estetico
    print("Selecciona una opcion")
    print("1.-Introduce un proyecto")
    print("2.-Selecciona los proyectos")
    print("3.-Salir del gestor")
    opcion = input("Escoge una opción: ")                  # input: Lee la opción introducida por el usuario.
    print("-"*35)                                          # Detalle estetico
    if opcion == "1":
        archivo = open("registro_proyectos.txt",'a')       # # Apertura del archivo, en modo append
        nombre = input("Ahora introduce el nombre del nuevo proyecto: ")
        archivo.write(nombre+"\n")
        archivo.close()                                    # Cierra el archivo.
    elif opcion == "2":
        archivo = open("registro_proyectos.txt",'r')       # Apertura del archivo, en modo lectura
        lineas = archivo.readlines()                       # Guarda todas las líneas del archivo en una lista.
        for linea in lineas:                               # Recorre cada línea almacenada en la lista.
            print(linea)                                   # imprime cada nombre.
            archivo.close()                                # Cierra el archivo.
    elif opcion == "3":
        print("Saliendo del gestor, adios")
        break                                              # Se cierra el programa
    else:
        print("Opción incorrecta")
    
```
### 02-Ficheros de datos. Registros
**01-Lectura basica.py**
```python
archivo = open('proyectos.csv','r')   # Aquí se abre el archivo proyectos.csv en modo lectura
lineas = archivo.readlines()          # se pretende leer todas las líneas del archivo y guardarlas en una lista llamada lineas
for linea in lineas:                  # Esto recorre la lista lineas          
    print(lineas)
```
**02-split de linea.py**
```python
'''
    split() significa dividir o separar un texto.
'''
archivo = open('proyectos.csv','r')    # Abre el archivo proyectos.csv en modo lectura ('r')
lineas = archivo.readlines()           # Lee todas las líneas del archivo y las guarda en una lista llamada lineas
for linea in lineas:                   # Recorre una por una todas las líneas guardadas en la lista
	partido = linea.split("|")         # Divide la línea cada vez que encuentra el símbolo |   # El resultado se guarda en una lista llamada partido
	print(partido)                     # # Muestra en pantalla la lista resultante
```
**03-Repaso de listas.py**
```python
lista = ['Ignacio Emanuel', 'Andrés Lago', 'nacho.kapo@ejemplo.com', 'carrer el wachin 28', 'Valencia', '612345678\n']  # Crea una lista llamada "lista" con varios elementos de texto


print(lista)         # Muestra la lista completa
print(lista[0])      # Muestra el primer elemento de la lista
print(lista[1])      # Muestra el segundo elemento de la lista
print(lista[2])      # Muestra el tercer elemento de la lista


# \n es un carácter especial que significa “salta a la siguiente línea”.

# Suele aparecer mucho cuando lees líneas de un archivo con readlines(), porque cada línea del archivo normalmente termina con \n.
```
**04-Diccionario.py**
```python
diccionario = {                              # Crea un diccionario llamado "diccionario"
  'nombre':'Ana',                            # "nombre" es la clave y "Ana" es su valor
  'apellidos':'García López', 
  'email':'ana.garcia@example.com',          # Guarda un email asociado a la clave "email"
  'direccion':'Calle Colón 24, Valencia', 
  'telefono':'612345678'                     # Guarda un teléfono asociado a la clave "telefono"
}

print(diccionario)                           # Muestra el diccionario completo
print(diccionario['nombre'])                 # Muestra solamente el valor asociado a la clave "nombre"


# Un diccionario funciona con parejas de clave : valor. Por ejemplo: 'nombre': 'Ana'
```
**05-csv a diccionario.py**
```python
# Primero abrimos
archivo = open('proyectos.csv','r')
# Solo leemos la primera linea
cabecera = archivo.readline()  # Singular
# Partimos la primera linea en una lista de cabeceras de columna
cabeceras = cabecera.split("|")
# Ahora sí ya lo leemos todo
lineas = archivo.readlines()  # Plural
# Recorro todas las lineas
for linea in lineas:
    # Parto una linea completa en campos individuales
    datos = linea.split("|")
    for i in range(0, len(datos)):
        print(cabeceras[i], ":", datos[i])
```
**06-leer json.py**
```python
import json

archivo = open("misdatos.json", 'r')
contenido = json.load(archivo)
#print(contenido)
print(contenido['nombre'])
archivo.close()
```
**misdatos.json**
```json
{
  "nombre": "Lucas Andrés Griego",
  "marca": "STURMPROJEKT",
  "nacimiento": "1995-10-06",
  "ciudad": "Valencia",
  "pais": "España",
  "profesion": "Desarrollador informatico",
  "especialidad": "Programación e Inteligencia Artificial",
  "experiencia_desde": 2025,
  "tecnologias": [
    "Python",
    "PHP",
    "JavaScript",
    "C++",
    "SQL",
    "Linux",
    "IA"
  ],
  "web": "https://sturmprojekt.es"
}
```
### 03-Apertura y cierre de ficheros. Modos de acceso. Escritura y lectura de información en ficheros
**01-apertura.py**
```python
archivo = open('archivo.txt','w')

# archivo: es una variable donde guardamos la referencia al archivo abierto.
# open(): es una función de Python que sirve para abrir archivos.
# 'archivo.txt': es el nombre del archivo que queremos abrir.
# 'w': indica que queremos abrirlo en modo escritura (write).


'''
    Modo	Significado	    Qué hace
    'w'	    Write	        Escribe, borrando lo anterior
    'r'	    Read	        Lee un archivo existente
    'a'	    Append	        Añade contenido al final
    'wb'	Write binary	Escribe datos binarios
    'rb'	Read binary	    Lee datos binarios
'''
```
**02-Cierre de archivos.py**
```python
archivo = open('archivo.txt','w')
archivo.close  #Cuando abres un archivo, Python utiliza recursos del sistema para trabajar con él. Cuando terminas, debes cerrarlo para liberar esos recursos y asegurar que se completen las escrituras pendientes.
```
**03-pickle.py**
```python
frutas = ['manzana','pera','platano']    # Creamos una lista llamada frutas con tres elementos.

archivo = open("frutas.txt",'w')         # Creamos o abrimos un archivo de texto llamado frutas.txt para escribir información.
archivo.write(str(frutas))
archivo.close()

'''
    str(frutas) convierte la lista en una cadena de texto.
    Pero hay un inconveniente: cuando recuperes la información, será texto, no una lista de Python.
    Y precisamente para solucionar esto aparece pickle.
'''
```
**04-pickle ahora si.py**
```python
import pickle                             # Esto permite utilizar las funciones de pickle.

frutas = ['manzana', 'pera', 'platano']   # Creamos la lista

archivo = open('frutas.dat', 'wb')        # Abrimos un archivo binario
pickle.dump(frutas, archivo)              # Guardamos la lista


'''
    ¿Qué es pickle?
    pickle es un módulo de Python que permite guardar objetos de Python en archivos y recuperarlos posteriormente.
    Por ejemplo, puedes guardar listas, diccionarios y otros objetos compatibles.
'''
```
**05-pickle devolver.py**
```python
import pickle                        # Importamos pickle

frutas = []                          # Creamos una lista vacía

archivo = open('frutas.dat', 'rb')   # Abrimos el archivo para leer
frutas = pickle.load(archivo)        # Recuperamos los datos
print(frutas)                        # Mostramos el resultado
archivo.close()                      # Cerramos el archivo


'''
    Diferencia entre dump() y load()
    pickle.dump()	Guarda	Pasar un objeto de Python a un archivo
    pickle.load()	Recupera	Pasar los datos del archivo a un objeto de Python
'''
```
### 04-Utilización de los sistemas de ficheros
**01-Crear nueva carpeta.py**
```python
import os                    # Importa el módulo os de Python, que permite interactuar con el sistema operativo y realizar operaciones con archivos y carpetas.

os.mkdir("documentos")


'''
    os.mkdir("documentos")
    - os: módulo del sistema operativo.
    - mkdir: significa make directory (crear directorio).
    - "documentos": nombre de la carpeta que queremos crear.
'''
```
**02-Eliminar carpeta.py**
```python
import os

os.rmdir("documentos")     # os.rmdir() significa remove directory (eliminar directorio).

'''
    Pero tiene una condición muy importante: la carpeta debe estar vacía.
    Por ejemplo:
    - Si documentos está vacía → se elimina.
    - Si contiene apuntes.txt → da un error.
    - Si no existe → da un error.
'''
```
**03-Crear archivo.py**
```python
'''
    Este programa crea un archivo llamado archivo.txt.
'''
archivo = open("archivo.txt",'w') # open() abre un archivo., "archivo.txt" indica el archivo que queremos utilizar, 'w' indica que queremos abrirlo en modo escritura (write).
archivo.close()                   # Cierra el archivo después de abrirlo.
```
**04-Eliminar archivo.py**
```python
'''
    Elimina el archivo archivo.txt del directorio de trabajo actual.
'''
import os
os.remove("archivo.txt")     # os.remove() se utiliza para eliminar archivos, no carpetas.
```
**05-Caminar.py**
```python
import os

arbol = os.walk("/var/www/html/tame2627dam1")   # os.walk() Permite recorrer la estructura de directorios, incluyendo carpetas, subcarpetas y archivos.
print(arbol)                                    # No muestra las carpetas ni los archivos. Muestra una representación del objeto iterador

'''
    os.walk() prepara un recorrido del árbol de directorios.
    "/var/www/html/tame2627dam1" es la ruta desde la que empezará.
    arbol guarda el iterador generado.
'''


'''
    En windows11:
   
   import os

    arbol = os.walk(r"D:\2627_DAM1\4-Programación\05-Lectura y escritura de información\04-Utilización de los sistemas de ficheros")
    print(arbol)

    ¿Qué hemos cambiado?
    Únicamente dos cosas en la ruta:
    1. Hemos sustituido /var/www/html/tame2627dam1 por tu ruta de Windows.
    2. Hemos añadido una r delante de las comillas para que Python interprete correctamente las barras invertidas \.
'''
```
**06-Recorrer arbol win11.py**
```python

import os

arbol = os.walk(r"D:\2627_DAM1\4-Programación\05-Lectura y escritura de información\04-Utilización de los sistemas de ficheros")

for carpeta, carpetas, archivos in arbol:
    print("Carpeta actual:", carpeta)

    print("Subcarpetas:")
    for subcarpeta in carpetas:
        print("  📁", subcarpeta)

    print("Archivos:")
    for archivo in archivos:
        print("  📄", archivo)

    print()
```
**06-Recorrer arbol.py**
```python
'''
    Este es uno de los ejercicios más importantes, porque combina os.walk() con varios bucles for.
    ¿Qué hace este programa?
    Recorre una carpeta y todas sus subcarpetas para mostrar:
    - La carpeta que está examinando.
    - Las subcarpetas que contiene.
    - Los archivos que contiene.
    No crea, modifica ni elimina archivos. Solo consulta y muestra información.
'''
import os                                          # Importar el módulo os

arbol = os.walk("/var/www/html/tame2627dam1")      # Preparar el recorrido

for carpeta, carpetas, archivos in arbol:          # Bucle for principal
    print("Carpeta actual:", carpeta)

    print("Subcarpetas:")
    for subcarpeta in carpetas:
        print("  📁", subcarpeta)

    print("Archivos:")
    for archivo in archivos:
        print("  📄", archivo)

    print()
    
'''
    os.walk() recorre los directorios y, en cada vuelta, nos da tres cosas: 
    la ruta actual, 
    sus subcarpetas 
    y sus archivos. 
    El for principal avanza por los directorios 
    y los otros dos for muestran lo que hay dentro de cada uno.
'''
```
**07-Guardar en archivo win11.py**
```python

import os

ruta = r"D:\2627_DAM1\4-Programación\05-Lectura y escritura de información\04-Utilización de los sistemas de ficheros"

with open("arbol.txt", "w") as salida:

    for carpeta, carpetas, archivos in os.walk(ruta):
        salida.write(carpeta + "\n")

        for archivo in archivos:
            salida.write("  - " + archivo + "\n")

print("Tree saved to arbol.txt")
```
**07-Guardar en archivo.py**
```python
'''
    Este programa Recorre una carpeta y todas sus subcarpetas. 
    Después guarda sus rutas y los nombres de los archivos encontrados en un documento de texto llamado arbol.txt.
'''
import os                                                 # Importamos el módulo os, permite a Python interactuar con el sistema operativo.

ruta = "/var/www/html/tame2627dam1"                       # Indicamos la ruta que queremos recorrer, Aquí creamos una variable llamada ruta. Dentro guardamos la dirección de la carpeta que queremos analizar.

with open("arbol.txt", "w") as salida:                    # Abrimos un archivo para escribir

    for carpeta, carpetas, archivos in os.walk(ruta):     # Recorremos los directorios
        salida.write(carpeta + "\n")

        for archivo in archivos:
            salida.write("  - " + archivo + "\n")         # Guardamos la ruta de la carpeta

print("Tree saved to arbol.txt")                          # Mostramos un mensaje final
```
### 06-Entrada desde teclado. Salida a pantalla. Formatos de visualización
**01-Comenzamos programa.py**
```python
'''
    Programa gestor de proyectos v0.3
    Lucas Andrés Griego
  
    Proyecto
    -nombre del proyecto
    -cliente
    -email
    -telefono
'''
```
**02-Cabecera de bienvenida.py**
```python
'''
    Programa gestor de proyectos v0.3
    Lucas Andrés Griego
  
    Proyecto
    -nombre del proyecto
    -cliente
    -email
    -telefono
'''

print("Programa gestor de proyectos")
print("v0.3 Lucas Andrés Griego")
```
**03-while True.py**
```python
'''
    Programa gestor de proyectos v0.3
    Lucas Andrés Griego
  
    Proyecto
    -nombre del proyecto
    -cliente
    -email
    -telefono
'''

print("Programa gestor de proyectos")
print("v0.3 Lucas Andrés Griego")

while True:
	print("Selecciona una opción")
	print("1.-Agregar un proyecto")
	print("2.-Listar proyectos")
```
**04-Seleccion.py**
```python
'''
    Programa gestor de proyectos v0.3
    Lucas Andrés Griego
  
    Proyecto
    -nombreProyecto
    -descripcion
    -cliente
    -telefono
'''

print("Programa gestor de proyectos")
print("v0.3 Lucas Andrés Griego")

while True:
	print("Selecciona una opción")
	print("1.-Agregar un proyecto")
	print("2.-Listar proyectos")
	opcion = input("Selecciona una opcion: ")
	if opcion == "1":
		
    elif opcion == "2":
```
**05-Insertamos registro.py**
```python
'''
    Programa gestor de proyectos v0.3
    Lucas Andrés Griego
  
    Proyecto
    -nombreProyecto
    -descripcion
    -cliente
    -telefono
'''

print("Programa gestor de proyectos")
print("v0.3 Lucas Andrés Griego")

while True:
    print("Selecciona una opción")
	print("1.-Agregar un proyecto")
    print("2.-Listar proyectos")
	
    opcion = input("Selecciona una opcion: ")
	
	if opcion == "1":
        nombreProyecto = input("Introduce el nombre del nuevo proyecto: ") 
        descripcion = input("Introduce una breve descripcion del proyecto: ") 
        cliente = input("Introduce nombre y apellidos del cliente: ") 
        telefono = input("Introduce telefono del cliente: ") 
        
        archivo = open("proyectos.csv", "a")
        archivo.write(nombreProyecto + "|" + descripcion + "|" + cliente + "|" + telefono + "\n")
        archivo.close()

        print("Tu proyecto ha sido guardado")
        archivo.close()
		
    elif opcion == "2":
        pass
```
**06-Listado de proyectos.py**
```python
'''
    Programa gestor de proyectos v0.3
    Lucas Andrés Griego
  
    Proyecto
    -nombreProyecto
    -descripcion
    -cliente
    -telefono
'''

print("Programa gestor de proyectos")
print("v0.3 Lucas Andrés Griego")
print("+ Proyectos = + Euros")

while True:
    print("Selecciona una opción")
	print("1.-Agregar un proyecto")
    print("2.-Listar proyectos")
	
    opcion = input("Selecciona una opcion: ")
	
	if opcion == "1":
        nombreProyecto = input("Introduce el nombre del nuevo proyecto: ") 
        descripcion = input("Introduce una breve descripcion del proyecto: ") 
        cliente = input("Introduce nombre y apellidos del cliente: ") 
        telefono = input("Introduce telefono del cliente: ") 
        
        archivo = open("proyectos.csv", "a")
        archivo.write(nombreProyecto + "|" + descripcion + "|" + cliente + "|" + telefono + "\n")
        archivo.close()

        print("Tu proyecto ha sido guardado")
        archivo.close()
		
    elif opcion == "2":
        archivo = open("proyectos.csv", "r")
        lineas = archivo.readlines()
        print(lineas)
        archivo.close()
```
**07-Listado de proyectos formateado.py**
```python
''' 
    Programa gestor de proyectos v0.3
    Lucas Andrés Griego
  
    Proyecto
    -nombreProyecto
    -descripcion
    -cliente
    -telefono
'''

print("Programa gestor de proyectos")
print("v0.3 Lucas Andrés Griego")
print("+ Proyectos = + Euros")

while True:
    print("Selecciona una opción")
	print("1.-Agregar un proyecto")
    print("2.-Listar proyectos")
	print("3.-Salir del programa")
	
    opcion = input("Selecciona una opcion: ")
	
	if opcion == "1":
        nombreProyecto = input("Introduce el nombre del nuevo proyecto: ") 
        descripcion = input("Introduce una breve descripcion del proyecto: ") 
        cliente = input("Introduce nombre y apellidos del cliente: ") 
        telefono = input("Introduce telefono del cliente: ") 
        
        archivo = open("proyectos.csv", "a")
        archivo.write(
            nombreProyecto + "|" + 
            descripcion + "|" + 
            cliente + "|" + 
            telefono + "\n"
        )
        archivo.close()

        print("Tu proyecto ha sido guardado")
        archivo.close()
		
    elif opcion == "2":
        archivo = open("proyectos.csv", "r")
        lineas = archivo.readlines()
        cabeceras = [
            "nombreProyecto",
            "descripcion",
            "cliente",
            "telefono"
        ]
        
        for linea in lineas:
            datos = linea.strip().split("|")
            print("\n------------------------------")
            for i in range(0, len(datos)):
                print(cabeceras[i], ":", datos[i])
        archivo.close()
        print("------------------------------")

	elif opcion == "3":
		print("Estas cerrando el programa, adios")
		break
```
**08-Listado de proyectos con cabeceras.py**
```python
''' 
    Programa gestor de proyectos v0.3
    Lucas Andrés Griego
  
    Proyecto
    -nombreProyecto
    -descripcion
    -cliente
    -telefono
'''
print("-"*30)
print("Programa gestor de proyectos")
print("v0.3 Lucas Andrés Griego")
print("+ Proyectos = + Euros")
print("-"*30)

while True:
    print("Selecciona una opción")
    print("1.-Agregar un proyecto")
    print("2.-Listar proyectos")
    print("3.-Salir del programa")
	
    opcion = input("Selecciona una opcion: ")
	
    if opcion == "1":
        nombreProyecto = input("Introduce el nombre del nuevo proyecto: ") 
        descripcion = input("Introduce una breve descripcion del proyecto: ") 
        cliente = input("Introduce nombre y apellidos del cliente: ") 
        telefono = input("Introduce telefono del cliente: ") 
        
        archivo = open("proyectos.csv", "a")
        archivo.write(
            nombreProyecto + "|" + 
            descripcion + "|" + 
            cliente + "|" + 
            telefono + "\n"
        )

        print("Tu proyecto ha sido guardado")
        archivo.close()
		
    elif opcion == "2":
        archivo = open("proyectos.csv", "r")
        # Leo la primera línea, que contiene las cabeceras
        cabecera = archivo.readline()
        # Separo las cabeceras
        cabeceras = cabecera.strip().split("|")
        # Leo el resto de líneas
        lineas = archivo.readlines()
        # Recorro todos los registros
        for linea in lineas:
            # Separo los campos del registro
            datos = linea.strip().split("|")
            print("------------------------------")
            # Muestro cabecera : valor
            for i in range(0, len(datos)):
                print(cabeceras[i], ":", datos[i])
        print("------------------------------")
        archivo.close()

    elif opcion == "3":
        print("Estas cerrando el programa, adios")
        break
```
### 07-Interfaces gráficas
**01-tkinter.py**
```python
import tkinter as tk     # Importa la biblioteca tkinter, que permite crear interfaces gráficas.

'''
    import: importa una biblioteca.
    tkinter: biblioteca de interfaces gráficas.
    as tk: le asigna un nombre más corto.
'''
```
**02-nueva ventana.py**
```python
import tkinter as tk

raiz = tk.Tk()     # Crea la ventana principal del programa y la guarda en la variable raiz.
raiz.mainloop()    # Inicia el bucle de eventos de Tkinter. Mientras está funcionando, la ventana puede responder a clics, teclas y otras acciones del usuario.
                   # Sin mainloop(), el programa normalmente terminaría sin mantener abierta la ventana.
```
**03-Pongo texto.py**
```python
import tkinter as tk

raiz = tk.Tk()

# Agregar texto a la ventana
etiqueta = tk.Label(raiz, text="¡Hola mundo!")
etiqueta.pack()

raiz.mainloop() # no te salgas del bucle

'''
    tk.Label() crea una etiqueta para mostrar información.
    - raiz: indica la ventana donde estará.
    - text="¡Hola mundo!": define su contenido.
    - .pack(): coloca el elemento dentro de la ventana.
'''
```
**04-Tamaño del texto.py**
```python
import tkinter as tk

raiz = tk.Tk()

# Agregar texto a la ventana
etiqueta = tk.Label(raiz, text="¡Hola mundo!", font=("Arial", 24)) # Aumenta el tamaño del texto
etiqueta.pack()

raiz.mainloop() # no te salgas del bucle


'''
    "Arial": tipo de letra.
    24: tamaño de la letra.
'''
```
**05-Creamos botones.py**
```python
'''
    En este archivo estás aprendiendo a crear botones en una ventana de Python utilizando Tkinter.
'''
import tkinter as tk     # Importar Tkinter

raiz = tk.Tk()           # Crear la ventana

# Agregar texto a la ventana
etiqueta = tk.Label(raiz, text="¡Hola mundo!", font=("Arial", 24)) # Aumenta el tamaño del texto
etiqueta.pack()          # Mostrar la etiqueta

boton = tk.Button(raiz,text="Pulsame si te atreves")
boton.pack()             # Colocar el botón

raiz.mainloop() # no te salgas del bucle
```
**06-Padding.py**
```python
'''
    ¿Qué significa Padding?
    En programación de interfaces, padding significa espacio de relleno.
    En tu código utilizas dos parámetros:
    - padx: espacio horizontal (izquierda y derecha).
    - pady: espacio vertical (arriba y abajo).
'''
import tkinter as tk    # importamos Tkinter

raiz = tk.Tk()          # creamos la ventana

# Agregar texto a la ventana
etiqueta = tk.Label(raiz, text="¡Hola mundo!", font=("Arial", 24)) # Aumenta el tamaño del texto (creamos la etiqueta)
etiqueta.pack(padx=20,pady=20)        # colocamos la etiqueta con espacio

boton = tk.Button(raiz,text="Pulsame si te atreves")   # creamos el botón
boton.pack(padx=20,pady=20)                            # colocamos el botón con espacio

raiz.mainloop() # no te salgas del bucle
```
**07-Comando en el boton.py**
```python
import tkinter as tk                    # Importamos Tkinter

def pulsaBoton():                       # Definimos una función
    print("Hola que tal, como estas")   # Instrucción dentro de la función

raiz = tk.Tk()                          # Creamos la ventana

# Agregar texto a la ventana
etiqueta = tk.Label(raiz, text="¡Hola mundo!", font=("Arial", 24)) # Aumenta el tamaño del texto (Creamos una etiquet)
etiqueta.pack(padx=20,pady=20)          # Colocamos la etiqueta

boton = tk.Button(raiz,text="Pulsame si te atreves",command=pulsaBoton)
boton.pack(padx=20,pady=20)             # Colocamos el botón

raiz.mainloop()                         # no te salgas del bucle (Mantenemos la ventana abierta)
```
**08-Escribir en la interfaz.py**
```python
import tkinter as tk

def pulsaBoton():                            # Definimos una función
    print("Hola que tal, como estas")        # Mostramos un mensaje en la consola
    resultado.config(text="prueba superada") # Del resultado, configuro que su texto es X o lo que yo quiera ej: "prueba superada"

raiz = tk.Tk()                               #Creamos la ventana

# Agregar texto a la ventana
etiqueta = tk.Label(raiz, text="¡Hola mundo!", font=("Arial", 24))        # Aumenta el tamaño del texto. Creamos la primera etiqueta
etiqueta.pack(padx=20,pady=20)                                            # Colocamos la etiqueta

boton = tk.Button(raiz,text="Pulsame si te atreves",command=pulsaBoton)   # Creamos el botón
boton.pack(padx=20,pady=20)                                               # Colocamos el botón

resultado = tk.Label(raiz, text="x", font=("Arial", 24))                  # Creamos la etiqueta del resultado
resultado.pack(padx=20,pady=20)                                           # Colocamos la etiqueta del resultado

raiz.mainloop() # no te salgas del bucle
```
**09-Entrada.py**
```python
import tkinter as tk

raiz = tk.Tk()                  # Creamos la ventana principal

entrada = tk.Entry(raiz)        # Creamos un campo de entrada
entrada.pack(padx=20,pady=20)   # Colocamos el campo en la ventana

raiz.mainloop()                 # no te salgas del bucle
```
**10-calculadora de IVA.py**
```python
'''
    Hasta ahora hemos aprendido a crear ventanas, mostrar textos, añadir botones, ejecutar funciones y recoger información con Entry.
    En este archivo vamos a juntar todos esos conocimientos para crear una calculadora de IVA del 21 %.
'''
import tkinter as tk

def calculaIVA():                     # Creamos una función
  basenumero = base.get()             # Obtenemos el número escrito por el usuario
  basenumero = float(basenumero)      # Convertimos el texto en número
  iva = basenumero*0.21               # Calculamos el IVA
  resultado.config(text=iva)          # Mostramos el resultado en la ventana

ventana = tk.Tk()                     # Creamos la ventana

base = tk.Entry(ventana)              # Creamos el campo para introducir números
base.pack(padx=20,pady=20)            # Colocamos el campo

boton_calcula = tk.Button(ventana,text="Calcula!",command=calculaIVA)    # Creamos el botón de calcular
boton_calcula.pack(padx=20,pady=20)                                      # Colocamos el botón

resultado = tk.Label(ventana,text="resultado")                           # Creamos la etiqueta para mostrar el resultado
resultado.pack(padx=20,pady=20)                                          # Colocamos la etiqueta

ventana.mainloop()                                                       # Mantenemos la ventana abierta
```
**11-ia.py**
```python
import tkinter as tk

# -----------------------------------
# Funciones
# -----------------------------------

def calculaIVA():
    try:
        basenumero = float(base.get().replace(",", "."))

        porcentaje = iva_seleccionado.get()
        iva = basenumero * porcentaje / 100
        total = basenumero + iva

        resultado_iva.config(
            text=f"{iva:.2f} €"
        )

        resultado_total.config(
            text=f"{total:.2f} €"
        )

        mensaje.config(
            text=f"IVA aplicado: {porcentaje}%",
            fg="#888888"
        )

    except ValueError:
        mensaje.config(
            text="⚠ Introduce un número válido",
            fg="#ff5c5c"
        )


def limpiar():
    base.delete(0, tk.END)
    resultado_iva.config(text="0.00 €")
    resultado_total.config(text="0.00 €")
    mensaje.config(text="Introduce una base imponible")
    base.focus()


# -----------------------------------
# Ventana
# -----------------------------------

ventana = tk.Tk()
ventana.title("Calculadora de IVA")
ventana.geometry("480x650")
ventana.resizable(False, False)
ventana.configure(bg="#111827")


# -----------------------------------
# Título
# -----------------------------------

titulo = tk.Label(
    ventana,
    text="CALCULADORA IVA",
    font=("Arial", 24, "bold"),
    bg="#111827",
    fg="white"
)

titulo.pack(pady=(35, 5))


subtitulo = tk.Label(
    ventana,
    text="Calcula impuestos de forma rápida",
    font=("Arial", 11),
    bg="#111827",
    fg="#9ca3af"
)

subtitulo.pack(pady=(0, 25))


# -----------------------------------
# Tarjeta principal
# -----------------------------------

tarjeta = tk.Frame(
    ventana,
    bg="#1f2937",
    padx=30,
    pady=25
)

tarjeta.pack(
    padx=35,
    fill="x"
)


# -----------------------------------
# Base imponible
# -----------------------------------

etiqueta_base = tk.Label(
    tarjeta,
    text="BASE IMPONIBLE",
    font=("Arial", 10, "bold"),
    bg="#1f2937",
    fg="#9ca3af"
)

etiqueta_base.pack(anchor="w")


base = tk.Entry(
    tarjeta,
    font=("Arial", 24),
    justify="right",
    bg="#111827",
    fg="white",
    insertbackground="white",
    relief="flat"
)

base.pack(
    fill="x",
    ipady=12,
    pady=(8, 20)
)


# -----------------------------------
# Selector IVA
# -----------------------------------

etiqueta_iva = tk.Label(
    tarjeta,
    text="TIPO DE IVA",
    font=("Arial", 10, "bold"),
    bg="#1f2937",
    fg="#9ca3af"
)

etiqueta_iva.pack(anchor="w")


iva_seleccionado = tk.IntVar(value=21)

tipos = tk.Frame(
    tarjeta,
    bg="#1f2937"
)

tipos.pack(
    fill="x",
    pady=(10, 20)
)


for porcentaje in [4, 10, 21]:

    boton = tk.Radiobutton(
        tipos,
        text=f"{porcentaje}%",
        variable=iva_seleccionado,
        value=porcentaje,
        indicatoron=False,
        font=("Arial", 12, "bold"),
        bg="#374151",
        fg="white",
        selectcolor="#2563eb",
        activebackground="#2563eb",
        activeforeground="white",
        relief="flat",
        padx=15,
        pady=8
    )

    boton.pack(
        side="left",
        expand=True,
        fill="x",
        padx=4
    )


# -----------------------------------
# Botón calcular
# -----------------------------------

boton_calcula = tk.Button(
    tarjeta,
    text="CALCULAR IVA",
    command=calculaIVA,
    font=("Arial", 13, "bold"),
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    relief="flat",
    cursor="hand2"
)

boton_calcula.pack(
    fill="x",
    ipady=10,
    pady=(5, 20)
)


# -----------------------------------
# Resultados
# -----------------------------------

texto_iva = tk.Label(
    tarjeta,
    text="IVA",
    font=("Arial", 10),
    bg="#1f2937",
    fg="#9ca3af"
)

texto_iva.pack(anchor="w")


resultado_iva = tk.Label(
    tarjeta,
    text="0.00 €",
    font=("Arial", 20, "bold"),
    bg="#1f2937",
    fg="#60a5fa"
)

resultado_iva.pack(anchor="e")


separador = tk.Frame(
    tarjeta,
    bg="#374151",
    height=1
)

separador.pack(
    fill="x",
    pady=15
)


texto_total = tk.Label(
    tarjeta,
    text="TOTAL CON IVA",
    font=("Arial", 10, "bold"),
    bg="#1f2937",
    fg="#9ca3af"
)

texto_total.pack(anchor="w")


resultado_total = tk.Label(
    tarjeta,
    text="0.00 €",
    font=("Arial", 30, "bold"),
    bg="#1f2937",
    fg="#34d399"
)

resultado_total.pack(anchor="e")


# -----------------------------------
# Mensajes
# -----------------------------------

mensaje = tk.Label(
    ventana,
    text="Introduce una base imponible",
    font=("Arial", 10),
    bg="#111827",
    fg="#888888"
)

mensaje.pack(pady=18)


# -----------------------------------
# Limpiar
# -----------------------------------

boton_limpiar = tk.Button(
    ventana,
    text="Limpiar",
    command=limpiar,
    font=("Arial", 10),
    bg="#111827",
    fg="#9ca3af",
    activebackground="#111827",
    activeforeground="white",
    relief="flat",
    cursor="hand2"
)

boton_limpiar.pack()


# Permite calcular pulsando ENTER
ventana.bind("<Return>", lambda event: calculaIVA())

# Foco inicial
base.focus()

ventana.mainloop()
```
### 08-Concepto de evento
**01-Agenda tkinter.py**
```python
import tkinter as tk    # Importa la biblioteca Tkinter y le asigna el alias tk, para que podamos utilizar sus funciones de forma abreviada.

ventana = tk.Tk()       # Crea la ventana principal de nuestra aplicación.

ventana.mainloop()      # Inicia el bucle de eventos de Tkinter. Gracias a él, la ventana permanece abierta y puede responder a acciones como hacer clic, escribir o cerrarla.
```
**02-Entradas.py**
```python
'''
    En lugar de mostrar una ventana vacía, presenta tres campos de entrada y un botón.
'''
import tkinter as tk

ventana = tk.Tk()

nombre = tk.Entry(ventana)                            # tk.Entry() crea una caja donde el usuario puede escribir texto en una sola línea.
nombre.pack(padx=20,pady=20)

apellidos = tk.Entry(ventana)
apellidos.pack(padx=20,pady=20)

email = tk.Entry(ventana)
email.pack(padx=20,pady=20)

boton = tk.Button(ventana,text="Guardar proyecto")    # Crea un botón con el texto «Guardar proyecto».
boton.pack(padx=20,pady=20)

ventana.mainloop()
```
**03-Labels.py**
```python
'''
    Este archivo mejora la interfaz anterior utilizando Label.
'''
import tkinter as tk

ventana = tk.Tk()

tk.Label(ventana, text="Nombre del proyecto").pack()       # tk.Label() crea una etiqueta que muestra información en pantalla.
nombre = tk.Entry(ventana)
nombre.pack(padx=20, pady=20)

tk.Label(ventana, text="Descripcion").pack()
apellidos = tk.Entry(ventana)
apellidos.pack(padx=20, pady=20)

tk.Label(ventana, text="Cliente").pack()
email = tk.Entry(ventana)
email.pack(padx=20, pady=20)

boton = tk.Button(ventana, text="Guardar proyecto")
boton.pack(padx=20, pady=20)

ventana.mainloop()


'''
    una interfaz gráfica no consiste únicamente en introducir información, sino también en indicar claramente qué debe escribir el usuario en cada campo.
    Componente	Función
    Label	    Mostrar texto informativo
    Entry	    Permitir escribir texto
    Button	    Ejecutar una acción cuando se pulsa, si tiene una función asociada
    El archivo utiliza tres etiquetas: Nombre, Apellidos y Email.
'''
```
**04-Guardar.py**
```python
'''
    Este es el archivo introduce una función que permite guardar la información de los proyectos.
'''
import tkinter as tk

ventana = tk.Tk()

def guardar():                                                            # Definimos función guardar
    archivo = open("proyectos.csv",'a')                                   # Abrir el archivo en modo append
    texto = nombre.get()+","+apellidos.get()+","+email.get()+"\n"         # Recuperar lo que ha escrito el usuario
    archivo.write(texto)
    archivo.close()                                                       # Cerrar el archivo

tk.Label(ventana, text="Nombre del proyecto").pack()
nombre = tk.Entry(ventana)
nombre.pack(padx=20, pady=20)

tk.Label(ventana, text="Descripcion").pack()
apellidos = tk.Entry(ventana)
apellidos.pack(padx=20, pady=20)

tk.Label(ventana, text="Cliente").pack()
email = tk.Entry(ventana)
email.pack(padx=20, pady=20)

boton = tk.Button(ventana, text="Guardar proyecto",command=guardar)
boton.pack(padx=20, pady=20)

ventana.mainloop()
```
**05-Area de texto.py**
```python
import tkinter as tk

ventana = tk.Tk()

area = tk.Text(ventana)           # Text crea un espacio para escribir textos de varias líneas.
area.pack(padx=20,pady=20)

ventana.mainloop()


'''
    La diferencia fundamental entre Entry y Text es que Entry está pensado para datos cortos de una sola línea, mientras que Text permite introducir párrafos enteros.
'''
```
**06-Escribir dentro del area.py**
```python
import tkinter as tk

ventana = tk.Tk()

area = tk.Text(ventana)
area.pack(padx=20,pady=20)

area.insert("1.0", "Hola que tal")   # .insert()  Se utiliza para introducir texto en una posición concreta
                                     # "1.0"  En un componente Text, las posiciones pueden expresarse como línea.columna. Las líneas empiezan en 1 y las columnas en 0.
ventana.mainloop()


'''
    Estos seis archivos introducen varias instrucciones que aparecen continuamente en aplicaciones desarrolladas con Tkinter.
    Instrucción	    ¿Para qué sirve?
    tk.Tk()	        Crear la ventana principal
    tk.Label()	    Mostrar etiquetas
    tk.Entry()	    Crear entradas de una línea
    tk.Button()	    Crear botones
    tk.Text()	    Crear áreas de texto multilínea
    .pack()	        Colocar elementos en la ventana
    .get()	        Leer el contenido de un Entry
    .insert()	    Insertar contenido en una posición
    command=	    Asociar una función a un botón
    open()	        Abrir o crear un archivo
    .write()	    Escribir en un archivo
    .close()	    Cerrar el archivo
    .mainloop()	    Mantener activa la interfaz gráfica
'''
```
### 09-Creación de controladores de eventos
**01-Grid.py**
```python
'''
    objetivo es enseñarte a crear una ventana y colocar elementos utilizando el sistema de cuadrícula de Tkinter.
'''
import tkinter as tk                                       # Importa la biblioteca tkinter, que permite crear interfaces gráficas con Python.

ventana = tk.Tk()                                          # Crea la ventana principal de la aplicación.

tk.Label(ventana, text="Insertar").grid(row=0,column=0)    # Esta línea hace dos cosas: crea una etiqueta y la coloca dentro de la ventana.

tk.Label(ventana, text="Leer").grid(row=0,column=1)        # Hace exactamente lo mismo que la línea anterior, pero con dos diferencias: - El texto será "Leer". - Se coloca en la columna 1.

ventana.mainloop()                                         # Inicia el bucle principal de eventos de la aplicación.
```
**02-Panel.py**
```python
'''
    Este archivo añade un concepto muy importante: los contenedores Frame.
    En lugar de colocar todos los elementos directamente sobre la ventana, podemos organizarla en diferentes secciones.
'''
import tkinter as tk

ventana = tk.Tk()

insertar = tk.Frame(ventana)       # Crea un contenedor llamado insertar. Un Frame es una zona de la interfaz que permite agrupar elementos gráficos.
insertar.grid(row=0,column=0)      # Coloca el panel insertar en la primera fila y primera columna de la ventana.
leer = tk.Frame(ventana)           # Crea un segundo contenedor llamado leer.
leer.grid(row=0,column=1)          # Coloca el panel leer en la primera fila y segunda columna.

tk.Label(insertar,text="Insertar").pack(padx=20,pady=20)    # Crea una etiqueta dentro del panel insertar.
tk.Label(leer,text="Leer").pack(padx=20,pady=20)            # Crea una etiqueta con el texto "Leer" dentro del segundo panel

ventana.mainloop()                                          # Inicia el bucle principal de eventos, manteniendo la ventana abierta y respondiendo a las interacciones.
```
**03-Controles.py**
```python
'''
    Ahora no solamente tenemos dos paneles, sino que incorporamos un formulario en el que el usuario puede escribir información.
'''
import tkinter as tk                                        # Importa Tkinter.

ventana = tk.Tk()                                           # Crea la ventana principal.

insertar = tk.Frame(ventana)                                # Crea el panel izquierdo.
insertar.grid(row=0,column=0)                               # Lo coloca en la columna 0.
leer = tk.Frame(ventana)                                    # Crea el panel derecho.
leer.grid(row=0,column=1)                                   # Lo coloca en la columna 1.

tk.Label(insertar,text="Insertar").pack(padx=20,pady=20)    # Crea el título "Insertar" dentro del panel izquierdo, con un espacio exterior de 20 píxeles alrededor.

tk.Label(insertar, text="Nombre").pack()                    # Crea una etiqueta con el texto "Nombre".
nombre = tk.Entry(insertar)                                 # Entry es un cuadro de texto de una sola línea.   # Permite al usuario escribir un nombre, un apellido, un correo electrónico u otro valor.
nombre.pack(padx=20, pady=20)                               

tk.Label(insertar, text="Apellidos").pack()
apellidos = tk.Entry(insertar)
apellidos.pack(padx=20, pady=20)

tk.Label(insertar, text="Email").pack()
email = tk.Entry(insertar)
email.pack(padx=20, pady=20)

boton = tk.Button(insertar, text="Guardar contacto")
boton.pack(padx=20, pady=20)

tk.Label(leer,text="Leer").pack(padx=20,pady=20)

area = tk.Text(leer)
area.pack(padx=20,pady=20)

ventana.mainloop()
```
**04-Escribir.py**
```python
'''
    Este archivo introduce las funciones y la escritura de archivos.
    Ahora el botón "Guardar contacto" sí realizará una acción.
'''
import tkinter as tk

def guardar():                                                        # Define una función llamada guardar
    archivo = open("agenda.csv",'a')                                  # Abre un archivo llamado agenda.csv en modo añadir.
    texto = nombre.get()+","+apellidos.get()+","+email.get()+"\n"
    archivo.write(texto)
    archivo.close()

ventana = tk.Tk()

insertar = tk.Frame(ventana)
insertar.grid(row=0,column=0)
leer = tk.Frame(ventana)
leer.grid(row=0,column=1)

tk.Label(insertar,text="Insertar").pack(padx=20,pady=20)

tk.Label(insertar, text="Nombre").pack()
nombre = tk.Entry(insertar)
nombre.pack(padx=20, pady=20)

tk.Label(insertar, text="Apellidos").pack()
apellidos = tk.Entry(insertar)
apellidos.pack(padx=20, pady=20)

tk.Label(insertar, text="Email").pack()
email = tk.Entry(insertar)
email.pack(padx=20, pady=20)

boton = tk.Button(insertar, text="Guardar contacto",command=guardar)
boton.pack(padx=20, pady=20)

tk.Label(leer,text="Leer").pack(padx=20,pady=20)

area = tk.Text(leer)
area.pack(padx=20,pady=20)

ventana.mainloop()
```
**05-IA.py**
```python
import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

ARCHIVO = "agenda.csv"


class AgendaApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Agenda de contactos")
        self.ventana.geometry("950x600")
        self.ventana.minsize(850, 520)

        self.contacto_seleccionado = None

        # -----------------------------
        # ESTILOS
        # -----------------------------
        estilo = ttk.Style()

        try:
            estilo.theme_use("clam")
        except tk.TclError:
            pass

        estilo.configure(
            "TFrame",
            background="#f4f6f8"
        )

        estilo.configure(
            "Card.TFrame",
            background="white"
        )

        estilo.configure(
            "Titulo.TLabel",
            font=("Segoe UI", 22, "bold"),
            background="#f4f6f8",
            foreground="#202124"
        )

        estilo.configure(
            "Subtitulo.TLabel",
            font=("Segoe UI", 11),
            background="#f4f6f8",
            foreground="#6b7280"
        )

        estilo.configure(
            "CardTitle.TLabel",
            font=("Segoe UI", 14, "bold"),
            background="white",
            foreground="#202124"
        )

        estilo.configure(
            "Campo.TLabel",
            font=("Segoe UI", 10),
            background="white",
            foreground="#374151"
        )

        estilo.configure(
            "TEntry",
            padding=8,
            font=("Segoe UI", 10)
        )

        estilo.configure(
            "Guardar.TButton",
            font=("Segoe UI", 10, "bold"),
            padding=(15, 10)
        )

        estilo.configure(
            "Accion.TButton",
            font=("Segoe UI", 10),
            padding=(12, 8)
        )

        estilo.configure(
            "Treeview",
            font=("Segoe UI", 10),
            rowheight=35,
            background="white",
            fieldbackground="white"
        )

        estilo.configure(
            "Treeview.Heading",
            font=("Segoe UI", 10, "bold"),
            padding=8
        )

        estilo.map(
            "Treeview",
            background=[("selected", "#dbeafe")],
            foreground=[("selected", "#1e3a8a")]
        )

        # -----------------------------
        # CONTENEDOR PRINCIPAL
        # -----------------------------
        principal = ttk.Frame(ventana, padding=25)
        principal.pack(fill="both", expand=True)

        principal.columnconfigure(1, weight=1)
        principal.rowconfigure(1, weight=1)

        # -----------------------------
        # ENCABEZADO
        # -----------------------------
        encabezado = ttk.Frame(principal)
        encabezado.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew",
            pady=(0, 20)
        )

        ttk.Label(
            encabezado,
            text="Agenda de contactos",
            style="Titulo.TLabel"
        ).pack(anchor="w")

        ttk.Label(
            encabezado,
            text="Administra tus contactos de forma rápida y sencilla",
            style="Subtitulo.TLabel"
        ).pack(anchor="w", pady=(3, 0))

        # -----------------------------
        # PANEL IZQUIERDO
        # -----------------------------
        formulario = ttk.Frame(
            principal,
            padding=20,
            style="Card.TFrame"
        )

        formulario.grid(
            row=1,
            column=0,
            sticky="ns",
            padx=(0, 20)
        )

        ttk.Label(
            formulario,
            text="Nuevo contacto",
            style="CardTitle.TLabel"
        ).pack(anchor="w", pady=(0, 20))

        # Nombre
        ttk.Label(
            formulario,
            text="Nombre",
            style="Campo.TLabel"
        ).pack(anchor="w")

        self.nombre = ttk.Entry(formulario, width=32)
        self.nombre.pack(fill="x", pady=(5, 15))

        # Apellidos
        ttk.Label(
            formulario,
            text="Apellidos",
            style="Campo.TLabel"
        ).pack(anchor="w")

        self.apellidos = ttk.Entry(formulario)
        self.apellidos.pack(fill="x", pady=(5, 15))

        # Email
        ttk.Label(
            formulario,
            text="Email",
            style="Campo.TLabel"
        ).pack(anchor="w")

        self.email = ttk.Entry(formulario)
        self.email.pack(fill="x", pady=(5, 20))

        self.boton_guardar = ttk.Button(
            formulario,
            text="Guardar contacto",
            style="Guardar.TButton",
            command=self.guardar
        )

        self.boton_guardar.pack(fill="x")

        ttk.Button(
            formulario,
            text="Limpiar formulario",
            style="Accion.TButton",
            command=self.limpiar_formulario
        ).pack(fill="x", pady=(10, 0))

        # -----------------------------
        # PANEL DERECHO
        # -----------------------------
        panel_contactos = ttk.Frame(
            principal,
            padding=20,
            style="Card.TFrame"
        )

        panel_contactos.grid(
            row=1,
            column=1,
            sticky="nsew"
        )

        panel_contactos.columnconfigure(0, weight=1)
        panel_contactos.rowconfigure(2, weight=1)

        # Título
        ttk.Label(
            panel_contactos,
            text="Mis contactos",
            style="CardTitle.TLabel"
        ).grid(row=0, column=0, sticky="w")

        # -----------------------------
        # BUSCADOR
        # -----------------------------
        zona_busqueda = ttk.Frame(
            panel_contactos,
            style="Card.TFrame"
        )

        zona_busqueda.grid(
            row=1,
            column=0,
            sticky="ew",
            pady=(15, 15)
        )

        zona_busqueda.columnconfigure(0, weight=1)

        self.busqueda = ttk.Entry(zona_busqueda)
        self.busqueda.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=(0, 10)
        )

        self.busqueda.insert(0, "Buscar contacto...")

        self.busqueda.bind(
            "<FocusIn>",
            self.quitar_placeholder
        )

        self.busqueda.bind(
            "<KeyRelease>",
            self.buscar
        )

        ttk.Button(
            zona_busqueda,
            text="Actualizar",
            command=self.cargar_contactos
        ).grid(row=0, column=1)

        # -----------------------------
        # TABLA
        # -----------------------------
        tabla_frame = ttk.Frame(
            panel_contactos,
            style="Card.TFrame"
        )

        tabla_frame.grid(
            row=2,
            column=0,
            sticky="nsew"
        )

        tabla_frame.rowconfigure(0, weight=1)
        tabla_frame.columnconfigure(0, weight=1)

        columnas = ("nombre", "apellidos", "email")

        self.tabla = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings"
        )

        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("apellidos", text="Apellidos")
        self.tabla.heading("email", text="Email")

        self.tabla.column("nombre", width=140)
        self.tabla.column("apellidos", width=180)
        self.tabla.column("email", width=240)

        self.tabla.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        scrollbar = ttk.Scrollbar(
            tabla_frame,
            orient="vertical",
            command=self.tabla.yview
        )

        scrollbar.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        self.tabla.configure(
            yscrollcommand=scrollbar.set
        )

        self.tabla.bind(
            "<<TreeviewSelect>>",
            self.seleccionar_contacto
        )

        # -----------------------------
        # BOTONES DE ACCIONES
        # -----------------------------
        acciones = ttk.Frame(
            panel_contactos,
            style="Card.TFrame"
        )

        acciones.grid(
            row=3,
            column=0,
            sticky="ew",
            pady=(15, 0)
        )

        ttk.Button(
            acciones,
            text="Editar",
            style="Accion.TButton",
            command=self.preparar_edicion
        ).pack(side="left")

        ttk.Button(
            acciones,
            text="Eliminar",
            style="Accion.TButton",
            command=self.eliminar
        ).pack(side="left", padx=(10, 0))

        # -----------------------------
        # BARRA INFERIOR
        # -----------------------------
        self.estado = ttk.Label(
            principal,
            text="",
            style="Subtitulo.TLabel"
        )

        self.estado.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="w",
            pady=(15, 0)
        )

        # Enter guarda
        self.email.bind(
            "<Return>",
            lambda event: self.guardar()
        )

        self.cargar_contactos()
        self.nombre.focus()


    # ==================================================
    # FUNCIONES
    # ==================================================

    def guardar(self):
        nombre = self.nombre.get().strip()
        apellidos = self.apellidos.get().strip()
        email = self.email.get().strip()

        # Validación
        if not nombre:
            messagebox.showwarning(
                "Datos incompletos",
                "Introduce el nombre del contacto."
            )
            self.nombre.focus()
            return

        if not apellidos:
            messagebox.showwarning(
                "Datos incompletos",
                "Introduce los apellidos."
            )
            self.apellidos.focus()
            return

        if not self.email_valido(email):
            messagebox.showwarning(
                "Email incorrecto",
                "Introduce una dirección de email válida."
            )
            self.email.focus()
            return

        # Si estamos editando
        if self.contacto_seleccionado is not None:
            self.guardar_edicion(
                nombre,
                apellidos,
                email
            )
            return

        # Comprobar duplicados
        if self.email_existe(email):
            messagebox.showwarning(
                "Contacto existente",
                "Ya existe un contacto con ese email."
            )
            return

        # Guardar usando módulo csv
        with open(
            ARCHIVO,
            "a",
            newline="",
            encoding="utf-8"
        ) as archivo:

            escritor = csv.writer(archivo)

            escritor.writerow(
                [nombre, apellidos, email]
            )

        self.estado.config(
            text=f"✓ Contacto '{nombre}' guardado correctamente"
        )

        self.limpiar_formulario()
        self.cargar_contactos()


    def cargar_contactos(self):
        self.limpiar_tabla()

        if not os.path.exists(ARCHIVO):
            self.estado.config(
                text="Todavía no hay contactos guardados."
            )
            return

        contactos = self.obtener_contactos()

        for indice, contacto in enumerate(contactos):
            if len(contacto) >= 3:
                self.tabla.insert(
                    "",
                    "end",
                    iid=str(indice),
                    values=(
                        contacto[0],
                        contacto[1],
                        contacto[2]
                    )
                )

        cantidad = len(contactos)

        if cantidad == 1:
            texto = "1 contacto"
        else:
            texto = f"{cantidad} contactos"

        self.estado.config(
            text=f"{texto} guardados"
        )


    def obtener_contactos(self):
        contactos = []

        if not os.path.exists(ARCHIVO):
            return contactos

        with open(
            ARCHIVO,
            "r",
            newline="",
            encoding="utf-8"
        ) as archivo:

            lector = csv.reader(archivo)

            for fila in lector:
                if len(fila) >= 3:
                    contactos.append(fila)

        return contactos


    def seleccionar_contacto(self, event=None):
        seleccion = self.tabla.selection()

        if not seleccion:
            return

        valores = self.tabla.item(
            seleccion[0],
            "values"
        )

        self.contacto_seleccionado = {
            "indice": int(seleccion[0]),
            "datos": valores
        }


    def preparar_edicion(self):
        seleccion = self.tabla.selection()

        if not seleccion:
            messagebox.showinfo(
                "Editar contacto",
                "Selecciona primero un contacto."
            )
            return

        item = seleccion[0]

        valores = self.tabla.item(
            item,
            "values"
        )

        self.nombre.delete(0, tk.END)
        self.apellidos.delete(0, tk.END)
        self.email.delete(0, tk.END)

        self.nombre.insert(0, valores[0])
        self.apellidos.insert(0, valores[1])
        self.email.insert(0, valores[2])

        self.contacto_seleccionado = {
            "indice": int(item),
            "datos": valores
        }

        self.boton_guardar.config(
            text="Guardar cambios"
        )

        self.nombre.focus()


    def guardar_edicion(
        self,
        nombre,
        apellidos,
        email
    ):
        contactos = self.obtener_contactos()

        indice = self.contacto_seleccionado["indice"]

        if indice >= len(contactos):
            return

        # Evitar emails duplicados
        for i, contacto in enumerate(contactos):

            if i != indice:
                if contacto[2].lower() == email.lower():

                    messagebox.showwarning(
                        "Email duplicado",
                        "Otro contacto ya utiliza ese email."
                    )
                    return

        contactos[indice] = [
            nombre,
            apellidos,
            email
        ]

        self.guardar_todos(contactos)

        self.estado.config(
            text=f"✓ Contacto '{nombre}' actualizado"
        )

        self.limpiar_formulario()
        self.cargar_contactos()


    def eliminar(self):
        seleccion = self.tabla.selection()

        if not seleccion:
            messagebox.showinfo(
                "Eliminar contacto",
                "Selecciona primero un contacto."
            )
            return

        item = seleccion[0]

        valores = self.tabla.item(
            item,
            "values"
        )

        confirmar = messagebox.askyesno(
            "Eliminar contacto",
            f"¿Seguro que quieres eliminar a "
            f"{valores[0]} {valores[1]}?"
        )

        if not confirmar:
            return

        contactos = self.obtener_contactos()

        indice = int(item)

        if indice < len(contactos):
            contactos.pop(indice)

        self.guardar_todos(contactos)

        self.limpiar_formulario()
        self.cargar_contactos()

        self.estado.config(
            text="✓ Contacto eliminado"
        )


    def guardar_todos(self, contactos):
        with open(
            ARCHIVO,
            "w",
            newline="",
            encoding="utf-8"
        ) as archivo:

            escritor = csv.writer(archivo)
            escritor.writerows(contactos)


    def buscar(self, event=None):
        texto = self.busqueda.get().strip().lower()

        if texto == "buscar contacto...":
            return

        self.limpiar_tabla()

        contactos = self.obtener_contactos()

        contador = 0

        for indice, contacto in enumerate(contactos):

            contenido = " ".join(contacto).lower()

            if texto in contenido:

                self.tabla.insert(
                    "",
                    "end",
                    iid=str(indice),
                    values=(
                        contacto[0],
                        contacto[1],
                        contacto[2]
                    )
                )

                contador += 1

        self.estado.config(
            text=f"{contador} resultados encontrados"
        )


    def quitar_placeholder(self, event=None):
        if self.busqueda.get() == "Buscar contacto...":
            self.busqueda.delete(0, tk.END)


    def limpiar_tabla(self):
        for elemento in self.tabla.get_children():
            self.tabla.delete(elemento)


    def limpiar_formulario(self):
        self.nombre.delete(0, tk.END)
        self.apellidos.delete(0, tk.END)
        self.email.delete(0, tk.END)

        self.contacto_seleccionado = None

        self.boton_guardar.config(
            text="Guardar contacto"
        )

        self.nombre.focus()


    def email_valido(self, email):
        return (
            "@" in email
            and "." in email.split("@")[-1]
            and " " not in email
        )


    def email_existe(self, email):
        for contacto in self.obtener_contactos():

            if contacto[2].lower() == email.lower():
                return True

        return False


# -----------------------------
# INICIAR APLICACIÓN
# -----------------------------
if __name__ == "__main__":

    ventana = tk.Tk()

    app = AgendaApp(ventana)

    ventana.mainloop()
```
## 2-Proyecto
### final
**01-mantenimiento.py**
```python
import tkinter as tk

ventana = tk.Tk()
ventana.title("Mantenimiento de mi coche")

titulo = tk.Label(
    ventana,
    text="Registro de mantenimiento",
    font=("Arial", 18)
)
titulo.pack(padx=20, pady=20)

ventana.mainloop()
```
**02-Entradas.py**
```python
import tkinter as tk

ventana = tk.Tk()
ventana.title("Mantenimiento de mi coche")

titulo = tk.Label(
    ventana,
    text="Registro de mantenimiento",
    font=("Arial", 18)
)
titulo.pack(padx=20, pady=20)

tk.Label(ventana, text="Fecha").pack()
fecha = tk.Entry(ventana)
fecha.pack(padx=20, pady=5)

tk.Label(ventana, text="Kilometraje").pack()
kilometraje = tk.Entry(ventana)
kilometraje.pack(padx=20, pady=5)

tk.Label(ventana, text="Detalle del mantenimiento").pack()
detalle = tk.Entry(ventana)
detalle.pack(padx=20, pady=5)

tk.Label(ventana, text="Coste").pack()
coste = tk.Entry(ventana)
coste.pack(padx=20, pady=5)

ventana.mainloop()

```
**03-Boton guardar.py**
```python
import tkinter as tk

def guardar():
    archivo = open("mantenimiento.csv", "a")
    texto = fecha.get() + "|" + kilometraje.get() + "|" + detalle.get() + "|" + coste.get() + "\n"
    archivo.write(texto)
    archivo.close()

    resultado.config(text="Mantenimiento guardado")

ventana = tk.Tk()
ventana.title("Mantenimiento de mi coche")

titulo = tk.Label(
    ventana,
    text="Registro de mantenimiento",
    font=("Arial", 18)
)
titulo.pack(padx=20, pady=20)

tk.Label(ventana, text="Fecha").pack()
fecha = tk.Entry(ventana)
fecha.pack(padx=20, pady=5)

tk.Label(ventana, text="Kilometraje").pack()
kilometraje = tk.Entry(ventana)
kilometraje.pack(padx=20, pady=5)

tk.Label(ventana, text="Detalle del mantenimiento").pack()
detalle = tk.Entry(ventana)
detalle.pack(padx=20, pady=5)

tk.Label(ventana, text="Coste").pack()
coste = tk.Entry(ventana)
coste.pack(padx=20, pady=5)

# Boton guardar
boton_guardar = tk.Button(
    ventana,
    text="Guardar mantenimiento",
    command=guardar
)
boton_guardar.pack(padx=20, pady=10)

resultado = tk.Label(ventana, text="")
resultado.pack(padx=20, pady=5)

ventana.mainloop()

```
**04-Listar.py**
```python
import tkinter as tk

def guardar():
    archivo = open("mantenimiento.csv", "a")
    texto = fecha.get() + "|" + kilometraje.get() + "|" + detalle.get() + "|" + coste.get() + "\n"
    archivo.write(texto)
    archivo.close()

    resultado.config(text="Mantenimiento guardado")
    
def listar():
    archivo = open("mantenimiento.csv", "r")
    lineas = archivo.readlines()
    archivo.close()

    area.delete("1.0", tk.END)

    for linea in lineas:
        datos = linea.strip().split("|")

        area.insert(tk.END, "Fecha: " + datos[0] + "\n")
        area.insert(tk.END, "Kilometraje: " + datos[1] + "\n")
        area.insert(tk.END, "Detalle: " + datos[2] + "\n")
        area.insert(tk.END, "Coste: " + datos[3] + "\n")
        area.insert(tk.END, "------------------------------\n")

ventana = tk.Tk()
ventana.title("Mantenimiento de mi coche")

titulo = tk.Label(
    ventana,
    text="Registro de mantenimiento",
    font=("Arial", 18)
)
titulo.pack(padx=20, pady=20)

tk.Label(ventana, text="Fecha").pack()
fecha = tk.Entry(ventana)
fecha.pack(padx=20, pady=5)

tk.Label(ventana, text="Kilometraje").pack()
kilometraje = tk.Entry(ventana)
kilometraje.pack(padx=20, pady=5)

tk.Label(ventana, text="Detalle del mantenimiento").pack()
detalle = tk.Entry(ventana)
detalle.pack(padx=20, pady=5)

tk.Label(ventana, text="Coste").pack()
coste = tk.Entry(ventana)
coste.pack(padx=20, pady=5)

# Boton guardar
boton_guardar = tk.Button(
    ventana,
    text="Guardar mantenimiento",
    command=guardar
)
boton_guardar.pack(padx=20, pady=10)

resultado = tk.Label(ventana, text="")
resultado.pack(padx=20, pady=5)

boton_listar = tk.Button(
    ventana,
    text="Listar mantenimientos",                 # Pulsa Listar dos veces: el contenido no debe duplicarse, porque primero vaciamos el area.
    command=listar
)
boton_listar.pack(padx=20, pady=10)

area = tk.Text(ventana, width=55, height=12)
area.pack(padx=20, pady=10)

ventana.mainloop()

```
**05-Programa completo.py**
```python
'''
    Programa para documentación y registro detallado del mantenimiento del coche.
    Permite introducir fecha, kilometraje, detalle y coste, guardar cada mantenimiento en un CSV y consultar los registros desde una ventana.
'''
print("-"*45)
print("Programa para documentación y registro")
print("del mantenimiento de tu coche")
print("Desarrollado por nurLukas de Sturmprojekt")
print("Poder en cada proyecto!")
print("-"*45)

import tkinter as tk

archivo = open("mantenimiento.csv", "a")
archivo.close()

def guardar():
    archivo = open("mantenimiento.csv", "a")
    texto = fecha.get() + "|" + kilometraje.get() + "|" + detalle.get() + "|" + coste.get() + "\n"
    archivo.write(texto)
    archivo.close()

    resultado.config(text="Mantenimiento guardado")
    
def listar():
    archivo = open("mantenimiento.csv", "r")
    lineas = archivo.readlines()
    archivo.close()

    area.delete("1.0", tk.END)

    for linea in lineas:
        datos = linea.strip().split("|")

        area.insert(tk.END, "Fecha: " + datos[0] + "\n")
        area.insert(tk.END, "Kilometraje: " + datos[1] + "\n")
        area.insert(tk.END, "Detalle: " + datos[2] + "\n")
        area.insert(tk.END, "Coste: " + datos[3] + "\n")
        area.insert(tk.END, "------------------------------\n")

ventana = tk.Tk()
ventana.title("Mantenimiento de mi coche")

formulario = tk.Frame(ventana)
formulario.grid(row=0, column=0, padx=20, pady=20)

listado = tk.Frame(ventana)
listado.grid(row=0, column=1, padx=20, pady=20)

titulo = tk.Label(
    formulario,
    text="Registro de mantenimiento",
    font=("Arial", 18)
)
titulo.pack(padx=20, pady=20)

tk.Label(formulario, text="Fecha").pack()
fecha = tk.Entry(formulario)
fecha.pack(padx=20, pady=5)

tk.Label(formulario, text="Kilometraje").pack()
kilometraje = tk.Entry(formulario)
kilometraje.pack(padx=20, pady=5)

tk.Label(formulario, text="Detalle del mantenimiento").pack()
detalle = tk.Entry(formulario)
detalle.pack(padx=20, pady=5)

tk.Label(formulario, text="Coste").pack()
coste = tk.Entry(formulario)
coste.pack(padx=20, pady=5)

boton_guardar = tk.Button(
    formulario,
    text="Guardar mantenimiento",
    command=guardar
)
boton_guardar.pack(padx=20, pady=10)

resultado = tk.Label(formulario, text="")
resultado.pack(padx=20, pady=5)

boton_listar = tk.Button(
    listado,
    text="Listar mantenimientos",
    command=listar
)
boton_listar.pack(padx=20, pady=10)

area = tk.Text(listado, width=55, height=12)
area.pack(padx=20, pady=10)

ventana.mainloop()
```
### sub1
**01-Escribir.py**
```python
'''
    Programa para documentación y registro detallado del mantenimiento del coche.
'''
print("-"*45)
print("Programa para documentación y registro")
print("del mantenimiento de tu coche")
print("Desarrollado por nurLukas de Sturmprojekt")
print("Poder en cada proyecto!")
print("-"*45)

archivo = open("mantenimiento.txt", "w")      # Abre mantenimiento.txt. El modo "w" lo crea si no existe; si existe, borra su contenido. 
archivo.write("Cambio de aceite.")             # Escribe el texto.
archivo.close()                                 # Cierra el archivo.

# Archivo es la variable que utilizamos para trabajar con el fichero abierto.
```
**02-Leer.py**
```python
'''
    Programa para documentación y registro detallado del mantenimiento del coche.
'''
print("-"*45)
print("Programa para documentación y registro")
print("del mantenimiento de tu coche")
print("Desarrollado por nurLukas de Sturmprojekt")
print("Poder en cada proyecto!")
print("-"*45)

archivo = open("mantenimiento.txt", "r")   # "r" abre el archivo para leerlo, sin modificarlo.
lineas = archivo.readlines()               # readlines() lee sus líneas y las devuelve en una lista. --> ['Cambio de aceite'], # lineas guarda esa lista.
print(lineas)                              # La muestra en la terminal.
archivo.close()                              # Cerramos el archivo.
```
**03-Anadir.py**
```python
'''
    Programa para documentación y registro detallado del mantenimiento del coche.
'''
print("-"*45)
print("Programa para documentación y registro")
print("del mantenimiento de tu coche")
print("Desarrollado por nurLukas de Sturmprojekt")
print("Poder en cada proyecto!")
print("-"*45)

detalle = input("Introduce el mantenimiento realizado: ")   # input() pide un texto y lo guarda en detalle.

archivo = open("mantenimiento.txt", "a")                    # "a" añade al final del archivo sin borrar lo anterior.
archivo.write(detalle + "\n")                               # "\n" escribe un salto de línea para separar los mantenimientos.
archivo.close()                                               # Cerramos el archivo.
```
**04-Listar.py**
```python
'''
    Programa para documentación y registro detallado del mantenimiento del coche.
'''
print("-"*45)
print("Programa para documentación y registro")
print("del mantenimiento de tu coche")
print("Desarrollado por nurLukas de Sturmprojekt")
print("Poder en cada proyecto!")
print("-"*45)

print("-"*45)
print("Mantenimientos realizados:")
archivo = open("mantenimiento.txt", "r")
lineas = archivo.readlines()  # Lee todas las líneas restantes del archivo y las guarda en una lista llamada lineas.

for linea in lineas:          # Recorre la lista, tomando una línea en cada repetición.
    print(linea.strip())      # Quita los espacios y saltos de línea de los extremos. Así evitamos líneas vacías entre los mantenimientos al imprimir.
    
archivo.close()

```
**05-Menu.py**
```python
'''
    Programa para documentación y registro detallado del mantenimiento del coche.
'''
print("-"*45)
print("Programa para documentación y registro")
print("del mantenimiento de tu coche")
print("Desarrollado por nurLukas de Sturmprojekt")
print("Poder en cada proyecto!")
print("-"*45)

print("Registro de mantenimientos realizados")

while True:
    print("-"*45)
    print("1.- Agregar mantenimiento realizado")
    print("2.- Listar mantenimientos")
    print("0.- Salir del programa")
    print("-"*45)
    
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        detalle = input("Introduce el mantenimiento realizado: ")
        archivo = open("mantenimiento.txt", "a")
        archivo.write("- " + detalle + "\n")
        archivo.close()
    
    elif opcion == "2":
        print("Mantenimientos realizados:")
        archivo = open("mantenimiento.txt", "r")
        lineas = archivo.readlines()
        
        for linea in lineas:
            print(linea.strip())
        archivo.close()
    
    elif opcion == "0": 
        print("Esta saliendo del programa, adios")
        break
    else:
        print("Opción incorrecta")
```
### sub2
**06-Registros.py**
```python
'''
    ( El contenido de este programa, corresponde a la subunidad 02: "ficheros de datos y registros". 
    Primero guardaremos un mantenimiento con sus cuatro campos. Después aprenderemos a separarlos al leer.
    Programa para documentación y registro detallado del mantenimiento del coche.
'''
print("-"*45)
print("Programa para documentación y registro")
print("del mantenimiento de tu coche")
print("Desarrollado por nurLukas de Sturmprojekt")
print("Poder en cada proyecto!")
print("-"*45)

print("Registrar mantenimiento")
print("-"*45)

fecha = input("Fecha del mantenimiento: ")
kilometraje = input("Kilometraje del coche: ")
detalle = input("Mantenimiento realizado: ")
coste = input("Coste del mantenimiento: ")

archivo = open("mantenimiento.csv", "a")
archivo.write(fecha + "|" + kilometraje + "|" + detalle + "|" + coste + "\n")
archivo.close()

print("Mantenimientos guardados")
archivo = open("mantenimiento.csv", "r")
lineas = archivo.readlines()

for linea in lineas:
    datos = linea.strip().split("|")
    print(datos)
    
archivo.close()
```
**07-Leer registros.py**
```python
'''
    ( El contenido de este programa, corresponde a la subunidad 02: "ficheros de datos y registros". 
    Programa para documentación y registro detallado del mantenimiento del coche.
'''
print("-"*45)
print("Programa para documentación y registro")
print("del mantenimiento de tu coche")
print("Desarrollado por nurLukas de Sturmprojekt")
print("Poder en cada proyecto!")
print("-"*45)

print("Mantenimientos guardados:")
print("-"*45)

archivo = open("mantenimiento.csv", "r")
lineas = archivo.readlines()

for linea in lineas:
    datos = linea.strip().split("|")

    print("------------------------------")
    print("Fecha:", datos[0])
    print("Kilometraje:", datos[1])
    print("Detalle:", datos[2])
    print("Coste:", datos[3])

archivo.close()
```
**08-Diccionario.py**
```python
'''
    ( El contenido de este programa, corresponde a la subunidad 02: "ficheros de datos y registros". 
    Programa para documentación y registro detallado del mantenimiento del coche.
'''
print("-"*45)
print("Programa para documentación y registro")
print("del mantenimiento de tu coche")
print("Desarrollado por nurLukas de Sturmprojekt")
print("Poder en cada proyecto!")
print("-"*45)

print("Mantenimientos guardados:")
print("-"*45)

archivo = open("mantenimiento.csv", "r")
lineas = archivo.readlines()

for linea in lineas:
    datos = linea.strip().split("|")

    mantenimiento = {
        "fecha": datos[0],
        "kilometraje": datos[1],
        "detalle": datos[2],
        "coste": datos[3]
    }

    print("------------------------------")
    print("Fecha:", mantenimiento["fecha"])
    print("Kilometraje:", mantenimiento["kilometraje"])
    print("Detalle:", mantenimiento["detalle"])
    print("Coste:", mantenimiento["coste"])
    
archivo.close()


'''
    datos[0]                 # Lista: accedemos por posición
    mantenimiento["fecha"]   # Diccionario: accedemos por clave
    
    En el diccionario, cada pareja tiene una clave y un valor. Por ejemplo:
    "fecha": datos[0]
'''
```
**09-Leer JSON.py**
```python
import json

print("Datos de mi coche")

archivo = open("coche.json", "r")
coche = json.load(archivo)
archivo.close()

print("Marca:", coche["marca"])
print("Modelo:", coche["modelo"])
print("Matrícula:", coche["matricula"])

'''
    Aquí no usamos split(): json.load() interpreta la estructura del archivo por nosotros.
'''
```
**coche.json**
```json
{
    "marca": "Seat",
    "modelo": "Ibiza",
    "matricula": "1234ABC"
}
```
### sub3
**10-Guardar copia.py**
```python
'''
	Guardaremos una lista en formato binario con pickle
'''

import pickle                            # permite guardar y recuperar objetos de Python, como listas.

mantenimiento = ["2026-10-12", "125000", "Cambio de aceite", "85.50"]

archivo = open("copia.dat", "wb")       # "wb" significa escribir (w) en formato binario (b). Si el archivo existe, sobrescribe su contenido.
pickle.dump(mantenimiento, archivo)     # pickle.dump(mantenimiento, archivo) guarda la lista en el archivo.
archivo.close()

print("Copia guardada")
```
**11-Leer copia.py**
```python
import pickle

archivo = open("copia.dat", "rb")       # "rb" abre el archivo para leer (r) en formato binario (b).
mantenimiento = pickle.load(archivo)    # pickle.load(archivo) recupera el objeto guardado.  mantenimiento recibe la lista recuperada.
archivo.close()

print(mantenimiento)
```
## 3-Resultado  de aprendizaje
**RA5.md**
```markdown
# Resultado de aprendizaje 5
**Resultado de aprendizaje**
Realiza operaciones de entrada y salida de información, utilizando procedimientos específicos del lenguaje y librerías de clases.

Criterios de evaluación
a) Se ha utilizado la consola para realizar operaciones de entrada y salida de información.
He utilizado input() para introducir información y print() para mostrarla, 
ejecutando los programas desde la consola CMD de Windows 11.

b) Se han aplicado formatos en la visualización de la información.
De forma muy basica, pude aplicar etiquetas para cada campo, saltos de línea y separadores entre "mantenimientos" en mis ejercicios. 

c) Se han reconocido las posibilidades de entrada / salida del lenguaje y las librerías asociadas.
Trabaje con entrada y salida por consola, mediante archivos y a través de una interfaz gráfica. 
He utilizado las funciones input(), print() y open(), además de las librerías json para leer datos estructurados, 
pickle para guardar y recuperar objetos de Python y tkinter para crear la interfaz gráfica.

d) Se han utilizado ficheros para almacenar y recuperar información.
Utilice archivos .csv, .txt, .json, (crado manualmente), para almacenar la información de forma persistente, y tambien para recuperarla y leerla. 

e) Se han creado programas que utilicen diversos métodos de acceso al contenido de los ficheros.
Los primeros ejercicios de la unidad 5, añaden "w" y acceso binario con pickle. 
Ejercicios posteriores Utilizas lectura y añadido con "r" y "a", 

f) Se han utilizado las herramientas del entorno de desarrollo para crear interfaces gráficos de usuario simples.
He creado una interfaz escribiendo Tkinter en Notepad++, tanto en mi proyecto final de unidad como en los ejercicios.

g) Se han programado controladores de eventos.
En el programa proyecto de final de unidad, guardar() y listar() están conectados a los botones mediante "command".

h) Se han escrito programas que utilicen interfaces gráficos para la entrada y salida de información.
Introduje información con Entry y la muestras con Text y Label.
```
```
**RA5.md**
```markdown
# Resultado de aprendizaje 5
**Resultado de aprendizaje**
Realiza operaciones de entrada y salida de información, utilizando procedimientos específicos del lenguaje y librerías de clases.

Criterios de evaluación
a) Se ha utilizado la consola para realizar operaciones de entrada y salida de información.
He utilizado input() para introducir información y print() para mostrarla, 
ejecutando los programas desde la consola CMD de Windows 11.

b) Se han aplicado formatos en la visualización de la información.
De forma muy basica, pude aplicar etiquetas para cada campo, saltos de línea y separadores entre "mantenimientos" en mis ejercicios. 

c) Se han reconocido las posibilidades de entrada / salida del lenguaje y las librerías asociadas.
Trabaje con entrada y salida por consola, mediante archivos y a través de una interfaz gráfica. 
He utilizado las funciones input(), print() y open(), además de las librerías json para leer datos estructurados, 
pickle para guardar y recuperar objetos de Python y tkinter para crear la interfaz gráfica.

d) Se han utilizado ficheros para almacenar y recuperar información.
Utilice archivos .csv, .txt, .json, (crado manualmente), para almacenar la información de forma persistente, y tambien para recuperarla y leerla. 

e) Se han creado programas que utilicen diversos métodos de acceso al contenido de los ficheros.
Los primeros ejercicios de la unidad 5, añaden "w" y acceso binario con pickle. 
Ejercicios posteriores Utilizas lectura y añadido con "r" y "a", 

f) Se han utilizado las herramientas del entorno de desarrollo para crear interfaces gráficos de usuario simples.
He creado una interfaz escribiendo Tkinter en Notepad++, tanto en mi proyecto final de unidad como en los ejercicios.

g) Se han programado controladores de eventos.
En el programa proyecto de final de unidad, guardar() y listar() están conectados a los botones mediante "command".

h) Se han escrito programas que utilicen interfaces gráficos para la entrada y salida de información.
Introduje información con Entry y la muestras con Text y Label.
```
