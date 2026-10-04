# Aquí el código cambia porque el assert está dentro de un try
try:
	edad = 16
	assert edad > 17, "Debes ser mayor de edad"       # Python comprueba: 16 > 17, eso es False, así que assert genera un AssertionError.
except Exception as e:                                # El except captura la excepción en la variable "e" producida. Entonces se ejecutan las siguientes instrucciones.
	print("No puedes acceder al contenido, eres menor de edad.")
	print(e)                                          # Imprime el texto contenido en esa excepción.
	
print("Buscate algo adecuado a tu edad.")