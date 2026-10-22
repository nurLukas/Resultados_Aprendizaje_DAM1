# Reporte de proyecto

## Información de generación

- **Fecha:** 2026-10-16 01:55:22 +0200
- **Usuario:** lucas
- **Equipo:** LUCAS
- **Sistema operativo:** Windows
- **Arquitectura:** x86_64
- **Directorio de ejecución:** `D:/Herramientas/portables/jocarsa-generador-windows-x64`
- **Proyecto documentado:** `D:/Resultados Aprendizaje_DAM1/1-Bases de datos/Unidad1`
- **HMAC-SHA-256 de autenticidad:** `94aba8f562e31f101c4f6129d7d090493e310d2e26c1a2fd522baf345cb87fa3`

> El HMAC-SHA-256 se calcula sobre el documento completo usando un secreto incluido en el programa y 64 ceros en el propio campo del HMAC. El secreto no se escribe en el informe. Este mecanismo permite comprobar integridad y que el documento fue generado con el mismo secreto.

## Estructura del proyecto

```
D:/Resultados Aprendizaje_DAM1/1-Bases de datos/Unidad1
├── 01-Ejercicios
│   ├── 01-Ficheros (planos, indexados, acceso directo, entre otros)
│   │   ├── 0-Introduccion.md
│   │   ├── 01-Nombres.txt
│   │   └── 02-Agenda.csv
│   ├── 02-Bases de datos. Conceptos, usos y tipos según el modelo de datos, la ubicación de la información
│   │   ├── 00-Introduccion.md
│   │   ├── 01-CRUD.md
│   │   ├── 02-Persistencia.md
│   │   ├── 03-Errores.md
│   │   └── mibasededatos
│   │       ├── clientes
│   │       ├── facturas
│   │       └── pedidos
│   ├── 03-Sistemas gestores de base de datos Funciones, componentes y tipos
│   │   ├── 00-Introducción.md
│   │   └── 01-MySQL.md
│   ├── 04-Bases de datos centralizadas y bases de datos distribuidas. Técnicas de fragmentación
│   │   ├── 01-Centralizadas.md
│   │   └── 02-Bases de datos distribuidas.md
│   ├── 05-Legislación sobre protección de datos
│   │   └── 00-Introducción.md
│   └── 06-Big Data introducción, análisis de datos, inteligencia de negocios
│       └── 01-Big data.md
├── 03-Resultado aprendizaje
│   └── RA1.MD
└── 2-Proyecto
    └── 0-Ejercicio final de unidad.md
```

## Bases de datos SQLite

Esta sección documenta únicamente el esquema de las bases SQLite detectadas. No se vuelcan registros ni datos de usuario.

No se han encontrado bases SQLite con extensiones .db, .sqlite o .sqlite3.

## Código (intercalado)

