try:
    # Pedimos los datos al usuario
    dividendo = int(input("Introduce el dividendo: "))
    divisor = int(input("Introduce el divisor: "))

    # Calculamos y mostramos la división
    division = dividendo / divisor
    print(division)

except Exception as e:
    # Capturamos el error para que el programa no se cierre
    print("Ha ocurrido un error pero continuamos:", e)

# El programa sigue ejecutándose después del try/except
print("El programa continúa")