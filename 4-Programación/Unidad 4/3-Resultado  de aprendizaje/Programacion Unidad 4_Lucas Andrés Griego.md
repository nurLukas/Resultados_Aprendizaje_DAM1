# Reporte de proyecto

## Información de generación

- **Fecha:** 2026-10-02 22:16:56 +0200
- **Usuario:** lucas
- **Equipo:** LUCAS
- **Sistema operativo:** Windows
- **Arquitectura:** x86_64
- **Directorio de ejecución:** `D:/Herramientas/portables/jocarsa-generador-windows-x64`
- **Proyecto documentado:** `D:/DAM1 Resultados Aprendisaje/4-Programación/Unidad 4`
- **HMAC-SHA-256 de autenticidad:** `bbaa5bfc64ae02e5e66d67061a9fdb8ef9c529afbe4666b7b0d7780618d35dab`

> El HMAC-SHA-256 se calcula sobre el documento completo usando un secreto incluido en el programa y 64 ceros en el propio campo del HMAC. El secreto no se escribe en el informe. Este mecanismo permite comprobar integridad y que el documento fue generado con el mismo secreto.

## Estructura del proyecto

```
D:/DAM1 Resultados Aprendisaje/4-Programación/Unidad 4
├── 1-Ejercicios
│   ├── 01-Concepto de clase
│   │   └── Conceptos de clase.md
│   ├── 02-Estructura y miembros de una clase. Visibilidad
│   │   └── Hablemos de perros.md
│   ├── 03-Creación de propiedades
│   │   ├── 01-Creo Clase.py
│   │   ├── 02-Creo Instancia.py
│   │   ├── 03-Otra instancia.py
│   │   ├── 04-Leo propiedades.py
│   │   └── 05-Escribo propiedades.py
│   ├── 04-Creación de métodos
│   │   ├── 01-Creo metodos.py
│   │   ├── 02-Metodos set y get.py
│   │   └── 03-Metodos y condicionales.py
│   ├── 05-Creación de constructores
│   │   └── 01-Creo constructor bien hecho.py
│   ├── 06-Utilización de clases y objetos
│   │   ├── 01-Creo clase productos.py
│   │   ├── 02-Lista de productos.py
│   │   ├── 03-Input.py
│   │   ├── 04-Print lista.py
│   │   ├── 05-Mejoro el print.py
│   │   └── 06-Recorriendo propiedades.py
│   └── 07-Utilización de clases heredadas
│       ├── 01-Audis y bmws.py
│       ├── 02-Herencia simple.py
│       └── 03-Herencia compleja.py
├── 2-Proyecto
│   ├── 01-Clase Proyecto.py
│   ├── 02-Creo un constructor.py
│   ├── 03-Propiedades.py
│   ├── 04- Metodos.py
│   ├── 05-Desarrollamos.py
│   ├── 06-Create y Read Menu.py
│   └── 07-Gestor de proyectos.py
└── 3-Resultado  de aprendisaje
    └── Ra4.md
```

## Bases de datos SQLite

Esta sección documenta únicamente el esquema de las bases SQLite detectadas. No se vuelcan registros ni datos de usuario.

No se han encontrado bases SQLite con extensiones .db, .sqlite o .sqlite3.

## Código (intercalado)

