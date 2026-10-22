# Reporte de proyecto

## Información de generación

- **Fecha:** 2026-10-19 20:28:56 +0200
- **Usuario:** lucas
- **Equipo:** LUCAS
- **Sistema operativo:** Windows
- **Arquitectura:** x86_64
- **Directorio de ejecución:** `D:/Herramientas/portables/jocarsa-generador-windows-x64`
- **Proyecto documentado:** `D:/Resultados Aprendizaje_DAM1/1-Bases de datos/Unidad2`
- **HMAC-SHA-256 de autenticidad:** `72e58c7230c0000415b07c081e2fd3a4c08ee21e38e5538b13716f5561b7fdcb`

> El HMAC-SHA-256 se calcula sobre el documento completo usando un secreto incluido en el programa y 64 ceros en el propio campo del HMAC. El secreto no se escribe en el informe. Este mecanismo permite comprobar integridad y que el documento fue generado con el mismo secreto.

## Estructura del proyecto

```
D:/Resultados Aprendizaje_DAM1/1-Bases de datos/Unidad2
├── 01-Ejercicios
│   ├── 01-Modelo de datos
│   │   └── 01-Modelo de datos.md
│   ├── 02-Terminología del modelo relacional
│   │   ├── 01-Instalar mysql.md
│   │   ├── 02-Terminologia.md
│   │   ├── 03-Listar bases de datos existentes.sql
│   │   ├── 04-Crear mi propia base de datos.sql
│   │   ├── 05-Usar la base de datos.sql
│   │   ├── 06-Crear tabla.sql
│   │   ├── 07-Describir la tabla.sql
│   │   ├── 08-Insertar un registro.sql
│   │   ├── 09-Leer registros.sql
│   │   └── 10-Resumen de la clase de hoy.md
│   ├── 03-Tipos de datos
│   │   └── 01-mysql tiene tipos de datos.md
│   ├── 04-Claves primarias
│   │   ├── 01-Repaso de como entrar en MySQL.md
│   │   ├── 02-repaso de creación de tablas.sql
│   │   ├── 03-altero la tabla.sql
│   │   └── 04-inserto un nuevo cliente.sql
│   ├── 05-Restricciones de validación
│   │   ├── 01-introduzco email plano.sql
│   │   ├── 02-restriccion email.sql
│   │   ├── 03-primero lo intento mal.sql
│   │   └── 04-ahora lo intento bien.sql
│   ├── 08-Claves ajenas
│   │   ├── 01-creamos servicios.sql
│   │   ├── 02-creamos pedidos.sql
│   │   ├── 03-50 clientes ficticios.sql
│   │   ├── 04-5 servicios de prueba.sql
│   │   └── 05-50 pedidos.sql
│   ├── 09-Vistas
│   │   ├── 01-repaso.md
│   │   ├── 02-select join.sql
│   │   ├── 03-uno con clientes.sql
│   │   ├── 04-ahora cruzo con servicios.sql
│   │   └── 05-creo vista.sql
│   ├── 10-Usuarios. Privilegios
│   │   ├── 01-usuario root.md
│   │   ├── 03-creo un nuevo usuario.sql
│   │   ├── 04-dar privilegios.sql
│   │   ├── 05-limites.sql
│   │   ├── 06-permiso especifico.sql
│   │   ├── 07-refrescar privilegios.sql
│   │   ├── 08-ahora salgo.sql
│   │   ├── 09-ahora entro con el nuevo usuario.sql
│   │   └── 2-crear usuario.sql
│   └── 11-Lenguaje de descripción de datos (DDL)
│       └── 01-Ejercicio de final de unidad.md
├── 02-Proyecto
│   ├── 01-Guia del proyecto.md
│   ├── 02-Crear base y tablas.sql
│   ├── 03-Claves y restricciones.sql
│   ├── 04-Datos de prueba.sql
│   ├── 05-Consultas y vista.sql
│   └── 06-Usuario y privilegios.sql
└── 03-Resultado aprendizaje
    └── RA2.md
```

## Bases de datos SQLite

Esta sección documenta únicamente el esquema de las bases SQLite detectadas. No se vuelcan registros ni datos de usuario.

No se han encontrado bases SQLite con extensiones .db, .sqlite o .sqlite3.

## Código (intercalado)

