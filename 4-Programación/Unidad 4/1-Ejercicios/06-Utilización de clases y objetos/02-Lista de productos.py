class Producto():                                                                       # Clase producto
    def __init__(self,nombre,marca,tipo):                                               # Constructor
        self.nombre = nombre                                                            # Atributo1
        self.apellidos = marca                                                          # Atributo2
        self.email = tipo                                                               # Atributo3
    
productos = []                                                                          # Creo lista "productos"

productos.append(Producto("Best X18","Medion Erazer","Portatil para juegos"))           # Creo producto
productos.append(Producto("X81025","Medion Erazer","Teclado para juegos"))
productos.append(Producto("Defender P40","Medion Erazer","Portatil para juegos"))
productos.append(Producto("Wizard P20","Medion Erazer","Ratón para juegos"))
productos.append(Producto("Mage P20","Medion Erazer","Auriculares para Juegos"))

print(productos)                                                                        # Imprimo "lista productos" 