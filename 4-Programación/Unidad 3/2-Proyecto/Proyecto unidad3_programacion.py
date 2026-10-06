'''
    Programa gestor de proyectos.
    Desarrollado po nurLukas de Sturmprojekt
'''
from funciones_externas import *                                   # Importo de archivo externo, funciones, y alguna cualidad estetica.

cabeceraBienvenida()                                               # Llamo a la función

proyectos = []                                                     # Creo lista "proyectos"

while True:                                                        # Bucle del menú
    muestraMenu()
    opcion = input("Introduce tu opción: ")                        # input para la selccion de opcions del usuario

    if opcion == "1":
        nuevoregistro = input("Introduce un nuevo proyecto: ")     # Se solicita al usuario la informacion necesaria, y se le brinda la posibilidad de introducir informacion
        proyectos = crearRegistro(proyectos, nuevoregistro)

    elif opcion == "2":                                            # Se genera una lista ordenada de los proyectos
        listarRegistros(proyectos)

    elif opcion == "3":                                            # Utilidad Update del CRUD, con instrucciones de uso. 
        indice = int(input("Introduce el indice a modificar: "))
        valor = input("Introduce el valor a insertar: ")
        proyectos = actualizarRegistro(proyectos, indice, valor)

    elif opcion == "4":                                            #Utilidad Delete, con instrucciones de uso
        indice = int(input("Introduce el indice a eliminar: "))
        proyectos = eliminarRegistro(proyectos, indice)

    elif opcion == "5":
        print("Estas saliendo, adios.")
        break                                                      # Cierre del programa

    print("-"*30)                                                  # Detalle estetico
    
    
