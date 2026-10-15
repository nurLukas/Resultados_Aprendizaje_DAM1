import pickle                             # Esto permite utilizar las funciones de pickle.

frutas = ['manzana', 'pera', 'platano']   # Creamos la lista

archivo = open('frutas.dat', 'wb')        # Abrimos un archivo binario
pickle.dump(frutas, archivo)              # Guardamos la lista


'''
    ¿Qué es pickle?
    pickle es un módulo de Python que permite guardar objetos de Python en archivos y recuperarlos posteriormente.
    Por ejemplo, puedes guardar listas, diccionarios y otros objetos compatibles.
'''