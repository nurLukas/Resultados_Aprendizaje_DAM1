SELECT
nombre,
precio,
precio > 500 AS 'Susceptible de descuento',
tipo,
tipo = 'Servicio' AS 'Es un servicio'
FROM servicios;