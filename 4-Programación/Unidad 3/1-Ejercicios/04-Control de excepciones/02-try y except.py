try:                             # Significa aproximadamente: “Intenta ejecutar este código.”
  division = 10/0                # Dentro del try, tenemos esta división que puede provocar el error.
  print(division)
except Exception as e:           # Significa: “Si ocurre un error, en lugar de detener el programa, entra aquí.”
  print("Ha ocurrido un error pero continuamos:", e)       # La variable e guarda información sobre el error que ha ocurrido.

print("Pero es que yo quiero que mi programa siga funcionando")        # Lo importante es que el programa no termina ahí. Después continúa y ejecuta el último print.