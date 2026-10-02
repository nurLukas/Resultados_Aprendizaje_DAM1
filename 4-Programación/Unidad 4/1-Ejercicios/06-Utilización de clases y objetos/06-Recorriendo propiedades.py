class Producto():                                  # Clase Producto
    def __init__(self,nombre,marca,tipo):          # Inicio constructor
        self.nombre = nombre                       # Atributo
        self.marca = marca                         # Atributo
        self.tipo = tipo                           # Atributo
    
productos = []                                     # Creo lista "productos"

print("-"*30)

print("vamos a insertar productos:")
while True:                                        # Bucle infinito
    print("Introducimos  un nuevo producto")
    nombre = input("Dime el nombre: ")             # Un input, (un input es una función)
    marca = input("Dime el marca: ")               # Otro input
    tipo = input("Dime el tipo de producto: ")     # Y otro input
    productos.append(Producto(nombre,marca,tipo))  # Creo objeto de clase "Producto", y ".append" lo añado a la lista "productos"
  
    print("#"*30)                                  # Embellecedor estético 
   
    for producto in productos:                     # "producto" es el nombre de una variable temporal que, en cada vuelta del for, representa uno de los objetos que hay dentro de la lista "productos",la acción: Recorro cada objeto de la lista "productos"
      
      for clave, valor in vars(producto).items():  # Recorro todos los atributos del objeto y obtengo su nombre y su valor
           
           print(clave, ":", valor)                # Muestro el nombre del atributo y el valor que contiene
  
    print("-"*30)                                  # Embellecedor estético                  
  
    print("#"*30)                                  # Embellecedor estético 