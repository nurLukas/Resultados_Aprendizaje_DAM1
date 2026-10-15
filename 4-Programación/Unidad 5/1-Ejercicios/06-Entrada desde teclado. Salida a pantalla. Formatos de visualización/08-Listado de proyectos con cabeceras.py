''' 
    Programa gestor de proyectos v0.3
    Lucas Andrés Griego
  
    Proyecto
    -nombreProyecto
    -descripcion
    -cliente
    -telefono
'''
print("-"*30)
print("Programa gestor de proyectos")
print("v0.3 Lucas Andrés Griego")
print("+ Proyectos = + Euros")
print("-"*30)

while True:
    print("Selecciona una opción")
    print("1.-Agregar un proyecto")
    print("2.-Listar proyectos")
    print("3.-Salir del programa")
	
    opcion = input("Selecciona una opcion: ")
	
    if opcion == "1":
        nombreProyecto = input("Introduce el nombre del nuevo proyecto: ") 
        descripcion = input("Introduce una breve descripcion del proyecto: ") 
        cliente = input("Introduce nombre y apellidos del cliente: ") 
        telefono = input("Introduce telefono del cliente: ") 
        
        archivo = open("proyectos.csv", "a")
        archivo.write(
            nombreProyecto + "|" + 
            descripcion + "|" + 
            cliente + "|" + 
            telefono + "\n"
        )

        print("Tu proyecto ha sido guardado")
        archivo.close()
		
    elif opcion == "2":
        archivo = open("proyectos.csv", "r")
        # Leo la primera línea, que contiene las cabeceras
        cabecera = archivo.readline()
        # Separo las cabeceras
        cabeceras = cabecera.strip().split("|")
        # Leo el resto de líneas
        lineas = archivo.readlines()
        # Recorro todos los registros
        for linea in lineas:
            # Separo los campos del registro
            datos = linea.strip().split("|")
            print("------------------------------")
            # Muestro cabecera : valor
            for i in range(0, len(datos)):
                print(cabeceras[i], ":", datos[i])
        print("------------------------------")
        archivo.close()

    elif opcion == "3":
        print("Estas cerrando el programa, adios")
        break