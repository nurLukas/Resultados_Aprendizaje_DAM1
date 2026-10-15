# Reporte de proyecto

## Información de generación

- **Fecha:** 2026-10-13 15:31:16 +0200
- **Usuario:** lucas
- **Equipo:** LUCAS
- **Sistema operativo:** Windows
- **Arquitectura:** x86_64
- **Directorio de ejecución:** `D:/Herramientas/portables/jocarsa-generador-windows-x64`
- **Proyecto documentado:** `D:/Resultados Aprendizaje_DAM1/3-Lenguajes de marcas y sistemas de gestión de información/Unidad 1`
- **HMAC-SHA-256 de autenticidad:** `4d5582bb7566515329076bfbaa44aa6f547689147c43aca36519ce18ac994be8`

> El HMAC-SHA-256 se calcula sobre el documento completo usando un secreto incluido en el programa y 64 ceros en el propio campo del HMAC. El secreto no se escribe en el informe. Este mecanismo permite comprobar integridad y que el documento fue generado con el mismo secreto.

## Estructura del proyecto

```
D:/Resultados Aprendizaje_DAM1/3-Lenguajes de marcas y sistemas de gestión de información/Unidad 1
├── 01-Ejercicios
│   ├── 01-Clasificación
│   │   ├── 01-Que es un lenguaje de marcas.md
│   │   └── 02-Markdown.md
│   ├── 02-Características y ámbitos de aplicación
│   │   ├── 01-Ejemplo Json.json
│   │   ├── 02-Muchos elementos.json
│   │   └── 03-Anidacion.json
│   ├── 03-Estructura y sintaxis
│   │   ├── 01-xml basico.xml
│   │   └── 02-varios emails.xml
│   ├── 04-Herramientas de edición
│   │   ├── 00-resumen.md
│   │   ├── 01-Validador.md
│   │   ├── 02-Identidad.json
│   │   ├── 03-datos basicos.json
│   │   ├── 04-Mas datos.json
│   │   ├── 05-Varios emails.json
│   │   ├── 06-varias redes sociales.json
│   │   ├── 07-array coleccion.json
│   │   ├── 08-Ampliamos Experiencias laborales.json
│   │   └── 09-Ahora mas experiencias.json
│   ├── 05-Elaboración de documentos bien formados
│   │   ├── 01-plantilla cliente.xml
│   │   ├── 02-validador.py
│   │   ├── 03-Instalación libreria lxml.md
│   │   └── plantilla validacion.xsd
│   ├── 06-Utilización de espacios de nombres
│   │   ├── 01-plantilla cliente.xml
│   │   ├── 07-plantilla con espacio de nombres.xml
│   │   └── 08-esto lo publicaria en mi web.html
│   └── 07-Ejercicio práctico
│       └── 01-Enunciado.md
├── 02-Proyecto
│   └── Mi JSON.json
└── 3-Resultado aprendizaje
    └── RA1.md
```

## Bases de datos SQLite

Esta sección documenta únicamente el esquema de las bases SQLite detectadas. No se vuelcan registros ni datos de usuario.

No se han encontrado bases SQLite con extensiones .db, .sqlite o .sqlite3.

## Código (intercalado)

