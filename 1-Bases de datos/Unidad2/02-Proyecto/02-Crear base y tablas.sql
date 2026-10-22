
CREATE DATABASE sturmprojekt
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE sturmprojekt;
SET NAMES utf8mb4;

CREATE TABLE clientes (
    nombre VARCHAR(100) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    proyecto VARCHAR(100) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE servicios (
    id_servicio INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id_servicio)
) ENGINE=InnoDB;

CREATE TABLE pedidos (
    id_pedido INT NOT NULL AUTO_INCREMENT,
    id_cliente INT NOT NULL,
    id_servicio INT NOT NULL,
    fecha_pedido DATE NOT NULL,
    estado VARCHAR(50) NOT NULL,
    precio_acordado DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id_pedido)
) ENGINE=InnoDB;

SHOW TABLES;
