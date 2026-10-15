'''
    split() significa dividir o separar un texto.
'''
archivo = open('proyectos.csv','r')    # Abre el archivo proyectos.csv en modo lectura ('r')
lineas = archivo.readlines()           # Lee todas las líneas del archivo y las guarda en una lista llamada lineas
for linea in lineas:                   # Recorre una por una todas las líneas guardadas en la lista
	partido = linea.split("|")         # Divide la línea cada vez que encuentra el símbolo |   # El resultado se guarda en una lista llamada partido
	print(partido)                     # # Muestra en pantalla la lista resultante