# Unidad2
## 01-Ejercicios
### 01-Modelo de datos
**01-Modelo de datos.md**
```markdown
# Concesionario de coches

- Coche	(Representa una tabla)
	-Id
	-Modelo - string
	-Marca - string
	-Año - int
	-Matricula - string
	-Número de bastidor - string
	-Color - string
	-Precio - float
	
- Clientes	(Representa otra tabla)
	-Id
	-Nombre
	-Apellidos
	-DNI 1:1
	-Fecha de nacimiento 1:1
	-Número de teléfono 1:n
	-correo electronico 1:n
	
- Pedidos	(Representa otra tabla más)
	-Número de pedido
	-Fecha de pedido
	-Id cliente FK
	-Id coche FK
	
	
```
### 02-Terminología del modelo relacional
**01-Instalar mysql.md**
```markdown
1.-Terminal (en aplicaciones o Control + Mayusculas + T)
2.-sudo apt update
3.-sudo apt install mysql-server
4.-sudo mysql_secure_installation

Entramos en MySQL:
5.-sudo mysql -u root -p

Si queréis salir de MySQL:
exit;
```
**02-Terminologia.md**
```markdown
# Servidor
	##  ases de datos
		Base de datos 1
			Tabla 1
				Columna 1
				Columna 2
				Columna 3
				Columna 4
				Columna 5
				...
				Registros (filas o tuplas)
			Tabla 2
			Tabla 3
			Tabla 4
			Tabla 5
				...
		Base de datos 2
		Base de datos 3
		Base de datos 4
		Base de datos 5
		Base de datos 6
				...
```
**03-Listar bases de datos existentes.sql**
```sql
sudo  mysql -u root -p
SHOW DATABASES;
```
**04-Crear mi propia base de datos.sql**
```sql
CREATE DATABASE sturmprojekt;
```
**05-Usar la base de datos.sql**
```sql
USE sturmprojekt;
```
**06-Crear tabla.sql**
```sql
SHOW TABLES;

CREATE TABLE clientes(
	nombre VARCHAR(100),
	apellidos VARCHAR(100),
	email VARCHAR(100),
	proyecto VARCHAR(100)
);

SHOW TABLES;
```
**07-Describir la tabla.sql**
```sql
DESCRIBE clientes;
```
**08-Insertar un registro.sql**
```sql
INSERT INTO clientes VALUES(
	"Lucas Ezequiel",
	"Andrés Griego",
	"admin@jsturmprojekt.es",
	"plataforma completa"
);
```
**09-Leer registros.sql**
```sql
SELECT * FROM clientes;
```
**10-Resumen de la clase de hoy.md**
```markdown
Hemos abierto la máquina virtual
Hemos instalado MySQL Server
Hemos iniciado sesión con MySQL

Hemos listado las bases de datos show
Hemos creado una base de datos create
Hemos entrado en la base datos use

Hemos listado las tablas de esa base de datos show
Hemos creado una nueva tabla create
Hemos insertado un registro insert
Hemos obtenido un listado de los registros select
```
### 03-Tipos de datos
**01-mysql tiene tipos de datos.md**
```markdown
VARCHAR - Cadenas de caracteres "cortas"
TEXT    - Bloques de texto muy largos
DATE    - Fechas
INT     - Números enteros

# Númericos:
TINYINT     -  1B   = 0-225  (puede representar valores de 0 a 255)
SMALLINT    -  2B   = 65.536
MEDIUMINT   -  3B   = 16.700.000
INT         -  4B   = 4.294.967.296
BIGINT	    -  8B   = 18.446.744.073.709.551.616

1TB =  1024 * 1024 * 1024 * 1024 = 1.099.511.627.776

# DECIMAL (números con decimales)
	FLOAT
	DOUBLE
	REAL

BIT       1b
BOOLEAN   1b
SERIAL

# Fecha:
	DATE       - fecha
	DATETIME   - fecha y hora
	TIME       - hora
	YEAR       - año

# Cadena:
	VARCAHR
	CHAR     - 1 solo caracter
	TINYTEXT           - 1B
	TEXT               - 2B
	MEDIUMTEXT         - 3B
	LONGTEXT           - 4B

```
### 04-Claves primarias
**01-Repaso de como entrar en MySQL.md**
```markdown
1.-Abrid la máquina virtual de Linux
2.-Introducis en la terminal: sudo mysql -u root -p
3.-Ponéis la contraseña 
4.-accedéis a la consola de mysql

5.-listamos las bases de datos - SHOW DATABASES;
6.-Usamos nuestra base de datos - USE sturmprojekt;
7.-Listamos las tablas - SHOW TABLES;
8.-Que forma tiene clientes: DESCRIBE clientes;
9.-Seleccionar los registros de clientes: SELECT * FROM clientes; 

10.-Insertar exactamente el mismo cliente:
INSERT INTO clientes VALUES('Lucas Ezequiel','Andrés Griego','admin@jsturmprojekt.es','plataforma completa');

11.-Listo de nuevo
```
**02-repaso de creación de tablas.sql**
```sql
CREATE TABLE clientes(
	nombre VARCHAR(100),
	apellidos VARCHAR(100),
	email VARCHAR(100)
);
```
**03-altero la tabla.sql**
```sql
ALTER TABLE clientes
ADD COLUMN Identificador INT AUTO_INCREMENT PRIMARY KEY;

SELECT * FROM clientes;
```
**04-inserto un nuevo cliente.sql**
```sql
INSERT INTO clientes VALUES(
	'Juan',
	'García Lopez',
	'juan@garcia.com',
	'Plataforma basica',
	NULL
);

SELECT * FROM clientes;
```
### 05-Restricciones de validación
**01-introduzco email plano.sql**
```sql
INSERT INTO clientes VALUES(
	'Jaime',
	'Martinez',
	"Hola que tal",
	'Plataforma basica',
  NULL
);

SELECT * FROM clientes;
```
**02-restriccion email.sql**
```sql
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
```
**03-primero lo intento mal.sql**
```sql
INSERT INTO clientes VALUES(
	'Sofía',
	'Romero García',
	"Hola que tal",
	'Plataforma Completa',
	NULL
);
```
**04-ahora lo intento bien.sql**
```sql
INSERT INTO clientes VALUES(
	'Sofía',
	'Romero García',
	'sofia.romero@example.com',
	'Plataforma Completa',
	NULL
);
```
### 08-Claves ajenas
**01-creamos servicios.sql**
```sql
SHOW TABLES;

CREATE TABLE servicios (
    id_servicio INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id_servicio)
) ENGINE=InnoDB;
```
**02-creamos pedidos.sql**
```sql
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
```
**03-50 clientes ficticios.sql**
```sql
USE sturmprojekt;

INSERT INTO clientes
(nombre, apellidos, email, proyecto)VALUES
('Adrián', 'Martínez López', 'adrian.martinez@example.com', 'Plataforma Básica'),
('Lucía', 'Fernández García', 'lucia.fernandez@example.com', 'Landing Web'),
('Pablo', 'Rodríguez Sánchez', 'pablo.rodriguez@example.com', 'Plataforma Completa'),
('Marina', 'González Torres', 'marina.gonzalez@example.com', 'Gestión de dominio/Despliegue'),
('Sergio', 'Ramírez Díaz', 'sergio.ramirez@example.com', 'Mantenimiento + Servicio Técnico'),
('Claudia', 'Moreno Pérez', 'claudia.moreno@example.com', 'Plataforma Básica'),
('Hugo', 'Jiménez Romero', 'hugo.jimenez@example.com', 'Landing Web'),
('Paula', 'Ruiz Navarro', 'paula.ruiz@example.com', 'Plataforma Completa'),
('Diego', 'Molina Castro', 'diego.molina@example.com', 'Gestión de dominio/Despliegue'),
('Irene', 'Ortega Herrera', 'irene.ortega@example.com', 'Mantenimiento + Servicio Técnico'),
('Álvaro', 'Delgado Martín', 'alvaro.delgado@example.com', 'Plataforma Completa'),
('Natalia', 'Vargas León', 'natalia.vargas@example.com', 'Plataforma Básica'),
('Mario', 'Santos Cabrera', 'mario.santos@example.com', 'Landing Web'),
('Carmen', 'Flores Medina', 'carmen.flores@example.com', 'Mantenimiento + Servicio Técnico'),
('Javier', 'Reyes Gil', 'javier.reyes@example.com', 'Gestión de dominio/Despliegue'),
('Valeria', 'Campos Rojas', 'valeria.campos@example.com', 'Plataforma Básica'),
('Rubén', 'Núñez Prieto', 'ruben.nunez@example.com', 'Plataforma Completa'),
('Aitana', 'Serrano Vega', 'aitana.serrano@example.com', 'Landing Web'),
('Óscar', 'Iglesias Fuentes', 'oscar.iglesias@example.com', 'Mantenimiento + Servicio Técnico'),
('Noelia', 'Cruz Márquez', 'noelia.cruz@example.com', 'Gestión de dominio/Despliegue'),
('Iván', 'Peña Soler', 'ivan.pena@example.com', 'Plataforma Básica'),
('Sara', 'Aguilar Molina', 'sara.aguilar@example.com', 'Landing Web'),
('Raúl', 'Pascual Nieto', 'raul.pascual@example.com', 'Plataforma Completa'),
('Eva', 'Blanco Carmona', 'eva.blanco@example.com', 'Mantenimiento + Servicio Técnico'),
('Víctor', 'Gallego Rubio', 'victor.gallego@example.com', 'Gestión de dominio/Despliegue'),
('Alba', 'Domínguez Cortés', 'alba.dominguez@example.com', 'Plataforma Básica'),
('Nicolás', 'Esteban Lozano', 'nicolas.esteban@example.com', 'Landing Web'),
('Andrea', 'Bravo Márquez', 'andrea.bravo@example.com', 'Plataforma Completa'),
('Samuel', 'Vidal Santos', 'samuel.vidal@example.com', 'Gestión de dominio/Despliegue'),
('Julia', 'Cordero Paredes', 'julia.cordero@example.com', 'Mantenimiento + Servicio Técnico'),
('Gabriel', 'Montes Rivas', 'gabriel.montes@example.com', 'Plataforma Completa'),
('Carla', 'Hidalgo Mora', 'carla.hidalgo@example.com', 'Plataforma Básica'),
('David', 'Prieto Alonso', 'david.prieto@example.com', 'Landing Web'),
('Nerea', 'Salazar Peña', 'nerea.salazar@example.com', 'Mantenimiento + Servicio Técnico'),
('Enrique', 'Fuentes Lara', 'enrique.fuentes@example.com', 'Gestión de dominio/Despliegue'),
('Olivia', 'Carrasco León', 'olivia.carrasco@example.com', 'Plataforma Básica'),
('Bruno', 'Méndez Varela', 'bruno.mendez@example.com', 'Plataforma Completa'),
('Rocío', 'Pérez Hidalgo', 'rocio.perez@example.com', 'Landing Web'),
('Guillermo', 'Soto Roldán', 'guillermo.soto@example.com', 'Mantenimiento + Servicio Técnico'),
('Teresa', 'Acosta Castaño', 'teresa.acosta@example.com', 'Gestión de dominio/Despliegue'),
('Joel', 'Román Ibáñez', 'joel.roman@example.com', 'Plataforma Básica'),
('Miriam', 'Lorenzo Escobar', 'miriam.lorenzo@example.com', 'Landing Web'),
('Marcos', 'Calvo Segura', 'marcos.calvo@example.com', 'Plataforma Completa'),
('Elisa', 'Ponce Beltrán', 'elisa.ponce@example.com', 'Gestión de dominio/Despliegue'),
('Fernando', 'Nieto Zamora', 'fernando.nieto@example.com', 'Mantenimiento + Servicio Técnico'),
('Beatriz', 'Suárez Robles', 'beatriz.suarez@example.com', 'Plataforma Completa'),
('Cristian', 'Herrero Vidal', 'cristian.herrero@example.com', 'Plataforma Básica'),
('Silvia', 'Arias Cifuentes', 'silvia.arias@example.com', 'Landing Web'),
('Roberto', 'Lara Benítez', 'roberto.lara@example.com', 'Gestión de dominio/Despliegue'),
('Patricia', 'Ferrer Montero', 'patricia.ferrer@example.com', 'Mantenimiento + Servicio Técnico');
```
**04-5 servicios de prueba.sql**
```sql
USE sturmprojekt;

INSERT INTO servicios
(nombre, tipo, descripcion, precio)VALUES
('Plataforma Básica', 'Producto',
 'Desarrollo web básico', 250.00),

('Plataforma Completa', 'Producto',
 'Desarrollo web completo', 350.00),

('Landing Web', 'Producto',
 'Página web estática', 150.00),

('Gestión de dominio/Despliegue', 'Servicio',
 'Configuración de dominio, DNS, hosting y despliegue web',
 35.00),

('Mantenimiento + Servicio Técnico', 'Servicio',
 'Mantenimiento, resolución de incidencias y soporte técnico',
 35.00);
```
**05-50 pedidos.sql**
```sql
USE sturmprojekt;

INSERT INTO pedidos
(id_cliente, id_servicio, fecha_pedido, estado, precio_acordado)VALUES
(11, 1, '2026-07-01', 'Finalizado', 250.00),
(12, 3, '2026-07-03', 'Finalizado', 150.00),
(13, 2, '2026-07-05', 'Finalizado', 350.00),
(14, 4, '2026-07-08', 'Finalizado', 35.00),
(15, 5, '2026-07-11', 'Finalizado', 35.00),

(16, 1, '2026-07-14', 'Finalizado', 250.00),
(17, 3, '2026-07-16', 'Finalizado', 150.00),
(18, 2, '2026-07-19', 'Finalizado', 350.00),
(19, 4, '2026-07-22', 'Finalizado', 35.00),
(20, 5, '2026-07-25', 'Finalizado', 35.00),

(21, 2, '2026-07-28', 'Finalizado', 350.00),
(22, 1, '2026-07-31', 'Finalizado', 250.00),
(23, 3, '2026-08-02', 'Finalizado', 150.00),
(24, 5, '2026-08-05', 'Finalizado', 35.00),
(25, 4, '2026-08-07', 'Finalizado', 35.00),

(26, 1, '2026-08-10', 'Finalizado', 250.00),
(27, 2, '2026-08-13', 'Finalizado', 350.00),
(28, 3, '2026-08-16', 'Finalizado', 150.00),
(29, 5, '2026-08-19', 'Finalizado', 35.00),
(30, 4, '2026-08-22', 'Finalizado', 35.00),

(31, 1, '2026-08-25', 'Finalizado', 250.00),
(32, 3, '2026-08-28', 'Finalizado', 150.00),
(33, 2, '2026-08-31', 'En desarrollo', 350.00),
(34, 5, '2026-09-02', 'Finalizado', 35.00),
(35, 4, '2026-09-04', 'Finalizado', 35.00),

(36, 1, '2026-09-06', 'En desarrollo', 250.00),
(37, 3, '2026-09-08', 'Finalizado', 150.00),
(38, 2, '2026-09-10', 'En desarrollo', 350.00),
(39, 4, '2026-09-12', 'Finalizado', 35.00),
(40, 5, '2026-09-14', 'En desarrollo', 35.00),

(41, 2, '2026-09-16', 'En desarrollo', 350.00),
(42, 1, '2026-09-18', 'En desarrollo', 250.00),
(43, 3, '2026-09-20', 'Finalizado', 150.00),
(44, 5, '2026-09-22', 'En desarrollo', 35.00),
(45, 4, '2026-09-24', 'Finalizado', 35.00),

(46, 1, '2026-09-26', 'En desarrollo', 250.00),
(47, 2, '2026-09-28', 'En desarrollo', 350.00),
(48, 3, '2026-09-30', 'Pendiente', 150.00),
(49, 5, '2026-10-02', 'Pendiente', 35.00),
(50, 4, '2026-10-03', 'Pendiente', 35.00),

(51, 1, '2026-10-04', 'En desarrollo', 250.00),
(52, 3, '2026-10-05', 'Pendiente', 150.00),
(53, 2, '2026-10-06', 'En desarrollo', 350.00),
(54, 4, '2026-10-07', 'Pendiente', 35.00),
(55, 5, '2026-10-08', 'Pendiente', 35.00),

(56, 2, '2026-10-09', 'En desarrollo', 350.00),
(57, 1, '2026-10-11', 'Pendiente', 250.00),
(58, 3, '2026-10-13', 'Pendiente', 150.00),
(59, 4, '2026-10-15', 'Pendiente', 35.00),
(60, 5, '2026-10-18', 'Pendiente', 35.00);
```
### 09-Vistas
**01-repaso.md**
```markdown
sudo mysql -u root -p

SHOW DATABASES;

USE sturmprojekt;

SHOW TABLES;

DESCRIBE clientes;
DESCRIBE servicios;
DESCRIBE pedidos;

SELECT * FROM clientes;
SELECT * FROM servicios;
SELECT * FROM pedidos;
```
**02-select join.sql**
```sql
SELECT
    pedidos.fecha_pedido,
    pedidos.id_pedido
FROM pedidos;
```
**03-uno con clientes.sql**
```sql
SELECT
    pedidos.fecha_pedido,
    pedidos.id_pedido,
    clientes.nombre,
    clientes.apellidos
FROM pedidos
LEFT JOIN clientes
ON pedidos.id_cliente = clientes.Identificador;


# El LEFT JOIN permite relacionar dos tablas mediante una columna común.
```
**04-ahora cruzo con servicios.sql**
```sql
SELECT
    pedidos.fecha_pedido,
    pedidos.id_pedido,
    clientes.nombre,
    clientes.apellidos,
    servicios.nombre AS producto,
    servicios.precio

FROM pedidos
LEFT JOIN clientes
    ON pedidos.id_cliente = clientes.Identificador
LEFT JOIN servicios
    ON pedidos.id_servicio = servicios.id_servicio;
```
**05-creo vista.sql**
```sql
USE sturmprojekt;

CREATE VIEW vista_completa AS
SELECT
    pedidos.fecha_pedido AS 'fecha del pedido',
    pedidos.id_pedido AS 'numero de pedido',
    clientes.nombre AS 'nombre del cliente',
    clientes.apellidos AS 'apellidos del cliente',
    servicios.nombre AS 'nombre del producto',
    servicios.precio AS 'precio del producto'

FROM pedidos
LEFT JOIN clientes
    ON pedidos.id_cliente = clientes.Identificador
LEFT JOIN servicios
    ON pedidos.id_servicio = servicios.id_servicio;
```
### 10-Usuarios. Privilegios
**01-usuario root.md**
```markdown
sudo mysql -u root -p
```
**03-creo un nuevo usuario.sql**
```sql
CREATE USER 'nurlucas'@'localhost' IDENTIFIED BY 'tame123';
```
**04-dar privilegios.sql**
```sql
GRANT USAGE ON *.* TO 'nurlucas'@'localhost';
```
**05-limites.sql**
```sql
ALTER USER 'nurlucas'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;
```
**06-permiso especifico.sql**
```sql
GRANT ALL PRIVILEGES ON sturmprojekt.* 
TO 'nurlucas'@'localhost';
```
**07-refrescar privilegios.sql**
```sql
FLUSH PRIVILEGES;
```
**08-ahora salgo.sql**
```sql
exit;
```
**09-ahora entro con el nuevo usuario.sql**
```sql
mysql -u nurlukas -p

SHOW DATABASES;
```
**2-crear usuario.sql**
```sql
1.-sudo mysql -u root -p
-- crea usuario nuevo con contraseña
-- creamos el nombre de usuario que querramos
CREATE USER 
'[tunombredeusuario]'@'[tuservidor]' IDENTIFIED BY '[tucontraseña]';

CREATE USER 'nurlucas'@'localhost' IDENTIFIED BY 'tame123';
@ = at (en)

# Comprobar el nivel de seguridad actual
SHOW VARIABLES LIKE 'validate_password%';
# Bajar la seguridad al nivel LOW
SET GLOBAL validate_password.policy = LOW;
SET GLOBAL validate_password.length = 7;

-- permite acceso a ese usuario
GRANT USAGE ON *.* TO '[tunombredeusuario]'@'[tuservidor]';
--[tuservidor] == localhost
-- La contraseña puede requerir Mayus, minus, numeros, caracteres, min len
GRANT USAGE ON *.* TO 'nurlukas'@'localhost';

-- quitale todos los limites que tenga
ALTER USER '[tunombredeusuario]'@'[tuservidor]' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

ALTER USER 'nurlukas'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

-- dale acceso a la base de datos empresadam
GRANT ALL PRIVILEGES ON [tubasededatos].* 
TO '[tunombredeusuario]'@'[tuservidor]';

GRANT ALL PRIVILEGES ON sturmprojekt.* 
TO 'nurlukas'@'localhost';
-- recarga la tabla de privilegios
FLUSH PRIVILEGES;
```
### 11-Lenguaje de descripción de datos (DDL)
**01-Ejercicio de final de unidad.md**
```markdown
Crea bases de datos definiendo su estructura y las características de sus elementos según el modelo relacional.

Criterios de evaluación
a) Se ha analizado el formato de almacenamiento de la información.
b) Se han creado las tablas y las relaciones entre ellas.
c) Se han seleccionado los tipos de datos adecuados.
d) Se han definido los campos clave en las tablas.
e) Se han implantado las restricciones reflejadas en el diseño lógico.
f) Se han creado vistas.
g) Se han creado los usuarios y se les han asignado privilegios.
h) Se han utilizado asistentes, herramientas gráficas y los lenguajes de definición y control de datos.

1.-Tenéis que crear una base de datos
Cual? La que queráis

Crear tablas - crear relaciones entre ellas (FK - cliente_id)
Especificar cuando usamos varchar, int, date
Definir campos clave Identificador - alter - primary - auto increment
alguna restriccion - como la del correo electronico
Crear Left join y vista
Crear un usuario y acceder con ese usuario

Creais la base de datos que queráis
Todo esto lo ponéis en archivos, numerados, como yo
La secuencia de todo esto la poneis en uno o varios archivos
```
## 02-Proyecto
**01-Guia del proyecto.md**
```markdown

sudo mysql -u root -p
```
**02-Crear base y tablas.sql**
```sql

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
```
**03-Claves y restricciones.sql**
```sql
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
```
**04-Datos de prueba.sql**
```sql
USE sturmprojekt;

-- Ejecutar una sola vez, tras 03 y 04, con las tablas vacias.
START TRANSACTION;
INSERT INTO clientes (nombre, apellidos, email, proyecto, Identificador) VALUES
('Lucas Ezequiel', 'Andrés Griego', 'admin@jsturmprojekt.es', 'Plataforma completa', 1),
('Juan', 'García López', 'juan@garcia.com', 'Plataforma básica', 2),
('Sofía', 'Romero García', 'sofia.romero@example.com', 'Proyecto en estudio', 3);

INSERT INTO servicios (id_servicio, nombre, tipo, descripcion, precio) VALUES
(1, 'Plataforma Básica', 'Producto', 'Desarrollo web básico', 250.00),
(2, 'Plataforma Completa', 'Producto', 'Desarrollo web completo', 350.00),
(3, 'Landing Web', 'Producto', 'Página web estática', 150.00),
(4, 'Gestión de dominio/Despliegue', 'Servicio', 'Configuración de dominio, DNS, hosting y despliegue web', 35.00),
(5, 'Mantenimiento + Servicio Técnico', 'Servicio', 'Mantenimiento, incidencias y soporte técnico', 35.00);

INSERT INTO pedidos (id_pedido, id_cliente, id_servicio, fecha_pedido, estado, precio_acordado) VALUES
(1, 1, 2, '2026-10-01', 'En desarrollo', 350.00),
(2, 1, 4, '2026-10-02', 'Finalizado', 35.00),
(3, 2, 1, '2026-10-03', 'Pendiente', 240.00);

SELECT * FROM clientes;
SELECT * FROM servicios;
SELECT * FROM pedidos;
```
**05-Consultas y vista.sql**
```sql
USE sturmprojekt;

-- Cada pedido, con su cliente y servicio.
SELECT p.id_pedido, p.fecha_pedido, c.nombre, c.apellidos,
       s.nombre AS servicio, s.precio AS precio_catalogo, p.precio_acordado
FROM pedidos AS p
LEFT JOIN clientes AS c ON p.id_cliente = c.Identificador
LEFT JOIN servicios AS s ON p.id_servicio = s.id_servicio
ORDER BY p.id_pedido;

-- Conserva todos los clientes, incluso sin pedidos.
-- El cliente 3 debe aparecer con columnas de pedido y servicio a NULL.
SELECT c.Identificador, c.nombre, p.id_pedido, s.nombre AS servicio
FROM clientes AS c
LEFT JOIN pedidos AS p ON c.Identificador = p.id_cliente
LEFT JOIN servicios AS s ON p.id_servicio = s.id_servicio
ORDER BY c.Identificador, p.id_pedido;

CREATE VIEW vista_completa AS
SELECT p.fecha_pedido, p.id_pedido, c.nombre AS nombre_cliente,
       c.apellidos AS apellidos_cliente, s.nombre AS nombre_servicio,
       s.precio AS precio_catalogo, p.precio_acordado, p.estado
FROM pedidos AS p
LEFT JOIN clientes AS c ON p.id_cliente = c.Identificador
LEFT JOIN servicios AS s ON p.id_servicio = s.id_servicio;

SELECT * FROM vista_completa ORDER BY id_pedido;
```
**06-Usuario y privilegios.sql**
```sql
CREATE USER 'nurlucas'@'localhost' IDENTIFIED BY 'tame2026';

GRANT ALL PRIVILEGES ON sturmprojekt.* TO 'nurlucas'@'localhost';


```
## 03-Resultado aprendizaje
**RA2.md**
```markdown
# Resultado de aprendizaje 2
**Resultado de aprendizaje**
Crea bases de datos definiendo su estructura y las características de sus elementos según el modelo relacional.

Criterios de evaluación
a) Se ha analizado el formato de almacenamiento de la información.
Hemos visto que en bases de datos relacionales los datos se almacenan en bases de datos, organizadas en tablas,
Estos son los tipos de datos que utilice yo en dichas tablas:
VARCHAR: textos de longitud variable, como nombres, apellidos, correos y estados.
INT: números enteros para los identificadores y las referencias entre tablas.
DATE: fechas de los pedidos, con formato AAAA-MM-DD.
DECIMAL(10,2): importes exactos, con diez cifras en total y dos decimales.
TEXT: descripciones extensas de los servicios

Aunque cabe destacar que hay muchos tipos de datos más.

b) Se han creado las tablas y las relaciones entre ellas.
En mi proyecto de final de unidad cree una base de datos basada en mi emprendimiento personal, mi DB contiene 3 tablas, "clientes", "servicios", y "pedidos".
Las tres tablas se relacionan a través de pedidos:
clientes (1) ──── (N) pedidos (N) ──── (1) servicios

- Clientes → pedidos: uno a muchos. Un cliente puede tener varios pedidos. 
Cada pedido pertenece a un único cliente mediante pedidos.id_cliente → clientes.Identificador.

- Servicios → pedidos: uno a muchos. Un servicio puede aparecer en varios pedidos. 
Cada pedido corresponde a un único servicio mediante pedidos.id_servicio → servicios.id_servicio.

c) Se han seleccionado los tipos de datos adecuados.
Los tipos de datos que seleccione son acordes a las necesidades de mi emprendimiento, para optimizar el uso de la DB,
Y no desperdiciar espacio. 

d) Se han definido los campos clave en las tablas.
Las claves primarias identifican de forma unica cada registro y utilizan AUTO_INCREMENT.
Las claves ajenas relacionan cada pedido con su cliente y su servicio:
- id_cliente referencia clientes.Identificador.
- id_servicio referencia servicios.id_servicio.


e) Se han implantado las restricciones reflejadas en el diseño lógico.
Mis restricciones definidas son:
- PRIMARY KEY: impide identificadores duplicados o nulos.
- FOREIGN KEY: impide crear pedidos con clientes o servicios inexistentes.
- NOT NULL: obliga a rellenar los campos donde lo has indicado, como la fecha del pedido y el precio.
- CHECK del correo: establece un patrón para validar el formato de clientes.email.

f) Se han creado vistas.
Tengo definida "vista_completa" 
Combina pedidos, clientes y servicios con dos LEFT JOIN y muestra:
- Fecha y número del pedido.
- Nombre y apellidos del cliente.
- Nombre y precio del servicio.

Para consultarla: SELECT * FROM vista_completa;

g) Se han creado los usuarios y se les han asignado privilegios.
Cree el usuario "nurlukas" y "nurlucas", aunque ambos trabajan con la misma base de datos y con el mismo nivel de permisos.

h) Se han utilizado asistentes, herramientas gráficas y los lenguajes de definición y control de datos.
- DDL (definición de datos): CREATE DATABASE, CREATE TABLE, ALTER TABLE y CREATE VIEW.
- DCL (control de datos): GRANT para asignar privilegios al usuario.
Asistentes y herramientas gráficas: Durante la clase utilizamos herramientas graficas para entender mejor la relacion entre tablas.
```