# Unidad 4
## 1-Ejercicios
### 01-Concepto de clase
**Conceptos de clase.md**
```markdown
# Concepto de "clase" e "instancia"

**Utilizaremos un perro, como "concepto" a modo de ejemplo.**

Perro es un concepto general.
Perro es una idea abstracta una categoria mental, que reúne ciertas propiedades 
que permiten reconer a algo como un perro-

- Un concepto, para nosotros es una "clase".

- Las derivaciones de perro, son "instancias", por ejemplo: un ejemplar concreto
  de la clase perro, seria mi pero Wulf, la perra Blonda.
  
- Las propiedades que describen a una instancia, son "atributos" por ejemplo, color = negro, edad = 4, peso = 10 kg.

- "Mamifero" seria una "clase superior", que contenga la clase "perro", y la clase "gato".


Mamifero                       <-- Clase superior
  |                                
  |
  |---> Perro                  <-- Clase
  |        |---> Wulf          <-- Instancia
  |        |
  |        |---> Blonda        <-- instancia
  | 
  |
  |---> Gato                   <-- Clase



Atributos 
* Wulf: 
- Color : negro
- Edad : 3 años
- Peso : 12 kg

* Blonda
- Color : marron
- Edad : 2 años
- Peso :  8 kg


Aun podemos subir varios niveles las clases superiores

por ejemplo con una clase llamada "animal" que engloba mamiferos, reptiles, etc.

Metodos: Luego aprenderemos de ellos, pero definen acciones. 
```
### 02-Estructura y miembros de una clase. Visibilidad
**Hablemos de perros.md**
```markdown
Un concepto es una clase.
Por ejemplo: un gato

Cuando un gato nace, tiene una serie de propiedades:
edad = 0
color = X
Todo esto se llama constructor - propiedades que se dan al nacer

Atributos estáticos - no acciones - propiedades
color = naranja
color_ojos = azul

Atributos dinámicos - acciones - métodos
maullar = acción
arañar = acción
caminar
saltar

Destructor: todo desaparece al morir
```
### 03-Creación de propiedades
**01-Creo Clase.py**
```python
class Perro():
    def __init__(self):
        self.edad = 0
        self.color = ""
        self.peso = 1
	
```
**02-Creo Instancia.py**
```python
class Perro():
	def__init__(serlf):
		self.edad:0
		self.color:""
		self.peso:1

Wulf = Perro()
print("Wulf")
```
**03-Otra instancia.py**
```python
class Perro():
    def __init__(self):
        self.edad = 0
        self.color = ""
        self.peso = 1

Wulf = Perro()
print(Wulf)

Blonda = Perro()
print(Blonda)
```
**04-Leo propiedades.py**
```python
class Perro():
    def __init__(self):
        self.edad = 0
        self.color = ""
        self.peso = 1

Wulf = Perro()
print("Wulf tiene",Wulf.edad,"años")      # Leo una propiedad

Blonda = Perro()
print("Blonda pesa",Blonda.peso,"Kg")    # Leo otra propiedad
```
**05-Escribo propiedades.py**
```python
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
```
### 04-Creación de métodos
**01-Creo metodos.py**
```python
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
```
**02-Metodos set y get.py**
```python
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
```
**03-Metodos y condicionales.py**
```python
class CuentaBancaria():
    def __init__(self):
        self.saldo = 0
        
    def retirarSaldo(self, cantidad):
        if cantidad < 10000:
            if cantidad < self.saldo:
                    self.saldo = self.saldo - cantidad
                    print("Operación relizada con exito, su saldo actual es de:",self.saldo)
            else: 
                print("Saldo insuficiente, consiga dinero roedor")
                
                
    def depositarSaldo(self, cantidad):
        if cantidad < 1:
            print("El monto a depositar, debe ser superior a 0 €, VACILÓN")
        else:
            if cantidad > 9999:
                print("Notificando a la entidad")
                
            self.saldo = self.saldo + cantidad
            print("Depósito realizado. Saldo:", self.saldo)
        
Micuenta1 = CuentaBancaria()
Micuenta1.depositarSaldo(0)


Micuenta2 = CuentaBancaria()
Micuenta2.depositarSaldo(10000)

Micuenta2.retirarSaldo(500)

        
```
### 05-Creación de constructores
**01-Creo constructor bien hecho.py**
```python
class Perro():                                   # Clase 
	def __init__(self,nombre,color,edad,peso):   # Constructor
		self.nombre = nombre				     # Atributo 
		self.color = color                       # Atributo 
		self.edad = 0                            # Atributo 
		self.peso = ""                           # Atributo 
		
wulf = Perro("Wulf","negro",0,1)                 # Creo instancia "Wulf"
print(wulf.nombre)
print(wulf.color)
```
### 06-Utilización de clases y objetos
**01-Creo clase productos.py**
```python
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

```
**02-Lista de productos.py**
```python
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
```
**03-Input.py**
```python
class Producto():                                   # Clase Producto
    def __init__(self,nombre,marca,tipo):           # Inicio constructor
        self.nombre = nombre                        # Atributo
        self.marca = marca
        self.tipo = tipo
    
productos = []                                      # Creo lista "productos"

print("vamos a insertar productos:")
while True:                                         # Bucle infitino
    print("Introducimos  un nuevo producto")
    nombre = input("Dime el nombre: ")              # Un input
    marca = input("Dime el marca: ")                # Otro input
    tipo = input("Dime el tipo de producto: ")      # Y otro input
    productos.append(Producto(nombre,marca,tipo))   # Creo objeto "Producto" y lo añado a la lista
```
**04-Print lista.py**
```python
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
    print(productos)                                # Imprimo 
    print("-"*30)
```
**05-Mejoro el print.py**
```python
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
```
**06-Recorriendo propiedades.py**
```python
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
```
### 07-Utilización de clases heredadas
**01-Audis y bmws.py**
```python
class Audi():                                # Clase Audi
    def __init__(self):                      # Constructor
        self.modelo = ""                     # Atributo
        self.motor = ""
        self.Km = 0
        self.color = ""
    def acelerar(self):                      # Metodo
        print("El coche esta acelerando")   
        



class BMW():                                 # Clase BMW
    def __init__(self):                      # Constructor
        self.modelo = ""                     # Atributo
        self.motor = ""
        self.Km = 0
        self.color = ""
    def acelerar(self):                      # Metodo
        print("El coche esta acelerando")
```
**02-Herencia simple.py**
```python
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
```
**03-Herencia compleja.py**
```python
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
```
## 2-Proyecto
**01-Clase Proyecto.py**
```python
class Proyecto():
```
**02-Creo un constructor.py**
```python
class Proyecto():
    def __init__(self):
```
**03-Propiedades.py**
```python
class Proyecto():
    def __init__(self,nombre,estado,descripcion,autor):
		self.nombre = nombre
		self.estado = estado
		self.descripcion = descripcion
		self.autor = autor
```
**04- Metodos.py**
```python
class Proyecto():
    def __init__(self,nombre,estado,descripcion,autor):
		self.nombre = nombre
		self.estado = estado
		self.descripcion = descripcion
		self.autor = autor
		
    def entraProyecto(self,nombre,estado,descripcion,autor):
        self.nombre = nombre
		self.estado = estado
		self.descripcion = descripcion
		self.autor = autor
    
    def saleProyecto(self):
        return [self.nombre,self.estado,self.descripcion,self.autor]
```
**05-Desarrollamos.py**
```python
class Proyecto():
    def __init__(self,nombre,estado,descripcion,autor):
        self.nombre = nombre
        self.estado = estado
        self.descripcion = descripcion
        self.autor = autor
		
    def entraProyecto(self,nombre,estado,descripcion,autor):
        self.nombre = nombre
        self.estado = estado
        self.descripcion = descripcion
        self.autor = autor
    
    def saleProyecto(self):
        return [self.nombre,self.estado,self.descripcion,self.autor]

proyectos = []

print("-"*35)
print("Gestor de proyectos v0.1")
print("Diseñado por Sturmprojekt")
print("¡Poder en cada proyecto!")
print("-"*35)
while True:
    print("Selecciona una opcion")
    print("1- Introducir un nuevo proyecto")
    print("2- Listar proyectos")
    opcion = input("Selecciona una opción: ")
    print("-"*35)
```
**06-Create y Read Menu.py**
```python
class Proyecto():                                               # Creo clase "Proyecto" 
    def __init__(self,nombre,estado,descripcion,autor):         # Aplico un constructor
        self.nombre = nombre                                    # Primero de 4 atributos
        self.estado = estado
        self.descripcion = descripcion
        self.autor = autor
		
    def entraProyecto(self,nombre,estado,descripcion,autor):    # Primer método
        self.nombre = nombre
        self.estado = estado
        self.descripcion = descripcion
        self.autor = autor
    
    def saleProyecto(self):                                      # Segundo método
        return [self.nombre,self.estado,self.descripcion,self.autor]

proyectos = []                                                   # Lista donde almacenaré los objetos de la clase Proyecto

print("*"*35)
print("Gestor de proyectos v0.1")                                # Nombre y versionado del programa
print("Diseñado por Sturmprojekt")                               # Desarrollador del programa
print("¡Poder en cada proyecto!")                                # Lema del desarrollador 
print("*"*35)                                                    # Elemento estético
while True:                                                      # Bucle "while True" para el menu CR (Create y Read)
    print("Selecciona una opcion")
    print("1- Introducir un nuevo proyecto:")                    # Primera opcion seleccionable de varias
    print("2- Listar proyectos:")
    print("3.- Salir")
    opcion = input("Selecciona una opción: ")                    # Primer input
    print("-"*35)
    if opcion == "1":                                            # Condicional aplicado
        nombre = input("Introduce el nombre del proyecto: ")
        estado = input("Introduce el estado del proyecto, ej: pendiente, en progreso, terminado, o pausado: ")
        descripcion = input("Introduce una breve descripcion del proyecto: ")
        autor = input("Introduce autor: ")
        proyectos.append(Proyecto(nombre,estado,descripcion,autor))
    elif opcion == "2":                                           # Otro condicional aplicado
        for proyecto in proyectos:
            print(proyecto.saleProyecto())
    elif opcion == "3":
        print("Saliendo del programa, adios...")
        print("-"*35)
        break                                                    # Implemento "break" para salir del programa
```
**07-Gestor de proyectos.py**
```python
class Proyecto():                                               # Creo clase "Proyecto" 
    def __init__(self,nombre,estado,descripcion,autor):         # Aplico un constructor
        self.nombre = nombre                                    # Primero de 4 atributos
        self.estado = estado
        self.descripcion = descripcion
        self.autor = autor
    
    def saleProyecto(self):                                      # Segundo método
        return [self.nombre,self.estado,self.descripcion,self.autor]  # Devuelvo los atributos del objeto Proyecto en forma de lista

proyectos = []                                                   # Lista donde almacenaré los objetos de la clase Proyecto

print("*"*35)
print("Gestor de proyectos v0.1")                                # Nombre y versionado del programa
print("Diseñado por Sturmprojekt")                               # Desarrollador del programa
print("¡Poder en cada proyecto!")                                # Lema del desarrollador 
print("*"*35)                                                    # Elemento estético
while True:                                                      # Bucle "while True" para el menu CR (Create y Read)
    print("Selecciona una opcion")
    print("1- Introducir un nuevo proyecto:")                    # Primera opcion seleccionable de varias
    print("2- Listar proyectos:")
    print("3- Salir")
    opcion = input("Selecciona una opción: ")                    # Primer input
    print("-"*35)
    if opcion == "1":                                            # Condicional aplicado
        nombre = input("Introduce el nombre del proyecto: ")
        estado = input("Introduce el estado del proyecto, ej: pendiente, en progreso, terminado, o pausado: ")
        descripcion = input("Introduce una breve descripcion del proyecto: ")
        autor = input("Introduce autor: ")
        proyectos.append(Proyecto(nombre,estado,descripcion,autor))  # Creo un objeto de la clase Proyecto y lo añado a la lista "proyectos"
    elif opcion == "2":                                           # Otro condicional aplicado
        for proyecto in proyectos:                                # "proyecto" es la VARIABLE TEMPORAL, que va representando cada objeto almacenado en proyectos
            print(proyecto.saleProyecto())
    elif opcion == "3":
        print("Saliendo del programa, adios...")
        print("-"*35)
        break                                                    # Implemento "break" para salir del programa
```
## 3-Resultado  de aprendisaje
**Ra4.md**
```markdown
# Resultado de aprendizaje 4
Resultado de aprendizaje
Desarrolla programas organizados en clases analizando y aplicando los principios de la programación orientada a objetos.

**Criterios de evaluación**
a) Se ha reconocido la sintaxis, estructura y componentes típicos de una clase.
Conforme fui avanzando en los ejercicios de cada subunidad correspondiente a la unidad 4, puse en practica los nuevos conocimientos necesarios para el proyecto final de unidad.

b) Se han definido clases.
Pude crear con exito clases, super clases e hiper clases, o clases padre.
Entendiendo tambien como funcionan los atributos que clases inferiores a heredado de clases superiores. 

c) Se han definido propiedades y métodos.
Se definieron "atributos" o "propiedades", entiendo que en este hambito son adjetivos, y tambien desarrolle varios métodos, algunos incluso en "clases inferiores" fueron heredados de "clases superiores"

d) Se han creado constructores.
Se aplicaron constructores "__init__" y " super().__init__"

e) Se han desarrollado programas que instancien y utilicen objetos de las clases creadas anteriormente.
Efectivamente se desarrollo programas en los ejercicios de clases donde te posees varias instancias de una misma clase.

f) Se han utilizado mecanismos para controlar la visibilidad de las clases y de sus miembros.
Los mecanismos para controlar la visibilidad de las clases y sus miembros, no lo vimos en clases.

g) Se han definido y utilizado clases heredadas.
Como se respondio anteriormente, se aplicaron clases heredadas, sobre todo en los ejercicios de subunidad desarrollados.

h) Se han creado y utilizado métodos estáticos.
Los métodos estáticos no fueron desarrollados en clases.

i) Se han creado y utilizado conjuntos y librerías de clases.
En esta unidad no esta ese contenido.
```
