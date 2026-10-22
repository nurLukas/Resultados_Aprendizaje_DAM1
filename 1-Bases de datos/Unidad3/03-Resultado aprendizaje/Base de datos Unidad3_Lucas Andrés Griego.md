# Reporte de proyecto

## Información de generación

- **Fecha:** 2026-10-21 20:41:21 +0200
- **Usuario:** lucas
- **Equipo:** LUCAS
- **Sistema operativo:** Windows
- **Arquitectura:** x86_64
- **Directorio de ejecución:** `D:/Herramientas/portables/jocarsa-generador-windows-x64`
- **Proyecto documentado:** `D:/Resultados Aprendizaje_DAM1/1-Bases de datos/Unidad3`
- **HMAC-SHA-256 de autenticidad:** `3dc9955a59cd461ea7e716093f749c0d876e97356beaa6dabe30ab9ee091f58f`

> El HMAC-SHA-256 se calcula sobre el documento completo usando un secreto incluido en el programa y 64 ceros en el propio campo del HMAC. El secreto no se escribe en el informe. Este mecanismo permite comprobar integridad y que el documento fue generado con el mismo secreto.

## Estructura del proyecto

```
D:/Resultados Aprendizaje_DAM1/1-Bases de datos/Unidad3
├── 01-Ejercicios
│   ├── 01-Proyección, selección y ordenación de registros
│   │   ├── 01-entramos en la base de datos.md
│   │   ├── 02-estructura.sql
│   │   ├── 03-datos de ejemplo.sql
│   │   ├── 04-entramos en la base de datos.sql
│   │   ├── 05-seleccion de campos.sql
│   │   ├── 06-proyeccion.sql
│   │   ├── 07-ordeno por apellido.sql
│   │   ├── 08-ASC explicito.sql
│   │   └── 09-DESC.sql
│   ├── 02-Operadores. Operadores de comparación. Operadores lógicos
│   │   ├── 01-preparacion.sql
│   │   ├── 02-listamos los servicios.sql
│   │   ├── 03-seleccion.sql
│   │   ├── 04-suma.sql
│   │   ├── 05-resta.sql
│   │   ├── 06-multiplicacion.sql
│   │   ├── 07-division.sql
│   │   ├── 08-calculo del iva de los productos.sql
│   │   ├── 09-comparacion.sql
│   │   ├── 10-preparacion operadores logicos.sql
│   │   ├── 11-seleccion de condiciones.sql
│   │   ├── 12-operador and.sql
│   │   └── 13-operador or.sql
│   ├── 03-Consultas de resumen
│   │   ├── 01-Utilizo mi base de datos.sql
│   │   ├── 02-Select del contenido de prueba.sql
│   │   ├── 03-quiero ver cuantos pedidos tengo.sql
│   │   ├── 04-suma.sql
│   │   ├── 05-promedio del pedido.sql
│   │   ├── 06-maximo.sql
│   │   └── 07-minimo.sql
│   ├── 04-Agrupamiento de registros
│   │   ├── 01-seleccionamos todo.sql
│   │   ├── 02-nueva tabla.sql
│   │   ├── 03-datos de muestra.sql
│   │   ├── 04-enumerar pedidos.sql
│   │   ├── 05-agrupar por año.sql
│   │   ├── 06-agrupar por mes y año.sql
│   │   ├── 07-agrupar por ciudad.sql
│   │   ├── 08-especifico el orden.sql
│   │   ├── 09-ordenar por ascendiente.sql
│   │   └── 10-varias combinaciones.sql
│   ├── 06-Composiciones externas
│   │   ├── 01-preparar la base de datos.sql
│   │   ├── 02-datos de ejemplo.sql
│   │   ├── 03-composicion.sql
│   │   ├── 04-primer cruce.sql
│   │   ├── 05-segundo cruce.sql
│   │   └── 06-simplificar columnas.sql
│   ├── 07-Subconsultas
│   │   ├── 01-vuelvo a la tienda.sql
│   │   ├── 02-promedio.sql
│   │   └── 03-subconsulta.sql
│   ├── 08-Combinación de múltiples selecciones
│   │   ├── 01-base de datos de productos.sql
│   │   ├── 02-insert into de muestra.sql
│   │   ├── 03-nos aseguramos.sql
│   │   ├── 04-nuevo usuario.sql
│   │   ├── 05-Nos conectasmos desde python a mysql.py
│   │   ├── 06-lo pinto en la web.py
│   │   └── 07-lo pinto con IA.py
│   └── 09-Optimización de consultas
│       ├── 01-preparacion de un blog.sql
│       ├── 02-Entradas de prueba.sql
│       ├── 03-comprobamos que todo esta ok.sql
│       ├── 04-crear usuario.sql
│       ├── 05-me conecto desde python.py
│       ├── 06-flask lo pinta bonito.py
│       ├── 07-plantilla html.html
│       ├── 08-un poco de estilo.html
│       ├── 09-trocearlo.html
│       ├── 10-uno las partes.py
│       ├── 11-articulos en html.py
│       ├── 12-retoques.py
│       └── 13-retoques css.py
├── 02-Proyecto
│   ├── 01-consultas.sql
│   ├── 02-consulta desde python.py
│   ├── 03-tienda web.py
│   └── 04-instrucciones para ver la tienda.md.md
└── 03-Resultado aprendizaje
    └── RA3.MD
```

## Bases de datos SQLite

Esta sección documenta únicamente el esquema de las bases SQLite detectadas. No se vuelcan registros ni datos de usuario.

No se han encontrado bases SQLite con extensiones .db, .sqlite o .sqlite3.

## Código (intercalado)

# Unidad3
## 01-Ejercicios
### 01-Proyección, selección y ordenación de registros
**01-entramos en la base de datos.md**

sudo mysql -u nurlukas -p

SHOW DATABASES;

**02-estructura.sql**

CREACION DOCUMENTADA: NO EJECUTAR SOBRE LA BASE EXISTENTE.
CREATE DATABASE sturmprojekt
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Selecciona la base sobre la que vamos a trabajar.
USE sturmprojekt;


