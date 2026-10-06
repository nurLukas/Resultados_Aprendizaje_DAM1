'''
    Archivo de almacenamiento de funciones.
    Funciones listas para externalizar con exito.
'''
def cabeceraBienvenida():
    print("-"*42)
    print("Programa gestor de proyectos v0.2")
    print("Diseñado por Sturmprojekt")
    print("¡Bienvenido!")
    print("-"*42)
    
def muestraMenu():
        print("-"*42)
        print("Tienes las siguientes opciones:")
        print("1- Crear proyecto")
        print("2- Listar proyectos")
        print("3- Actualizar/editar proyecto")
        print("4- Eliminar proyecto")
        print("5- Salir del programa")
        print("-"*42)
        
def listarRegistros(proyectos):
    print("Vamos a listar los proyectos")
    print(proyectos)

def crearRegistro(proyectos,registro):
    proyectos.append(registro)
    return proyectos

def actualizarRegistro(proyectos,indice,valor):
    proyectos[indice] = valor
    return proyectos

def eliminarRegistro(proyectos,indice):
    proyectos.pop(indice)
    return proyectos