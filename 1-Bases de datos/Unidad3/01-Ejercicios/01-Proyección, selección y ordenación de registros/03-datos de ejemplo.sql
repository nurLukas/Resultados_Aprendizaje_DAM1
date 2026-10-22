
-- Adaptacion a sturmprojekt a partir del listado facilitado por el alumno.
-- Datos ya existentes: 60 clientes, 5 servicios y 65 pedidos.
-- Los INSERT se documentan, pero estan comentados para no duplicar los datos.
-- No se ha ejecutado este archivo contra el servidor.
-- Conservamos INSERT INTO (...) VALUES, como en el ejercicio de clase.
-- No se crean datos para tablas de tienda_practicas ajenas a nuestro modelo.

USE sturmprojekt;

-- ============================================================
-- CLIENTES: datos cargados en las practicas anteriores de la Unidad 2.
-- Cada fila contiene nombre, apellidos, email, proyecto e identificador.
-- Se conservan los identificadores del listado para mantener las relaciones.
-- ============================================================
-- BLOQUE DOCUMENTAL: ejecutar solo en una reconstruccion con tablas vacias.
-- En la base actual estos identificadores ya existen; repetirlos daria
-- errores de clave primaria. No descomentar para las practicas actuales.
/*
INSERT INTO clientes (nombre, apellidos, email, proyecto, Identificador) VALUES
('Lucas Ezequiel', 'Andrés Griego', 'admin@jsturmprojekt.es', 'plataforma completa', 1),
('Juan', 'García Lopez', 'juan@garcia.com', 'Plataforma basica', 2),
('Ana', 'Fernández Ruiz', 'ana.fernandez@example.com', 'Landing Web', 3),
('Carlos', 'Medina López', 'carlos.medina@example.com', 'Plataforma Completa', 4),
('Laura', 'Sánchez Pérez', 'laura.sanchez@example.com', 'Plataforma Básica', 5),
('Daniel', 'Navarro Martín', 'daniel.navarro@example.com', 'Landing Web', 6),
('Sofía', 'Romero García', 'sofia.romero@example.com', 'Plataforma Completa', 7),
('Marta', 'Vega Torres', 'marta.vega@example.com', 'Plataforma Básica', 8),
('Alejandro', 'Morales Díaz', 'alejandro.morales@example.com', 'Gestión de dominio/Despliegue', 9),
('Elena', 'Castillo Fernández', 'elena.castillo@example.com', 'Mantenimiento + Servicio Técnico', 10),
('Adrián', 'Martínez López', 'adrian.martinez@example.com', 'Plataforma Básica', 11),
('Lucía', 'Fernández García', 'lucia.fernandez@example.com', 'Landing Web', 12),
('Pablo', 'Rodríguez Sánchez', 'pablo.rodriguez@example.com', 'Plataforma Completa', 13),
('Marina', 'González Torres', 'marina.gonzalez@example.com', 'Gestión de dominio/Despliegue', 14),
('Sergio', 'Ramírez Díaz', 'sergio.ramirez@example.com', 'Mantenimiento + Servicio Técnico', 15),
('Claudia', 'Moreno Pérez', 'claudia.moreno@example.com', 'Plataforma Básica', 16),
('Hugo', 'Jiménez Romero', 'hugo.jimenez@example.com', 'Landing Web', 17),
('Paula', 'Ruiz Navarro', 'paula.ruiz@example.com', 'Plataforma Completa', 18),
('Diego', 'Molina Castro', 'diego.molina@example.com', 'Gestión de dominio/Despliegue', 19),
('Irene', 'Ortega Herrera', 'irene.ortega@example.com', 'Mantenimiento + Servicio Técnico', 20),
('Álvaro', 'Delgado Martín', 'alvaro.delgado@example.com', 'Plataforma Completa', 21),
('Natalia', 'Vargas León', 'natalia.vargas@example.com', 'Plataforma Básica', 22),
('Mario', 'Santos Cabrera', 'mario.santos@example.com', 'Landing Web', 23),
('Carmen', 'Flores Medina', 'carmen.flores@example.com', 'Mantenimiento + Servicio Técnico', 24),
('Javier', 'Reyes Gil', 'javier.reyes@example.com', 'Gestión de dominio/Despliegue', 25),
('Valeria', 'Campos Rojas', 'valeria.campos@example.com', 'Plataforma Básica', 26),
('Rubén', 'Núñez Prieto', 'ruben.nunez@example.com', 'Plataforma Completa', 27),
('Aitana', 'Serrano Vega', 'aitana.serrano@example.com', 'Landing Web', 28),
('Óscar', 'Iglesias Fuentes', 'oscar.iglesias@example.com', 'Mantenimiento + Servicio Técnico', 29),
('Noelia', 'Cruz Márquez', 'noelia.cruz@example.com', 'Gestión de dominio/Despliegue', 30),
('Iván', 'Peña Soler', 'ivan.pena@example.com', 'Plataforma Básica', 31),
('Sara', 'Aguilar Molina', 'sara.aguilar@example.com', 'Landing Web', 32),
('Raúl', 'Pascual Nieto', 'raul.pascual@example.com', 'Plataforma Completa', 33),
('Eva', 'Blanco Carmona', 'eva.blanco@example.com', 'Mantenimiento + Servicio Técnico', 34),
('Víctor', 'Gallego Rubio', 'victor.gallego@example.com', 'Gestión de dominio/Despliegue', 35),
('Alba', 'Domínguez Cortés', 'alba.dominguez@example.com', 'Plataforma Básica', 36),
('Nicolás', 'Esteban Lozano', 'nicolas.esteban@example.com', 'Landing Web', 37),
('Andrea', 'Bravo Márquez', 'andrea.bravo@example.com', 'Plataforma Completa', 38),
('Samuel', 'Vidal Santos', 'samuel.vidal@example.com', 'Gestión de dominio/Despliegue', 39),
('Julia', 'Cordero Paredes', 'julia.cordero@example.com', 'Mantenimiento + Servicio Técnico', 40),
('Gabriel', 'Montes Rivas', 'gabriel.montes@example.com', 'Plataforma Completa', 41),
('Carla', 'Hidalgo Mora', 'carla.hidalgo@example.com', 'Plataforma Básica', 42),
('David', 'Prieto Alonso', 'david.prieto@example.com', 'Landing Web', 43),
('Nerea', 'Salazar Peña', 'nerea.salazar@example.com', 'Mantenimiento + Servicio Técnico', 44),
('Enrique', 'Fuentes Lara', 'enrique.fuentes@example.com', 'Gestión de dominio/Despliegue', 45),
('Olivia', 'Carrasco León', 'olivia.carrasco@example.com', 'Plataforma Básica', 46),
('Bruno', 'Méndez Varela', 'bruno.mendez@example.com', 'Plataforma Completa', 47),
('Rocío', 'Pérez Hidalgo', 'rocio.perez@example.com', 'Landing Web', 48),
('Guillermo', 'Soto Roldán', 'guillermo.soto@example.com', 'Mantenimiento + Servicio Técnico', 49),
('Teresa', 'Acosta Castaño', 'teresa.acosta@example.com', 'Gestión de dominio/Despliegue', 50),
('Joel', 'Román Ibáñez', 'joel.roman@example.com', 'Plataforma Básica', 51),
('Miriam', 'Lorenzo Escobar', 'miriam.lorenzo@example.com', 'Landing Web', 52),
('Marcos', 'Calvo Segura', 'marcos.calvo@example.com', 'Plataforma Completa', 53),
('Elisa', 'Ponce Beltrán', 'elisa.ponce@example.com', 'Gestión de dominio/Despliegue', 54),
('Fernando', 'Nieto Zamora', 'fernando.nieto@example.com', 'Mantenimiento + Servicio Técnico', 55),
('Beatriz', 'Suárez Robles', 'beatriz.suarez@example.com', 'Plataforma Completa', 56),
('Cristian', 'Herrero Vidal', 'cristian.herrero@example.com', 'Plataforma Básica', 57),
('Silvia', 'Arias Cifuentes', 'silvia.arias@example.com', 'Landing Web', 58),
('Roberto', 'Lara Benítez', 'roberto.lara@example.com', 'Gestión de dominio/Despliegue', 59),
('Patricia', 'Ferrer Montero', 'patricia.ferrer@example.com', 'Mantenimiento + Servicio Técnico', 60);
*/

