SELECT
anio,
ciudad,
COUNT(cliente)
FROM pedidos2
GROUP BY anio, ciudad
ORDER BY anio ASC;


-- GROUP BY crea un grupo por cada combinación de año y ciudad.
-- COUNT(cliente) cuenta los valores no nulos de cada grupo.
-- ORDER BY anio ASC muestra primero el año menor.