'''
    Programa para documentación y registro detallado del mantenimiento del coche.
'''
print("-"*45)
print("Programa para documentación y registro")
print("del mantenimiento de tu coche")
print("Desarrollado por nurLukas de Sturmprojekt")
print("Poder en cada proyecto!")
print("-"*45)

archivo = open("mantenimiento.txt", "r")   # "r" abre el archivo para leerlo, sin modificarlo.
lineas = archivo.readlines()               # readlines() lee sus líneas y las devuelve en una lista. --> ['Cambio de aceite'], # lineas guarda esa lista.
print(lineas)                              # La muestra en la terminal.
archivo.close()                              # Cerramos el archivo.
