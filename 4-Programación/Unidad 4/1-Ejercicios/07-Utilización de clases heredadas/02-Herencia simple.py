class altaGama():                           # Super clase
    def __init__(self):                     # Constructor
        self.Km = 0                         # Atributo
        self.color = ""                     # Atributo
    def acelerar(self):                     # Metodo
        print("El coche esta acelerando")

class Audi(altaGama):                       # Clase Audi
    def __init__(self):                     # Constructor
        super().__init__()                  # super() es para acceder a la "super clase", tambien nombrada como "clase padre"
        
class BMW(altaGama):                        # Clase BMW
    def __init__(self):                     # Constructor
        super().__init__()                  # super() es para acceder a la "super clase", tambien nombrada como "clase padre"

RSQ8 = Audi()                               # Se crea objeto "RSQ8", instancia de la clase "Audi", y "super().__init__()", hace que se ejecute el constructor de altaGama, heredando sus atributos. "class Audi(altaGama)" permite heredar métodos como acelerar()
RSQ8.acelerar()

X6M = BMW()                                 # Se crea objeto "X6M", instancia de la clase "BMW", y gracias a "super().__init__()", reciben los atributos, y metodo de la super clase "altaGama"
X6M.acelerar() 