import tkinter as tk

def pulsaBoton():                            # Definimos una función
    print("Hola que tal, como estas")        # Mostramos un mensaje en la consola
    resultado.config(text="prueba superada") # Del resultado, configuro que su texto es X o lo que yo quiera ej: "prueba superada"

raiz = tk.Tk()                               #Creamos la ventana

# Agregar texto a la ventana
etiqueta = tk.Label(raiz, text="¡Hola mundo!", font=("Arial", 24))        # Aumenta el tamaño del texto. Creamos la primera etiqueta
etiqueta.pack(padx=20,pady=20)                                            # Colocamos la etiqueta

boton = tk.Button(raiz,text="Pulsame si te atreves",command=pulsaBoton)   # Creamos el botón
boton.pack(padx=20,pady=20)                                               # Colocamos el botón

resultado = tk.Label(raiz, text="x", font=("Arial", 24))                  # Creamos la etiqueta del resultado
resultado.pack(padx=20,pady=20)                                           # Colocamos la etiqueta del resultado

raiz.mainloop() # no te salgas del bucle