class Proyecto():                                               # Creo clase "Proyecto" 
    def __init__(self,nombre,estado,descripcion,autor):         # Aplico un constructor
        self.nombre = nombre                                    # Primero de 4 atributos
        self.estado = estado
        self.descripcion = descripcion
        self.autor = autor
    
    def saleProyecto(self):                                      # Segundo método
        return [self.nombre,self.estado,self.descripcion,self.autor]  # Devuelvo los atributos del objeto Proyecto en forma de lista

proyectos = []                                                   # Lista donde almacenaré los objetos de la clase Proyecto

print("*"*35)
print("Gestor de proyectos v0.1")                                # Nombre y versionado del programa
print("Diseñado por Sturmprojekt")                               # Desarrollador del programa
print("¡Poder en cada proyecto!")                                # Lema del desarrollador 
print("*"*35)                                                    # Elemento estético
while True:                                                      # Bucle "while True" para el menu CR (Create y Read)
    print("Selecciona una opcion")
    print("1- Introducir un nuevo proyecto:")                    # Primera opcion seleccionable de varias
    print("2- Listar proyectos:")
    print("3- Salir")
    opcion = input("Selecciona una opción: ")                    # Primer input
    print("-"*35)
    if opcion == "1":                                            # Condicional aplicado
        nombre = input("Introduce el nombre del proyecto: ")
        estado = input("Introduce el estado del proyecto, ej: pendiente, en progreso, terminado, o pausado: ")
        descripcion = input("Introduce una breve descripcion del proyecto: ")
        autor = input("Introduce autor: ")
        proyectos.append(Proyecto(nombre,estado,descripcion,autor))  # Creo un objeto de la clase Proyecto y lo añado a la lista "proyectos"
    elif opcion == "2":                                           # Otro condicional aplicado
        for proyecto in proyectos:                                # "proyecto" es la VARIABLE TEMPORAL, que va representando cada objeto almacenado en proyectos
            print(proyecto.saleProyecto())
    elif opcion == "3":
        print("Saliendo del programa, adios...")
        print("-"*35)
        break                                                    # Implemento "break" para salir del programa