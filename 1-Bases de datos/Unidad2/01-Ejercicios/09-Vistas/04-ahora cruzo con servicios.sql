SELECT
    pedidos.fecha_pedido,
    pedidos.id_pedido,
    clientes.nombre,
    clientes.apellidos,
    servicios.nombre AS producto,
    servicios.precio

FROM pedidos
LEFT JOIN clientes
    ON pedidos.id_cliente = clientes.Identificador
LEFT JOIN servicios
    ON pedidos.id_servicio = servicios.id_servicio;
