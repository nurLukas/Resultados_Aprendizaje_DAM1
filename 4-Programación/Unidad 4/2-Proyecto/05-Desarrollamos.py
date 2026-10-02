class Proyecto():
    def __init__(self,nombre,estado,descripcion,autor):
        self.nombre = nombre
        self.estado = estado
        self.descripcion = descripcion
        self.autor = autor
		
    def entraProyecto(self,nombre,estado,descripcion,autor):
        self.nombre = nombre
        self.estado = estado
        self.descripcion = descripcion
        self.autor = autor
    
    def saleProyecto(self):
        return [self.nombre,self.estado,self.descripcion,self.autor]

proyectos = []

print("-"*35)
print("Gestor de proyectos v0.1")
print("Diseñado por Sturmprojekt")
print("¡Poder en cada proyecto!")
print("-"*35)
while True:
    print("Selecciona una opcion")
    print("1- Introducir un nuevo proyecto")
    print("2- Listar proyectos")
    opcion = input("Selecciona una opción: ")
    print("-"*35)