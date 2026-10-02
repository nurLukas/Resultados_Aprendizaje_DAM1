class Producto():                                   # Clase Producto
    def __init__(self,nombre,marca,tipo):           # Inicio constructor
        self.nombre = nombre                        # Atributo
        self.marca = marca
        self.tipo = tipo
    
productos = []                                      # Creo lista "productos"

print("-"*30)

print("vamos a insertar productos:")
while True:                                         # Bucle infitino
    print("Introducimos  un nuevo producto")
    nombre = input("Dime el nombre: ")              # Un input
    marca = input("Dime el marca: ")                # Otro input
    tipo = input("Dime el tipo de producto: ")      # Y otro input
    productos.append(Producto(nombre,marca,tipo))   # Creo objeto "Producto" y lo añado a la lista
  
    print("-"*30)                                   # Embellecedor estético 
    for producto in productos:                      # "producto" es el nombre de una variable temporal que, en cada vuelta del for, representa uno de los objetos que hay dentro de la lista "productos"
        print(producto.nombre)
        print(producto.marca)
        print(producto.tipo)
        print("-"*20)                                 
    print("-"*30)