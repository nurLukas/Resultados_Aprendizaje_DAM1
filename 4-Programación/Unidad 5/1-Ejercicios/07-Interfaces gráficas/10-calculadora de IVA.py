'''
    Hasta ahora hemos aprendido a crear ventanas, mostrar textos, añadir botones, ejecutar funciones y recoger información con Entry.
    En este archivo vamos a juntar todos esos conocimientos para crear una calculadora de IVA del 21 %.
'''
import tkinter as tk

def calculaIVA():                     # Creamos una función
  basenumero = base.get()             # Obtenemos el número escrito por el usuario
  basenumero = float(basenumero)      # Convertimos el texto en número
  iva = basenumero*0.21               # Calculamos el IVA
  resultado.config(text=iva)          # Mostramos el resultado en la ventana

ventana = tk.Tk()                     # Creamos la ventana

base = tk.Entry(ventana)              # Creamos el campo para introducir números
base.pack(padx=20,pady=20)            # Colocamos el campo

boton_calcula = tk.Button(ventana,text="Calcula!",command=calculaIVA)    # Creamos el botón de calcular
boton_calcula.pack(padx=20,pady=20)                                      # Colocamos el botón

resultado = tk.Label(ventana,text="resultado")                           # Creamos la etiqueta para mostrar el resultado
resultado.pack(padx=20,pady=20)                                          # Colocamos la etiqueta

ventana.mainloop()                                                       # Mantenemos la ventana abierta