/* ESTRUCTURA DOCUMENTADA: NO VOLVER A CREAR.
CREATE TABLE clientes (
    nombre VARCHAR(100),
    apellidos VARCHAR(100),
    email VARCHAR(100),
    proyecto VARCHAR(100),
    Identificador INT AUTO_INCREMENT PRIMARY KEY
);

ESTRUCTURA DOCUMENTADA: NO VOLVER A CREAR.
CREATE TABLE servicios (
    id_servicio INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id_servicio)
) ENGINE=InnoDB;


ESTRUCTURA DOCUMENTADA: NO VOLVER A CREAR.
CREATE TABLE pedidos (
    id_pedido INT NOT NULL AUTO_INCREMENT,
    id_cliente INT NOT NULL,
    id_servicio INT NOT NULL,
    fecha_pedido DATE NOT NULL,
    estado VARCHAR(50) NOT NULL,
    precio_acordado DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id_pedido),
    CONSTRAINT fk_cliente
        FOREIGN KEY (id_cliente) REFERENCES clientes(Identificador),
    CONSTRAINT fk_servicio
        FOREIGN KEY (id_servicio) REFERENCES servicios(id_servicio)
) ENGINE=InnoDB;

 RESTRICCIONES DEL PROYECTO ANTERIOR: NO DUPLICAR.
ALTER TABLE clientes
ADD CONSTRAINT chk_clientes_email
CHECK (email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+[.][A-Za-z]{2,}$');

ALTER TABLE servicios
ADD CONSTRAINT chk_servicios_precio CHECK (precio >= 0);

ALTER TABLE pedidos
ADD CONSTRAINT chk_pedidos_precio CHECK (precio_acordado >= 0);


-- Equivalente a idx_productos_precio del archivo original.
CREATE INDEX idx_servicios_precio
ON servicios(precio);

-- Equivalente a idx_pedidos_fecha del archivo original.
CREATE INDEX idx_pedidos_fecha
ON pedidos(fecha_pedido);

-- No se insertan datos en este archivo: corresponde al archivo 03.
-- La vista_completa existente se conserva; no se redefine aqui,
-- porque el archivo de estructura original tampoco crea vistas.

**03-datos de ejemplo.sql**


-- Adaptacion a sturmprojekt a partir del listado facilitado por el alumno.
-- Datos ya existentes: 60 clientes, 5 servicios y 65 pedidos.
-- Los INSERT se documentan, pero estan comentados para no duplicar los datos.
-- No se ha ejecutado este archivo contra el servidor.
-- Conservamos INSERT INTO (...) VALUES, como en el ejercicio de clase.
-- No se crean datos para tablas de tienda_practicas ajenas a nuestro modelo.

USE sturmprojekt;


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
```
**04-entramos en la base de datos.sql**
```sql
USE sturmprojekt;

SHOW TABLES;

SELECT * FROM clientes;
```
**05-seleccion de campos.sql**
```sql
SELECT
nombre,
apellidos
FROM clientes;
```
**06-proyeccion.sql**
```sql
SELECT
nombre AS 'Nombre del cliente',
apellidos AS 'Apellidos del cliente'
FROM clientes;
```
**07-ordeno por apellido.sql**
```sql
SELECT
nombre AS 'Nombre del cliente',
apellidos AS 'Apellidos del cliente'
FROM clientes
ORDER BY apellidos;

```
**08-ASC explicito.sql**
```sql
SELECT
nombre AS 'Nombre del cliente',
apellidos AS 'Apellidos del cliente'
FROM clientes
ORDER BY apellidos ASC;
```
**09-DESC.sql**
```sql
SELECT
nombre AS 'Nombre del cliente',
apellidos AS 'Apellidos del cliente'
FROM clientes
ORDER BY apellidos DESC;
```
### 02-Operadores. Operadores de comparación. Operadores lógicos
**01-preparacion.sql**
```sql
USE sturmprojekt;

SHOW TABLES;
```
**02-listamos los servicios.sql**
```sql
SELECT * FROM servicios;
```
**03-seleccion.sql**
```sql
SELECT
nombre AS 'Nombre del servicio',
precio AS 'Precio del servicio'
FROM servicios;
```
**04-suma.sql**
```sql
SELECT
nombre AS 'Nombre del servicio',
precio AS 'Precio del servicio',
precio + 20
FROM servicios;
```
**05-resta.sql**
```sql
SELECT
nombre AS 'Nombre del servicio',
precio AS 'Precio del servicio',
precio - 20
FROM servicios;
```
**06-multiplicacion.sql**
```sql
SELECT
nombre AS 'Nombre del servicio',
precio AS 'Precio del servicio',
precio * 20
FROM servicios;
```
**07-division.sql**
```sql
SELECT
nombre AS 'Nombre del servicio',
precio AS 'Precio del servicio',
precio / 20
FROM servicios;
```
**08-calculo del iva de los productos.sql**
```sql
SELECT
nombre AS 'Nombre del servicio',
precio AS 'Precio del servicio',
precio * 0.21 AS 'IVA 21%'
FROM servicios;
```
**09-comparacion.sql**
```sql
SELECT
nombre AS 'Nombre del servicio',
precio AS 'Base imponible',
precio > 500 AS 'Candidato',
precio * (precio > 500) * 0.1 AS 'Descuento',
precio - precio * (precio > 500) * 0.1 AS 'Total final'
FROM servicios;
```
**10-preparacion operadores logicos.sql**
```sql
SELECT * FROM servicios;
```
**11-seleccion de condiciones.sql**
```sql
SELECT
nombre,
precio,
precio > 500 AS 'Susceptible de descuento',
tipo,
tipo = 'Servicio' AS 'Es un servicio'
FROM servicios;
```
**12-operador and.sql**
```sql
SELECT
nombre,
precio,
precio > 500 AS 'Caro',
tipo,
tipo = 'Servicio' AS 'Es un servicio',
precio * (precio > 500 AND tipo = 'Servicio') * 0.1 AS 'Descuento'
FROM servicios;
```
**13-operador or.sql**
```sql
SELECT
nombre,
precio,
precio > 500 AS 'Caro',
tipo,
tipo = 'Servicio' AS 'Es un servicio',
precio * (precio > 500 OR tipo = 'Servicio') * 0.1 AS 'Descuento'
FROM servicios;
```
### 03-Consultas de resumen
**01-Utilizo mi base de datos.sql**
```sql
USE sturmprojekt;
```
**02-Select del contenido de prueba.sql**
```sql
SELECT * FROM pedidos;
```
**03-quiero ver cuantos pedidos tengo.sql**
```sql
SELECT * FROM pedidos;

SELECT COUNT(id_cliente) FROM pedidos;
```
**04-suma.sql**
```sql
SELECT SUM(precio_acordado) FROM pedidos;
```
**05-promedio del pedido.sql**
```sql
SELECT AVG(precio_acordado) FROM pedidos;


-- AVG calcula la media de los valores de precio_acordado.
-- Incluye todos los pedidos, independientemente de su estado.
-- No modifica los datos almacenados.
```
**06-maximo.sql**
```sql
SELECT
MAX(precio_acordado)
FROM pedidos;

-- MAX devuelve el mayor valor de precio_acordado.
```
**07-minimo.sql**
```sql
SELECT
MIN(precio_acordado)
FROM pedidos;


-- MIN devuelve el menor valor de precio_acordado.
```
### 04-Agrupamiento de registros
**01-seleccionamos todo.sql**
```sql
SELECT * FROM pedidos;
```
**02-nueva tabla.sql**
```sql
CREATE TABLE pedidos2 (
    id INT PRIMARY KEY AUTO_INCREMENT,
    anio INT,
    mes INT,
    dia INT,
    cliente VARCHAR(100),
    importe DECIMAL(6,2),
    ciudad VARCHAR(100)
);
```
**03-datos de muestra.sql**
```sql
INSERT INTO pedidos2 (anio, mes, dia, cliente, importe, ciudad) VALUES
(2024,1,5,'Ana García',125.50,'Valencia'),
(2024,1,12,'Luis Martínez',89.90,'Madrid'),
(2024,1,18,'Marta López',245.75,'Barcelona'),
(2024,1,25,'Carlos Sánchez',67.40,'Sevilla'),
(2024,2,3,'Laura Pérez',310.20,'Valencia'),
(2024,2,8,'David Romero',156.80,'Alicante'),
(2024,2,14,'Elena Torres',99.99,'Madrid'),
(2024,2,22,'Javier Ruiz',420.50,'Bilbao'),
(2024,3,2,'Sofía Navarro',78.25,'Valencia'),
(2024,3,9,'Miguel Ortega',530.00,'Barcelona'),

(2024,3,15,'Paula Molina',145.60,'Sevilla'),
(2024,3,27,'Daniel Castro',215.30,'Madrid'),
(2024,4,4,'Lucía Ramos',340.90,'Valencia'),
(2024,4,11,'Alejandro Gil',65.75,'Alicante'),
(2024,4,19,'Carmen Vega',180.40,'Murcia'),
(2024,4,26,'Pablo Serrano',275.90,'Barcelona'),
(2024,5,3,'Irene Campos',112.30,'Valencia'),
(2024,5,10,'Sergio León',450.00,'Madrid'),
(2024,5,17,'Natalia Vidal',89.50,'Sevilla'),
(2024,5,29,'Rubén Cano',625.80,'Bilbao'),

(2024,6,5,'Beatriz Mora',135.40,'Valencia'),
(2024,6,12,'Álvaro Reyes',290.75,'Barcelona'),
(2024,6,20,'Silvia Pastor',75.20,'Alicante'),
(2024,6,28,'Raúl Méndez',510.30,'Madrid'),
(2024,7,2,'Andrea Ferrer',220.60,'Valencia'),
(2024,7,9,'Hugo Lozano',95.80,'Sevilla'),
(2024,7,16,'Patricia Soler',365.25,'Barcelona'),
(2024,7,24,'Marcos Ibáñez',142.70,'Murcia'),
(2024,8,1,'Cristina Nieto',680.90,'Madrid'),
(2024,8,8,'Adrián Arias',55.60,'Valencia'),

(2024,8,15,'Nuria Pascual',245.00,'Alicante'),
(2024,8,23,'Víctor Calvo',390.40,'Barcelona'),
(2024,9,3,'Rosa Domínguez',120.90,'Sevilla'),
(2024,9,10,'Óscar Peña',540.20,'Madrid'),
(2024,9,18,'Teresa Blasco',210.80,'Valencia'),
(2024,9,26,'Mario Gallego',88.40,'Bilbao'),
(2024,10,4,'Eva Carmona',475.50,'Barcelona'),
(2024,10,11,'Jorge Fuentes',160.30,'Valencia'),
(2024,10,19,'Clara Esteban',295.75,'Madrid'),
(2024,10,27,'Iván Caballero',74.90,'Alicante'),

(2024,11,5,'Alicia Giménez',350.00,'Valencia'),
(2024,11,12,'Gonzalo Parra',610.40,'Barcelona'),
(2024,11,20,'Lorena Crespo',105.60,'Sevilla'),
(2024,11,28,'Fernando Costa',260.80,'Madrid'),
(2024,12,3,'Marina Roig',195.25,'Valencia'),
(2024,12,10,'Alberto Luna',720.90,'Bilbao'),
(2024,12,17,'Sara Montes',130.50,'Alicante'),
(2024,12,23,'Roberto Martí',480.75,'Barcelona'),
(2024,12,27,'Isabel Prieto',215.40,'Madrid'),
(2024,12,30,'Guillermo Sáez',95.90,'Valencia'),

(2025,1,4,'Ana García',175.20,'Valencia'),
(2025,1,11,'Luis Martínez',240.50,'Madrid'),
(2025,1,19,'Marta López',380.90,'Barcelona'),
(2025,1,27,'Carlos Sánchez',110.30,'Sevilla'),
(2025,2,2,'Laura Pérez',560.40,'Valencia'),
(2025,2,9,'David Romero',195.75,'Alicante'),
(2025,2,16,'Elena Torres',85.90,'Madrid'),
(2025,2,24,'Javier Ruiz',690.25,'Bilbao'),
(2025,3,3,'Sofía Navarro',140.80,'Valencia'),
(2025,3,10,'Miguel Ortega',425.60,'Barcelona'),

(2025,3,18,'Paula Molina',275.30,'Sevilla'),
(2025,3,26,'Daniel Castro',520.90,'Madrid'),
(2025,4,2,'Lucía Ramos',180.50,'Valencia'),
(2025,4,9,'Alejandro Gil',330.75,'Alicante'),
(2025,4,17,'Carmen Vega',95.40,'Murcia'),
(2025,4,25,'Pablo Serrano',610.80,'Barcelona'),
(2025,5,3,'Irene Campos',225.90,'Valencia'),
(2025,5,11,'Sergio León',740.20,'Madrid'),
(2025,5,19,'Natalia Vidal',135.60,'Sevilla'),
(2025,5,27,'Rubén Cano',490.50,'Bilbao'),

(2025,6,4,'Beatriz Mora',310.40,'Valencia'),
(2025,6,12,'Álvaro Reyes',580.90,'Barcelona'),
(2025,6,20,'Silvia Pastor',125.75,'Alicante'),
(2025,6,28,'Raúl Méndez',850.30,'Madrid'),
(2025,7,5,'Andrea Ferrer',340.60,'Valencia'),
(2025,7,13,'Hugo Lozano',175.90,'Sevilla'),
(2025,7,21,'Patricia Soler',625.40,'Barcelona'),
(2025,7,29,'Marcos Ibáñez',230.80,'Murcia'),
(2025,8,4,'Cristina Nieto',910.50,'Madrid'),
(2025,8,12,'Adrián Arias',115.40,'Valencia'),

(2025,8,20,'Nuria Pascual',420.75,'Alicante'),
(2025,8,28,'Víctor Calvo',670.90,'Barcelona'),
(2025,9,5,'Rosa Domínguez',205.30,'Sevilla'),
(2025,9,13,'Óscar Peña',780.60,'Madrid'),
(2025,9,21,'Teresa Blasco',365.80,'Valencia'),
(2025,9,29,'Mario Gallego',145.90,'Bilbao'),
(2025,10,4,'Eva Carmona',690.20,'Barcelona'),
(2025,10,12,'Jorge Fuentes',285.50,'Valencia'),
(2025,10,20,'Clara Esteban',510.75,'Madrid'),
(2025,10,28,'Iván Caballero',125.40,'Alicante'),

(2025,11,3,'Alicia Giménez',475.80,'Valencia'),
(2025,11,11,'Gonzalo Parra',825.30,'Barcelona'),
(2025,11,19,'Lorena Crespo',190.60,'Sevilla'),
(2025,11,27,'Fernando Costa',430.90,'Madrid'),
(2025,12,4,'Marina Roig',320.50,'Valencia'),
(2025,12,12,'Alberto Luna',950.75,'Bilbao'),
(2025,12,18,'Sara Montes',210.40,'Alicante'),
(2025,12,23,'Roberto Martí',720.90,'Barcelona'),
(2025,12,27,'Isabel Prieto',380.25,'Madrid'),
(2025,12,30,'Guillermo Sáez',165.80,'Valencia');
```
**04-enumerar pedidos.sql**
```sql
SELECT COUNT(cliente) FROM pedidos2;
```
**05-agrupar por año.sql**
```sql
SELECT
anio,
COUNT(cliente)
FROM pedidos2
GROUP BY anio;
```
**06-agrupar por mes y año.sql**
```sql
SELECT
anio,
mes,
COUNT(cliente)
FROM pedidos2
GROUP BY anio, mes;
```
**07-agrupar por ciudad.sql**
```sql
SELECT
ciudad,
COUNT(cliente)
FROM pedidos2
GROUP BY ciudad;
```
**08-especifico el orden.sql**
```sql
SELECT
ciudad,
COUNT(cliente)
FROM pedidos2
GROUP BY ciudad
ORDER BY COUNT(cliente) DESC;


-- GROUP BY reúne los registros de cada ciudad.
-- COUNT(cliente) cuenta los valores no nulos de cada grupo.
-- ORDER BY ... DESC muestra primero las ciudades con más pedidos.
```
**09-ordenar por ascendiente.sql**
```sql
SELECT
ciudad,
COUNT(cliente)
FROM pedidos2
GROUP BY ciudad
ORDER BY COUNT(cliente) ASC;
```
**10-varias combinaciones.sql**
```sql
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
```
### 06-Composiciones externas
**01-preparar la base de datos.sql**
```sql
-- Estas acciones ya se realizaron en la Unidad 2 sobre sturmprojekt:
-- creación de la base de datos, tablas, relaciones y carga de datos.
-- Conservamos el contenido original como referencia de clase.
-- Este archivo no se ha vuelto a ejecutar en la Unidad 3,
-- para evitar errores por tablas existentes y duplicación de datos.

sudo mysql -u root -p

CREATE DATABASE sturmprojekt;

USE sturmprojekt;

CREATE TABLE clientes (
  nombre varchar(100) DEFAULT NULL,
  apellidos varchar(100) DEFAULT NULL,
  email varchar(100) DEFAULT NULL,
  proyecto varchar(100) DEFAULT NULL,
  Identificador int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (Identificador)
);

# Creo tabla de servicios
CREATE TABLE servicios (
    id_servicio INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id_servicio)
) ENGINE=InnoDB;


# Agrego algunos servicios
INSERT INTO servicios
(nombre, tipo, descripcion, precio)
VALUES
('Plataforma Básica', 'Producto',
 'Desarrollo web básico', 250.00),

('Plataforma Completa', 'Producto',
 'Desarrollo web completo', 350.00),

('Landing Web', 'Producto',
 'Pagina web estatica', 150.00);
 
 
# Creo tabla de pedidos
CREATE TABLE pedidos (
    id_pedido INT NOT NULL AUTO_INCREMENT,
    id_cliente INT NOT NULL,
    id_servicio INT NOT NULL,
    fecha_pedido DATE NOT NULL,
    estado VARCHAR(50) NOT NULL,
    precio_acordado DECIMAL(10,2) NOT NULL,

    PRIMARY KEY (id_pedido),

    CONSTRAINT fk_cliente
        FOREIGN KEY (id_cliente)
        REFERENCES clientes(Identificador),

    CONSTRAINT fk_servicio
        FOREIGN KEY (id_servicio)
        REFERENCES servicios(id_servicio)
) ENGINE=InnoDB;

# Inserto algunos pedidos
INSERT INTO pedidos
(id_cliente, id_servicio, fecha_pedido, estado, precio_acordado)
VALUES
(1, 2, '2026-10-19', 'En desarrollo', 850.00),
(2, 1, '2026-10-19', 'Pendiente', 350.00);

**02-datos de ejemplo.sql**

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
```
**03-composicion.sql**
```sql
SELECT
pedidos.fecha_pedido,
pedidos.id_cliente,
pedidos.id_servicio
FROM pedidos;
```
**04-primer cruce.sql**
```sql
SELECT
pedidos.fecha_pedido,
pedidos.id_cliente,
pedidos.id_servicio,
clientes.nombre,
clientes.apellidos,
clientes.email
FROM pedidos
LEFT JOIN clientes
ON pedidos.id_cliente = clientes.Identificador;



-- LEFT JOIN conserva todos los pedidos.
-- ON relaciona id_cliente con Identificador de clientes.
-- Añadimos el nombre, los apellidos y el email del cliente.
-- Si no hubiera coincidencia, esos campos aparecerían como NULL.
```
**05-segundo cruce.sql**
```sql
SELECT
pedidos.fecha_pedido,
pedidos.id_cliente,
pedidos.id_servicio,
clientes.nombre,
clientes.apellidos,
clientes.email,
servicios.nombre,
servicios.tipo
FROM pedidos
LEFT JOIN clientes
ON pedidos.id_cliente = clientes.Identificador
LEFT JOIN servicios
ON pedidos.id_servicio = servicios.id_servicio;


-- El primer LEFT JOIN relaciona pedidos con clientes.
-- El segundo LEFT JOIN relaciona pedidos con servicios.
```
**06-simplificar columnas.sql**
```sql
SELECT
pedidos.fecha_pedido,
clientes.nombre,
clientes.apellidos,
servicios.nombre
FROM pedidos
LEFT JOIN clientes
ON pedidos.id_cliente = clientes.Identificador
LEFT JOIN servicios
ON pedidos.id_servicio = servicios.id_servicio;
```
### 07-Subconsultas
**01-vuelvo a la tienda.sql**
```sql
USE sturmprojekt;
```
**02-promedio.sql**
```sql
SELECT
AVG(precio_acordado)
FROM pedidos;
```
**03-subconsulta.sql**
```sql
SELECT
pedidos.fecha_pedido,
pedidos.id_cliente,
pedidos.precio_acordado,
pedidos.precio_acordado > (
    SELECT AVG(precio_acordado) FROM pedidos
) AS porencima
FROM pedidos;



-- La subconsulta calcula el importe medio de todos los pedidos.
-- La consulta principal compara cada importe con esa media.
-- porencima muestra 1 si la supera y 0 si no.
```
### 08-Combinación de múltiples selecciones
**01-base de datos de productos.sql**
```sql
sudo mysql -u root -p

CREATE DATABASE tiendazapatillas;

USE tiendazapatillas;

CREATE TABLE productos(
	id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100),
  descripcion VARCHAR(255),
  precio DECIMAL(4,2)
);
```
**02-insert into de muestra.sql**
```sql
INSERT INTO productos (nombre, descripcion, precio) VALUES
('Velocity Run', 'Zapatillas ligeras para running urbano', 49.99);

INSERT INTO productos (nombre, descripcion, precio) VALUES
('Urban Step', 'Zapatillas casual para uso diario', 39.95);

INSERT INTO productos (nombre, descripcion, precio) VALUES
('Mountain Grip', 'Zapatillas resistentes para senderismo', 59.90);

INSERT INTO productos (nombre, descripcion, precio) VALUES
('Cloud Walk', 'Zapatillas cómodas con suela acolchada', 44.50);

INSERT INTO productos (nombre, descripcion, precio) VALUES
('Street Flex', 'Zapatillas flexibles de estilo urbano', 35.99);

INSERT INTO productos (nombre, descripcion, precio) VALUES
('Rapid X', 'Zapatillas deportivas para entrenamiento', 54.95);

INSERT INTO productos (nombre, descripcion, precio) VALUES
('Ocean Breeze', 'Zapatillas transpirables para verano', 42.00);

INSERT INTO productos (nombre, descripcion, precio) VALUES
('Night Runner', 'Zapatillas de running con detalles reflectantes', 64.90);

INSERT INTO productos (nombre, descripcion, precio) VALUES
('Retro Wave', 'Zapatillas casual de inspiración retro', 47.50);

INSERT INTO productos (nombre, descripcion, precio) VALUES
('Power Jump', 'Zapatillas deportivas con amortiguación reforzada', 69.99);

INSERT INTO productos (nombre, descripcion, precio) VALUES
('City Motion', 'Zapatillas urbanas cómodas y ligeras', 41.95);

INSERT INTO productos (nombre, descripcion, precio) VALUES
('Trail Storm', 'Zapatillas de trail con suela antideslizante', 74.90);

INSERT INTO productos (nombre, descripcion, precio) VALUES
('Air Flow', 'Zapatillas deportivas con tejido transpirable', 52.50);

INSERT INTO productos (nombre, descripcion, precio) VALUES
('Classic One', 'Zapatillas clásicas para uso cotidiano', 34.99);

INSERT INTO productos (nombre, descripcion, precio) VALUES
('Sprint Pro', 'Zapatillas ligeras para carreras rápidas', 79.95);

INSERT INTO productos (nombre, descripcion, precio) VALUES
('Green Path', 'Zapatillas fabricadas con materiales reciclados', 58.00);

INSERT INTO productos (nombre, descripcion, precio) VALUES
('Metro Walk', 'Zapatillas cómodas para caminar por ciudad', 43.90);

INSERT INTO productos (nombre, descripcion, precio) VALUES
('Jump Max', 'Zapatillas deportivas de gran amortiguación', 67.50);

INSERT INTO productos (nombre, descripcion, precio) VALUES
('Daily Comfort', 'Zapatillas acolchadas para uso diario', 38.95);

INSERT INTO productos (nombre, descripcion, precio) VALUES
('Speed Light', 'Zapatillas ultraligeras para entrenamiento', 62.99);
```
**03-nos aseguramos.sql**
```sql
SELECT * FROM productos;
```
**04-nuevo usuario.sql**
```sql
-- Para usar tame123, debes reducir la política de contraseñas. Entra como administrador desde la terminal de Linux:
-- sudo mysql
-- Permite contraseñas sin exigir mayúsculas, números y símbolos.
-- SET GLOBAL validate_password.policy = LOW;
-- tame123 tiene siete caracteres.
-- SET GLOBAL validate_password.length = 7;


CREATE USER 'tiendazapatillas'@'localhost' IDENTIFIED BY 'tame123';

GRANT USAGE ON *.* TO 'tiendazapatillas'@'localhost';

ALTER USER 'tiendazapatillas'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON tiendazapatillas.* 
TO 'tiendazapatillas'@'localhost';

FLUSH PRIVILEGES;
```
**05-Nos conectasmos desde python a mysql.py**
```python
import mysql.connector

# Conectamos con la base de datos
connection = mysql.connector.connect(
    host='localhost',
    user='tiendazapatillas',
    password='tame123',
    database='tiendazapatillas'
)		

# Creo un cursor que es el que transporta la información
cursor = connection.cursor()

# Le pido algo a la base de datos
cursor.execute("SELECT * FROM productos")	# en este momento programacion se une con bbdd

filas = cursor.fetchall()						# quiero todos los registros

# Devuelvo las filas
for fila in filas:
  print(fila)

cursor.close()
connection.close()
```
**06-lo pinto en la web.py**
```python
from flask import Flask              # Importo la libreria de pintar en la web
import mysql.connector               # E importo la libreria de conectar a MySQL

# Conectamos con la base de datos
connection = mysql.connector.connect(
    host='localhost',
    user='tiendazapatillas',
    password='TiendaZapatillas123$',
    database='tiendazapatillas'
)

# Creo un cursor que es el que transporta la información
cursor = connection.cursor()

aplicacion = Flask(__name__)         # Creo una aplicación


@aplicacion.route("/")
def inicio():                        # Cada vez que alguien pida la pagina principal del servidor
    cadena = ""

    # Le pido algo a la base de datos
    cursor.execute("SELECT * FROM productos")    # En este momento programacion se une con BBDD
    filas = cursor.fetchall()                    # Quiero todos los registros

    # Devuelvo las filas
    for fila in filas:
        cadena += fila

    return cadena


if __name__ == "__main__":
    aplicacion.run()


cursor.close()
connection.close()
```
**07-lo pinto con IA.py**
```python
from flask import Flask
import mysql.connector

# Conectamos con la base de datos
connection = mysql.connector.connect(
    host='localhost',
    user='tiendazapatillas',
    password='TiendaZapatillas123$',
    database='tiendazapatillas'
)

# Creo un cursor que es el que transporta la información
cursor = connection.cursor()

aplicacion = Flask(__name__)


@aplicacion.route("/")
def inicio():

    cadena = """
    <!doctype html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Tienda de zapatillas</title>

        <style>
            *{
                box-sizing:border-box;
            }

            body{
                margin:0;
                font-family:Arial, sans-serif;
                background:#f5f5f5;
            }

            header{
                background:#222;
                color:white;
                padding:30px;
                text-align:center;
            }

            header h1{
                margin:0;
            }

            main{
                max-width:1200px;
                margin:auto;
                padding:30px;
            }

            .productos{
                display:grid;
                grid-template-columns:repeat(auto-fit, minmax(250px, 1fr));
                gap:20px;
            }

            .producto{
                background:white;
                padding:25px;
                border-radius:10px;
                box-shadow:0px 3px 10px rgba(0,0,0,0.1);
                transition:0.3s;
            }

            .producto:hover{
                transform:translateY(-5px);
                box-shadow:0px 8px 20px rgba(0,0,0,0.15);
            }

            .producto h2{
                margin-top:0;
                color:#222;
            }

            .descripcion{
                color:#666;
                min-height:60px;
                line-height:1.5;
            }

            .precio{
                font-size:24px;
                font-weight:bold;
                color:#16833b;
                margin-top:20px;
            }

            .id{
                font-size:11px;
                color:#aaa;
            }

            button{
                width:100%;
                border:0;
                padding:12px;
                margin-top:15px;
                background:#222;
                color:white;
                border-radius:5px;
                cursor:pointer;
            }

            button:hover{
                background:#444;
            }
        </style>
    </head>

    <body>

        <header>
            <h1>Tienda de zapatillas</h1>
            <p>Nuestros productos</p>
        </header>

        <main>
            <div class="productos">
    """

    # Le pido los productos a la base de datos
    cursor.execute("SELECT * FROM productos")
    filas = cursor.fetchall()

    # Creo una tarjeta por cada producto
    for fila in filas:

        cadena += """
            <div class="producto">
                <div class="id">Producto #""" + str(fila[0]) + """</div>

                <h2>""" + str(fila[1]) + """</h2>

                <div class="descripcion">
                    """ + str(fila[2]) + """
                </div>

                <div class="precio">
                    """ + str(fila[3]) + """ €
                </div>

                <button>Ver producto</button>
            </div>
        """

    cadena += """
            </div>
        </main>

    </body>
    </html>
    """

    return cadena


if __name__ == "__main__":
    aplicacion.run()
```
### 09-Optimización de consultas
**01-preparacion de un blog.sql**
```sql
sudo mysql -u root -p

CREATE DATABASE blog2627;

USE blog2627;

CREATE TABLE entradas(
	id INT PRIMARY KEY AUTO_INCREMENT,
  titulo VARCHAR(100),
  fecha DATE,
  contenido TEXT
);
```
**02-Entradas de prueba.sql**
```sql
INSERT INTO entradas (titulo, fecha, contenido) VALUES

(
'Bienvenidos a mi blog',
'2026-01-10',
'Bienvenidos a mi espacio personal sobre programación, tecnología, inteligencia artificial y educación. Soy José Vicente Carratalá, desarrollador de software y profesor de informática. Aquí compartiré experiencias, proyectos, tutoriales y reflexiones sobre el mundo tecnológico.'
),

(
'Por qué sigo programando después de tantos años',
'2026-01-18',
'Comencé a trabajar con la programación hace más de dos décadas. Desde entonces han cambiado los lenguajes, los frameworks y las herramientas, pero la esencia continúa siendo la misma: resolver problemas mediante código. Cada nuevo proyecto representa una oportunidad para aprender.'
),

(
'Python como lenguaje para aprender programación',
'2026-02-03',
'Python es uno de mis lenguajes favoritos para enseñar programación. Su sintaxis sencilla permite concentrarse en los conceptos fundamentales: variables, estructuras de control, funciones, clases y objetos. Además, permite desarrollar aplicaciones reales desde las primeras clases.'
),

(
'La inteligencia artificial está transformando la educación',
'2026-02-15',
'La inteligencia artificial generativa está cambiando la manera de enseñar y aprender. Los alumnos pueden disponer de asistentes personalizados, generar ejemplos de código y resolver dudas. El verdadero reto consiste en integrar estas herramientas sin perder el pensamiento crítico.'
),

(
'Creando aplicaciones web con PHP y SQLite',
'2026-03-02',
'PHP y SQLite forman una combinación muy interesante para desarrollar aplicaciones web ligeras. SQLite permite almacenar información sin configurar un servidor de bases de datos independiente. Esta arquitectura resulta especialmente útil para prototipos y herramientas internas.'
),

(
'Introducción a las bases de datos relacionales',
'2026-03-12',
'Las bases de datos relacionales siguen siendo fundamentales en el desarrollo de software. Tablas, registros, claves primarias y claves foráneas permiten organizar información de manera consistente. Comprender SQL es una habilidad imprescindible para cualquier programador.'
),

(
'Mi experiencia enseñando desarrollo de aplicaciones',
'2026-03-25',
'La enseñanza de programación requiere combinar teoría y práctica. Durante mis clases intento que los estudiantes construyan aplicaciones funcionales y comprendan cómo se relacionan los diferentes componentes de un sistema informático.'
),

(
'Primeros pasos con modelos de inteligencia artificial locales',
'2026-04-04',
'Ejecutar modelos de lenguaje en un ordenador personal ofrece ventajas importantes. Herramientas como Ollama permiten experimentar con inteligencia artificial sin depender constantemente de servicios externos. Es una excelente oportunidad para investigar privacidad, rendimiento y personalización.'
),

(
'Cómo construir un sistema RAG',
'2026-04-17',
'Los sistemas RAG combinan modelos de lenguaje con recuperación de información. En lugar de depender exclusivamente del conocimiento del modelo, podemos consultar documentos propios y utilizarlos como contexto para generar respuestas más relevantes.'
),

(
'Automatizando tareas repetitivas con Python',
'2026-05-06',
'Una de las mayores ventajas de Python es su capacidad para automatizar procesos. Podemos procesar miles de archivos, transformar documentos, analizar información y generar informes. Una automatización bien diseñada puede ahorrar muchas horas de trabajo.'
),

(
'Desarrollo de videojuegos como herramienta educativa',
'2026-05-19',
'Los videojuegos son una excelente manera de aprender programación orientada a objetos. Conceptos como clases, herencia, métodos, colisiones y movimiento se comprenden mejor cuando podemos observar sus resultados directamente en pantalla.'
),

(
'Experimentando con OpenCV',
'2026-06-08',
'OpenCV permite trabajar con imágenes y vídeo utilizando Python. Podemos dibujar objetos, detectar movimientos y desarrollar simulaciones visuales. Es una biblioteca especialmente interesante para enseñar programación gráfica y visión artificial.'
),

(
'Diseñando mi propio sistema ERP',
'2026-06-21',
'Desarrollar un ERP desde cero es un desafío que combina bases de datos, interfaces, autenticación, permisos y arquitectura modular. Mi objetivo es construir un sistema flexible que permita crear aplicaciones empresariales reutilizando componentes comunes.'
),

(
'La importancia de diseñar componentes reutilizables',
'2026-07-05',
'Cuando desarrollamos múltiples aplicaciones, resulta fundamental evitar repetir código. Los componentes reutilizables permiten construir interfaces consistentes, reducir errores y acelerar el desarrollo de nuevos proyectos.'
),

(
'Cómo organizar una plataforma de formación online',
'2026-07-18',
'Una plataforma educativa necesita gestionar alumnos, asignaturas, materiales, evaluaciones y seguimiento del progreso. La integración de estas funcionalidades permite ofrecer una experiencia más completa tanto al estudiante como al profesor.'
),

(
'Procesamiento automático de vídeos educativos',
'2026-08-03',
'Los vídeos educativos pueden procesarse automáticamente mediante herramientas como FFmpeg y Whisper. Es posible convertir formatos, extraer audio, generar transcripciones y preparar materiales que posteriormente pueden utilizarse en sistemas de búsqueda inteligente.'
),

(
'Construyendo una base de datos propia',
'2026-08-20',
'Crear un motor de bases de datos permite comprender aspectos internos que normalmente permanecen ocultos. El almacenamiento, los índices, las consultas y la gestión de registros son problemas fascinantes desde el punto de vista de la ingeniería del software.'
),

(
'Integrando Moodle con aplicaciones externas',
'2026-09-04',
'Moodle ofrece numerosas posibilidades de integración con herramientas propias. Mediante APIs y servicios web podemos automatizar matriculaciones, consultar información académica y conectar diferentes sistemas de gestión educativa.'
),

(
'Gráficas y dashboards para aplicaciones empresariales',
'2026-09-22',
'Los datos adquieren mucho más valor cuando podemos visualizarlos. Las gráficas de barras, líneas, áreas y sectores permiten identificar tendencias y comparar resultados. Un dashboard bien diseñado facilita la interpretación de la información.'
),

(
'El futuro de la programación con inteligencia artificial',
'2026-10-08',
'La programación está evolucionando hacia un modelo de colaboración entre desarrolladores y asistentes inteligentes. La inteligencia artificial puede generar código, detectar errores y proponer arquitecturas, pero comprender los fundamentos sigue siendo imprescindible para construir software de calidad.'
);
```
**03-comprobamos que todo esta ok.sql**
```sql
SELECT * FROM entradas;
```
**04-crear usuario.sql**
```sql
CREATE USER 'blog2627'@'localhost' IDENTIFIED BY 'Blog2627$';

GRANT USAGE ON *.* TO 'blog2627'@'localhost';

ALTER USER 'blog2627'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON blog2627.* 
TO 'blog2627'@'localhost';

FLUSH PRIVILEGES;
```
**05-me conecto desde python.py**
```python
# Importo la libreria de MySQL
import mysql.connector

# Me conecto a la base de datos con el usuario que acabo de crear
connection = mysql.connector.connect(
    host='localhost',
    user='blog2627',
    password='Blog2627$',
    database='blog2627'
)		

# Creo un cursor para poder pedir cosas
cursor = connection.cursor()

# Ejecuto una petición sobre el cursor
cursor.execute("SELECT * FROM entradas;")

# Dame todas las filas
entradas = cursor.fetchall()	

# Devuelveme todas las entradas
for entrada in entradas:
  print(entrada)

# Cierro los recursos que haya abierto
cursor.close()
connection.close()
```
**06-flask lo pinta bonito.py**
```python

# Importo la libreria de MySQL
import mysql.connector

# Importo la libreria de Flask para presentar cosas en la web
from flask import Flask

# Me conecto a la base de datos con el usuario que acabo de crear
connection = mysql.connector.connect(
    host='localhost',
    user='blog2627',
    password='Blog2627$',
    database='blog2627'
)

# Creo un cursor para poder pedir cosas
cursor = connection.cursor()

# Creo una aplicación web
aplicacion = Flask(__name__)

# Defino que es lo que pasa en el punto de inicio
@aplicacion.route("/")
def inicio():
    salida = ""

    # Ejecuto una petición sobre el cursor
    cursor.execute("SELECT * FROM entradas;")

    # Dame todas las filas
    entradas = cursor.fetchall()

    # Devuelveme todas las entradas
    for entrada in entradas:
        salida += str(entrada) + "<br>"

    return salida

# Arranco la aplicación web
if __name__ == "__main__":
    aplicacion.run(debug=True)
```
**07-plantilla html.html**
```html
<!doctype html>
<html lang="es">
  <head>
    <title>El blog de Jose Vicente</title>
    <meta charset="utf-8">
  </head>
  <body>
    <header>
      <h1>El blog de Jose Vicente</h1>
    </header>
    <main>
      <section>
      </section>
    </main>
    <footer>
      <p>(c) 2026 Jose Vicente Carratala</p>
    </footer>
  </body>
</html>
```
**08-un poco de estilo.html**
```html
<!doctype html>
<html lang="es">
  <head>
    <title>El blog de Jose Vicente</title>
    <meta charset="utf-8">
    <style>
      body{background:grey;}
      header,main,footer{background:white;padding:20px;margin:auto;width:800px;}
    </style>
  </head>
  <body>
    <header>
      <h1>El blog de Jose Vicente</h1>
    </header>
    <main>
      <section>
      </section>
    </main>
    <footer>
      <p>(c) 2026 Jose Vicente Carratala</p>
    </footer>
  </body>
</html>
```
**09-trocearlo.html**
```html
<!-- Inicio del trozo de cabeza -->
<!doctype html>
<html lang="es">
  <head>
    <title>El blog de Jose Vicente</title>
    <meta charset="utf-8">
    <style>
      body{background:grey;}
      header,main,footer{background:white;padding:20px;margin:auto;width:800px;}
    </style>
  </head>
  <body>
    <header>
      <h1>El blog de Jose Vicente</h1>
    </header>
    <main>
      <section>
<!-- Final del trozo de cabeza -->
        
        
<!-- Inicio del trozo de pie de pagina --> 
      </section>
    </main>
    <footer>
      <p>(c) 2026 Jose Vicente Carratala</p>
    </footer>
  </body>
</html>
<!-- Final del trozo de pie de pagina --> 
```
**10-uno las partes.py**
```python

# Importo la libreria de MySQL
import mysql.connector

# Importo la libreria de Flask para presentar cosas en la web
from flask import Flask

# Me conecto a la base de datos con el usuario que acabo de crear
connection = mysql.connector.connect(
    host='localhost',
    user='blog2627',
    password='Blog2627$',
    database='blog2627'
)

# Creo un cursor para poder pedir cosas
cursor = connection.cursor()

# Creo una aplicación web
aplicacion = Flask(__name__)

# Defino que es lo que pasa en el punto de inicio
@aplicacion.route("/")
def inicio():
  
  	cabeza = """
    <!-- Inicio del trozo de cabeza -->
<!doctype html>
<html lang="es">
  <head>
    <title>El blog de Jose Vicente</title>
    <meta charset="utf-8">
    <style>
      body{background:grey;}
      header,main,footer{background:white;padding:20px;margin:auto;width:800px;}
    </style>
  </head>
  <body>
    <header>
      <h1>El blog de Jose Vicente</h1>
    </header>
    <main>
      <section>
<!-- Final del trozo de cabeza -->
    """
    cuerpo = ""

    # Ejecuto una petición sobre el cursor
    cursor.execute("SELECT * FROM entradas;")

    # Dame todas las filas
    entradas = cursor.fetchall()

    # Devuelveme todas las entradas
    for entrada in entradas:
        cuerpo += str(entrada) + "<br>"
        
		piedepagina = """
    <!-- Inicio del trozo de pie de pagina --> 
      </section>
    </main>
    <footer>
      <p>(c) 2026 Jose Vicente Carratala</p>
    </footer>
  </body>
</html>
<!-- Final del trozo de pie de pagina --> 
    """
    return cabeza+cuerpo+piedepagina

# Arranco la aplicación web
if __name__ == "__main__":
    aplicacion.run(debug=True)
```
**11-articulos en html.py**
```python

# Importo la libreria de MySQL
import mysql.connector

# Importo la libreria de Flask para presentar cosas en la web
from flask import Flask

# Me conecto a la base de datos con el usuario que acabo de crear
connection = mysql.connector.connect(
    host='localhost',
    user='blog2627',
    password='Blog2627$',
    database='blog2627'
)

# Creo un cursor para poder pedir cosas
cursor = connection.cursor()

# Creo una aplicación web
aplicacion = Flask(__name__)

# Defino que es lo que pasa en el punto de inicio
@aplicacion.route("/")
def inicio():

    cabeza = """
    <!-- Inicio del trozo de cabeza -->
<!doctype html>
<html lang="es">
  <head>
    <title>El blog de Jose Vicente</title>
    <meta charset="utf-8">
    <style>
      body{background:grey;}
      header,main,footer{background:white;padding:20px;margin:auto;width:800px;}
    </style>
  </head>
  <body>
    <header>
      <h1>El blog de Jose Vicente</h1>
    </header>
    <main>
      <section>
<!-- Final del trozo de cabeza -->
    """

    cuerpo = ""

    # Ejecuto una petición sobre el cursor
    cursor.execute("SELECT * FROM entradas;")

    # Dame todas las filas
    entradas = cursor.fetchall()

    # Devuelveme todas las entradas
    for entrada in entradas:
        cuerpo += """
        	<article>
          	<h4>"""+entrada[1]+"""</h4>
            <time>"""+str(entrada[2])+"""</time>
            <p>"""+entrada[3]+"""</p>
          </article>
        """

    piedepagina = """
    <!-- Inicio del trozo de pie de pagina -->
      </section>
    </main>
    <footer>
      <p>(c) 2026 Jose Vicente Carratala</p>
    </footer>
  </body>
</html>
<!-- Final del trozo de pie de pagina -->
    """

    return cabeza + cuerpo + piedepagina


# Arranco la aplicación web
if __name__ == "__main__":
    aplicacion.run(debug=True)
```
**12-retoques.py**
```python

# Importo la libreria de MySQL
import mysql.connector

# Importo la libreria de Flask para presentar cosas en la web
from flask import Flask

# Me conecto a la base de datos con el usuario que acabo de crear
connection = mysql.connector.connect(
    host='localhost',
    user='blog2627',
    password='Blog2627$',
    database='blog2627'
)

# Creo un cursor para poder pedir cosas
cursor = connection.cursor()

# Creo una aplicación web
aplicacion = Flask(__name__)

# Defino que es lo que pasa en el punto de inicio
@aplicacion.route("/")
def inicio():

    cabeza = """
    <!-- Inicio del trozo de cabeza -->
<!doctype html>
<html lang="es">
  <head>
    <title>El blog de Jose Vicente</title>
    <meta charset="utf-8">
    <style>
      body{background:grey;}
      header,main,footer{background:white;padding:20px;margin:auto;width:800px;}
    </style>
  </head>
  <body>
    <header>
      <h1>El blog de Jose Vicente</h1>
    </header>
    <main>
    <p></p>
      <section>
      <hr>
<!-- Final del trozo de cabeza -->
    """

    cuerpo = ""

    # Ejecuto una petición sobre el cursor
    cursor.execute("SELECT * FROM entradas;")

    # Dame todas las filas
    entradas = cursor.fetchall()

    # Devuelveme todas las entradas
    for entrada in entradas:
        cuerpo += """
        	<article>
          	<h4>"""+entrada[1]+"""</h4>
            <time>"""+str(entrada[2])+"""</time>
            <p>"""+entrada[3]+"""</p>
          </article>
          <hr>
        """

    piedepagina = """
    <!-- Inicio del trozo de pie de pagina -->
      </section>
    </main>
    <footer>
      <p>(c) 2026 Jose Vicente Carratala</p>
    </footer>
  </body>
</html>
<!-- Final del trozo de pie de pagina -->
    """

    return cabeza + cuerpo + piedepagina


# Arranco la aplicación web
if __name__ == "__main__":
    aplicacion.run(debug=True)
```
**13-retoques css.py**
```python

# Importo la libreria de MySQL
import mysql.connector

# Importo la libreria de Flask para presentar cosas en la web
from flask import Flask

# Me conecto a la base de datos con el usuario que acabo de crear
connection = mysql.connector.connect(
    host='localhost',
    user='blog2627',
    password='Blog2627$',
    database='blog2627'
)

# Creo un cursor para poder pedir cosas
cursor = connection.cursor()

# Creo una aplicación web
aplicacion = Flask(__name__)

# Defino que es lo que pasa en el punto de inicio
@aplicacion.route("/")
def inicio():

    cabeza = """
    <!-- Inicio del trozo de cabeza -->
<!doctype html>
<html lang="es">
  <head>
    <title>El blog de Jose Vicente</title>
    <meta charset="utf-8">
    <style>
      body{background:grey;font-family:sans-serif;}
      header,main,footer{background:white;padding:20px;margin:auto;width:300px;}
      p{text-align:justify;font-size:11px;}
      .imagen{width:100%;height:200px;background:grey;border-radius:10px;
      background:url(https://media.licdn.com/dms/image/v2/D4D22AQHCNtw3Cp9Dyw/feedshare-shrink_800/feedshare-shrink_800/0/1710619757165?e=2147483647&v=beta&t=PU6PGO8fh-PhOx2V8ALEBeq5n1i5ooypcs76mQf7JHw);
      background-size:cover;background-position:center center;}
      section{display:grid;grid-template-columns:repeat(1,1fr);gap:20px;}
    </style>
  </head>
  <body>
    <header>
      <h1>El blog de Jose Vicente</h1>
    </header>
    <main>
    <p>Soy José Vicente Carratalá, docente, programador y desarrollador de software, con más de 25 años de experiencia en el ámbito de la informática y la formación tecnológica. Me apasionan la programación, la inteligencia artificial, las bases de datos y el desarrollo de aplicaciones web.
<br>
<br>A lo largo de mi trayectoria he combinado la enseñanza con la creación de proyectos tecnológicos propios, buscando siempre soluciones prácticas, innovadoras y accesibles. Me considero una persona curiosa, autodidacta y creativa, con una filosofía clara: aprender haciendo, experimentar constantemente y compartir el conocimiento.</p>
      <section>
  
<!-- Final del trozo de cabeza -->
    """

    cuerpo = ""

    # Ejecuto una petición sobre el cursor
    cursor.execute("SELECT * FROM entradas;")

    # Dame todas las filas
    entradas = cursor.fetchall()

    # Devuelveme todas las entradas
    for entrada in entradas:
        cuerpo += """
        	<article>
          	<div class='imagen'></div>
          	<h4>"""+entrada[1]+"""</h4>
            <time>"""+str(entrada[2])+"""</time>
            <p>"""+entrada[3]+"""</p>
          </article>
         
        """

    piedepagina = """
    <!-- Inicio del trozo de pie de pagina -->
      </section>
    </main>
    <footer>
      <p>(c) 2026 Jose Vicente Carratala</p>
    </footer>
  </body>
</html>
<!-- Final del trozo de pie de pagina -->
    """

    return cabeza + cuerpo + piedepagina


# Arranco la aplicación web
if __name__ == "__main__":
    aplicacion.run(debug=True)
```
## 02-Proyecto
**01-consultas.sql**
```sql
-- PROYECTO FINAL DE LA UNIDAD 3
-- Tienda de servicios Sturmprojekt.
-- Utilizamos las tablas y los datos existentes.

USE sturmprojekt;

-- 1. Consultamos el catálogo completo.
SELECT * FROM servicios;

-- 2. Seleccionamos columnas y utilizamos alias.
SELECT
nombre AS 'Nombre del servicio',
precio AS 'Precio del servicio'
FROM servicios;

-- 3. Ordenamos los precios en ambos sentidos.
SELECT nombre, precio
FROM servicios
ORDER BY precio ASC;

SELECT nombre, precio
FROM servicios
ORDER BY precio DESC;

-- 4. Operaciones aritméticas sobre los precios.
-- Solo calculan resultados: no cambian los datos.
SELECT
nombre,
precio,
precio + 20 AS suma,
precio - 20 AS resta,
precio * 20 AS multiplicacion,
precio / 20 AS division,
precio * 0.21 AS cuota_iva
FROM servicios;

-- 5. Comparaciones y operadores lógicos.
SELECT
nombre,
precio,
tipo,
precio > 500 AS caro,
tipo = 'Servicio' AS es_servicio,
precio * (precio > 500 AND tipo = 'Servicio') * 0.1
AS descuento_and,
precio * (precio > 500 OR tipo = 'Servicio') * 0.1
AS descuento_or
FROM servicios;

-- 6. Consultas resumen de los pedidos.
SELECT COUNT(id_cliente) FROM pedidos;
SELECT SUM(precio_acordado) FROM pedidos;
SELECT AVG(precio_acordado) FROM pedidos;
SELECT MAX(precio_acordado) FROM pedidos;
SELECT MIN(precio_acordado) FROM pedidos;

-- 7. Agrupamos los pedidos por estado y ordenamos el recuento.
SELECT
estado,
COUNT(id_cliente)
FROM pedidos
GROUP BY estado
ORDER BY COUNT(id_cliente) DESC;

-- 8. Relacionamos pedidos y clientes.
SELECT
pedidos.fecha_pedido,
clientes.nombre,
clientes.apellidos
FROM pedidos
LEFT JOIN clientes
ON pedidos.id_cliente = clientes.Identificador;

-- 9. Añadimos el servicio contratado.
SELECT
pedidos.fecha_pedido,
clientes.nombre,
clientes.apellidos,
servicios.nombre,
pedidos.precio_acordado
FROM pedidos
LEFT JOIN clientes
ON pedidos.id_cliente = clientes.Identificador
LEFT JOIN servicios
ON pedidos.id_servicio = servicios.id_servicio;

-- 10. Subconsulta: comparamos cada pedido con el promedio.
SELECT
fecha_pedido,
id_cliente,
precio_acordado,
precio_acordado > (
    SELECT AVG(precio_acordado) FROM pedidos
) AS porencima
FROM pedidos;

-- 11. Índices creados durante las prácticas de la Unidad 3.
-- No se ejecutan otra vez porque ya existen.
-- No hemos medido su efecto sobre el rendimiento.

/*
CREATE INDEX idx_servicios_precio
ON servicios(precio);

CREATE INDEX idx_pedidos_fecha
ON pedidos(fecha_pedido);
*/
```
**02-consulta desde python.py**
```python
# Consultamos los servicios desde Python.
import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='nurlukas',
    password='tame123',
    database='sturmprojekt'
)

