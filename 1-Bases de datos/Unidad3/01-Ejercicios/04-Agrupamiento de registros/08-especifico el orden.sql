SELECT
ciudad,
COUNT(cliente)
FROM pedidos2
GROUP BY ciudad
ORDER BY COUNT(cliente) DESC;


-- GROUP BY reúne los registros de cada ciudad.
-- COUNT(cliente) cuenta los valores no nulos de cada grupo.
-- ORDER BY ... DESC muestra primero las ciudades con más pedidos.