# Unidad 1
## 01-Ejercicios
### 01-Clasificación
**01-Que es un lenguaje de marcas.md**
```markdown
# Lenguaje de marcas.

Un lenguaje de marcas es un sistema para codificar documentos incorporando etiquetas o marcas junto al texto. 
Estas reglas permiten estructurar, presentar y definir la información para que sea interpretada por personas o plataformas, 
siendo el HTML el más extendido.

Ejemplos de Lenguajes de marcas:

* HTML (HyperText Markup Language)
* XML (eXtensible Markup Language)
* CSS (Cascading Style Sheets)
* JSON (JavaScript Object Notation)
* YAML (YAML Ain’t Markup Language)
* Markdown
* SVG (Scalable Vector Graphics)
```
**02-Markdown.md**
```markdown
# Esto es un título de nivel 1

## Esto es un título de nivel 2

### Esto es un título de nivel 3

Esto es un texto plano y no pasa nada

- Platanos
- Manzanas
- Peras

* Audi
* Seat
* Volskwagen

1. Me levanto
2. Desayuno
3. Ducha



--- 
(barra separadora)

| Orden | Lunes | Martes      | Miercoles | Jueves | Viernes |
|-------|-------|-------------|-----------|--------|---------|
| 	1   | Programacion        |           |        |         | 
| 	2	| Base de datos       |           |        |         | 
| 	3 	| Lenguajes de marcas |           |        |         | 

Esto es **negrita** Y esto es *cursiva*

[La web de Sturmprojekt es la mejor](https://www.Sturmprojekt.es)

> Ser, o no ser, esa es la cuestión


Python tiene la instrucción `print` y es muy útil

Y un programa en pyton sería:

```
print("Hola mundo en Python")
```
```
### 02-Características y ámbitos de aplicación
**01-Ejemplo Json.json**
```json
{
	"nombre":"Lucas Ezequiel",
	"apellidos":"Andrés Griego",
	"email":"admin@sturmprojekt.es"
}
```
**02-Muchos elementos.json**
```json
{
	"nombre":"Lucas Ezequiel",
	"apellidos":"Andrés Griego",
	"email":[
		"admin@sturmprojekt.es",
		"info@sturmprojekt.es"
	]
}
```
**03-Anidacion.json**
```json
{
	"datos personales":{
  	"nombre":"Lucas Ezequiel",
    "apellidos":"Andrés Griego"
  },
  "experiencia laboral":{
  	"experiencia":"descripcion",
    "experiencia":"descripcion",
    "experiencia":"descripcion",
    "experiencia":"descripcion",
    "experiencia":"descripcion"
  },
  "formación":{
  	"formacion":"descripcion",
    "formacion":"descripcion",
    "formacion":"descripcion",
    "formacion":"descripcion",
    "formacion":"descripcion",
    "formacion":"descripcion"
  },
  "hobbies":["hobbie 1","hobbie 2","hobbie 3"]
}
```
### 03-Estructura y sintaxis
**01-xml basico.xml**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<persona>
  <nombre>Lucas Ezequiel</nombre>
  <apellidos>Andrés Griego</<apellidos>
  <email>admin@sturmprojekt.es</email>
