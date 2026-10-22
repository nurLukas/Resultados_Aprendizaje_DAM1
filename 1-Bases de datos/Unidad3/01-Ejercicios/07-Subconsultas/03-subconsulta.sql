SELECT
pedidos.fecha_pedido,
pedidos.id_cliente,
pedidos.precio_acordado,
pedidos.precio_acordado > (
    SELECT AVG(precio_acordado) FROM pedidos
) AS porencima
FROM pedidos;



-- La subconsulta calcula el importe medio de todos los pedidos.
-- La consulta principal compara cada importe con esa media.
-- porencima muestra 1 si la supera y 0 si no.