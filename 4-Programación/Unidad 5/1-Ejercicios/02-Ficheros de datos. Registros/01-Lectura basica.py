archivo = open('proyectos.csv','r')   # Aquí se abre el archivo proyectos.csv en modo lectura
lineas = archivo.readlines()          # se pretende leer todas las líneas del archivo y guardarlas en una lista llamada lineas
for linea in lineas:                  # Esto recorre la lista lineas          
    print(lineas)