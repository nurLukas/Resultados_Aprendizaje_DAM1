-- PROYECTO FINAL DE LA UNIDAD 3
-- Tienda de servicios Sturmprojekt.
-- Utilizamos las tablas y los datos existentes.

USE sturmprojekt;

-- 1. Consultamos el catálogo completo.
SELECT * FROM servicios;

-- 2. Seleccionamos columnas y utilizamos alias.
SELECT
nombre AS 'Nombre del servicio',
precio AS 'Precio del servicio'
FROM servicios;

-- 3. Ordenamos los precios en ambos sentidos.
SELECT nombre, precio
FROM servicios
ORDER BY precio ASC;

SELECT nombre, precio
FROM servicios
ORDER BY precio DESC;

-- 4. Operaciones aritméticas sobre los precios.
-- Solo calculan resultados: no cambian los datos.
SELECT
nombre,
precio,
precio + 20 AS suma,
precio - 20 AS resta,
precio * 20 AS multiplicacion,
precio / 20 AS division,
precio * 0.21 AS cuota_iva
FROM servicios;

-- 5. Comparaciones y operadores lógicos.
SELECT
nombre,
precio,
tipo,
precio > 500 AS caro,
tipo = 'Servicio' AS es_servicio,
precio * (precio > 500 AND tipo = 'Servicio') * 0.1
AS descuento_and,
precio * (precio > 500 OR tipo = 'Servicio') * 0.1
AS descuento_or
FROM servicios;

-- 6. Consultas resumen de los pedidos.
SELECT COUNT(id_cliente) FROM pedidos;
SELECT SUM(precio_acordado) FROM pedidos;
SELECT AVG(precio_acordado) FROM pedidos;
SELECT MAX(precio_acordado) FROM pedidos;
SELECT MIN(precio_acordado) FROM pedidos;

-- 7. Agrupamos los pedidos por estado y ordenamos el recuento.
SELECT
estado,
COUNT(id_cliente)
FROM pedidos
GROUP BY estado
ORDER BY COUNT(id_cliente) DESC;

-- 8. Relacionamos pedidos y clientes.
SELECT
pedidos.fecha_pedido,
clientes.nombre,
clientes.apellidos
FROM pedidos
LEFT JOIN clientes
ON pedidos.id_cliente = clientes.Identificador;

-- 9. Añadimos el servicio contratado.
SELECT
pedidos.fecha_pedido,
clientes.nombre,
clientes.apellidos,
servicios.nombre,
pedidos.precio_acordado
FROM pedidos
LEFT JOIN clientes
ON pedidos.id_cliente = clientes.Identificador
LEFT JOIN servicios
ON pedidos.id_servicio = servicios.id_servicio;

-- 10. Subconsulta: comparamos cada pedido con el promedio.
SELECT
fecha_pedido,
id_cliente,
precio_acordado,
precio_acordado > (
    SELECT AVG(precio_acordado) FROM pedidos
) AS porencima
FROM pedidos;

-- 11. Índices creados durante las prácticas de la Unidad 3.
-- No se ejecutan otra vez porque ya existen.
-- No hemos medido su efecto sobre el rendimiento.

/*
CREATE INDEX idx_servicios_precio
ON servicios(precio);

CREATE INDEX idx_pedidos_fecha
ON pedidos(fecha_pedido);
*/