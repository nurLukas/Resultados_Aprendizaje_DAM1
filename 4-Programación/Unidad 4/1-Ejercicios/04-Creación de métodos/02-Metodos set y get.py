class Perro():
    
    def __init__(self):
        self.edad = 0           # Una propiedad
        self.color = ""         # Otra propiedad
        self.peso = 1           # Y otra más  (son atributos)

    def ladrar(self):
        print("El perro esta ladrando")  # Metodo
   
   def correr(self):
        print("El perro corre")          # Otro metodo

    def getColor(self):                  # Creo metodo get
        return self.color

    def setColor(self,nuevocolor):       # Creo metodo set
        self.color = nuevocolor



Wulf = Perro()
Wulf.setColor("negro")
print(Wulf.getColor())
Wulf.ladrar()
Wulf.correr()