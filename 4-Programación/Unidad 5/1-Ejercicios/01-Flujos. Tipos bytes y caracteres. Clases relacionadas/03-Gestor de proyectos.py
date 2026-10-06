'''
    Implementacion de escritura tipo append
'''

print("-"*45)                                                  # Detalle estetico
print("Programa gestor de proyectos v0.1")                     # Cabecera de presentación
print("Desarrollado por nurLukas de Sturmprojekt")             # Cabecera de presentación
print("-"*45)                                                  # Detalle estetico

while True:                                                    # Bucle del menú
    nombre = input("Introduce el nombre del proyecto: ")       # input con indicaciones
    archivo = open("registro_proyectos.txt",'a')               # "a" significa append, es decir, añadir al final. A diferencia de "w", no borra lo que ya existe.
    archivo.write(nombre+"\n")                                 # "\n" significa salto de línea, así que cada contacto queda en una línea diferente.
    archivo.close()                                            # cerramos el archivo abierto previamente.
    
    
    
    
    
   