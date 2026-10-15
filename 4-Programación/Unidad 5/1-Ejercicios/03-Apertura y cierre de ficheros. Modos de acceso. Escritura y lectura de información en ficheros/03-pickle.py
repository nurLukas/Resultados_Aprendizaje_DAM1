frutas = ['manzana','pera','platano']    # Creamos una lista llamada frutas con tres elementos.

archivo = open("frutas.txt",'w')         # Creamos o abrimos un archivo de texto llamado frutas.txt para escribir información.
archivo.write(str(frutas))
archivo.close()

'''
    str(frutas) convierte la lista en una cadena de texto.
    Pero hay un inconveniente: cuando recuperes la información, será texto, no una lista de Python.
    Y precisamente para solucionar esto aparece pickle.
'''