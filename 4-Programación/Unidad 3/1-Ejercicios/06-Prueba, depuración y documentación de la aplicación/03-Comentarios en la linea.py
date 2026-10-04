'''
    Programa gestor basico 
    Diseñado por nurLukas de Sturmprojekt
    v 0.2
    Changelog:
    0.1 - CRUD básico con menú
    0.2 - Añadido funcionalidad a las opciones del if
    Entrada: usuario mediante input en consola
    Salida: print mediante consola
'''

# Saludo - Antes de comenzar, introduzco un print de bievenida, con informacion de versionado y autor.
print("-"*42)
print("Programa gestor de proyectos v0.2")
print("Diseñado por Sturmprojekt")
print("¡Bienvenido!")
print("-"*42)

# Ahora entramos en un menu infinito de tal forma que la aplicación repite su ejecución
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

# Tratamiento de las opciones   
    if opcion == "1":                                           # Esto es lo que va a ocurrir cuando el usuario use la opción 1                                         
        print("Vamos a crear el proyecto")
    if opcion == "2":                                           # Esto es lo que va a ocurrir cuando el usuario use la opción 2
        print("Te listo los proyectos")
    if opcion == "3":                                           # Esto es lo que va a ocurrir cuando el usuario use la opción 3
        print("Selecciona el proyecto que quieres actualizar")
    if opcion == "4":                                           # Esto es lo que va a ocurrir cuando el usuario use la opción 4
        print("Selecciona el proyecto que quieres eliminar")
    if opcion == "5":                                           # Esto es lo que va a ocurrir cuando el usuario use la opción 5
        print("Cerrando el gestor")
        break