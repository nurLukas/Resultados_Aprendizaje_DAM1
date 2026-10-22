SELECT
pedidos.fecha_pedido,
pedidos.id_cliente,
pedidos.id_servicio,
clientes.nombre,
clientes.apellidos,
clientes.email,
servicios.nombre,
servicios.tipo
FROM pedidos
LEFT JOIN clientes
ON pedidos.id_cliente = clientes.Identificador
LEFT JOIN servicios
ON pedidos.id_servicio = servicios.id_servicio;


-- El primer LEFT JOIN relaciona pedidos con clientes.
-- El segundo LEFT JOIN relaciona pedidos con servicios.