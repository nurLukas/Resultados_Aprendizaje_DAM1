import tkinter as tk

ventana = tk.Tk()
ventana.title("Mantenimiento de mi coche")

titulo = tk.Label(
    ventana,
    text="Registro de mantenimiento",
    font=("Arial", 18)
)
titulo.pack(padx=20, pady=20)

ventana.mainloop()