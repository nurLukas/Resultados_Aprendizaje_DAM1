import pickle

archivo = open("copia.dat", "rb")       # "rb" abre el archivo para leer (r) en formato binario (b).
mantenimiento = pickle.load(archivo)    # pickle.load(archivo) recupera el objeto guardado.  mantenimiento recibe la lista recuperada.
archivo.close()

print(mantenimiento)