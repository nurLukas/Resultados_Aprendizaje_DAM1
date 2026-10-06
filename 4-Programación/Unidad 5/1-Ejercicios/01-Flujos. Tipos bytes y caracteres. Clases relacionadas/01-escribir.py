archivo = open("test.txt",'w')                                # 'w' Indica que a abrimos el archivo especificado, en modo escritura
archivo.write("El contenido de esta unidad, esta muy guay")   # Esto es lo que escribimos en el archivo externo abierto previamente
archivo.close()                                               # Cerrar el arcvhi es una buena practica que debemos tener siempre