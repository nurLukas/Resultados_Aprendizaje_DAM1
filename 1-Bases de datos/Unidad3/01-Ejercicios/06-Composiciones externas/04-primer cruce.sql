SELECT
pedidos.fecha_pedido,
pedidos.id_cliente,
pedidos.id_servicio,
clientes.nombre,
clientes.apellidos,
clientes.email
FROM pedidos
LEFT JOIN clientes
ON pedidos.id_cliente = clientes.Identificador;



-- LEFT JOIN conserva todos los pedidos.
-- ON relaciona id_cliente con Identificador de clientes.
-- Añadimos el nombre, los apellidos y el email del cliente.
-- Si no hubiera coincidencia, esos campos aparecerían como NULL.