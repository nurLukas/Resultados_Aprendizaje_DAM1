import tkinter as tk

raiz = tk.Tk()

# Agregar texto a la ventana
etiqueta = tk.Label(raiz, text="¡Hola mundo!")
etiqueta.pack()

raiz.mainloop() # no te salgas del bucle

'''
    tk.Label() crea una etiqueta para mostrar información.
    - raiz: indica la ventana donde estará.
    - text="¡Hola mundo!": define su contenido.
    - .pack(): coloca el elemento dentro de la ventana.
'''