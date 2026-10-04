'''
    Programa gestor basico de proyectos 
    Diseñado por nurLukas de Sturmprojekt
    v 0.3
'''
from funciones_externas import *
 
def listarProyecto():
    print("Vamos a listar los proyectos: ")
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
    

