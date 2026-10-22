SELECT
nombre AS 'Nombre del servicio',
precio AS 'Base imponible',
precio > 500 AS 'Candidato',
precio * (precio > 500) * 0.1 AS 'Descuento',
precio - precio * (precio > 500) * 0.1 AS 'Total final'
FROM servicios;