SELECT
    pedidos.fecha_pedido,
    pedidos.id_pedido,
    clientes.nombre,
    clientes.apellidos
FROM pedidos
LEFT JOIN clientes
ON pedidos.id_cliente = clientes.Identificador;


# El LEFT JOIN permite relacionar dos tablas mediante una columna común.