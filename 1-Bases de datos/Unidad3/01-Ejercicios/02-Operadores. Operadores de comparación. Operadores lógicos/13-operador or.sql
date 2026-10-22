SELECT
nombre,
precio,
precio > 500 AS 'Caro',
tipo,
tipo = 'Servicio' AS 'Es un servicio',
precio * (precio > 500 OR tipo = 'Servicio') * 0.1 AS 'Descuento'
FROM servicios;