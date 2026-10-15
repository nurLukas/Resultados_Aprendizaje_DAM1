'''
    Programa para documentación y registro detallado del mantenimiento del coche.
'''
print("-"*45)
print("Programa para documentación y registro")
print("del mantenimiento de tu coche")
print("Desarrollado por nurLukas de Sturmprojekt")
print("Poder en cada proyecto!")
print("-"*45)

archivo = open("mantenimiento.txt", "w")      # Abre mantenimiento.txt. El modo "w" lo crea si no existe; si existe, borra su contenido. 
archivo.write("Cambio de aceite.")             # Escribe el texto.
archivo.close()                                 # Cierra el archivo.

# Archivo es la variable que utilizamos para trabajar con el fichero abierto.