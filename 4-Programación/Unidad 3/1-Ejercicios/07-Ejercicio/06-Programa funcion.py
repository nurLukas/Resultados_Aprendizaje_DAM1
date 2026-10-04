'''
    Programa gestor basico de proyectos 
    Diseñado por nurLukas de Sturmprojekt
    v 0.3
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
 
def listarProyecto():
    print("Vamos a listar los proyectos")
    print(nombreProyecto)
    
cabeceraBienvenida()
nombreProyecto = ""
while True:
    muestraMenu()
    print("-"*42)
    opcion = input("Selecciona y escribe la opción deseada: ")
    print("-"*42)
    if opcion == "2":
        listarProyecto()
    

