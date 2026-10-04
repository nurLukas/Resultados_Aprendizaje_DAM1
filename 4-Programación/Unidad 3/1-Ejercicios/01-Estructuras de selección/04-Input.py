temperatura = input("Dime la temperatura, del entorno de trabajo: ")   # Aplicamos por primera vez un input

temperatura = int(temperatura)                                     # Conversión explícita.--> input() siempre devuelve un str, entonces con este movimiento transformamos la información de srt a int.

if temperatura <= 20:
    print("Que fresquito, así da gusto.")
elif temperatura <= 25 and temperatura:
    print("Aún se esta bien")
elif temperatura > 25 and temperatura < 31:
    print("Está comenzando a hacer calor")
elif temperatura >= 31 and temperatura < 36:
    print("Que calor hace!")
else:
	print("¡Esto parace un infierno!")