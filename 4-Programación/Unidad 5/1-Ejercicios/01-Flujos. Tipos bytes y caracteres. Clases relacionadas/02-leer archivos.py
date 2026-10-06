archivo = open("test.txt",'r')      # Abrimos el archivo en modo lectura
lector = archivo.readlines()        # guarda todas sus líneas en una lista con readlines()
print(lector)                       # muestra esa lista
archivo.close()                     # Cerramos el archivo