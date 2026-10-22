USE sturmprojekt;

CREATE VIEW vista_completa AS
SELECT
    pedidos.fecha_pedido AS 'fecha del pedido',
    pedidos.id_pedido AS 'numero de pedido',
    clientes.nombre AS 'nombre del cliente',
    clientes.apellidos AS 'apellidos del cliente',
    servicios.nombre AS 'nombre del producto',
    servicios.precio AS 'precio del producto'

FROM pedidos
LEFT JOIN clientes
    ON pedidos.id_cliente = clientes.Identificador
LEFT JOIN servicios
    ON pedidos.id_servicio = servicios.id_servicio;
