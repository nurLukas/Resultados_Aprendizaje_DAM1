'''
    ¿Qué significa Padding?
    En programación de interfaces, padding significa espacio de relleno.
    En tu código utilizas dos parámetros:
    - padx: espacio horizontal (izquierda y derecha).
    - pady: espacio vertical (arriba y abajo).
'''
import tkinter as tk    # importamos Tkinter

raiz = tk.Tk()          # creamos la ventana

# Agregar texto a la ventana
etiqueta = tk.Label(raiz, text="¡Hola mundo!", font=("Arial", 24)) # Aumenta el tamaño del texto (creamos la etiqueta)
etiqueta.pack(padx=20,pady=20)        # colocamos la etiqueta con espacio

boton = tk.Button(raiz,text="Pulsame si te atreves")   # creamos el botón
boton.pack(padx=20,pady=20)                            # colocamos el botón con espacio

raiz.mainloop() # no te salgas del bucle