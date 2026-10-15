import os

os.rmdir("documentos")     # os.rmdir() significa remove directory (eliminar directorio).

'''
    Pero tiene una condición muy importante: la carpeta debe estar vacía.
    Por ejemplo:
    - Si documentos está vacía → se elimina.
    - Si contiene apuntes.txt → da un error.
    - Si no existe → da un error.
'''