'''
    Programa para documentación y registro detallado del mantenimiento del coche.
    Permite introducir fecha, kilometraje, detalle y coste, guardar cada mantenimiento en un CSV y consultar los registros desde una ventana.
'''
print("-"*45)
print("Programa para documentación y registro")
print("del mantenimiento de tu coche")
print("Desarrollado por nurLukas de Sturmprojekt")
print("Poder en cada proyecto!")
print("-"*45)

import tkinter as tk

archivo = open("mantenimiento.csv", "a")
archivo.close()

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

formulario = tk.Frame(ventana)
formulario.grid(row=0, column=0, padx=20, pady=20)

listado = tk.Frame(ventana)
listado.grid(row=0, column=1, padx=20, pady=20)

titulo = tk.Label(
    formulario,
    text="Registro de mantenimiento",
    font=("Arial", 18)
)
titulo.pack(padx=20, pady=20)

tk.Label(formulario, text="Fecha").pack()
fecha = tk.Entry(formulario)
fecha.pack(padx=20, pady=5)

tk.Label(formulario, text="Kilometraje").pack()
kilometraje = tk.Entry(formulario)
kilometraje.pack(padx=20, pady=5)

tk.Label(formulario, text="Detalle del mantenimiento").pack()
detalle = tk.Entry(formulario)
detalle.pack(padx=20, pady=5)

tk.Label(formulario, text="Coste").pack()
coste = tk.Entry(formulario)
coste.pack(padx=20, pady=5)

boton_guardar = tk.Button(
    formulario,
    text="Guardar mantenimiento",
    command=guardar
)
boton_guardar.pack(padx=20, pady=10)

resultado = tk.Label(formulario, text="")
resultado.pack(padx=20, pady=5)

boton_listar = tk.Button(
    listado,
    text="Listar mantenimientos",
    command=listar
)
boton_listar.pack(padx=20, pady=10)

area = tk.Text(listado, width=55, height=12)
area.pack(padx=20, pady=10)

ventana.mainloop()