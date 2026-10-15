'''
    En lugar de mostrar una ventana vacía, presenta tres campos de entrada y un botón.
'''
import tkinter as tk

ventana = tk.Tk()

nombre = tk.Entry(ventana)                            # tk.Entry() crea una caja donde el usuario puede escribir texto en una sola línea.
nombre.pack(padx=20,pady=20)

apellidos = tk.Entry(ventana)
apellidos.pack(padx=20,pady=20)

email = tk.Entry(ventana)
email.pack(padx=20,pady=20)

boton = tk.Button(ventana,text="Guardar proyecto")    # Crea un botón con el texto «Guardar proyecto».
boton.pack(padx=20,pady=20)

ventana.mainloop()