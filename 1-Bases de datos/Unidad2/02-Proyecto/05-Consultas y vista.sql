USE sturmprojekt;

-- Cada pedido, con su cliente y servicio.
SELECT p.id_pedido, p.fecha_pedido, c.nombre, c.apellidos,
       s.nombre AS servicio, s.precio AS precio_catalogo, p.precio_acordado
FROM pedidos AS p
LEFT JOIN clientes AS c ON p.id_cliente = c.Identificador
LEFT JOIN servicios AS s ON p.id_servicio = s.id_servicio
ORDER BY p.id_pedido;

-- Conserva todos los clientes, incluso sin pedidos.
-- El cliente 3 debe aparecer con columnas de pedido y servicio a NULL.
SELECT c.Identificador, c.nombre, p.id_pedido, s.nombre AS servicio
FROM clientes AS c
LEFT JOIN pedidos AS p ON c.Identificador = p.id_cliente
LEFT JOIN servicios AS s ON p.id_servicio = s.id_servicio
ORDER BY c.Identificador, p.id_pedido;

CREATE VIEW vista_completa AS
SELECT p.fecha_pedido, p.id_pedido, c.nombre AS nombre_cliente,
       c.apellidos AS apellidos_cliente, s.nombre AS nombre_servicio,
       s.precio AS precio_catalogo, p.precio_acordado, p.estado
FROM pedidos AS p
LEFT JOIN clientes AS c ON p.id_cliente = c.Identificador
LEFT JOIN servicios AS s ON p.id_servicio = s.id_servicio;

SELECT * FROM vista_completa ORDER BY id_pedido;
