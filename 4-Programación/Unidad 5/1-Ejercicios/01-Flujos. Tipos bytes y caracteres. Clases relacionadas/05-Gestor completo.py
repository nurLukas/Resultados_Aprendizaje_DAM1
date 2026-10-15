'''
    Implementacion de lectura y escritura.
'''

print("-"*45)                                              # Detalle estetico.
print("Programa gestor de proyectos v0.2")                 # Cabecera de presentación.
print("Desarrollado por nurLukas de Sturmprojekt")         # Cabecera de presentación.
print("-"*45)                                              # Detalle estetico

while True:                                                # Bucle infinito,  mantiene el menú activo hasta que el usuario elige salir.
    print("-"*35)                                          # Detalle estetico
    print("Selecciona una opcion")
    print("1.-Introduce un proyecto")
    print("2.-Selecciona los proyectos")
    print("3.-Salir del gestor")
    opcion = input("Escoge una opción: ")                  # input: Lee la opción introducida por el usuario.
    print("-"*35)                                          # Detalle estetico
    if opcion == "1":
        archivo = open("registro_proyectos.txt",'a')       # # Apertura del archivo, en modo append
        nombre = input("Ahora introduce el nombre del nuevo proyecto: ")
        archivo.write(nombre+"\n")
        archivo.close()                                    # Cierra el archivo.
    elif opcion == "2":
        archivo = open("registro_proyectos.txt",'r')       # Apertura del archivo, en modo lectura
        lineas = archivo.readlines()                       # Guarda todas las líneas del archivo en una lista.
        for linea in lineas:                               # Recorre cada línea almacenada en la lista.
            print(linea)                                   # imprime cada nombre.
            archivo.close()                                # Cierra el archivo.
    elif opcion == "3":
        print("Saliendo del gestor, adios")
        break                                              # Se cierra el programa
    else:
        print("Opción incorrecta")
    