cursor = connection.cursor()

cursor.execute("SELECT nombre, descripcion, precio FROM servicios")
filas = cursor.fetchall()

for fila in filas:
    print(fila)

cursor.close()
connection.close()
```
**03-tienda web.py**
```python
# Mostramos nuestro catálogo con Flask, HTML y CSS.
from flask import Flask
import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='nurlukas',
    password='tame123',
    database='sturmprojekt'
)

cursor = connection.cursor()

aplicacion = Flask(__name__)


@aplicacion.route("/")
def inicio():

    # Cabecera y estilos básicos.
    cabeza = """
    <!doctype html>
    <html lang="es">
    <head>
        <meta charset="utf-8">
        <title>Servicios Sturmprojekt</title>
        <style>
            body {
                background: grey;
                font-family: sans-serif;
            }
            header, main, footer {
                background: white;
                padding: 20px;
                margin: auto;
                max-width: 800px;
            }
            article {
                padding: 15px;
                border: 1px solid grey;
                margin-bottom: 15px;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Sturmprojekt</h1>
            <p>Catálogo de servicios</p>
        </header>
        <main>
    """

    cuerpo = ""

    # Recuperamos nombre, descripción y precio.
    cursor.execute(
        "SELECT nombre, descripcion, precio FROM servicios"
    )
    filas = cursor.fetchall()

    # Creamos una ficha para cada servicio.
    for fila in filas:
        cuerpo += """
        <article>
            <h2>""" + str(fila[0]) + """</h2>
            <p>""" + str(fila[1]) + """</p>
            <p>Precio: """ + str(fila[2]) + """ €</p>
        </article>
        """

    piedepagina = """
        </main>
        <footer>
            <p>Proyecto final de Bases de Datos — Unidad 3</p>
        </footer>
    </body>
    </html>
    """

    return cabeza + cuerpo + piedepagina


