import tkinter as tk

ventana = tk.Tk()

area = tk.Text(ventana)
area.pack(padx=20,pady=20)

area.insert("1.0", "Hola que tal")   # .insert()  Se utiliza para introducir texto en una posición concreta
                                     # "1.0"  En un componente Text, las posiciones pueden expresarse como línea.columna. Las líneas empiezan en 1 y las columnas en 0.
ventana.mainloop()


'''
    Estos seis archivos introducen varias instrucciones que aparecen continuamente en aplicaciones desarrolladas con Tkinter.
    Instrucción	    ¿Para qué sirve?
    tk.Tk()	        Crear la ventana principal
    tk.Label()	    Mostrar etiquetas
    tk.Entry()	    Crear entradas de una línea
    tk.Button()	    Crear botones
    tk.Text()	    Crear áreas de texto multilínea
    .pack()	        Colocar elementos en la ventana
    .get()	        Leer el contenido de un Entry
    .insert()	    Insertar contenido en una posición
    command=	    Asociar una función a un botón
    open()	        Abrir o crear un archivo
    .write()	    Escribir en un archivo
    .close()	    Cerrar el archivo
    .mainloop()	    Mantener activa la interfaz gráfica
'''