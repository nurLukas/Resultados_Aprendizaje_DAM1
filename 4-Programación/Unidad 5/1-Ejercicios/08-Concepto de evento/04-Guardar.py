'''
    Este es el archivo introduce una función que permite guardar la información de los proyectos.
'''
import tkinter as tk

ventana = tk.Tk()

def guardar():                                                            # Definimos función guardar
    archivo = open("proyectos.csv",'a')                                   # Abrir el archivo en modo append
    texto = nombre.get()+","+apellidos.get()+","+email.get()+"\n"         # Recuperar lo que ha escrito el usuario
    archivo.write(texto)
    archivo.close()                                                       # Cerrar el archivo

tk.Label(ventana, text="Nombre del proyecto").pack()
nombre = tk.Entry(ventana)
nombre.pack(padx=20, pady=20)

tk.Label(ventana, text="Descripcion").pack()
apellidos = tk.Entry(ventana)
apellidos.pack(padx=20, pady=20)

tk.Label(ventana, text="Cliente").pack()
email = tk.Entry(ventana)
email.pack(padx=20, pady=20)

boton = tk.Button(ventana, text="Guardar proyecto",command=guardar)
boton.pack(padx=20, pady=20)

ventana.mainloop()