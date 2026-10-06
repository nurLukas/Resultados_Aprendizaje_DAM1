'''
    Implementacion de lectura tipo "read".
'''

print("-"*45)                                          # Detalle estetico.
print("Programa gestor de proyectos v0.1")             # Cabecera de presentación.
print("Desarrollado por nurLukas de Sturmprojekt")     # Cabecera de presentación.
print("-"*45)                                          # Detalle estetico.


archivo = open("registro_proyectos.txt",'r')
lineas = archivo.readlines()                           # crea una lista parecida a: ["Ruffoo\n", "zandtvoort\n", "Corcobo\n"].
for linea in lineas:                                   # Para cada elemento que haya dentro de lineas, guárdalo temporalmente en la variable linea.
    print(linea)                                       # imprime cada nombre.
archivo.close()                                        # Cierra el archivo.