class Perro():                                   # Clase 
	def __init__(self,nombre,color,edad,peso):   # Constructor
		self.nombre = nombre				     # Atributo 
		self.color = color                       # Atributo 
		self.edad = 0                            # Atributo 
		self.peso = ""                           # Atributo 
		
wulf = Perro("Wulf","negro",0,1)                 # Creo instancia "Wulf"
print(wulf.nombre)
print(wulf.color)