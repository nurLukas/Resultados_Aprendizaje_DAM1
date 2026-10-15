'''
    Programa para documentación y registro detallado del mantenimiento del coche.
'''
print("-"*45)
print("Programa para documentación y registro")
print("del mantenimiento de tu coche")
print("Desarrollado por nurLukas de Sturmprojekt")
print("Poder en cada proyecto!")
print("-"*45)

print("-"*45)
print("Mantenimientos realizados:")
archivo = open("mantenimiento.txt", "r")
lineas = archivo.readlines()  # Lee todas las líneas restantes del archivo y las guarda en una lista llamada lineas.

for linea in lineas:          # Recorre la lista, tomando una línea en cada repetición.
    print(linea.strip())      # Quita los espacios y saltos de línea de los extremos. Así evitamos líneas vacías entre los mantenimientos al imprimir.
    
archivo.close()

