'''
    En este archivo estás aprendiendo a crear botones en una ventana de Python utilizando Tkinter.
'''
import tkinter as tk     # Importar Tkinter

raiz = tk.Tk()           # Crear la ventana

# Agregar texto a la ventana
etiqueta = tk.Label(raiz, text="¡Hola mundo!", font=("Arial", 24)) # Aumenta el tamaño del texto
etiqueta.pack()          # Mostrar la etiqueta

boton = tk.Button(raiz,text="Pulsame si te atreves")
boton.pack()             # Colocar el botón

raiz.mainloop() # no te salgas del bucle