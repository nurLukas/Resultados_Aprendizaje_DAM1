import tkinter as tk

def guardar():
    archivo = open("mantenimiento.csv", "a")
    texto = fecha.get() + "|" + kilometraje.get() + "|" + detalle.get() + "|" + coste.get() + "\n"
    archivo.write(texto)
    archivo.close()

    resultado.config(text="Mantenimiento guardado")
    
def listar():
    archivo = open("mantenimiento.csv", "r")
    lineas = archivo.readlines()
    archivo.close()

    area.delete("1.0", tk.END)

    for linea in lineas:
        datos = linea.strip().split("|")

        area.insert(tk.END, "Fecha: " + datos[0] + "\n")
        area.insert(tk.END, "Kilometraje: " + datos[1] + "\n")
        area.insert(tk.END, "Detalle: " + datos[2] + "\n")
        area.insert(tk.END, "Coste: " + datos[3] + "\n")
        area.insert(tk.END, "------------------------------\n")

ventana = tk.Tk()
ventana.title("Mantenimiento de mi coche")

titulo = tk.Label(
    ventana,
    text="Registro de mantenimiento",
    font=("Arial", 18)
)
titulo.pack(padx=20, pady=20)

tk.Label(ventana, text="Fecha").pack()
fecha = tk.Entry(ventana)
fecha.pack(padx=20, pady=5)

tk.Label(ventana, text="Kilometraje").pack()
kilometraje = tk.Entry(ventana)
kilometraje.pack(padx=20, pady=5)

tk.Label(ventana, text="Detalle del mantenimiento").pack()
detalle = tk.Entry(ventana)
detalle.pack(padx=20, pady=5)

tk.Label(ventana, text="Coste").pack()
coste = tk.Entry(ventana)
coste.pack(padx=20, pady=5)

# Boton guardar
boton_guardar = tk.Button(
    ventana,
    text="Guardar mantenimiento",
    command=guardar
)
boton_guardar.pack(padx=20, pady=10)

resultado = tk.Label(ventana, text="")
resultado.pack(padx=20, pady=5)

boton_listar = tk.Button(
    ventana,
    text="Listar mantenimientos",                 # Pulsa Listar dos veces: el contenido no debe duplicarse, porque primero vaciamos el area.
    command=listar
)
boton_listar.pack(padx=20, pady=10)

area = tk.Text(ventana, width=55, height=12)
area.pack(padx=20, pady=10)

ventana.mainloop()

