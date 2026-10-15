'''
    Este programa crea un archivo llamado archivo.txt.
'''
archivo = open("archivo.txt",'w') # open() abre un archivo., "archivo.txt" indica el archivo que queremos utilizar, 'w' indica que queremos abrirlo en modo escritura (write).
archivo.close()                   # Cierra el archivo después de abrirlo.