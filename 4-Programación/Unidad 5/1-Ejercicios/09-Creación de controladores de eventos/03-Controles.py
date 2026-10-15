'''
    Ahora no solamente tenemos dos paneles, sino que incorporamos un formulario en el que el usuario puede escribir información.
'''
import tkinter as tk                                        # Importa Tkinter.

ventana = tk.Tk()                                           # Crea la ventana principal.

insertar = tk.Frame(ventana)                                # Crea el panel izquierdo.
insertar.grid(row=0,column=0)                               # Lo coloca en la columna 0.
leer = tk.Frame(ventana)                                    # Crea el panel derecho.
leer.grid(row=0,column=1)                                   # Lo coloca en la columna 1.

tk.Label(insertar,text="Insertar").pack(padx=20,pady=20)    # Crea el título "Insertar" dentro del panel izquierdo, con un espacio exterior de 20 píxeles alrededor.

tk.Label(insertar, text="Nombre").pack()                    # Crea una etiqueta con el texto "Nombre".
nombre = tk.Entry(insertar)                                 # Entry es un cuadro de texto de una sola línea.   # Permite al usuario escribir un nombre, un apellido, un correo electrónico u otro valor.
nombre.pack(padx=20, pady=20)                               

tk.Label(insertar, text="Apellidos").pack()
apellidos = tk.Entry(insertar)
apellidos.pack(padx=20, pady=20)

tk.Label(insertar, text="Email").pack()
email = tk.Entry(insertar)
email.pack(padx=20, pady=20)

boton = tk.Button(insertar, text="Guardar contacto")
boton.pack(padx=20, pady=20)

tk.Label(leer,text="Leer").pack(padx=20,pady=20)

area = tk.Text(leer)
area.pack(padx=20,pady=20)

ventana.mainloop()