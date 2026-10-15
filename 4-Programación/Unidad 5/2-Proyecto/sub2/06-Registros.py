'''
    ( El contenido de este programa, corresponde a la subunidad 02: "ficheros de datos y registros". 
    Primero guardaremos un mantenimiento con sus cuatro campos. Después aprenderemos a separarlos al leer.
    Programa para documentación y registro detallado del mantenimiento del coche.
'''
print("-"*45)
print("Programa para documentación y registro")
print("del mantenimiento de tu coche")
print("Desarrollado por nurLukas de Sturmprojekt")
print("Poder en cada proyecto!")
print("-"*45)

print("Registrar mantenimiento")
print("-"*45)

fecha = input("Fecha del mantenimiento: ")
kilometraje = input("Kilometraje del coche: ")
detalle = input("Mantenimiento realizado: ")
coste = input("Coste del mantenimiento: ")

archivo = open("mantenimiento.csv", "a")
archivo.write(fecha + "|" + kilometraje + "|" + detalle + "|" + coste + "\n")
archivo.close()

print("Mantenimientos guardados")
archivo = open("mantenimiento.csv", "r")
lineas = archivo.readlines()

for linea in lineas:
    datos = linea.strip().split("|")
    print(datos)
    
archivo.close()
