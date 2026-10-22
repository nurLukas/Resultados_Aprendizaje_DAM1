USE sturmprojekt;

-- Ejecutar una sola vez, tras 03 y 04, con las tablas vacias.
START TRANSACTION;
INSERT INTO clientes (nombre, apellidos, email, proyecto, Identificador) VALUES
('Lucas Ezequiel', 'Andrés Griego', 'admin@jsturmprojekt.es', 'Plataforma completa', 1),
('Juan', 'García López', 'juan@garcia.com', 'Plataforma básica', 2),
('Sofía', 'Romero García', 'sofia.romero@example.com', 'Proyecto en estudio', 3);

INSERT INTO servicios (id_servicio, nombre, tipo, descripcion, precio) VALUES
(1, 'Plataforma Básica', 'Producto', 'Desarrollo web básico', 250.00),
(2, 'Plataforma Completa', 'Producto', 'Desarrollo web completo', 350.00),
(3, 'Landing Web', 'Producto', 'Página web estática', 150.00),
(4, 'Gestión de dominio/Despliegue', 'Servicio', 'Configuración de dominio, DNS, hosting y despliegue web', 35.00),
(5, 'Mantenimiento + Servicio Técnico', 'Servicio', 'Mantenimiento, incidencias y soporte técnico', 35.00);

INSERT INTO pedidos (id_pedido, id_cliente, id_servicio, fecha_pedido, estado, precio_acordado) VALUES
(1, 1, 2, '2026-10-01', 'En desarrollo', 350.00),
(2, 1, 4, '2026-10-02', 'Finalizado', 35.00),
(3, 2, 1, '2026-10-03', 'Pendiente', 240.00);

SELECT * FROM clientes;
SELECT * FROM servicios;
SELECT * FROM pedidos;
