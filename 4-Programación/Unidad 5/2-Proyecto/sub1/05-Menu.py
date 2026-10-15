'''
    Programa para documentación y registro detallado del mantenimiento del coche.
'''
print("-"*45)
print("Programa para documentación y registro")
print("del mantenimiento de tu coche")
print("Desarrollado por nurLukas de Sturmprojekt")
print("Poder en cada proyecto!")
print("-"*45)

print("Registro de mantenimientos realizados")

while True:
    print("-"*45)
    print("1.- Agregar mantenimiento realizado")
    print("2.- Listar mantenimientos")
    print("0.- Salir del programa")
    print("-"*45)
    
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        detalle = input("Introduce el mantenimiento realizado: ")
        archivo = open("mantenimiento.txt", "a")
        archivo.write("- " + detalle + "\n")
        archivo.close()
    
    elif opcion == "2":
        print("Mantenimientos realizados:")
        archivo = open("mantenimiento.txt", "r")
        lineas = archivo.readlines()
        
        for linea in lineas:
            print(linea.strip())
        archivo.close()
    
    elif opcion == "0": 
        print("Esta saliendo del programa, adios")
        break
    else:
        print("Opción incorrecta")