</persona>
```
**02-varios emails.xml**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<persona>
  <nombre>Lucas Ezequiel</nombre>
  <apellidos>Andrés Griego</apellidos>
  <emails>
    <personal>admin@sturmprojekt.es</personal>  
    <trabajo>lucas.and95@gmail.com</trabajo>  
  </emails>
</persona>
```
### 04-Herramientas de edición
**00-resumen.md**
```markdown
# JSON:

Conjunto de parejas de clave - valor
clave:valor,
clave:valor,
...

Luego cada valor PUEDE contener a su vez parejas de clave valor

ANIDACION
Puedes guardar, si quieres, multiples niveles


clave:valor,
clave:valor,
clave:valor,
clave:
	clave:valor,
	clave:valor,
	clave:
		clave:valor,
		clave:valor,
		clave:valor,
		clave:valor,
  ,
  clave:valor,
clave:valor,
clave:valor,
...


Las llaves indican bloques de clave+valor
Los corchetes indican listas de elementos
```
**01-Validador.md**
```markdown
https://jsonlint.com/
```
**02-Identidad.json**
```json
{
	"datos_personales":"",
	"formacion":"",
	"experiencia":"",
	"idiomas":"",
	"conduccion":"",
	"aficiones":""	
}
```
**03-datos basicos.json**
```json
{
	"datos_personales":"Lucas Ezequiel",
	"formacion":"Informático",
	"experiencia":"Poca",
	"idiomas":"Español",
	"conduccion":"B1",
	"aficiones":"Ganar pasta"	
}
```
**04-Mas datos.json**
```json
{
	"datos_personales":{
		"nombre":"Lucas Ezequiel"
		"apeliidos":"Andrés Griego",
		"email": "lucas.and95@gmail.com"		
	},
	"formacion":"Informático",
	"experiencia":"Poca",
	"idiomas":"Español",
	"conduccion":"B1",
	"aficiones":"Ganar pasta"	
}
```
**05-Varios emails.json**
```json
{
	"datos_personales":{
		"nombre":"Lucas Ezequiel",
		"apeliidos":"Andrés Griego",
		"email":{
			"personal":"lucas.and95@gmail.com",
			"trabajo":"admin@sturmprojekt.es"
		}
		"redes sociales":"facebook"
	},
	"formacion":"Informático",
	"experiencia":"Poca",
	"idiomas":"Español",
	"conduccion":"B1",
	"aficiones":"Ganar pasta"	
}
```
**06-varias redes sociales.json**
```json
{
	"datos_personales":{
  	"nombre":"Lucas Ezequiel",
    "apellidos":"Andrés griego",
    "email":{
		"personal":"lucas.and95@gmail.com",
		"trabajo":"admin@sturmprojekt.es"
    },
    "redes_sociales":{
		"Github":"https://github.com/nurLukas"
		"Instagram":"https://www.instagram.com/sturmprojekt",
		"LinkedIn":"https://www.linkedin.com/in/lucas-andr%C3%A9s-griego-794a9b13a/"
    }
  },
  "formacion":"Informático",
  "experiencia":"Poca",
  "idiomas":"Español",
  "conduccion":"B1",
  "aficiones":"Ganar dinero"
}
```
**07-array coleccion.json**
```json
{
	"datos_personales":{
  	"nombre":"Lucas Ezequiel",
    "apellidos":"Andrés griego",
    "email":{
		"personal":"lucas.and95@gmail.com",
		"trabajo":"admin@sturmprojekt.es"
    },
    "redes_sociales":{
		"Github":"https://github.com/nurLukas",
		"Instagram":"https://www.instagram.com/sturmprojekt",
		"LinkedIn":"https://www.linkedin.com/in/lucas-andr%C3%A9s-griego-794a9b13a/"
    }
  },
  "formacion":"Informático",
  "experiencia":[
	"una",
	"dos",
	"tres",
	"cuatro"
  ],
  "idiomas":"Español",
  "conduccion":"B1",
  "aficiones":"Ganar dinero"
}
```
**08-Ampliamos Experiencias laborales.json**
```json
{
	"datos_personales":{
  	"nombre":"Lucas Ezequiel",
    "apellidos":"Andrés griego",
    "email":{
		"personal":"lucas.and95@gmail.com",
		"trabajo":"admin@sturmprojekt.es"
    },
    "redes_sociales":{
		"Github":"https://github.com/nurLukas",
		"Instagram":"https://www.instagram.com/sturmprojekt",
		"LinkedIn":"https://www.linkedin.com/in/lucas-andr%C3%A9s-griego-794a9b13a/"
    }
  },
  "formacion":"Informático",
  "experiencia":[
    {
		"empresa":"X",
		"fecha_de_inicio":"YYYY-MM-DD",
		"fecha_de_final":"YYYY-MM-DD",
		"cargo":"X",
		"responsabilidades":"X",
		"descripción":"X",
    },
    "dos",
    "tres",
    "cuatro"
  ],
  "idiomas":"Español",
  "conduccion":"B1",
  "aficiones":"Ganar dinero"
}
```
**09-Ahora mas experiencias.json**
```json
{
	"datos_personales":{
  	"nombre":"Lucas Ezequiel",
    "apellidos":"Andrés griego",
    "email":{
		"personal":"lucas.and95@gmail.com",
		"trabajo":"admin@sturmprojekt.es"
    },
    "redes_sociales":{
		"Github":"https://github.com/nurLukas",
		"Instagram":"https://www.instagram.com/sturmprojekt",
		"LinkedIn":"https://www.linkedin.com/in/lucas-andr%C3%A9s-griego-794a9b13a/"
    }
  },
  "formacion":"Informático",
  "experiencia":[
    {
		"empresa":"X",
		"fecha_de_inicio":"YYYY-MM-DD",
		"fecha_de_final":"YYYY-MM-DD",
		"cargo":"X",
		"responsabilidades":"X",
		"descripción":"X"
    },
    {
		"empresa":"X",
		"fecha_de_inicio":"YYYY-MM-DD",
		"fecha_de_final":"YYYY-MM-DD",
		"cargo":"X",
		"responsabilidades":"X",
		"descripción":"X"
    },
    {
		"empresa":"X",
		"fecha_de_inicio":"YYYY-MM-DD",
		"fecha_de_final":"YYYY-MM-DD",
		"cargo":"X",
		"responsabilidades":"X",
		"descripción":"X"
    },
    {
		"empresa":"X",
		"fecha_de_inicio":"YYYY-MM-DD",
		"fecha_de_final":"YYYY-MM-DD",
		"cargo":"X",
		"responsabilidades":"X",
		"descripción":"X"
    }
  ],
  "idiomas":"Español",
  "conduccion":"B1",
  "aficiones":"Ganar dinero"
}
```
### 05-Elaboración de documentos bien formados
**01-plantilla cliente.xml**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<persona>
  <nombre>Lucas Ezequiel</nombre>
  <apellidos>Andrés Griego</apellidos>
  <email>admin@sturmprojekt.es</email>
