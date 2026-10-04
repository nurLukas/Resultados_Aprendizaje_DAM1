clientes = []                           # Variable de tipo "lista", vacia.

clientes.append("Juan") # 0             # Insertamos - la clave es append
clientes.append("Jorge") # 1            # Insertamos - la clave es append

# Ahora Los índices son: [0] Juan
#                        [1] Jorge


print(clientes)                         # Leemos - Seleccionamos - la clave es print

clientes[1] = "Jaime"                   # Actualizamos - Update, (En la posición 1, reemplaza el valor actual por "Jaime".)

# Ahora Los índices son: [0] Juan
#                        [1] Jaime


print(clientes)


clientes.pop(1)                                                   # Elimina el elemento que está en la posición "1"  (Jaime)

# clientes.remove("Jaime") ---> alternativa a clientes.pop(1), ---> Elimina buscando el valor "Jaime"

print(clientes)