# Concesionario de coches

- Coche	(Representa una tabla)
	-Id
	-Modelo - string
	-Marca - string
	-Año - int
	-Matricula - string
	-Número de bastidor - string
	-Color - string
	-Precio - float
	
- Clientes	(Representa otra tabla)
	-Id
	-Nombre
	-Apellidos
	-DNI 1:1
	-Fecha de nacimiento 1:1
	-Número de teléfono 1:n
	-correo electronico 1:n
	
- Pedidos	(Representa otra tabla más)
	-Número de pedido
	-Fecha de pedido
	-Id cliente FK
	-Id coche FK
	
	