</persona>
```
**02-validador.py**
```python
from lxml import etree

# Cargar el esquema XSD
archivo_xsd = etree.parse("plantilla validacion.xsd")
esquema = etree.XMLSchema(archivo_xsd)

# Cargar el XML
archivo_xml = etree.parse("01-plantilla cliente.xml")

# Validar
if esquema.validate(archivo_xml):
    print("El XML es válido")
else:
    print("El XML NO es válido")

    # Mostrar los errores
    for error in esquema.error_log:
        print("Línea:", error.line)
        print("Error:", error.message)
```
**03-Instalación libreria lxml.md**
```markdown
lxml no es una libreria del sistema

se instala en el cmd con el comando:

* Windows: python -m pip install lxml (en el cmd)

* Linux: pip3 install lxml
```
### 06-Utilización de espacios de nombres
**01-plantilla cliente.xml**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<persona>
  <nombre>Lucas Ezequiel</nombre>
  <apellidos>Andrés Griego</apellidos>
  <email>admin@sturmprojekt.es</email>
</persona>
```
**07-plantilla con espacio de nombres.xml**
```xml
<?xml version="1.0" encoding="UTF-8"?>

<nurLukas:persona xmlns:nurLukas="https//nurLukas.com/persona">
  <nurLukas:nombre>Lucas Ezequiel</nurLukas:nombre>
  <nurLukas:apellidos>Andrés Griego</nurLukas:apellidos>
  <nurLukas:email>admin@sturmprojekt.es</nurLukas:email>
</nurLukas:persona>
```
**08-esto lo publicaria en mi web.html**
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>nurLukas - Namespace Persona</title>
</head>
<body>

    <h1>nurLukas - Namespace Persona</h1>

    <p>
        Este URI identifica el espacio de nombres XML utilizado
        para representar personas en documentos XML de nurLukas.
    </p>

    <h2>URI del espacio de nombres</h2>

    <code>https://nurLukas.com/persona</code>

    <h2>Elementos</h2>

    <ul>
        <li><strong>persona</strong> - Representa una persona.</li>
        <li><strong>nombre</strong> - Nombre de la persona.</li>
        <li><strong>apellidos</strong> - Apellidos de la persona.</li>
        <li><strong>email</strong> - Dirección de correo electrónico.</li>
    </ul>

    <h2>Ejemplo</h2>

    <pre>