if __name__ == "__main__":
    aplicacion.run()
```
**04-instrucciones para ver la tienda.md.md**
```markdown
# Ver la tienda de Sturmprojekt desde Windows

Los archivos del proyecto se transfirieron desde Windows al servidor Ubuntu mediante FileZilla. 
La tienda se ejecuta en Ubuntu y se visualiza en el navegador de Windows mediante una conexión SSH.

## 1. Abrir la conexión desde Windows

en PowerShell 

ssh -L 5000:localhost:5000 nurlukas@IP_SERVIDOR (previamente investigue mi ip del servidor mediante el comando ifconfig, ya que la ip se actualiza constantemente)

ip ahora  mismo:192.168.1.29

La opción `-L 5000:localhost:5000` permite acceder desde el puerto 5000 de Windows al puerto 5000 de Ubuntu a través de SSH.

## 2. Entrar en la carpeta del proyecto en Ubuntu

Dentro de consola SSH, vamos a la carpeta donde transferiste los archivos con FileZilla:

cd "/ruta/de/la/carpeta"

Sustituye `/ruta/de/la/carpeta` por la ruta real de destino en Ubuntu, no por una ruta de Windows.

Comprueba que los archivos están presentes:

ls

Debe aparecer el archivo `03-tienda web.py`.