-- ============================================================
-- SERVICIOS: catalogo ya cargado en la Unidad 2.
-- Es el equivalente a productos en la tienda del ejemplo de clase.
-- precio es el precio de catalogo; tipo distingue Producto y Servicio.
-- ============================================================
-- BLOQUE DOCUMENTAL: ejecutar solo en una reconstruccion con tablas vacias.
-- En la base actual estos identificadores ya existen; repetirlos daria
-- errores de clave primaria. No descomentar para las practicas actuales.
/*
INSERT INTO servicios (id_servicio, nombre, tipo, descripcion, precio) VALUES
(1, 'Plataforma Básica', 'Producto', 'Desarrollo web básico', 250.00),
(2, 'Plataforma Completa', 'Producto', 'Desarrollo web completo', 350.00),
(3, 'Landing Web', 'Producto', 'Pagina web estatica', 150.00),
(4, 'Gestión de dominio/Despliegue', 'Servicio', 'Configuración de dominio, DNS, hosting y despliegue web', 35.00),
(5, 'Mantenimiento + Servicio Técnico', 'Servicio', 'Mantenimiento, resolución de incidencias y soporte técnico', 35.00);
*/

-- ============================================================
-- PEDIDOS: datos existentes de las practicas anteriores.
-- id_cliente e id_servicio enlazan con las filas de las tablas anteriores.
-- Por eso se documentan clientes y servicios antes que pedidos.
-- precio_acordado puede diferir del precio de catalogo del servicio.
-- No se modifica ningun importe del listado facilitado.
-- ============================================================
-- BLOQUE DOCUMENTAL: ejecutar solo en una reconstruccion con tablas vacias.
-- En la base actual estos identificadores ya existen; repetirlos daria
-- errores de clave primaria. No descomentar para las practicas actuales.
/*
INSERT INTO pedidos (id_pedido, id_cliente, id_servicio, fecha_pedido, estado, precio_acordado) VALUES
(1, 1, 2, '2026-10-19', 'En desarrollo', 850.00),
(2, 2, 1, '2026-10-19', 'Pendiente', 350.00),
(3, 1, 3, '2026-09-05', 'Finalizado', 150.00),
(4, 2, 1, '2026-09-12', 'Finalizado', 250.00),
(5, 3, 3, '2026-09-18', 'Finalizado', 150.00),
(6, 4, 2, '2026-09-25', 'En desarrollo', 350.00),
(7, 5, 1, '2026-10-02', 'En desarrollo', 250.00),
(8, 6, 3, '2026-10-05', 'Pendiente', 150.00),
(9, 7, 2, '2026-10-08', 'En desarrollo', 350.00),
(10, 8, 1, '2026-10-10', 'Pendiente', 250.00),
(11, 3, 1, '2026-10-14', 'Pendiente', 250.00),
(12, 5, 3, '2026-10-17', 'En desarrollo', 150.00),
(13, 9, 4, '2026-10-19', 'En desarrollo', 35.00),
(14, 10, 5, '2026-10-19', 'Pendiente', 35.00),
(15, 9, 5, '2026-10-19', 'Pendiente', 35.00),
(16, 11, 1, '2026-07-01', 'Finalizado', 250.00),
(17, 12, 3, '2026-07-03', 'Finalizado', 150.00),
(18, 13, 2, '2026-07-05', 'Finalizado', 350.00),
(19, 14, 4, '2026-07-08', 'Finalizado', 35.00),
(20, 15, 5, '2026-07-11', 'Finalizado', 35.00),
(21, 16, 1, '2026-07-14', 'Finalizado', 250.00),
(22, 17, 3, '2026-07-16', 'Finalizado', 150.00),
(23, 18, 2, '2026-07-19', 'Finalizado', 350.00),
(24, 19, 4, '2026-07-22', 'Finalizado', 35.00),
(25, 20, 5, '2026-07-25', 'Finalizado', 35.00),
(26, 21, 2, '2026-07-28', 'Finalizado', 350.00),
(27, 22, 1, '2026-07-31', 'Finalizado', 250.00),
(28, 23, 3, '2026-08-02', 'Finalizado', 150.00),
(29, 24, 5, '2026-08-05', 'Finalizado', 35.00),
(30, 25, 4, '2026-08-07', 'Finalizado', 35.00),
(31, 26, 1, '2026-08-10', 'Finalizado', 250.00),
(32, 27, 2, '2026-08-13', 'Finalizado', 350.00),
(33, 28, 3, '2026-08-16', 'Finalizado', 150.00),
(34, 29, 5, '2026-08-19', 'Finalizado', 35.00),
(35, 30, 4, '2026-08-22', 'Finalizado', 35.00),
(36, 31, 1, '2026-08-25', 'Finalizado', 250.00),
(37, 32, 3, '2026-08-28', 'Finalizado', 150.00),
(38, 33, 2, '2026-08-31', 'En desarrollo', 350.00),
(39, 34, 5, '2026-09-02', 'Finalizado', 35.00),
(40, 35, 4, '2026-09-04', 'Finalizado', 35.00),
(41, 36, 1, '2026-09-06', 'En desarrollo', 250.00),
(42, 37, 3, '2026-09-08', 'Finalizado', 150.00),
(43, 38, 2, '2026-09-10', 'En desarrollo', 350.00),
(44, 39, 4, '2026-09-12', 'Finalizado', 35.00),
(45, 40, 5, '2026-09-14', 'En desarrollo', 35.00),
(46, 41, 2, '2026-09-16', 'En desarrollo', 350.00),
(47, 42, 1, '2026-09-18', 'En desarrollo', 250.00),
(48, 43, 3, '2026-09-20', 'Finalizado', 150.00),
(49, 44, 5, '2026-09-22', 'En desarrollo', 35.00),
(50, 45, 4, '2026-09-24', 'Finalizado', 35.00),
(51, 46, 1, '2026-09-26', 'En desarrollo', 250.00),
(52, 47, 2, '2026-09-28', 'En desarrollo', 350.00),
(53, 48, 3, '2026-09-30', 'Pendiente', 150.00),
(54, 49, 5, '2026-10-02', 'Pendiente', 35.00),
(55, 50, 4, '2026-10-03', 'Pendiente', 35.00),
(56, 51, 1, '2026-10-04', 'En desarrollo', 250.00),
(57, 52, 3, '2026-10-05', 'Pendiente', 150.00),
(58, 53, 2, '2026-10-06', 'En desarrollo', 350.00),
(59, 54, 4, '2026-10-07', 'Pendiente', 35.00),
(60, 55, 5, '2026-10-08', 'Pendiente', 35.00),
(61, 56, 2, '2026-10-09', 'En desarrollo', 350.00),
(62, 57, 1, '2026-10-11', 'Pendiente', 250.00),
(63, 58, 3, '2026-10-13', 'Pendiente', 150.00),
(64, 59, 4, '2026-10-15', 'Pendiente', 35.00),
(65, 60, 5, '2026-10-18', 'Pendiente', 35.00);
*/

-- COMPROBACION: estas consultas solo muestran los datos existentes.
-- Los recuentos indicados corresponden al listado recibido, no a una
-- nueva ejecucion comprobada en el servidor.
SELECT * FROM clientes;
SELECT * FROM servicios;
SELECT * FROM pedidos;