# Unidad1
## 01-Ejercicios
### 01-Ficheros (planos, indexados, acceso directo, entre otros)
**0-Introduccion.md**
```markdown
# Ficheros (planos, indexados, acceso directo, entre otros)
- Planos
	- texto txt
	- markdown
	- odt
	- docx
- Estructurados
	- csv, tsv
	- json
	- yaml
	- ods
	- xlsx
- Indexados
	- csv con índice
- Acceso directo
	- Acceso por bytes de archivo
	- Acceso por hash
- Imágenes
	- jpg
	- png
	- bmp
```
### 02-Bases de datos. Conceptos, usos y tipos según el modelo de datos, la ubicación de la información
**00-Introduccion.md**
```markdown
Motor de bases de datos - mueve
Almacenamiento de bases de datos - Almacena
	Base de datos 1
		Tabla1
			Columna1(nombre)
				Tuplas
			Columna2(apellidos)
			Columna3(telefono)
		Tabla2
	
	Base de datos 2
	
	Base de datos 3
```
**01-CRUD.md**
```markdown
# ¿ Que es un CRUD?

- Create - Crean nuevos registros
- Read - Leen registros existentes
- Update - Actualizan registros existentes
- Delete - Eliminan registros existentes
```
**02-Persistencia.md**
```markdown
Memoria temporal versus persistencia

Variable en python = memoria temporal = RAM

# Persistencia
Información persistente es aquella que queremos guardar para siempre en:
- Discos duros
- Memorias flash
- y similares

**No hablamos de RAM o procesador**

Hablamos de apagar el ordenador
Tenerlo apagado un año si hace falta
Y al encender, poder recuperar nuestra información

```
**03-Errores.md**
```markdown
Informática = Infor + mática
infor = informático
mática = automática

Tratamiento automatizado de la información

Una gran responsabilidad en nuestro hombros

Lo importante no es solo tratar los datos
sino tratarlos de forma integra y asegurar su copia
```
#### mibasededatos
##### clientes
##### facturas
##### pedidos
### 03-Sistemas gestores de base de datos Funciones, componentes y tipos
**00-Introducción.md**
```markdown
# Sistemas gestores de base de datos Funciones, componentes y tipos
- Funciones
	- Definir datos, 
	- manipular datos, 
	- controlar el acceso - usuario y contraseña
	- la seguridad y la concurrencia - cuando hay muchos usuarios a la vez
	- asegurar la integridad de los datos - que los datos sean fiables
	- proporcionar mecanismo de copia de seguridad - y usarlo frecuentemente
- Componentes
	- Motor de almacenamiento - guarda los datos
	- Procesador de consultas - Le pedimos cosas, lo procesa y nos devuelve resultados
	- Optimizar consultas - PAra que consuman los menores recursos posibles
	- Gestor de transacciones
- Tipos
	- Jerárquicos (p. ej: carpetas) - Carpetas en tu disco duro, eso es una base de datos
	- En red - Disponibles en una red local
	- Relacionales (xSQL) - Tablas columnas y filas - y relaciones entre ellas
	- Orientados a objetos - ORM - 
	- NoSQL: documentales, clave-valor, columnares, grafos...
- Otras clasificaciones
	- Por arquitectura: centralizados, cliente/servidor, distribuidos, cloud...
	- Número de usuarios: monousuario y multiusuario
	- Finalidad: Operaciones/análisis 
```
**01-MySQL.md**
```markdown
# MySQL 
Es un sistema gestor de bases de datos

Requiere instalación 
Se puede instalar también como * MariaDB

Está para Windows, para Mac, Linux:
- Windows: XAMPP https://www.apachefriends.org/es/index.html 
- Mac: MAMP https://www.mamp.info/en/windows/

Si estáis en Linux, ya hablaremos

Windows: http://localhost:80/phpmyadmin 

Mac: http://localhost:8888/phpmyadmin

```
### 04-Bases de datos centralizadas y bases de datos distribuidas. Técnicas de fragmentación
**01-Centralizadas.md**
```markdown
Son aquellas que se encuentran en UN servidor Responden a la arquitectura cliente servidor (Hay muchos clientes que se conectan a un servidor) 
Proporcionan servicio a todos los clientes que se conecten

Es el caso del 99.99% de las bases de datos

Si hay muchos accesos, el servidor se puede saturar
```
**02-Bases de datos distribuidas.md**
```markdown
Distribuidas en varias maquinas, o en varias regiones geograficas

Si un solo servidor se satura, en ese caso:

1.- varios servidores, cada uno contiene una copia de la base de datos
"CDN" - Varios servidores espejo conectados en regiones diferentes, ej: cloudflare

2.- varios servidores, cada uno de ellos tiene una pieza de la base de datos, la suma hace la base de datos completa

```
### 05-Legislación sobre protección de datos
**00-Introducción.md**
```markdown
# Legislación sobre protección de datos
- Principales 
	- Reglamento (UE) 2016/679 — RGPD (Reglamento General de Protección de Datos)
	- Ley Orgánica 3/2018 — LOPDGDD (Ley Orgánica de Protección de Datos Personales y garantía de los derechos digitales)

https://www.boe.es/doue/2016/119/L00001-00088.pdf
https://www.boe.es/buscar/act.php?id=BOE-A-2018-16673
```
### 06-Big Data introducción, análisis de datos, inteligencia de negocios
**01-Big data.md**
```markdown
Hace referencia a la recolección de grandes cantidades de datos
Cuanto más grande sea el conjunto más difícil es procesarlo
Cuanto más grande sea el conjunto, más informacioń de valor vamos a encontrar

Analizar y extraer conclusiones de valor

Extraer conclusiones y tomar decisiones de valor
```
## 03-Resultado aprendizaje
**RA1.MD**
```markdown
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
```
## 2-Proyecto
**0-Ejercicio final de unidad.md**
```markdown
# Trabajo final de unidad 1

## Resumen de lo realizado en las tutorias de la unidad 1

Al principio de la primer unidad de esta asigatura se sentaron las bases de conocimento, definiciones, tipologias, morfolia, etc.
De las bases de datos, su estructura y gestores.
Vimos datos persistentes en el tiempo y datos volatiles que desaparecen al apagar el ordenador.
Hemos visto diferentes formatos de archivos, que fueron creados con el objetivo de almacenar información, algunos de manera más basica y desordenada, 
y otros de forma mas compleja y ordenada.
Legue a la conclusión de que todos son necesarios e indispensables para que la rueda de la informática siga girando.

Una vez vistos los conocimientos basicos nos adentramos en los gestores de bases de datos, tipos de redes de datos y sus difernecias, ventajas y desventajas.
Como tambien el marco legal que abarca esta cuestion, ya que los datos son sensibles, y muy valiosos, dichos reglamentos vistos, abarcan normativas tanto nacionales
especificas de España, como internacionales con cobertura de toda la Union Europea.
Las normativas Europeas por suerte son mas reestrictivas que las norteamericanas, y eso nos progeje más.

Volviendo a los sistemas gestores de bases de datos. vimos como clasificarlos según su modelo de datos, arquitectura y cantidad de usuarios, cabe destacar que hay otras 
maneras de clasificar, además de las nombradas.
Por ultimo analizamos el termino "Big data" y todo lo que abarca, (bastas cantidades de datos capaces de ser explotados para obtener veneficios, pero a la vez son dificiles
de gestionar, debido a la masa de datos.
```
