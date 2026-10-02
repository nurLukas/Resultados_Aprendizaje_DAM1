class Perro():
    def __init__(self):
        self.edad = 0
        self.color = ""
        self.peso = ""

Wulf = Perro()
print("Wulf tiene",Wulf.edad,"años")        # Leo una propiedad

Wulf.peso = 1                               # Escribo una propiedad
print("Wulf pesa",Wulf.peso,"Kg")           # Leo una propiedad

Blonda = Perro()
Blonda.peso = "1,5"
print("Blonda pesa",Blonda.peso,"Kg")       # Leo otra propiedad

Blonda.color = "marron"                     # Escribo una propiedad
print("Blonda es de color",Blonda.color)    # Leo una propiedad