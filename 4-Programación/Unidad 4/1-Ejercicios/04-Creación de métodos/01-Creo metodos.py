class Perro():
    def __init__(self):
        self.edad = 0           # Una propiedad
        self.color = ""         # Otra propiedad
        self.peso = 1           # Y otra más
	
    def ladrar(self):
        print("El perro esta ladrando")   # Metodo
	
    def correr(self):
        print("El perro corre")           # Otro metodo

Wulf = Perro()
Wulf.ladrar()
Wulf.correr()