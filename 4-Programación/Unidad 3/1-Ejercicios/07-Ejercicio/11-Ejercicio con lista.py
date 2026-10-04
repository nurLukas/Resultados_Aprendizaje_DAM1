from funciones_externas import *
  
cabeceraBienvenida()
proyectos = []
while True:
    muestraMenu()
    opcion = input("Introduce tu opción:")
    if opcion == "1":
        nuevoregistro = input("Introduce un nuevo proyecto: ")
        proyectos = crearRegistro(proyectos,nuevoregistro)
    elif opcion == "2":
        listarRegistros(proyectos)
    elif opcion == "3":
        actualizarRegistro(proyectos,registro)
    elif opcion == "4":
        eliminarRegistro(proyectos,registro)