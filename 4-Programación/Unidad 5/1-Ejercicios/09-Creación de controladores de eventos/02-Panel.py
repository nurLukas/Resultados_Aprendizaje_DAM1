'''
    Este archivo añade un concepto muy importante: los contenedores Frame.
    En lugar de colocar todos los elementos directamente sobre la ventana, podemos organizarla en diferentes secciones.
'''
import tkinter as tk

ventana = tk.Tk()

insertar = tk.Frame(ventana)       # Crea un contenedor llamado insertar. Un Frame es una zona de la interfaz que permite agrupar elementos gráficos.
insertar.grid(row=0,column=0)      # Coloca el panel insertar en la primera fila y primera columna de la ventana.
leer = tk.Frame(ventana)           # Crea un segundo contenedor llamado leer.
leer.grid(row=0,column=1)          # Coloca el panel leer en la primera fila y segunda columna.

tk.Label(insertar,text="Insertar").pack(padx=20,pady=20)    # Crea una etiqueta dentro del panel insertar.
tk.Label(leer,text="Leer").pack(padx=20,pady=20)            # Crea una etiqueta con el texto "Leer" dentro del segundo panel

ventana.mainloop()                                          # Inicia el bucle principal de eventos, manteniendo la ventana abierta y respondiendo a las interacciones.