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