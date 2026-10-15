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