&lt;?xml version="1.0" encoding="UTF-8"?&gt;

&lt;nurLukas:persona
    xmlns:nurLukas="https://nurLukas.com/persona"&gt;

    &lt;nurLukas:nombre&gt;Lucas Ezequiel&lt;/nurLukas:nombre&gt;
    &lt;nurLukas:apellidos&gt;Andrés Griego&lt;/nurLukas:apellidos&gt;
    &lt;nurLukas:email&gt;admin@sturmprojekt.es&lt;/nurLukas:email&gt;

&lt;/nurLukas:persona&gt;
    </pre>

</body>
</html>
```
### 07-Ejercicio práctico
**01-Enunciado.md**
```markdown
Crear un archivo de lenguaje de marcas 
XML, o JSON

Recomiendo JSON porque es más seguro a futuro

El archivo de marcas debe ser un archivo de vuestra propia identidad
Deberá ser tan completo como sea posible

-Curriculum
-Web personal
-Portafolio
-IA

... muchas otras cosas a lo largo del curso
```
## 02-Proyecto
**Mi JSON.json**
```json
{
  "datos personales": {
    "nombre": "Lucas Ezequiel",
    "apellidos": "Andrés Griego",
    "marca_personal": "Sturmprojekt",
    "ubicacion": {
      "pais": "España",
      "provincia": "Valencia",
      "localidad": "Pobla Llarga"
    },
    "contacto": {
      "telefono": "694211111",
      "correo_electronico": "lucas.and95@gmail.com",
      "redes sociales": {
        "Github": "https://github.com/nurLukas",
        "linkedin": "https://www.linkedin.com/in/nurlukas/",
        "instagam": "https://www.instagram.com/sturmprojekt",
        "web_empresarial": "www.sturmprojekt.es"
      }
    }
  },
  "perfil_profesional": {
    "principal": "Estudiante de Desarrollo de Aplicaciones Multiplataforma y desarrollador web",
    "especializacion": [
      "Desarrollo web",
      "Desarrollo frontend",
      "Desarrollo backend",
      "JavaScript",
      "Node.js",
      "Express.js",
      "Bases de datos PostgreSQL",
      "Administración de servidores",
      "Docker",
      "Cloudflare",
      "DNS",
      "SSL/TLS",
      "Seguridad web",
      "Git y GitHub",
      "SEO técnico",
      "Analítica web",
      "Redes privadas con WireGuard"
    ],
    "marca": "STURMPROJEKT",
    "descripcion": "Estudiante de Desarrollo de Aplicaciones Multiplataforma (DAM) con experiencia práctica en desarrollo web, despliegue, administración de servidores y gestión de proyectos tecnológicos. Fundador de STURMPROJEKT, proyecto orientado al desarrollo y mantenimiento de páginas web para negocios locales, incluyendo infraestructura, dominios, DNS, seguridad y soporte técnico."
  },
  "experiencia_laboral": [
    {
      "periodo": "2025-actualidad",
      "actividad": "Fundador y Responsable Técnico de STURMPROJEKT",
      "descripcion": "Desarrollo, maquetación y despliegue de aplicaciones y páginas web corporativas para negocios locales."
    },
    {
      "periodo": "2025-actualidad",
      "actividad": "Administración de servidores e infraestructura web",
      "descripcion": "Administración y mantenimiento de servidores Ubuntu Server, despliegue de servicios mediante Docker y Docker Compose y gestión de infraestructura web."
    },
    {
      "periodo": "2025-actualidad",
      "actividad": "Gestión de dominios, DNS y seguridad",
      "descripcion": "Administración de dominios, configuración y enrutamiento DNS, gestión de certificados SSL/TLS y protección de servicios mediante Cloudflare."
    },
    {
      "periodo": "2025-actualidad",
      "actividad": "SEO técnico y analítica web",
      "descripcion": "Implementación de estrategias de posicionamiento SEO técnico, optimización del rendimiento y velocidad de carga y análisis mediante herramientas de analítica web."
    },
    {
      "periodo": "2023-2026",
      "actividad": "Operador de logística en Family Cash",
      "descripcion": "Preparación de pedidos mediante PDA, operaciones logísticas y gestión de cámaras frigoríficas."
    },
    {
      "periodo": "2023-2024",
      "actividad": "Operador de producción en Ice Cream Factory Comaker",
      "descripcion": "Producción de mezclas y realización de controles fisicoquímicos de calidad a gran escala."
    },
    {
      "periodo": "2021-2023",
      "actividad": "Logística y almacén",
      "descripcion": "Experiencia en Natural Fruit y SEUR realizando clasificación automatizada, picking, preparación de mercancías y operaciones de distribución."
    },
    {
      "actividad": "Producción y asesoramiento técnico industrial",
      "empresa": "Alpha Química S.R.L.",
      "descripcion": "Trabajo como operario de producción, asesor técnico y responsable de gestión de maquinaria industrial relacionada con el sector lácteo."
    }
  ],
  "formacion_academica": [
    {
      "periodo": "2024-actualidad",
      "titulacion": "Ciclo Formativo de Grado Superior en Desarrollo de Aplicaciones Multiplataforma (DAM)",
      "centro": "Tame Centro de Formación",
      "pais": "España"
    },
    {
      "periodo": "Finalizado en 2022",
      "titulacion": "Perito Clasificador de Granos y Oleaginosas",
      "centro": "Escuela de Recibidores de Granos Rosario",
      "pais": "Argentina",
      "observaciones": "Matriculado"
    },
    {
      "periodo": "Finalizado en 2014",
      "titulacion": "Bachiller Técnico Superior",
      "centro": "Escuela Superior Integral de Lechería La Santísima Trinidad",
      "pais": "Argentina"
    }
  ],
  "competencias_tecnicas": {
    "frontend_backend": [
      "HTML5",
      "CSS3",
      "JavaScript ES6+",
      "Node.js",
      "Express.js"
    ],
    "bases_de_datos_seguridad": [
      "PostgreSQL",
      "JWT",
      "Bcrypt",
      "Autenticación",
      "Encriptación"
    ],
    "infraestructura_devops": [
      "Ubuntu Server",
      "Docker",
      "Cloudflare",
      "DNS",
      "SSL/TLS"
    ],
    "herramientas_redes": [
      "Git",
      "GitHub",
      "Google Analytics",
      "Google search",
      "WireGuard",
      "Redes privadas"
    ]
  },
  "idiomas": [
    {
      "idioma": "Español",
      "nivel": "Nativo"
    },
    {
      "idioma": "Inglés",
      "nivel": "B1",
      "marco_referencia": "MCER"
    },
    {
      "idioma": "Alemán",
      "nivel": "A2",
      "marco_referencia": "MCER"
    }
  ],
  "movilidad": {
    "permiso_conducir": {
      "categoria": "B",
      "disponible": true
    },
    "vehiculo_propio": true
  }
}
```
## 3-Resultado aprendizaje
**RA1.md**
```markdown
# Resultado de aprendizaje 1
**Resultado de aprendizaje**
Reconoce las características de lenguajes de marcas analizando e interpretando fragmentos de código.

