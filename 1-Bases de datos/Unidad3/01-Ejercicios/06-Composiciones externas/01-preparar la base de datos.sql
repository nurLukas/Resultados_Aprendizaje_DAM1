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