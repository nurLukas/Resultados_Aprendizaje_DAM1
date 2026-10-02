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