Criterios de evaluación
a) Se han identificado las características generales de los lenguajes de marcas.
Los lenguajes de marcas emplean etiquetas para estructurar y describir texto y datos; 
pueden indicar su presentación o su estructura lógica, 
y facilitan que personas y sistemas informáticos interpreten y procesen el contenido.

b) Se han reconocido las ventajas que proporcionan en el tratamiento de la información.
Los lenguajes de marcas ofrecen múltiples ventajas en el tratamiento de la información, 
especialmente en términos de organización, interoperabilidad, automatización y accesibilidad.
**Por ejemplo:**
1. Estructura y organización clara
ej: Un libro en XML con etiquetas <capítulo>, <párrafo> y <nota>.
2. Interoperabilidad y estandarización
ej: Un sistema de reservas de hotel que envía datos en JSON a una app de viajes.
3. Automatización y procesamiento eficiente
ej: Un archivo XML de inventario que se convierte automáticamente en un informe en PDF.
4. Accesibilidad y reutilización
ej: Un sitio web en HTML con etiquetas semánticas para que un lector de pantalla lo interprete.

c) Se han clasificado los lenguajes de marcas e identificado los más relevantes.
Los lenguajes de marcas se pueden clasificar según su función principal, su estructura o su aplicacion.
Los más relevantes son: HTML5, XML, JSON, CSS, SVG, Markdown y YAML.

