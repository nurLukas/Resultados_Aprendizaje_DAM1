'''
	Guardaremos una lista en formato binario con pickle
'''

import pickle                            # permite guardar y recuperar objetos de Python, como listas.

mantenimiento = ["2026-10-12", "125000", "Cambio de aceite", "85.50"]

archivo = open("copia.dat", "wb")       # "wb" significa escribir (w) en formato binario (b). Si el archivo existe, sobrescribe su contenido.
pickle.dump(mantenimiento, archivo)     # pickle.dump(mantenimiento, archivo) guarda la lista en el archivo.
archivo.close()

print("Copia guardada")