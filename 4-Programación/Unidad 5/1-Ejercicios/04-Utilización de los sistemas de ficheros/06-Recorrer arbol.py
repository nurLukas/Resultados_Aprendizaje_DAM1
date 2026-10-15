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