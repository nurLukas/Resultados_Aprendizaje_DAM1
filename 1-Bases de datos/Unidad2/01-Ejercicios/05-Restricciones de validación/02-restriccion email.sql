ALTER TABLE clientes
ADD CONSTRAINT chk_clientes_email
CHECK (
    email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
);

+----------------+---------------------+-------------------------------+-----------------------------------+---------------+
| nombre         | apellidos           | email                         | proyecto                          | Identificador |
+----------------+---------------------+-------------------------------+-----------------------------------+---------------+
| Lucas Ezequiel | Andrés Griego       | admin@jsturmprojekt.es        | plataforma completa               |             1 |
| Juan           | García Lopez        | juan@garcia.com               | Plataforma basica                 |             2 |
| Ana            | Fernández Ruiz      | ana.fernandez@example.com     | Landing Web                       |             3 |
| Carlos         | Medina López        | carlos.medina@example.com     | Plataforma Completa               |             4 |
| Laura          | Sánchez Pérez       | laura.sanchez@example.com     | Plataforma Básica                 |             5 |
| Daniel         | Navarro Martín      | daniel.navarro@example.com    | Landing Web                       |             6 |
| Sofía          | Romero García       | sofia.romero@example.com      | Plataforma Completa               |             7 |
| Marta          | Vega Torres         | marta.vega@example.com        | Plataforma Básica                 |             8 |
| Alejandro      | Morales Díaz        | alejandro.morales@example.com | Gestión de dominio/Despliegue     |             9 |
| Elena          | Castillo Fernández  | elena.castillo@example.com    | Mantenimiento + Servicio Técnico  |            10 |
+----------------+---------------------+-------------------------------+-----------------------------------+---------------+
(Nuesta tabla no necesita ser rectificada antes de aplicar el ALTER TABLE, ya que cumple desde el principio con la restriccion del email aplicado.

# Si algun cliente no cumpliese la restriccion de email, deberia borrarlo, antes de aplicarla, porque nos dara un error si tuvieramos un dato que no cumple la restriccion.
DELETE FROM clientes WHERE Identificador = 4;  (elimino el cliente que no cumple la condición, para luego generar el ALTER TABLE que aplica la condición)

Rectificado ello, ya puedo dar el siguiente comando:

ALTER TABLE clientes
ADD CONSTRAINT chk_clientes_email
CHECK (
    email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
);