d) Se han diferenciado sus ámbitos de aplicación.
- Para desarrollo web: HTML5, CSS, JSON y SVG son imprescindibles.
- Para intercambio de datos: JSON y XML dominan el mercado.
- Para la web semántica: RDF, JSON-LD y SPARQL son clave.
- Para documentación: Markdown es el rey por su simplicidad.
- Para sectores específicos: Usa el estándar del sector (ej.: HL7 en salud, FpML en finanzas).

e) Se han reconocido la necesidad y los ámbitos específicos de aplicación de un lenguaje de marcas de propósito general.
Un lenguaje de marcas de "propósito general", es el diseñado para ser flexible, y aplicable en diferentes contextos, 
sin estar limitado a un sector o función específica. 
Su principal valor radica en su capacidad para estructurar, describir y transportar información de manera estandarizada, 
lo que lo hace útil en una amplia variedad de ámbitos.
Para mí, el mejor ejemplo de ello es JSON, utilizado en paginas gubernamentales, en progamas informaticos, videojuegos, paginas web privadas, etc.

f) Se han analizado las características propias de diferentes lenguajes de marcas.
Conclusión:
- JSON es el rey para APIs y datos ligeros.
- XML sigue siendo relevante para datos complejos y estándares.
- YAML domina en configuraciones y DevOps.
- Markdown es imbatible para documentación rápida y texto plano.
- HTML5 es esencial para desarrollo web.
- RDF/JSON-LD son clave para la web semántica.
- Lenguajes especializados (HL7, KML, TEI) son indispensables en sus sectores.

g) Se ha identificado la estructura de un documento y sus reglas sintácticas.
La jerarquía y relaciones entre los elementos de por ejemplo un JSON.
Las etiquetas o elementos que lo componen (ej.: <titulo>, <autor>, <capitulo>), en XML.
Las reglas de sintaxis que rigen cómo se escriben esas etiquetas (ej.: apertura y cierre obligatorio, orden de los elementos, atributos permitidos).

h) Se ha contrastado la necesidad de crear documentos bien formados y la influencia en su procesamiento.
Además de seguir las instrucciones del profesor para realizar documentos bien formados de acuerdo a las reglas 
especificas de cada lenguaje de marcas, se nos brindo herramientas para depurar los documentos, buscar fallos, 
corregir, etc, la herramienta que utilice yo para verificar mi json fue: https://jsonlint.com/.

i) Se han identificado las ventajas que aportan los espacios de nombres.
Los espacios de nombres (namespaces) son esenciales en lenguajes como XML, SVG, y otros, 
que permiten organizar y evitar conflictos entre elementos o atributos con el mismo nombre pero pertenecientes a contextos diferentes. 

Ejemplo:
xml

<libro>
    <titulo>Cien años de soledad</titulo>
</libro>
<pelicula>
    <titulo>Cien años de soledad</titulo>
</pelicula>

Solución con namespaces:
xml

<libro xmlns:lib="http://ejemplo.com/libro">
    <lib:titulo>Cien años de soledad</lib:titulo>
</libro>
<pelicula xmlns:pel="http://ejemplo.com/pelicula">
    <pel:titulo>Cien años de soledad</pel:titulo>
</pelicula>
```
