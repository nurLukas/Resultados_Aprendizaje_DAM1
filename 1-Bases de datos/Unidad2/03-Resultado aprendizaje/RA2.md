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