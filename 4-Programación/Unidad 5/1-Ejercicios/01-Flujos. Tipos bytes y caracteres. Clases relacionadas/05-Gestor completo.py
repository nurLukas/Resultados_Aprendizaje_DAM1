'''
    Implementacion de lectura y escritura.
'''

print("-"*45)                                          # Detalle estetico.
print("Programa gestor de proyectos v0.2")             # Cabecera de presentación.
print("Desarrollado por nurLukas de Sturmprojekt")     # Cabecera de presentación.
print("-"*45) 

while True:
  print("-"*30)
  print("Selecciona una opcion")
  print("1.-Introduce un registro")
  print("2.-Selecciona los registros")
  opcion = input("Escoge una opción: ")
  print("-"*30)
  if opcion == "1":
    archivo = open("agenda.txt",'a')
    nombre = input("Ahora introduce el nuevo nombre: ")
    archivo.write(nombre+"\n")
    archivo.close()
  elif opcion == "2":
    archivo = open("agenda.txt",'r')
    lineas = archivo.readlines()
    for linea in lineas:
      print(linea)
    archivo.close()