## 3. Comprobar la conexión con MySQL

connection = mysql.connector.connect(
    host='localhost',
    user='nurlukas',
    password='tame123',
    database='sturmprojekt'
)

Si lo corriges en Windows, vuelve a transferir el archivo actualizado mediante FileZilla.

`localhost` es correcto porque Python y MySQL se ejecutan en el mismo servidor Ubuntu. La contraseña de MySQL puede ser distinta de la contraseña SSH.

## 4. Iniciar la tienda

Desde la carpeta del proyecto, ejecuta:

python3 "03-tienda web.py"

Este comando se ejecuta en la terminal de Ubuntu, no dentro de la consola `mysql>`.

Para arrancar correctamente, Ubuntu debe tener disponibles Flask y MySQL Connector para Python, y MySQL debe estar funcionando con la base `sturmprojekt` y su tabla `servicios`.

Si la aplicación arranca, aparecerá un mensaje similar a:

Running on http://127.0.0.1:5000

## 5. Abrir la tienda en Windows

Abre el navegador de Windows y entra en:

[http://localhost:5000](http://localhost:5000)

La página mostrará el nombre, la descripción y el precio de los servicios almacenados en `sturmprojekt`.

Mantén abierta la conexión SSH y el programa Python mientras utilizas la tienda. No es necesario modificar el código para escuchar en todas las interfaces ni abrir el puerto 5000 del servidor: el acceso se realiza mediante el túnel SSH.

```
## 03-Resultado aprendizaje
**RA3.MD**
```markdown
# Resultado de aprendizaje 3

## Resultado de aprendizaje
Consulta la información almacenada en una base de datos empleando asistentes, herramientas gráficas y el lenguaje de manipulación de datos.

*Criterios de evaluación*
a) Se han identificado las herramientas y sentencias para realizar consultas.
Se utiliza la consola de MySQL y se ejecutan sentencias como SHOW DATABASES, USE, SHOW TABLES y SELECT. 
También se realizan consultas desde Python mediante mysql.connector.

b) Se han realizado consultas simples sobre una tabla.
Se consultan tablas completas y columnas concretas. 
Por ejemplo: SELECT nombre, apellidos FROM clientes. 
También se utilizan alias y expresiones calculadas.

c) Se han realizado consultas sobre el contenido de varias tablas mediante composiciones internas.


d) Se han realizado consultas sobre el contenido de varias tablas mediante composiciones externas.
Se han mostrado ejemplos de LEFT JOIN. 
Se relacionan matriculas, alumnos y asignaturas.

e) Se han realizado consultas resumen.
Se utilizan COUNT, SUM, AVG, MAX y MIN. 
También se agrupan registros con GROUP BY y se ordenan los resultados con ORDER BY.

f) Se han realizado consultas con subconsultas.
Se utiliza una subconsulta que calcula AVG(importe), para comparar el importe de cada pedido con el promedio.

g) Se han realizado consultas que implican múltiples selecciones.


h) Se han aplicado criterios de optimización de consultas.


# Me faltan la C, G, Y H.
```
