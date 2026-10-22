-- Datos de ejemplo agregador previamente en unidad 2



-- ============================================
-- Clientes             
-- ============================================
INSERT INTO clientes
(nombre, apellidos, email, proyecto)VALUES
('Ana', 'Fernández Ruiz',
 'ana.fernandez@example.com', 'Landing Web'),

('Carlos', 'Medina López',
 'carlos.medina@example.com', 'Plataforma Completa'),

('Laura', 'Sánchez Pérez',
 'laura.sanchez@example.com', 'Plataforma Básica'),

('Daniel', 'Navarro Martín',
 'daniel.navarro@example.com', 'Landing Web'),

('Sofía', 'Romero García',
 'sofia.romero@example.com', 'Plataforma Completa'),

('Marta', 'Vega Torres',
 'marta.vega@example.com', 'Plataforma Básica'),
 
 ('Alejandro', 'Morales Díaz',
 'alejandro.morales@example.com',
 'Gestión de dominio/Despliegue'),

('Elena', 'Castillo Fernández',
 'elena.castillo@example.com',
 'Mantenimiento + Servicio Técnico');


-- ============================================
-- servicios
-- ============================================
INSERT INTO servicios
(nombre, tipo, descripcion, precio)
VALUES
('Gestión de dominio/Despliegue', 'Servicio',
 'Configuración de dominio, DNS, hosting y despliegue web',
 35.00),

('Mantenimiento + Servicio Técnico', 'Servicio',
 'Mantenimiento, resolución de incidencias y soporte técnico',
 35.00);


-- ============================================
-- pedidos
-- ============================================
INSERT INTO pedidos
(id_cliente, id_servicio, fecha_pedido, estado, precio_acordado)VALUES
(1, 3, '2026-09-05', 'Finalizado', 150.00),

(2, 1, '2026-09-12', 'Finalizado', 250.00),

(3, 3, '2026-09-18', 'Finalizado', 150.00),

(4, 2, '2026-09-25', 'En desarrollo', 350.00),

(5, 1, '2026-10-02', 'En desarrollo', 250.00),

(6, 3, '2026-10-05', 'Pendiente', 150.00),

(7, 2, '2026-10-08', 'En desarrollo', 350.00),

(8, 1, '2026-10-10', 'Pendiente', 250.00),

(3, 1, '2026-10-14', 'Pendiente', 250.00),

(5, 3, '2026-10-17', 'En desarrollo', 150.00),

(9, 4, '2026-10-19', 'En desarrollo', 35.00),

(10, 5, '2026-10-19', 'Pendiente', 35.00),

(9, 5, '2026-10-19', 'Pendiente', 35.00);
