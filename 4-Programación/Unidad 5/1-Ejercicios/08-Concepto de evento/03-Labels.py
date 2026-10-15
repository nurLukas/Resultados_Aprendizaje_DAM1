'''
    Este archivo mejora la interfaz anterior utilizando Label.
'''
import tkinter as tk

ventana = tk.Tk()

tk.Label(ventana, text="Nombre del proyecto").pack()       # tk.Label() crea una etiqueta que muestra información en pantalla.
nombre = tk.Entry(ventana)
nombre.pack(padx=20, pady=20)

tk.Label(ventana, text="Descripcion").pack()
apellidos = tk.Entry(ventana)
apellidos.pack(padx=20, pady=20)

tk.Label(ventana, text="Cliente").pack()
email = tk.Entry(ventana)
email.pack(padx=20, pady=20)

boton = tk.Button(ventana, text="Guardar proyecto")
boton.pack(padx=20, pady=20)

ventana.mainloop()


'''
    una interfaz gráfica no consiste únicamente en introducir información, sino también en indicar claramente qué debe escribir el usuario en cada campo.
    Componente	Función
    Label	    Mostrar texto informativo
    Entry	    Permitir escribir texto
    Button	    Ejecutar una acción cuando se pulsa, si tiene una función asociada
    El archivo utiliza tres etiquetas: Nombre, Apellidos y Email.
'''