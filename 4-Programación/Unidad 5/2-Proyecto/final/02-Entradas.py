import tkinter as tk

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

ventana.mainloop()

