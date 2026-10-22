SHOW TABLES;

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

SHOW TABLES;