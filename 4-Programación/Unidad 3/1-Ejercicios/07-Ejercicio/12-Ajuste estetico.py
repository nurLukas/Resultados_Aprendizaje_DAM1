from funciones_externas import *

cabeceraBienvenida()

proyectos = []

while True:
    muestraMenu()
    opcion = input("Introduce tu opción: ")

    if opcion == "1":
        nuevoregistro = input("Introduce un nuevo proyecto: ")
        proyectos = crearRegistro(proyectos, nuevoregistro)

    elif opcion == "2":
        listarRegistros(proyectos)

    elif opcion == "3":
        indice = int(input("Introduce el indice a modificar: "))
        valor = input("Introduce el nuevo valor: ")
        proyectos = actualizarRegistro(proyectos, indice, valor)

    elif opcion == "4":
        indice = int(input("Introduce el indice a eliminar: "))
        proyectos = eliminarRegistro(proyectos, indice)

    elif opcion == "5":
        print("Estas saliendo del programa gestor, adios.")
        break