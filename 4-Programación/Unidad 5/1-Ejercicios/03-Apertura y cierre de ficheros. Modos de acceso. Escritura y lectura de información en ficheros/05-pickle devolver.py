import pickle                        # Importamos pickle

frutas = []                          # Creamos una lista vacía

archivo = open('frutas.dat', 'rb')   # Abrimos el archivo para leer
frutas = pickle.load(archivo)        # Recuperamos los datos
print(frutas)                        # Mostramos el resultado
archivo.close()                      # Cerramos el archivo


'''
    Diferencia entre dump() y load()
    pickle.dump()	Guarda	Pasar un objeto de Python a un archivo
    pickle.load()	Recupera	Pasar los datos del archivo a un objeto de Python
'''