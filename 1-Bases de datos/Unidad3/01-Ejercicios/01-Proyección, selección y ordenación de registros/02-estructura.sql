-- Adaptacion del archivo de clase a la base sturmprojekt de la Unidad 2.
-- Conserva las operaciones de definicion de tablas, claves, relaciones e indices.
-- La tienda de clase tiene diez tablas; nuestro modelo tiene tres.
-- servicios ocupa el papel del catalogo de productos; pedidos relaciona
-- cada cliente con el servicio contratado. No se inventan tablas adicionales.

-- ============================================================
-- 1. BASE DE DATOS: TRABAJO REALIZADO EN LA UNIDAD 2
-- ============================================================
-- En clase se borra y se vuelve a crear tienda_practicas.
-- Aqui se documenta la creacion, pero NO se ejecuta porque sturmprojekt
-- ya existe y contiene datos de la Unidad 2.
-- DROP DATABASE eliminaria tambien sus tablas, datos y vista_completa.
-- El usuario nurlukas ha recibido un error de permisos al intentar crear
-- tienda_practicas. Para este archivo utilizamos su base existente.

/* CREACION DOCUMENTADA: NO EJECUTAR SOBRE LA BASE EXISTENTE.
CREATE DATABASE sturmprojekt
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
*/

-- Selecciona la base sobre la que vamos a trabajar.
USE sturmprojekt;

-- ============================================================
-- 2. CLIENTES: TABLA Y CLAVE CREADAS EN LA UNIDAD 2
-- ============================================================
-- Almacena los datos del cliente y el proyecto solicitado.
-- VARCHAR(100) almacena textos de hasta 100 caracteres.
-- PRIMARY KEY identifica cada fila de forma unica.
-- AUTO_INCREMENT genera el identificador al insertar clientes.
-- Esta definicion reproduce los campos y la nulabilidad mostrados
-- por tu DESCRIBE. Se deja comentada porque la tabla ya existe.

/* ESTRUCTURA DOCUMENTADA: NO VOLVER A CREAR.
CREATE TABLE clientes (
    nombre VARCHAR(100),
    apellidos VARCHAR(100),
    email VARCHAR(100),
    proyecto VARCHAR(100),
    Identificador INT AUTO_INCREMENT PRIMARY KEY
);
*/

-- ============================================================
-- 3. SERVICIOS: TABLA CREADA EN LA UNIDAD 2
-- ============================================================
-- Equivale al catalogo de productos del ejemplo de clase.
-- tipo distingue productos y servicios dentro de tu catalogo.
-- TEXT permite descripciones extensas.
-- DECIMAL(10,2) guarda importes con diez cifras en total y dos decimales.
-- NOT NULL exige un valor en los campos indicados.

/* ESTRUCTURA DOCUMENTADA: NO VOLVER A CREAR.
CREATE TABLE servicios (
    id_servicio INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id_servicio)
) ENGINE=InnoDB;
*/

-- ============================================================
-- 4. PEDIDOS Y RELACIONES: TRABAJO DE LA UNIDAD 2
-- ============================================================
-- Registra que cliente contrata que servicio, en que fecha,
-- en que estado esta el pedido y que precio se ha acordado.
-- DATE almacena una fecha.
-- FOREIGN KEY impide referenciar clientes o servicios inexistentes.
-- InnoDB es el motor utilizado en los archivos de la Unidad 2.
-- Las relaciones corresponden al modelo documentado en esa unidad.
-- DESCRIBE muestra los campos y claves, pero no la definicion completa
-- de las restricciones; esta se documenta a partir de los archivos SQL.

/* ESTRUCTURA DOCUMENTADA: NO VOLVER A CREAR.
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
*/

-- ============================================================
-- 5. RESTRICCIONES DOCUMENTADAS EN EL PROYECTO DE LA UNIDAD 2
-- ============================================================
-- CHECK valida una condicion antes de admitir los datos.
-- El patron del correo comprueba su formato, no que la cuenta exista.
-- Los otros CHECK impiden precios negativos.
-- No se ejecutan de nuevo. Su presencia en tu servidor no puede
-- confirmarse unicamente con los resultados de DESCRIBE facilitados.

/* RESTRICCIONES DEL PROYECTO ANTERIOR: NO DUPLICAR.
ALTER TABLE clientes
ADD CONSTRAINT chk_clientes_email
CHECK (email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+[.][A-Za-z]{2,}$');

ALTER TABLE servicios
ADD CONSTRAINT chk_servicios_precio CHECK (precio >= 0);

ALTER TABLE pedidos
ADD CONSTRAINT chk_pedidos_precio CHECK (precio_acordado >= 0);
*/

-- ============================================================
-- 6. INDICES PARA PRACTICAR OPTIMIZACION: UNIDAD 3
-- ============================================================
-- El original crea indices sobre campos de su tienda.
-- Se adaptan a los campos disponibles en nuestro modelo.
-- Un indice puede facilitar determinadas busquedas y ordenaciones.
-- No demuestra por si solo una mejora de tiempo: aqui no se mide.
-- No se crean indices de ciudad, provincia o categoria porque esos
-- campos no existen en nuestras tres tablas.
-- Las claves primarias ya tienen indice. No se vuelven a indexar.
-- Los campos id_cliente e id_servicio ya aparecen como MUL en DESCRIBE:
-- no anadimos otro indice simple sobre ellos.
-- EJECUTAR ESTAS DOS CREACIONES UNA SOLA VEZ.
-- Si ya existe un indice con el mismo nombre, MySQL dara un error.

-- Equivalente a idx_productos_precio del archivo original.
CREATE INDEX idx_servicios_precio
ON servicios(precio);

-- Equivalente a idx_pedidos_fecha del archivo original.
CREATE INDEX idx_pedidos_fecha
ON pedidos(fecha_pedido);

-- No se insertan datos en este archivo: corresponde al archivo 03.
-- La vista_completa existente se conserva; no se redefine aqui,
-- porque el archivo de estructura original tampoco crea vistas.
