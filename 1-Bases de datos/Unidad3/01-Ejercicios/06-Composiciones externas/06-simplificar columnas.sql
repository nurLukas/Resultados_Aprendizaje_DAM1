SELECT
pedidos.fecha_pedido,
clientes.nombre,
clientes.apellidos,
servicios.nombre
FROM pedidos
LEFT JOIN clientes
ON pedidos.id_cliente = clientes.Identificador
LEFT JOIN servicios
ON pedidos.id_servicio = servicios.id_servicio;