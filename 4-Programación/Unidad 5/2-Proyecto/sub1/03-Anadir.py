'''
    Programa para documentación y registro detallado del mantenimiento del coche.
'''
print("-"*45)
print("Programa para documentación y registro")
print("del mantenimiento de tu coche")
print("Desarrollado por nurLukas de Sturmprojekt")
print("Poder en cada proyecto!")
print("-"*45)

detalle = input("Introduce el mantenimiento realizado: ")   # input() pide un texto y lo guarda en detalle.

archivo = open("mantenimiento.txt", "a")                    # "a" añade al final del archivo sin borrar lo anterior.
archivo.write(detalle + "\n")                               # "\n" escribe un salto de línea para separar los mantenimientos.
archivo.close()                                               # Cerramos el archivo.