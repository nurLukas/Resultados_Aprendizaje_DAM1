'''
    Programa gestor de proyectos v0.3
    Lucas Andrés Griego
  
    Proyecto
    -nombreProyecto
    -descripcion
    -cliente
    -telefono
'''

print("Programa gestor de proyectos")
print("v0.3 Lucas Andrés Griego")
print("+ Proyectos = + Euros")

while True:
    print("Selecciona una opción")
	print("1.-Agregar un proyecto")
    print("2.-Listar proyectos")
	
    opcion = input("Selecciona una opcion: ")
	
	if opcion == "1":
        nombreProyecto = input("Introduce el nombre del nuevo proyecto: ") 
        descripcion = input("Introduce una breve descripcion del proyecto: ") 
        cliente = input("Introduce nombre y apellidos del cliente: ") 
        telefono = input("Introduce telefono del cliente: ") 
        
        archivo = open("proyectos.csv", "a")
        archivo.write(nombreProyecto + "|" + descripcion + "|" + cliente + "|" + telefono + "\n")
        archivo.close()

        print("Tu proyecto ha sido guardado")
        archivo.close()
		
    elif opcion == "2":
        archivo = open("proyectos.csv", "r")
        lineas = archivo.readlines()
        print(lineas)
        archivo.close()