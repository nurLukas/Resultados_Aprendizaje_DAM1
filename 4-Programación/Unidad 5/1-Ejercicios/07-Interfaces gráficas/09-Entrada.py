import tkinter as tk

raiz = tk.Tk()                  # Creamos la ventana principal

entrada = tk.Entry(raiz)        # Creamos un campo de entrada
entrada.pack(padx=20,pady=20)   # Colocamos el campo en la ventana

raiz.mainloop()                 # no te salgas del bucle