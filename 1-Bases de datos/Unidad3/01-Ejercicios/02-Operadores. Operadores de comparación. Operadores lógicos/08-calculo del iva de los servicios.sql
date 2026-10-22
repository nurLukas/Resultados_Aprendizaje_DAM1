SELECT
nombre AS 'Nombre del servicio',
precio AS 'Precio del servicio',
precio * 0.21 AS 'IVA 21%'
FROM servicios;




-- 

SELECT
nombre AS 'Nombre del servicio',
precio AS 'Precio del servicio',
precio * 0.21 AS 'IVA 21%'
precio + precio * 0,21 AS 'Total precio más IVA'
FROM servicios;