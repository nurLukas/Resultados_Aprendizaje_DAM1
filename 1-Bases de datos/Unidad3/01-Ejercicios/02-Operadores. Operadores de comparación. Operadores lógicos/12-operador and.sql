SELECT
nombre,
precio,
precio > 500 AS 'Caro',
tipo,
tipo = 'Servicio' AS 'Es un servicio',
precio * (precio > 500 AND tipo = 'Servicio') * 0.1 AS 'Descuento'
FROM servicios;