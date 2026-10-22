SHOW TABLES;

CREATE TABLE servicios (
    id_servicio INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id_servicio)
) ENGINE=InnoDB;