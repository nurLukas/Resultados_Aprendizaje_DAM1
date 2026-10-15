import tkinter as tk

ventana = tk.Tk()

area = tk.Text(ventana)           # Text crea un espacio para escribir textos de varias líneas.
area.pack(padx=20,pady=20)

ventana.mainloop()


'''
    La diferencia fundamental entre Entry y Text es que Entry está pensado para datos cortos de una sola línea, mientras que Text permite introducir párrafos enteros.
'''