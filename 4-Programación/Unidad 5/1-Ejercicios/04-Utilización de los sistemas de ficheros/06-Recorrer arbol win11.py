
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
