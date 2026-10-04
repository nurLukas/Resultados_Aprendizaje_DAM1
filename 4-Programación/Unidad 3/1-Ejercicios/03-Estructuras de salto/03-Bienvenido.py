# Cabecera de presentación
print("-"*42)
print("Programa gestor de proyectos v0.1")
print("Diseñado por Sturmprojekt")
print("¡Bienvenido!")
print("-"*42)

# Bucle infinito con el CRUD
print("-"*42)
while True:
    print("Tienes las siguientes opciones:")
    print("1- Crear proyecto")
    print("2- Listar proyectos")
    print("3- Actualizar/editar proyecto")
    print("4- Eliminar proyecto")
    print("5- Salir del programa")
    print("-"*42)
    opcion = input("Selecciona y escribe la opción deseada: ")
    print("-"*42)
    
# Tratamiento de las opciones seleccionadas
    if opcion == "1":
        print("Vamos a crear el proyecto")
    if opcion == "2":
        print("Te listo los proyectos")
    if opcion == "3":
        print("Selecciona el proyecto que quieres actualizar")
    if opcion == "4":
        print("Selecciona el proyecto que quieres eliminar")
    if opcion == "5":
        print("Cerrando el gestor")
        break
        
# "Estructuras de salto". Es este programa gestor, se demuestra como saltamos de bloque en bloque, dentro de su estructura.