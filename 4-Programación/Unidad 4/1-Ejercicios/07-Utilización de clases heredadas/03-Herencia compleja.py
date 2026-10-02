class Automovil():                                     # Hiper clase
    def __init__(self):
        self.Km = 0                                    # Atributo
        self.color = ""                                # Atributo
    def arrastrarse(self):
        print("El coche se arrastra a 150 km/h")       # Método

class altaGama(Automovil):                                      # Super clase
    def __init__(self):                                # Constructor
        super().__init__()                             # Ese "super().__init__()", está llamando al constructor de Automovil
    def acelerar(self):                                # Método
        print("El coche esta acelerando a 250 km/h")

class Audi(altaGama):                                  # Clase Audi
    def __init__(self):                                # Constructor
        super().__init__()                             # super() es para acceder a la "super clase", tambien nombrada como "clase padre"
        
class BMW(altaGama):                                   # Clase BMW
    def __init__(self):                                # Constructor
        super().__init__()                             # super() es para acceder a la "super clase", tambien nombrada como "clase padre"

class Opel(Automovil):
    def __init__(self):
        super().__init__()

RSQ8 = Audi()                                          # Se crea objeto "RSQ8", instancia de la clase "Audi", y gracias a "super().__init__()", reciben los atributos, y método de la super clase "altaGama"
RSQ8.acelerar()

X6M = BMW()                                            # Se crea objeto "X6M", instancia de la clase "BMW", y gracias a "super().__init__()", reciben los atributos, y método de la super clase "altaGama"
X6M.acelerar() 

Astra = Opel()                                         # Creo un objeto Opel, que hereda directamente de Automovil
Astra.arrastrarse()                                    # Método heredado de Automovil