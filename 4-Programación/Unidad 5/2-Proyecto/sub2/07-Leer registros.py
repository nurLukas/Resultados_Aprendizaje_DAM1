'''
    ( El contenido de este programa, corresponde a la subunidad 02: "ficheros de datos y registros". 
    Programa para documentación y registro detallado del mantenimiento del coche.
'''
print("-"*45)
print("Programa para documentación y registro")
print("del mantenimiento de tu coche")
print("Desarrollado por nurLukas de Sturmprojekt")
print("Poder en cada proyecto!")
print("-"*45)

print("Mantenimientos guardados:")
print("-"*45)

archivo = open("mantenimiento.csv", "r")
lineas = archivo.readlines()

for linea in lineas:
    datos = linea.strip().split("|")

    print("------------------------------")
    print("Fecha:", datos[0])
    print("Kilometraje:", datos[1])
    print("Detalle:", datos[2])
    print("Coste:", datos[3])

archivo.close()