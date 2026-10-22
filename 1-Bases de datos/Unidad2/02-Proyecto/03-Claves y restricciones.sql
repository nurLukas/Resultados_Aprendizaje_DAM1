USE sturmprojekt;

ALTER TABLE clientes
  ADD COLUMN Identificador INT NOT NULL AUTO_INCREMENT PRIMARY KEY;


ALTER TABLE clientes
  ADD CONSTRAINT chk_clientes_email
  CHECK (email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+[.][A-Za-z]{2,}$');

ALTER TABLE servicios
  ADD CONSTRAINT chk_servicios_precio CHECK (precio >= 0);

ALTER TABLE pedidos
  ADD CONSTRAINT chk_pedidos_precio CHECK (precio_acordado >= 0),
  ADD CONSTRAINT fk_cliente FOREIGN KEY (id_cliente)
    REFERENCES clientes (Identificador)
    ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT fk_servicio FOREIGN KEY (id_servicio)
    REFERENCES servicios (id_servicio)
    ON DELETE RESTRICT ON UPDATE RESTRICT;

DESCRIBE clientes;
DESCRIBE servicios;
DESCRIBE pedidos;
