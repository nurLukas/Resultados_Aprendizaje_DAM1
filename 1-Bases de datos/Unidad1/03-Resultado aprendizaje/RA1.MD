# Resultado de aprendizaje 1
**Resultado de aprendizaje**
Reconoce los elementos de las bases de datos analizando sus funciones y valorando la utilidad de los sistemas gestores.

Criterios de evaluación
a) Se han analizado los sistemas lógicos de almacenamiento y sus características.
Los sistemas de almacenamiento, permiten almacenar y organizar la información, de tal forma que luego pueda consultarse, 
modificar, o eliminarla.
* En los apuntes realiados en clase vimos los siguientes tipos:
- Ficheros planos: almacenan información en archivos como TXT, Markdown, ODT y DOCX.
- Ficheros estructurados: organizan los datos mediante formatos como CSV, TSV, JSON, YAML.
- Ficheros indexados: utilizan índices que facilitan localizar la información, como un CSV.
- Ficheros de acceso directo: permiten acceder a la información mediante posiciones de bytes o valores hash.
- Archivos de imágenes: utilizan formatos como JPG, PNG y BMP.

Tambien diferenciamos entre almacenamiento temporal y persistente, siendo este ultimo el que se puede almacenar,
incluso si se apaga el ordenador.

b) Se han identificado los distintos tipos de bases de datos según el modelo de datos utilizado.
Las bases de datos pueden clasificarse según la manera en que organizan y relacionan la información:
- Jerárquicas: organizan los datos en forma de árbol, con relaciones entre elementos superiores e inferiores.
- En red: permiten que un registro tenga múltiples relaciones con otros registros.
- Relacionales: almacenan los datos en tablas formadas por filas y columnas, que pueden relacionarse entre sí. Utilizan habitualmente SQL.
- Orientadas a objetos: organizan la información mediante objetos.
- NoSQL: incluyen distintos modelos, como bases de datos documentales, clave-valor, columnares y de grafos.

c) Se han identificado los distintos tipos de bases de datos en función de la ubicación de la información.
Según dónde se almacene la información, podemos distinguir:
1. Bases de datos centralizadas: toda la información se encuentra en un único servidor al que se conectan distintos clientes. 
Su inconveniente es que el servidor puede saturarse si recibe demasiadas solicitudes.
2. Bases de datos distribuidas: la información se encuentra repartida entre varios servidores, 
que pueden estar ubicados en diferentes máquinas o regiones geográficas.

La diferencia principal es que una base de datos centralizada utiliza un servidor principal, 
mientras que una distribuida reparte la información entre varios servidores.
Este ultimo caso representa el 99% de las bases de datos.

d) Se ha evaluado la utilidad de un sistema gestor de bases de datos.
Un SGBD, (Sistema Gestor de Bases de Datos), es un programa que permite crear, organizar, consultar, modificar y administrar bases de datos.

e) Se ha reconocido la función de cada uno de los elementos de un sistema gestor de bases de datos.
1. Motor de almacenamiento: se encarga de guardar y recuperar los datos de la base de datos.
2. Procesador de consultas: recibe las consultas, las procesa y devuelve los resultados.
3. Optimizador de consultas: busca la manera de ejecutar una consulta, utilizando la menor cantidad de recursos.

Estos componentes trabajan conjuntamente para que la información pueda almacenarse, consultarse y modificarse de manera eficiente.

f) Se han clasificado los sistemas gestores de bases de datos.
Como se dijo anterior mente, * según el modelo de datos:
- Jerárquicos.
- En red.
- Relacionales (SQL).
- Orientados a objetos.
- NoSQL.

* Según su arquitectura:
- Centralizados.
- Cliente/servidor.
- Distribuidos.
- En la nube (cloud).

* Según el número de usuarios:
- Monousuario: utilizados por un solo usuario.
- Multiusuario: permiten trabajar a varios usuarios simultáneamente.

g) Se ha reconocido la utilidad de las bases de datos distribuidas.
Las bases de datos distribuidas permiten almacenar información en diferentes servidores o ubicaciones geográficas.
Son útiles cuando un servidor puede saturarse debido a la cantidad de usuarios o solicitudes.
Existen varias formas de distribuir la información:
1. Replicación: varios servidores mantienen copias de una misma base de datos. (Se difumina la información)
2. Distribución por fragmentos: cada servidor guarda una parte de la información y la unión de todas las partes constituye la base de datos completa.

h) Se han analizado las políticas de fragmentación de la información.
La fragmentación consiste en dividir una base de datos en diferentes partes para almacenarlas en distintos servidores.
Cada servidor puede contener una pieza de la base de datos y que la suma de todas ellas forma la base de datos completa.

i) Se ha identificado la legislación vigente sobre protección de datos.
Las normas principales sobre protección de datos personales son:
1. Reglamento General de Protección de Datos (RGPD)
Es el Reglamento (UE) 2016/679, regula el tratamiento y la protección de los datos personales en la Unión Europea.
Establece obligaciones para las organizaciones que utilizan datos personales y reconoce derechos a las personas sobre su información.
2. Ley Orgánica de Protección de Datos Personales y garantía de los derechos digitales (LOPDGDD)
Es la Ley Orgánica 3/2018, que complementa y adapta el marco de protección de datos personales al ordenamiento jurídico español.
También acude a la garantía de determinados derechos digitales.

j) Se han reconocido los conceptos de Big Data y de la inteligencia de negocios.
Hace referencia a la recopilación y el tratamiento de grandes cantidades de datos.
Cuanto mayor es el volumen de información, más difícil puede resultar procesarla, 
pero también pueden encontrarse patrones y conclusiones de valor, estrategico, economico,, geopolitico.
Su finalidad es analizar los datos e información útil para tomar decisiones, sacar ventajas, etc.