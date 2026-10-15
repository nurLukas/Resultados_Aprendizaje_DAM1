import tkinter as tk                    # Importamos Tkinter

def pulsaBoton():                       # Definimos una función
    print("Hola que tal, como estas")   # Instrucción dentro de la función

raiz = tk.Tk()                          # Creamos la ventana

# Agregar texto a la ventana
etiqueta = tk.Label(raiz, text="¡Hola mundo!", font=("Arial", 24)) # Aumenta el tamaño del texto (Creamos una etiquet)
etiqueta.pack(padx=20,pady=20)          # Colocamos la etiqueta

boton = tk.Button(raiz,text="Pulsame si te atreves",command=pulsaBoton)
boton.pack(padx=20,pady=20)             # Colocamos el botón

raiz.mainloop()                         # no te salgas del bucle (Mantenemos la ventana abierta)