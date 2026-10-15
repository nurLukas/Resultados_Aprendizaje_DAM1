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

    mantenimiento = {
        "fecha": datos[0],
        "kilometraje": datos[1],
        "detalle": datos[2],
        "coste": datos[3]
    }

    print("------------------------------")
    print("Fecha:", mantenimiento["fecha"])
    print("Kilometraje:", mantenimiento["kilometraje"])
    print("Detalle:", mantenimiento["detalle"])
    print("Coste:", mantenimiento["coste"])
    
archivo.close()


'''
    datos[0]                 # Lista: accedemos por posición
    mantenimiento["fecha"]   # Diccionario: accedemos por clave
    
    En el diccionario, cada pareja tiene una clave y un valor. Por ejemplo:
    "fecha": datos[0]
'''