class Producto():                                 # Clase
	def __init__(self,nombre,marca,tipo):         # Constructor
		self.nombre = nombre                      # Atributo 
		self.marca = marca                        # Atributo 
		self.tipo = tipo                          # Atributo 
		
producto1 = Producto(                             # Instancia1
	"Best X18",
	"Medion Erazer",
	"Portatil para juegos"
)

producto1 = Producto(                             # Instancia2
	"X81025",
	"Medion Erazer",
	"Teclado para juegos"
)

producto1 = Producto(                             # Instancia3
	"Defender P40",
	"Medion Erazer",
	"Portatil para juegos"
)

producto1 = Producto(                             # Instancia4
	"Wizard P20",
	"Medion Erazer",
	"Ratón para juegos"
)

producto1 = Producto(                             # Instancia5
	"Mage P20",
	"Medion Erazer",
	"Auriculares para Juegos"
)

print("producto1")                              # Pinto las instancias creadas
print("producto2")
print("producto3")
print("producto4")
print("producto5")

