import json

print("Datos de mi coche")

archivo = open("coche.json", "r")
coche = json.load(archivo)
archivo.close()

print("Marca:", coche["marca"])
print("Modelo:", coche["modelo"])
print("Matrícula:", coche["matricula"])

'''
    Aquí no usamos split(): json.load() interpreta la estructura del archivo por nosotros.
'''