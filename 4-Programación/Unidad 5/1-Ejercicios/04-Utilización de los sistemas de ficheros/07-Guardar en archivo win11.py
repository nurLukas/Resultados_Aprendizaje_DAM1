
import os

ruta = r"D:\2627_DAM1\4-Programación\05-Lectura y escritura de información\04-Utilización de los sistemas de ficheros"

with open("arbol.txt", "w") as salida:

    for carpeta, carpetas, archivos in os.walk(ruta):
        salida.write(carpeta + "\n")

        for archivo in archivos:
            salida.write("  - " + archivo + "\n")

print("Tree saved to arbol.txt")
