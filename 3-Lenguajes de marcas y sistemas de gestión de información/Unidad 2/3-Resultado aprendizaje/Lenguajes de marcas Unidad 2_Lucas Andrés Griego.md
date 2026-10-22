# Reporte de proyecto

## Información de generación

- **Fecha:** 2026-10-15 05:04:47 +0200
- **Usuario:** lucas
- **Equipo:** LUCAS
- **Sistema operativo:** Windows
- **Arquitectura:** x86_64
- **Directorio de ejecución:** `D:/Herramientas/portables/jocarsa-generador-windows-x64`
- **Proyecto documentado:** `D:/Resultados Aprendizaje_DAM1/3-Lenguajes de marcas y sistemas de gestión de información/Unidad 2`
- **HMAC-SHA-256 de autenticidad:** `7ef74580f8affde9c1e1e432be688db3c1ddd2856f3e26357e823f27ff825820`

> El HMAC-SHA-256 se calcula sobre el documento completo usando un secreto incluido en el programa y 64 ceros en el propio campo del HMAC. El secreto no se escribe en el informe. Este mecanismo permite comprobar integridad y que el documento fue generado con el mismo secreto.

## Estructura del proyecto

```
D:/Resultados Aprendizaje_DAM1/3-Lenguajes de marcas y sistemas de gestión de información/Unidad 2
├── 01-Ejercicios
│   ├── 01-Estándares web. Versiones. Clasificación
│   │   └── 01-Introduccion.md
│   ├── 02-Estructura de un documento HTML
│   │   ├── 01-etiqueta de documento.html
│   │   ├── 02-etiqueta html.html
│   │   ├── 03-cabeza y cuerpo.html
│   │   ├── 04-comentarios.html
│   │   ├── 05-lenguaje del documento.html
│   │   ├── 06-titulo de la web.html
│   │   ├── 07-meta codificación de la web.html
│   │   ├── 08-validacion de documento.md
│   │   └── 09-SEO.md
│   ├── 03-Identificación de etiquetas y atributos de HTML
│   │   ├── 01-Estructura base.html
│   │   ├── 02-Etiquetas y titulares.html
│   │   ├── 03-nav.html
│   │   ├── 04-anchor.html
│   │   ├── 05-section.html
│   │   ├── 06-Cabeceras de section.html
│   │   ├── 07-Parrafos.html
│   │   ├── 08-article.html
│   │   ├── 09-Importar imagen.html
│   │   ├── 10-formulacio.html
│   │   ├── 11-List Item y Unordered List.html
│   │   └── fotocarnet.jpg
│   ├── 05-Hojas de estilo (CSS)
│   │   ├── 00-listado de colores.md
│   │   ├── 00-style externo.html
│   │   ├── 01-punto de partida.html
│   │   ├── 02-style interno.html
│   │   ├── 03-Fondos para contenedores.html
│   │   ├── 04-margin.html
│   │   ├── 05-font family.html
│   │   ├── 06-Tamaño texto.html
│   │   ├── 07-Estilo del menu.html
│   │   ├── 08-br.html
│   │   ├── 09-negrita.html
│   │   ├── 10-flex.html
│   │   ├── 11-grid.html
│   │   ├── 12-footer.html
│   │   ├── 13-Ajusto fuente.html
│   │   ├── fotocarnet.jpg
│   │   └── style.css
│   └── 06-Validación de documentos HTML y CSS
│       ├── 01-Archivo validado.html
│       ├── fotocarnet.jpg
│       └── style.css
├── 02-Proyecto
│   ├── 01-Archivo validado.html
│   ├── fotocarnet.jpg
│   └── style.css
└── 3-Resultado aprendizaje
    └── RA2.md
```

## Bases de datos SQLite

Esta sección documenta únicamente el esquema de las bases SQLite detectadas. No se vuelcan registros ni datos de usuario.

No se han encontrado bases SQLite con extensiones .db, .sqlite o .sqlite3.

## Código (intercalado)

# Unidad 2
## 01-Ejercicios
### 01-Estándares web. Versiones. Clasificación
**01-Introduccion.md**
```markdown
1991 - Tim Berners-Lee publica HTML
(Hyper Text Markup Language)

No es genérico como XML

HTML es un lenguaje con un conjunto de marcas muy definido
Con un propósito muy marcado que es crear sitios web

Tiene un conjunto de marcas cerrado

Originalmente servía para crear documentos

Se convirtieron en páginas web

Las paginas web se convirtieron en sitios web

Los sitios web se convirtieron en aplicaciones web
```
### 02-Estructura de un documento HTML
**01-etiqueta de documento.html**
```html
<!doctype html>
```
**02-etiqueta html.html**
```html
<!doctype html>
<html>
  
</html>
```
**03-cabeza y cuerpo.html**
```html
<!doctype html>
<html>
	<head>
	</head>
	<body>
	</body>
</html>
```
**04-comentarios.html**
```html
<!doctype html>
<html>
	<head>
		<!-- La información de la cabeza no la ve el ser humano sino que se envía al navegador -->
	</head>
	<body>
		<!-- La información del cuerpo es la que ve el ser humano en el navegador web -->
	</body>
</html>
```
**05-lenguaje del documento.html**
```html
<!doctype html>
<html lang="es">
	<head>
		<!-- Se envía al navegador -->
	</head>
	<body>
		<!-- Lo ve el ser humano en el navegador web -->
	</body>
</html>
```
**06-titulo de la web.html**
```html
<!doctype html>
<html lang="es">
	<head>
		<!-- Se envía al navegador -->
    <title>Lucas Andrés Griego</title>
  </head>
	<body>
		<!-- Lo ve el ser humano en el navegador web -->
	</body>
</html>
```
**07-meta codificación de la web.html**
```html
<!doctype html>
<html lang="es">
	<head>
		<!-- Se envía al navegador -->
    <title>Lucas Andrés Griego</title>
    <meta charset="utf-8">
	</head>
	<body>
		<!-- Lo ve el ser humano en el navegador web -->
	</body>
</html>
```
**08-validacion de documento.md**
```markdown
La W3C es la entidad que pone las normas de HTML
Es un consorcio formado por muchas empresas
Cualquier persona puede formar parte de la W3C


link: https://validator.w3.org/#validate_by_input
```
**09-SEO.md**
```markdown
# SEO
Search 
Engine 
Optimization

Optimizar tu página web para que salga bien en los buscadores
Realmente queremos decir Google

# SEO -> GEO

Generative
Engine 
Optimization

Reglas para que tu web salga bien en las IA

Las reglas de sintaxis marcan como se debe escribir tu web
Segun el consorcio que pone esas normas
```
### 03-Identificación de etiquetas y atributos de HTML
**01-Estructura base.html**
```html
<!doctype html>
<html lang="es">
	<head>
		<title>Lucas Andrés Griego</title>
		<meta charset="utf-8">
	</head>
	<body>
	</body>
</html>
```
**02-Etiquetas y titulares.html**
```html
<!doctype html>
<html lang="es">
	<head>
		<title>Lucas Andrés Griego</title>
		<meta charset="utf-8">
	</head>
	<body>
		<header>
			<h1>Lucas Andrés Griego</h1>
			<h2>Propietario de Sturmprojekt</h2>
		</header>
		<main></main>
		<footer></footer>
	</body>
</html>
```
**03-nav.html**
```html
<!doctype html>
<html lang="es">
	<head>
		<title>Lucas Andrés Griego</title>
		<meta charset="utf-8">
	</head>
	<body>
		<header>
			<h1>Lucas Andrés Griego</h1>
			<h2>Propietario de Sturmprojekt</h2>
			<nav>
			
			</nav>
		</header>
		<main></main>
		<footer></footer>
	</body>
</html>
```
**04-anchor.html**
```html
<!doctype html>
<html lang="es">
	<head>
		<title>Lucas Andrés Griego</title>
		<meta charset="utf-8">
	</head>
	<body>
		<header>
			<h1>Lucas Andrés Griego</h1>
			<h2>Propietario de Sturmprojekt</h2>
			<nav>
				<a href="#sobremi">Sobre mi</a>
				<a href="#contacto">Contacto</a>
				<a href="#miweb">Mi web</a>
			</nav>
		</header>
		<main></main>
		<footer></footer>
	</body>
</html>
```
**05-section.html**
```html
<!doctype html>
<html lang="es">
	<head>
		<title>Lucas Andrés Griego</title>
		<meta charset="utf-8">
	</head>
	<body>
	<!-- Esto es un comentario -->
		<header>
			<h1>Lucas Andrés Griego</h1>
			<h2>Propietario de Sturmprojekt</h2>
			<nav>
				<a href="#sobremi">Sobre mi</a>
				<a href="#contacto">Contacto</a>
				<a href="#miweb">Mi web</a>
			</nav>
		</header>
		<main>
			<section id="sobremi"></section>
			<section id="contacto"></section>
			<section id="miweb"></section>
		</main>
		<footer></footer>
	</body>
</html>
```
**06-Cabeceras de section.html**
```html
<!doctype html>
<html lang="es">
	<head>
		<title>Lucas Andrés Griego</title>
		<meta charset="utf-8">
	</head>
	<body>
	<!-- Esto es un comentario -->
		<header>
			<h1>Lucas Andrés Griego</h1>
			<h2>Propietario de Sturmprojekt</h2>
			<nav>
				<a href="#sobremi">Sobre mi</a>
				<a href="#contacto">Contacto</a>
				<a href="#miweb">Mi web</a>
			</nav>
		</header>
		<main>
			<section id="sobremi">
				<h3>Sobre mi</h3>
			</section>
			<section id="contacto">
				<h3>Contacto</h3>
			</section>
			<section id="miweb">
				<h3>Mi web</h3>
			</section>
		</main>
		<footer></footer>
	</body>
</html>
```
**07-Parrafos.html**
```html
<!doctype html>
<html lang="es">
	<head>
		<title>Lucas Andrés Griego</title>
		<meta charset="utf-8">
	</head>
	<body>
	<!-- Esto es un comentario -->
		<header>
			<h1>Lucas Andrés Griego</h1>
			<h2>Propietario de Sturmprojekt</h2>
			<nav>
				<a href="#sobremi">Sobre mi</a>
				<a href="#contacto">Contacto</a>
				<a href="#miweb">Mi web</a>
				<a href="#proyectos">Mis proyectos</a>
			</nav>
		</header>
		<main>
			<section id="sobremi">
				<h3>Sobre mi</h3>
				<p>Soy Lucas Andrés Griego, estudiante de Desarrollo de Aplicaciones Multiplataforma (DAM) y creador de STURMPROJEKT. Me apasionan la informática, la programación y la administración de sistemas Linux. Disfruto aprendiendo mediante la práctica, experimentando con servidores, contenedores Docker, desarrollo web y nuevas tecnologías. Compagino mis estudios con proyectos personales y trabajos para clientes, buscando mejorar mis conocimientos y adquirir experiencia real en el sector tecnológico.</p>
			</section>
			<section id="contacto">
				<h3>Contacto</h3>
				<p>Si quieres ponerte en contacto conmigo para hablar sobre algún proyecto, proponer una colaboración o intercambiar conocimientos sobre tecnología, estaré encantado de escucharte. Puedes encontrarme a través de STURMPROJEKT o conectar conmigo mediante mis perfiles de GitHub, LinkedIn e Instagram. Siempre estoy abierto a nuevas ideas, oportunidades y proyectos que me permitan seguir aprendiendo y creciendo profesionalmente.</p>
			</section>
			<section id="miweb">
				<h3>Mi web</h3>
				<p>STURMPROJEKT es mi proyecto personal y profesional, nacido de mi interés por Linux, los servidores y el aprovechamiento de los recursos tecnológicos. Lo que comenzó como un laboratorio de experimentación con infraestructura auto hospedada ha evolucionado hacia un proyecto dedicado al desarrollo web, hosting, gestión de dominios, despliegue de aplicaciones y mantenimiento de servidores. En mi página puedes conocer los servicios que ofrezco, explorar mi infraestructura y descubrir algunos de los trabajos que he realizado.</p>
			</section>
			<section id="proyectos">
				<h3>Mis proyectos</h3>
				<p>Me gusta desarrollar proyectos que me permitan aprender y solucionar problemas reales. Entre ellos destaca STURMPROJEKT, donde trabajo con infraestructura, alojamiento web y administración de sistemas. También experimento con servidores propios y comparto parte de mi aprendizaje y código en GitHub.</p>
			</section>
		</main>
		<footer></footer>
	</body>
</html>
```
**08-article.html**
```html
<!doctype html>
<html lang="es">
	<head>
		<title>Lucas Andrés Griego</title>
		<meta charset="utf-8">
	</head>
	<body>
	<!-- Esto es un comentario -->
		<header>
			<h1>Lucas Andrés Griego</h1>
			<h2>Propietario de Sturmprojekt</h2>
			<nav>
				<a href="#sobremi">Sobre mi</a>
				<a href="#contacto">Contacto</a>
				<a href="#miweb">Mi web</a>
				<a href="#proyectos">Mis proyectos</a>
			</nav>
		</header>
		<main>
			<section id="sobremi">
				<h3>Sobre mi</h3>
				<p>Soy Lucas Andrés Griego, estudiante de Desarrollo de Aplicaciones Multiplataforma (DAM) y creador de STURMPROJEKT. Me apasionan la informática, la programación y la administración de sistemas Linux. Disfruto aprendiendo mediante la práctica, experimentando con servidores, contenedores Docker, desarrollo web y nuevas tecnologías. Compagino mis estudios con proyectos personales y trabajos para clientes, buscando mejorar mis conocimientos y adquirir experiencia real en el sector tecnológico.</p>
			</section>
			<section id="contacto">
				<h3>Contacto</h3>
				<p>Si quieres ponerte en contacto conmigo para hablar sobre algún proyecto, proponer una colaboración o intercambiar conocimientos sobre tecnología, estaré encantado de escucharte. Puedes encontrarme a través de STURMPROJEKT o conectar conmigo mediante mis perfiles de GitHub, LinkedIn e Instagram. Siempre estoy abierto a nuevas ideas, oportunidades y proyectos que me permitan seguir aprendiendo y creciendo profesionalmente.</p>
			</section>
			<section id="miweb">
				<h3>Mi web</h3>
				<p>STURMPROJEKT es mi proyecto personal y profesional, nacido de mi interés por Linux, los servidores y el aprovechamiento de los recursos tecnológicos. Lo que comenzó como un laboratorio de experimentación con infraestructura auto hospedada ha evolucionado hacia un proyecto dedicado al desarrollo web, hosting, gestión de dominios, despliegue de aplicaciones y mantenimiento de servidores. En mi página puedes conocer los servicios que ofrezco, explorar mi infraestructura y descubrir algunos de los trabajos que he realizado.</p>
			</section>
			<section id="proyectos">
				<h3>Mis proyectos</h3><p>Me gusta desarrollar proyectos que me permitan aprender y solucionar problemas reales. Entre ellos destaca STURMPROJEKT, donde trabajo con infraestructura, alojamiento web y administración de sistemas. También experimento con servidores propios y comparto parte de mi aprendizaje y código en GitHub.</p>
				<article>
					<h4>STURMPROJEKT - Infraestructura propia</h4>
					<p>
					He desarrollado mi propia infraestructura
					de servidores Linux, utilizando Docker,
					Nginx Proxy Manager y Cloudflare para
					alojar y gestionar diferentes servicios.
					Este proyecto me permite experimentar
					con redes, seguridad y administración
					de sistemas.
					</p>
				</article>
				<article>
					<h4>SUMEX Gráfica - Desarrollo web</h4>
					<p>
					Uno de mis primeros trabajos para
					clientes fue el desarrollo y despliegue
					de la página web de SUMEX Gráfica.
					Me encargué de la infraestructura,
					configuración del dominio, DNS,
					certificados SSL y publicación
					de la web mediante Docker y Cloudflare.
					</p>
				</article>
				<article>
					<h4>Monitorización de servidores Linux</h4>
					<p>
					He trabajado en la monitorización
					de servidores Linux y contenedores
					Docker, utilizando herramientas
					de terminal como btop para supervisar
					el consumo de recursos, procesos
					y rendimiento de los sistemas.
					</p>
				</article>
				<article>
					<h4>Servidor Minecraft Bedrock</h4>
					<p>
					He desplegado un servidor dedicado
					de Minecraft Bedrock sobre Linux,
					trabajando con Docker, configuración
					de red y administración remota.
					Este proyecto me ha permitido
					practicar el alojamiento de
					servicios multijugador.
					</p>
				</article>
				<article>
					<h4>Servidor dedicado de Valheim</h4>
					<p>
					Otro de mis proyectos ha sido el
					despliegue de un servidor dedicado
					de Valheim en mi propia infraestructura.
					He trabajado con la configuración
					del entorno Linux, la gestión de
					recursos y la conectividad necesaria
					para alojar partidas multijugador.
					</p>
				</article>
		</main>
		<footer></footer>
	</body>
</html>
```
**09-Importar imagen.html**
```html
<!doctype html>
<html lang="es">
	<head>
		<title>Lucas Andrés Griego</title>
		<meta charset="utf-8">
	</head>
	<body>
	<!-- Esto es un comentario -->
		<header>
			<h1>Lucas Andrés Griego</h1>
			<h2>Propietario de Sturmprojekt</h2>
			<nav>
				<a href="#sobremi">Sobre mi</a>
				<a href="#miweb">Mi web</a>
				<a href="#proyectos">Mis proyectos</a>
				<a href="#contacto">Contacto</a>
			</nav>
		</header>
		<main>
			<section id="sobremi">
				<h3>Sobre mi</h3>
				<img src="fotocarnet.jpg" alt="Foto de Lucas Andrés Griego">
				<p>Soy Lucas Andrés Griego, estudiante de Desarrollo de Aplicaciones Multiplataforma (DAM) y creador de STURMPROJEKT. Me apasionan la informática, la programación y la administración de sistemas Linux. Disfruto aprendiendo mediante la práctica, experimentando con servidores, contenedores Docker, desarrollo web y nuevas tecnologías. Compagino mis estudios con proyectos personales y trabajos para clientes, buscando mejorar mis conocimientos y adquirir experiencia real en el sector tecnológico.</p>
			</section>
			<section id="contacto">
				<h3>Contacto</h3>
				<p>Si quieres ponerte en contacto conmigo para hablar sobre algún proyecto, proponer una colaboración o intercambiar conocimientos sobre tecnología, estaré encantado de escucharte. Puedes encontrarme a través de STURMPROJEKT o conectar conmigo mediante mis perfiles de GitHub, LinkedIn e Instagram. Siempre estoy abierto a nuevas ideas, oportunidades y proyectos que me permitan seguir aprendiendo y creciendo profesionalmente.</p>
			</section>
			<section id="miweb">
				<h3>Mi web</h3>
				<p>STURMPROJEKT es mi proyecto personal y profesional, nacido de mi interés por Linux, los servidores y el aprovechamiento de los recursos tecnológicos. Lo que comenzó como un laboratorio de experimentación con infraestructura auto hospedada ha evolucionado hacia un proyecto dedicado al desarrollo web, hosting, gestión de dominios, despliegue de aplicaciones y mantenimiento de servidores. En mi página puedes conocer los servicios que ofrezco, explorar mi infraestructura y descubrir algunos de los trabajos que he realizado.</p>
			</section>
			<section id="proyectos">
				<h3>Mis proyectos</h3><p>Me gusta desarrollar proyectos que me permitan aprender y solucionar problemas reales. Entre ellos destaca STURMPROJEKT, donde trabajo con infraestructura, alojamiento web y administración de sistemas. También experimento con servidores propios y comparto parte de mi aprendizaje y código en GitHub.</p>
				<article>
					<h4>STURMPROJEKT - Infraestructura propia</h4>
					<p>
					He desarrollado mi propia infraestructura
					de servidores Linux, utilizando Docker,
					Nginx Proxy Manager y Cloudflare para
					alojar y gestionar diferentes servicios.
					Este proyecto me permite experimentar
					con redes, seguridad y administración
					de sistemas.
					</p>
				</article>
				<article>
					<h4>SUMEX Gráfica - Desarrollo web</h4>
					<p>
					Uno de mis primeros trabajos para
					clientes fue el desarrollo y despliegue
					de la página web de SUMEX Gráfica.
					Me encargué de la infraestructura,
					configuración del dominio, DNS,
					certificados SSL y publicación
					de la web mediante Docker y Cloudflare.
					</p>
				</article>
				<article>
					<h4>Monitorización de servidores Linux</h4>
					<p>
					He trabajado en la monitorización
					de servidores Linux y contenedores
					Docker, utilizando herramientas
					de terminal como btop para supervisar
					el consumo de recursos, procesos
					y rendimiento de los sistemas.
					</p>
				</article>
				<article>
					<h4>Servidor Minecraft Bedrock</h4>
					<p>
					He desplegado un servidor dedicado
					de Minecraft Bedrock sobre Linux,
					trabajando con Docker, configuración
					de red y administración remota.
					Este proyecto me ha permitido
					practicar el alojamiento de
					servicios multijugador.
					</p>
				</article>
				<article>
					<h4>Servidor dedicado de Valheim</h4>
					<p>
					Otro de mis proyectos ha sido el
					despliegue de un servidor dedicado
					de Valheim en mi propia infraestructura.
					He trabajado con la configuración
					del entorno Linux, la gestión de
					recursos y la conectividad necesaria
					para alojar partidas multijugador.
					</p>
				</article>
			</section>
		</main>
		<footer></footer>
	</body>
</html>
```
**10-formulacio.html**
```html
<!doctype html>
<html lang="es">
	<head>
		<title>Lucas Andrés Griego</title>
		<meta charset="utf-8">
	</head>
	<body>
	<!-- Esto es un comentario -->
		<header>
			<h1>Lucas Andrés Griego</h1>
			<h2>Propietario de Sturmprojekt</h2>
			<nav>
				<a href="#sobremi">Sobre mi</a>
				<a href="#miweb">Mi web</a>
				<a href="#proyectos">Mis proyectos</a>
				<a href="#contacto">Contacto</a>
			</nav>
		</header>
		<main>
			<section id="sobremi">
				<h3>Sobre mi</h3>
				<img src="fotocarnet.jpg" alt="Foto de Lucas Andrés Griego">
				<p>Soy Lucas Andrés Griego, estudiante de Desarrollo de Aplicaciones Multiplataforma (DAM) y creador de STURMPROJEKT. Me apasionan la informática, la programación y la administración de sistemas Linux. Disfruto aprendiendo mediante la práctica, experimentando con servidores, contenedores Docker, desarrollo web y nuevas tecnologías. Compagino mis estudios con proyectos personales y trabajos para clientes, buscando mejorar mis conocimientos y adquirir experiencia real en el sector tecnológico.</p>
			</section>
			<section id="miweb">
				<h3>Mi web</h3>
				<p>STURMPROJEKT es mi proyecto personal y profesional, nacido de mi interés por Linux, los servidores y el aprovechamiento de los recursos tecnológicos. Lo que comenzó como un laboratorio de experimentación con infraestructura auto hospedada ha evolucionado hacia un proyecto dedicado al desarrollo web, hosting, gestión de dominios, despliegue de aplicaciones y mantenimiento de servidores. En mi página puedes conocer los servicios que ofrezco, explorar mi infraestructura y descubrir algunos de los trabajos que he realizado.</p>
			</section>
			<section id="proyectos">
				<h3>Mis proyectos</h3><p>Me gusta desarrollar proyectos que me permitan aprender y solucionar problemas reales. Entre ellos destaca STURMPROJEKT, donde trabajo con infraestructura, alojamiento web y administración de sistemas. También experimento con servidores propios y comparto parte de mi aprendizaje y código en GitHub.</p>
				<article>
					<h4>STURMPROJEKT - Infraestructura propia</h4>
					<p>
					He desarrollado mi propia infraestructura
					de servidores Linux, utilizando Docker,
					Nginx Proxy Manager y Cloudflare para
					alojar y gestionar diferentes servicios.
					Este proyecto me permite experimentar
					con redes, seguridad y administración
					de sistemas.
					</p>
				</article>
				<article>
					<h4>SUMEX Gráfica - Desarrollo web</h4>
					<p>
					Uno de mis primeros trabajos para
					clientes fue el desarrollo y despliegue
					de la página web de SUMEX Gráfica.
					Me encargué de la infraestructura,
					configuración del dominio, DNS,
					certificados SSL y publicación
					de la web mediante Docker y Cloudflare.
					</p>
				</article>
				<article>
					<h4>Monitorización de servidores Linux</h4>
					<p>
					He trabajado en la monitorización
					de servidores Linux y contenedores
					Docker, utilizando herramientas
					de terminal como btop para supervisar
					el consumo de recursos, procesos
					y rendimiento de los sistemas.
					</p>
				</article>
				<article>
					<h4>Servidor Minecraft Bedrock</h4>
					<p>
					He desplegado un servidor dedicado
					de Minecraft Bedrock sobre Linux,
					trabajando con Docker, configuración
					de red y administración remota.
					Este proyecto me ha permitido
					practicar el alojamiento de
					servicios multijugador.
					</p>
				</article>
				<article>
					<h4>Servidor dedicado de Valheim</h4>
					<p>
					Otro de mis proyectos ha sido el
					despliegue de un servidor dedicado
					de Valheim en mi propia infraestructura.
					He trabajado con la configuración
					del entorno Linux, la gestión de
					recursos y la conectividad necesaria
					para alojar partidas multijugador.
					</p>
				</article>
			</section>
			<section id="contacto">
				<h3>Contacto</h3>
				<p>Si quieres ponerte en contacto conmigo para hablar sobre algún proyecto, proponer una colaboración o intercambiar conocimientos sobre tecnología, estaré encantado de escucharte. Puedes encontrarme a través de STURMPROJEKT o conectar conmigo mediante mis perfiles de GitHub, LinkedIn e Instagram. Siempre estoy abierto a nuevas ideas, oportunidades y proyectos que me permitan seguir aprendiendo y creciendo profesionalmente.</p>
				<form>
					<label>Introduce tu nombre</label>
					<input name="nombre">
					<label>Introduce tu correo</label>
					<input name="correo">
					<label>Introduce tu mensaje</label>
					<textarea name="mensaje"></textarea>
					<input type="submit">
				</form>
			</section>
		</main>
		<footer></footer>
	</body>
</html>
```
**11-List Item y Unordered List.html**
```html
<!doctype html>
<html lang="es">
	<head>
		<title>Lucas Andrés Griego</title>
		<meta charset="utf-8">
	</head>
	<body>
	<!-- Esto es un comentario -->
		<header>
			<h1>Lucas Andrés Griego</h1>
			<h2>Propietario de Sturmprojekt</h2>
			<nav>
				<a href="#sobremi">Sobre mi</a>
				<a href="#miweb">Mi web</a>
				<a href="#formacion">Formación</a>
				<a href="#proyectos">Mis proyectos</a>
				<a href="#contacto">Contacto</a>
			</nav>
		</header>
		<main>
			<section id="sobremi">
				<h3>Sobre mi</h3>
				<img src="fotocarnet.jpg" alt="Foto de Lucas Andrés Griego">
				<p>Soy Lucas Andrés Griego, estudiante de Desarrollo de Aplicaciones Multiplataforma (DAM) y creador de STURMPROJEKT. Me apasionan la informática, la programación y la administración de sistemas Linux. Disfruto aprendiendo mediante la práctica, experimentando con servidores, contenedores Docker, desarrollo web y nuevas tecnologías. Compagino mis estudios con proyectos personales y trabajos para clientes, buscando mejorar mis conocimientos y adquirir experiencia real en el sector tecnológico.</p>
			</section>
			<section id="formacion">
				<h3>Mi formación</h3>
				<p>Actualmente estudio Desarrollo de Aplicaciones Multiplataforma (DAM), donde estoy ampliando mis conocimientos informáticos. Durante mi formación estudio materias como:</p>
				<!-- Aqui van las listas <ul> (lista desordenada, es decir, con viñetas.) y <li> (representa cada elemento de la lista.) -->
				<ul>
					<li>Programación</li>
					<li>Bases de datos</li>
					<li>Entornos de desarrollo</li>
				</ul>
			</section>
			<section id="miweb">
				<h3>Mi web</h3>
				<p>STURMPROJEKT es mi proyecto personal y profesional, nacido de mi interés por Linux, los servidores y el aprovechamiento de los recursos tecnológicos. Lo que comenzó como un laboratorio de experimentación con infraestructura auto hospedada ha evolucionado hacia un proyecto dedicado al desarrollo web, hosting, gestión de dominios, despliegue de aplicaciones y mantenimiento de servidores. En mi página puedes conocer los servicios que ofrezco, explorar mi infraestructura y descubrir algunos de los trabajos que he realizado.</p>
			</section>
			<section id="proyectos">
				<h3>Mis proyectos</h3><p>Me gusta desarrollar proyectos que me permitan aprender y solucionar problemas reales. Entre ellos destaca STURMPROJEKT, donde trabajo con infraestructura, alojamiento web y administración de sistemas. También experimento con servidores propios y comparto parte de mi aprendizaje y código en GitHub.</p>
				<article>
					<h4>STURMPROJEKT - Infraestructura propia</h4>
					<p>He desarrollado mi propia infraestructura de servidores Linux, utilizando Docker, Nginx Proxy Manager y Cloudflare para alojar y gestionar diferentes servicios. Este proyecto me permite experimentar con redes, seguridad y administración de sistemas.</p>
				</article>
				<article>
					<h4>SUMEX Gráfica - Desarrollo web</h4>
					<p>Uno de mis primeros trabajos para clientes fue el desarrollo y despliegue de la página web de SUMEX Gráfica. Me encargué de la infraestructura, configuración del dominio, DNS, certificados SSL y publicación de la web mediante Docker y Cloudflare.</p>
				</article>
				<article>
					<h4>Monitorización de servidores Linux</h4>
					<p>He trabajado en la monitorización de servidores Linux y contenedores Docker, utilizando herramientas de terminal como btop para supervisar el consumo de recursos, procesos y rendimiento de los sistemas.</p>
				</article>
				<article>
					<h4>Servidor Minecraft Bedrock</h4>
					<p>He desplegado un servidor dedicado de Minecraft Bedrock sobre Linux, trabajando con Docker, configuración de red y administración remota. Este proyecto me ha permitido practicar el alojamiento de servicios multijugador.</p>
				</article>
				<article>
					<h4>Servidor dedicado de Valheim</h4>
					<p>Otro de mis proyectos ha sido el despliegue de un servidor dedicado de Valheim en mi propia infraestructura. He trabajado con la configuración del entorno Linux, la gestión de recursos y la conectividad necesaria para alojar partidas multijugador.</p>
				</article>
			</section>
			<section id="contacto">
				<h3>Contacto</h3>
				<p>Si quieres ponerte en contacto conmigo para hablar sobre algún proyecto, proponer una colaboración o intercambiar conocimientos sobre tecnología, estaré encantado de escucharte. Puedes encontrarme a través de STURMPROJEKT o conectar conmigo mediante mis perfiles de GitHub, LinkedIn e Instagram. Siempre estoy abierto a nuevas ideas, oportunidades y proyectos que me permitan seguir aprendiendo y creciendo profesionalmente.</p>
				<form>
					<label>Introduce tu nombre</label>
					<input name="nombre">
					<label>Introduce tu correo</label>
					<input name="correo">
					<label>Introduce tu mensaje</label>
					<textarea name="mensaje"></textarea>
					<input type="submit">
				</form>
			</section>
		</main>
		<footer></footer>
	</body>
</html>
```
### 05-Hojas de estilo (CSS)
**00-listado de colores.md**
```markdown
# aliceblue
# antiquewhite
aqua
aquamarine
# azure
# beige
# bisque
black
# blanchedalmond
blue
blueviolet
## brown
# burlywood
cadetblue
chartreuse
## chocolate
coral
## cornflowerblue
# cornsilk
crimson
cyan
darkblue
darkcyan
darkgoldenrod
# darkgray
darkgreen
# darkgrey
darkkhaki
darkmagenta
darkolivegreen
darkorange
darkorchid
darkred
darksalmon
# darkseagreen
darkslateblue
darkslategray
darkslategrey
darkturquoise
darkviolet
deeppink
## deepskyblue
# dimgray
dimgrey
# dodgerblue
firebrick
floralwhite
forestgreen
fuchsia
gainsboro
ghostwhite
gold
goldenrod
gray
green
greenyellow
grey
honeydew
hotpink
indianred
indigo
ivory
khaki
lavender
lavenderblush
lawngreen
lemonchiffon
lightblue
lightcoral
lightcyan
lightgoldenrodyellow
lightgray
lightgreen
lightgrey
lightpink
lightsalmon
lightseagreen
lightskyblue
lightslategray
lightslategrey
lightsteelblue
lightyellow
lime
limegreen
linen
magenta
maroon
mediumaquamarine
mediumblue
mediumorchid
mediumpurple
mediumseagreen
mediumslateblue
mediumspringgreen
mediumturquoise
mediumvioletred
midnightblue
mintcream
mistyrose
# moccasin
navajowhite
navy
oldlace
olive
olivedrab
orange
orangered
orchid
palegoldenrod
palegreen
paleturquoise
palevioletred
papayawhip
peachpuff
peru
pink
plum
powderblue
purple
rebeccapurple
red
rosybrown
# royalblue
saddlebrown
salmon
sandybrown
seagreen
seashell
sienna
# silver
# skyblue
slateblue
slategray
slategrey
snow
springgreen
steelblue
tan
teal
thistle
tomato
turquoise
violet
wheat
white
whitesmoke
yellow
yellowgreen
```
**00-style externo.html**
```html
<!doctype html>
<html lang="es">
	<head>
		<title>Lucas Andrés Griego</title>
		<meta charset="utf-8">
		<link rel="stylesheet" href="style.css">
	</head>
	<body>
	<!-- Esto es un comentario -->
		<header>
			<h1>Lucas Andrés Griego</h1>
			<h2>Propietario de Sturmprojekt</h2>
			<nav>
				<a href="#sobremi">Sobre mi</a>
				<a href="#miweb">Mi web</a>
				<a href="#formacion">Formación</a>
				<a href="#proyectos">Mis proyectos</a>
				<a href="#contacto">Contacto</a>
			</nav>
		</header>
		<main>
			<section id="sobremi">
				<h3>Sobre mi</h3>
				<img src="fotocarnet.jpg" alt="Foto de Lucas Andrés Griego">
				<p>Soy Lucas Andrés Griego, estudiante de Desarrollo de Aplicaciones Multiplataforma (DAM) y creador de STURMPROJEKT. Me apasionan la informática, la programación y la administración de sistemas Linux. Disfruto aprendiendo mediante la práctica, experimentando con servidores, contenedores Docker, desarrollo web y nuevas tecnologías. Compagino mis estudios con proyectos personales y trabajos para clientes, buscando mejorar mis conocimientos y adquirir experiencia real en el sector tecnológico.</p>
			</section>
			<section id="formacion">
				<h3>Mi formación</h3>
				<p>Actualmente estudio Desarrollo de Aplicaciones Multiplataforma (DAM), donde estoy ampliando mis conocimientos informáticos. Durante mi formación estudio materias como:</p>
				<!-- Aqui van las listas <ul> (lista desordenada, es decir, con viñetas.) y <li> (representa cada elemento de la lista.) -->
				<ul>
					<li>Programación</li>
					<li>Bases de datos</li>
					<li>Entornos de desarrollo</li>
				</ul>
			</section>
			<section id="miweb">
				<h3>Mi web</h3>
				<p>STURMPROJEKT es mi proyecto personal y profesional, nacido de mi interés por Linux, los servidores y el aprovechamiento de los recursos tecnológicos. Lo que comenzó como un laboratorio de experimentación con infraestructura auto hospedada ha evolucionado hacia un proyecto dedicado al desarrollo web, hosting, gestión de dominios, despliegue de aplicaciones y mantenimiento de servidores. En mi página puedes conocer los servicios que ofrezco, explorar mi infraestructura y descubrir algunos de los trabajos que he realizado.</p>
			</section>
			<section id="proyectos">
				<h3>Mis proyectos</h3><p>Me gusta desarrollar proyectos que me permitan aprender y solucionar problemas reales. Entre ellos destaca STURMPROJEKT, donde trabajo con infraestructura, alojamiento web y administración de sistemas. También experimento con servidores propios y comparto parte de mi aprendizaje y código en GitHub.</p>
				<article>
					<h4>STURMPROJEKT - Infraestructura propia</h4>
					<p>He desarrollado mi propia infraestructura de servidores Linux, utilizando Docker, Nginx Proxy Manager y Cloudflare para alojar y gestionar diferentes servicios. Este proyecto me permite experimentar con redes, seguridad y administración de sistemas.</p>
				</article>
				<article>
					<h4>SUMEX Gráfica - Desarrollo web</h4>
					<p>Uno de mis primeros trabajos para clientes fue el desarrollo y despliegue de la página web de SUMEX Gráfica. Me encargué de la infraestructura, configuración del dominio, DNS, certificados SSL y publicación de la web mediante Docker y Cloudflare.</p>
				</article>
				<article>
					<h4>Monitorización de servidores Linux</h4>
					<p>He trabajado en la monitorización de servidores Linux y contenedores Docker, utilizando herramientas de terminal como btop para supervisar el consumo de recursos, procesos y rendimiento de los sistemas.</p>
				</article>
				<article>
					<h4>Servidor Minecraft Bedrock</h4>
					<p>He desplegado un servidor dedicado de Minecraft Bedrock sobre Linux, trabajando con Docker, configuración de red y administración remota. Este proyecto me ha permitido practicar el alojamiento de servicios multijugador.</p>
				</article>
				<article>
					<h4>Servidor dedicado de Valheim</h4>
					<p>Otro de mis proyectos ha sido el despliegue de un servidor dedicado de Valheim en mi propia infraestructura. He trabajado con la configuración del entorno Linux, la gestión de recursos y la conectividad necesaria para alojar partidas multijugador.</p>
				</article>
			</section>
			<section id="contacto">
				<h3>Contacto</h3>
				<p>Si quieres ponerte en contacto conmigo para hablar sobre algún proyecto, proponer una colaboración o intercambiar conocimientos sobre tecnología, estaré encantado de escucharte. Puedes encontrarme a través de STURMPROJEKT o conectar conmigo mediante mis perfiles de GitHub, LinkedIn e Instagram. Siempre estoy abierto a nuevas ideas, oportunidades y proyectos que me permitan seguir aprendiendo y creciendo profesionalmente.</p>
				<form>
					<label>Introduce tu nombre</label>
					<input name="nombre">
					<label>Introduce tu correo</label>
					<input name="correo">
					<label>Introduce tu mensaje</label>
					<textarea name="mensaje"></textarea>
					<input type="submit">
				</form>
			</section>
		</main>
		<footer></footer>
	</body>
</html>
```
**01-punto de partida.html**
```html
<!doctype html>
<html lang="es">
	<head>
		<title>Lucas Andrés Griego</title>
		<meta charset="utf-8">
	</head>
	<body>
	<!-- Esto es un comentario -->
		<header>
			<h1>Lucas Andrés Griego</h1>
			<h2>Propietario de Sturmprojekt</h2>
			<nav>
				<a href="#sobremi">Sobre mi</a>
				<a href="#miweb">Mi web</a>
				<a href="#formacion">Formación</a>
				<a href="#proyectos">Mis proyectos</a>
				<a href="#contacto">Contacto</a>
			</nav>
		</header>
		<main>
			<section id="sobremi">
				<h3>Sobre mi</h3>
				<img src="fotocarnet.jpg" alt="Foto de Lucas Andrés Griego">
				<p>Soy Lucas Andrés Griego, estudiante de Desarrollo de Aplicaciones Multiplataforma (DAM) y creador de STURMPROJEKT. Me apasionan la informática, la programación y la administración de sistemas Linux. Disfruto aprendiendo mediante la práctica, experimentando con servidores, contenedores Docker, desarrollo web y nuevas tecnologías. Compagino mis estudios con proyectos personales y trabajos para clientes, buscando mejorar mis conocimientos y adquirir experiencia real en el sector tecnológico.</p>
			</section>
			<section id="formacion">
				<h3>Mi formación</h3>
				<p>Actualmente estudio Desarrollo de Aplicaciones Multiplataforma (DAM), donde estoy ampliando mis conocimientos informáticos. Durante mi formación estudio materias como:</p>
				<!-- Aqui van las listas <ul> (lista desordenada, es decir, con viñetas.) y <li> (representa cada elemento de la lista.) -->
				<ul>
					<li>Programación</li>
					<li>Bases de datos</li>
					<li>Entornos de desarrollo</li>
				</ul>
			</section>
			<section id="miweb">
				<h3>Mi web</h3>
				<p>STURMPROJEKT es mi proyecto personal y profesional, nacido de mi interés por Linux, los servidores y el aprovechamiento de los recursos tecnológicos. Lo que comenzó como un laboratorio de experimentación con infraestructura auto hospedada ha evolucionado hacia un proyecto dedicado al desarrollo web, hosting, gestión de dominios, despliegue de aplicaciones y mantenimiento de servidores. En mi página puedes conocer los servicios que ofrezco, explorar mi infraestructura y descubrir algunos de los trabajos que he realizado.</p>
			</section>
			<section id="proyectos">
				<h3>Mis proyectos</h3><p>Me gusta desarrollar proyectos que me permitan aprender y solucionar problemas reales. Entre ellos destaca STURMPROJEKT, donde trabajo con infraestructura, alojamiento web y administración de sistemas. También experimento con servidores propios y comparto parte de mi aprendizaje y código en GitHub.</p>
				<article>
					<h4>STURMPROJEKT - Infraestructura propia</h4>
					<p>He desarrollado mi propia infraestructura de servidores Linux, utilizando Docker, Nginx Proxy Manager y Cloudflare para alojar y gestionar diferentes servicios. Este proyecto me permite experimentar con redes, seguridad y administración de sistemas.</p>
				</article>
				<article>
					<h4>SUMEX Gráfica - Desarrollo web</h4>
					<p>Uno de mis primeros trabajos para clientes fue el desarrollo y despliegue de la página web de SUMEX Gráfica. Me encargué de la infraestructura, configuración del dominio, DNS, certificados SSL y publicación de la web mediante Docker y Cloudflare.</p>
				</article>
				<article>
					<h4>Monitorización de servidores Linux</h4>
					<p>He trabajado en la monitorización de servidores Linux y contenedores Docker, utilizando herramientas de terminal como btop para supervisar el consumo de recursos, procesos y rendimiento de los sistemas.</p>
				</article>
				<article>
					<h4>Servidor Minecraft Bedrock</h4>
					<p>He desplegado un servidor dedicado de Minecraft Bedrock sobre Linux, trabajando con Docker, configuración de red y administración remota. Este proyecto me ha permitido practicar el alojamiento de servicios multijugador.</p>
				</article>
				<article>
					<h4>Servidor dedicado de Valheim</h4>
					<p>Otro de mis proyectos ha sido el despliegue de un servidor dedicado de Valheim en mi propia infraestructura. He trabajado con la configuración del entorno Linux, la gestión de recursos y la conectividad necesaria para alojar partidas multijugador.</p>
				</article>
			</section>
			<section id="contacto">
				<h3>Contacto</h3>
				<p>Si quieres ponerte en contacto conmigo para hablar sobre algún proyecto, proponer una colaboración o intercambiar conocimientos sobre tecnología, estaré encantado de escucharte. Puedes encontrarme a través de STURMPROJEKT o conectar conmigo mediante mis perfiles de GitHub, LinkedIn e Instagram. Siempre estoy abierto a nuevas ideas, oportunidades y proyectos que me permitan seguir aprendiendo y creciendo profesionalmente.</p>
				<form>
					<label>Introduce tu nombre</label>
					<input name="nombre">
					<label>Introduce tu correo</label>
					<input name="correo">
					<label>Introduce tu mensaje</label>
					<textarea name="mensaje"></textarea>
					<input type="submit">
				</form>
			</section>
		</main>
		<footer></footer>
	</body>
</html>
```
**02-style interno.html**
```html
<!doctype html>
<html lang="es">
	<head>
		<title>Lucas Andrés Griego</title>
		<meta charset="utf-8">
		<style>
			/* Todo lo que pongamos aqui dentro será CSS */
			body{
				background:skyblue;
			}
		</style>
	</head>
	<body>
	<!-- Esto es un comentario -->
		<header>
			<h1>Lucas Andrés Griego</h1>
			<h2>Propietario de Sturmprojekt</h2>
			<nav>
				<a href="#sobremi">Sobre mi</a>
				<a href="#miweb">Mi web</a>
				<a href="#formacion">Formación</a>
				<a href="#proyectos">Mis proyectos</a>
				<a href="#contacto">Contacto</a>
			</nav>
		</header>
		<main>
			<section id="sobremi">
				<h3>Sobre mi</h3>
				<img src="fotocarnet.jpg" alt="Foto de Lucas Andrés Griego">
				<p>Soy Lucas Andrés Griego, estudiante de Desarrollo de Aplicaciones Multiplataforma (DAM) y creador de STURMPROJEKT. Me apasionan la informática, la programación y la administración de sistemas Linux. Disfruto aprendiendo mediante la práctica, experimentando con servidores, contenedores Docker, desarrollo web y nuevas tecnologías. Compagino mis estudios con proyectos personales y trabajos para clientes, buscando mejorar mis conocimientos y adquirir experiencia real en el sector tecnológico.</p>
			</section>
			<section id="formacion">
				<h3>Mi formación</h3>
				<p>Actualmente estudio Desarrollo de Aplicaciones Multiplataforma (DAM), donde estoy ampliando mis conocimientos informáticos. Durante mi formación estudio materias como:</p>
				<!-- Aqui van las listas <ul> (lista desordenada, es decir, con viñetas.) y <li> (representa cada elemento de la lista.) -->
				<ul>
					<li>Programación</li>
					<li>Bases de datos</li>
					<li>Entornos de desarrollo</li>
				</ul>
			</section>
			<section id="miweb">
				<h3>Mi web</h3>
				<p>STURMPROJEKT es mi proyecto personal y profesional, nacido de mi interés por Linux, los servidores y el aprovechamiento de los recursos tecnológicos. Lo que comenzó como un laboratorio de experimentación con infraestructura auto hospedada ha evolucionado hacia un proyecto dedicado al desarrollo web, hosting, gestión de dominios, despliegue de aplicaciones y mantenimiento de servidores. En mi página puedes conocer los servicios que ofrezco, explorar mi infraestructura y descubrir algunos de los trabajos que he realizado.</p>
			</section>
			<section id="proyectos">
				<h3>Mis proyectos</h3><p>Me gusta desarrollar proyectos que me permitan aprender y solucionar problemas reales. Entre ellos destaca STURMPROJEKT, donde trabajo con infraestructura, alojamiento web y administración de sistemas. También experimento con servidores propios y comparto parte de mi aprendizaje y código en GitHub.</p>
				<article>
					<h4>STURMPROJEKT - Infraestructura propia</h4>
					<p>He desarrollado mi propia infraestructura de servidores Linux, utilizando Docker, Nginx Proxy Manager y Cloudflare para alojar y gestionar diferentes servicios. Este proyecto me permite experimentar con redes, seguridad y administración de sistemas.</p>
				</article>
				<article>
					<h4>SUMEX Gráfica - Desarrollo web</h4>
					<p>Uno de mis primeros trabajos para clientes fue el desarrollo y despliegue de la página web de SUMEX Gráfica. Me encargué de la infraestructura, configuración del dominio, DNS, certificados SSL y publicación de la web mediante Docker y Cloudflare.</p>
				</article>
				<article>
					<h4>Monitorización de servidores Linux</h4>
					<p>He trabajado en la monitorización de servidores Linux y contenedores Docker, utilizando herramientas de terminal como btop para supervisar el consumo de recursos, procesos y rendimiento de los sistemas.</p>
				</article>
				<article>
					<h4>Servidor Minecraft Bedrock</h4>
					<p>He desplegado un servidor dedicado de Minecraft Bedrock sobre Linux, trabajando con Docker, configuración de red y administración remota. Este proyecto me ha permitido practicar el alojamiento de servicios multijugador.</p>
				</article>
				<article>
					<h4>Servidor dedicado de Valheim</h4>
					<p>Otro de mis proyectos ha sido el despliegue de un servidor dedicado de Valheim en mi propia infraestructura. He trabajado con la configuración del entorno Linux, la gestión de recursos y la conectividad necesaria para alojar partidas multijugador.</p>
				</article>
			</section>
			<section id="contacto">
				<h3>Contacto</h3>
				<p>Si quieres ponerte en contacto conmigo para hablar sobre algún proyecto, proponer una colaboración o intercambiar conocimientos sobre tecnología, estaré encantado de escucharte. Puedes encontrarme a través de STURMPROJEKT o conectar conmigo mediante mis perfiles de GitHub, LinkedIn e Instagram. Siempre estoy abierto a nuevas ideas, oportunidades y proyectos que me permitan seguir aprendiendo y creciendo profesionalmente.</p>
				<form>
					<label>Introduce tu nombre</label>
					<input name="nombre">
					<label>Introduce tu correo</label>
					<input name="correo">
					<label>Introduce tu mensaje</label>
					<textarea name="mensaje"></textarea>
					<input type="submit">
				</form>
			</section>
		</main>
		<footer></footer>
	</body>
</html>
```
**03-Fondos para contenedores.html**
```html
<!doctype html>
<html lang="es">
	<head>
		<title>Lucas Andrés Griego</title>
		<meta charset="utf-8">
		<style>
			/* Todo lo que pongamos aqui dentro será CSS */
			body{
				background:skyblue;
			}
			header,main,footer{
				background:cornflowerblue;
				width:900px;
			}
			img{
			width:50%;
			}
		</style>
	</head>
	<body>
	<!-- Esto es un comentario -->
		<header>
			<h1>Lucas Andrés Griego</h1>
			<h2>Propietario de Sturmprojekt</h2>
			<nav>
				<a href="#sobremi">Sobre mi</a>
				<a href="#miweb">Mi web</a>
				<a href="#formacion">Formación</a>
				<a href="#proyectos">Mis proyectos</a>
				<a href="#contacto">Contacto</a>
			</nav>
		</header>
		<main>
			<section id="sobremi">
				<h3>Sobre mi</h3>
				<img src="fotocarnet.jpg" alt="Foto de Lucas Andrés Griego">
				<p>Soy Lucas Andrés Griego, estudiante de Desarrollo de Aplicaciones Multiplataforma (DAM) y creador de STURMPROJEKT. Me apasionan la informática, la programación y la administración de sistemas Linux. Disfruto aprendiendo mediante la práctica, experimentando con servidores, contenedores Docker, desarrollo web y nuevas tecnologías. Compagino mis estudios con proyectos personales y trabajos para clientes, buscando mejorar mis conocimientos y adquirir experiencia real en el sector tecnológico.</p>
			</section>
			<section id="formacion">
				<h3>Mi formación</h3>
				<p>Actualmente estudio Desarrollo de Aplicaciones Multiplataforma (DAM), donde estoy ampliando mis conocimientos informáticos. Durante mi formación estudio materias como:</p>
				<!-- Aqui van las listas <ul> (lista desordenada, es decir, con viñetas.) y <li> (representa cada elemento de la lista.) -->
				<ul>
					<li>Programación</li>
					<li>Bases de datos</li>
					<li>Entornos de desarrollo</li>
				</ul>
			</section>
			<section id="miweb">
				<h3>Mi web</h3>
				<p>STURMPROJEKT es mi proyecto personal y profesional, nacido de mi interés por Linux, los servidores y el aprovechamiento de los recursos tecnológicos. Lo que comenzó como un laboratorio de experimentación con infraestructura auto hospedada ha evolucionado hacia un proyecto dedicado al desarrollo web, hosting, gestión de dominios, despliegue de aplicaciones y mantenimiento de servidores. En mi página puedes conocer los servicios que ofrezco, explorar mi infraestructura y descubrir algunos de los trabajos que he realizado.</p>
			</section>
			<section id="proyectos">
				<h3>Mis proyectos</h3><p>Me gusta desarrollar proyectos que me permitan aprender y solucionar problemas reales. Entre ellos destaca STURMPROJEKT, donde trabajo con infraestructura, alojamiento web y administración de sistemas. También experimento con servidores propios y comparto parte de mi aprendizaje y código en GitHub.</p>
				<article>
					<h4>STURMPROJEKT - Infraestructura propia</h4>
					<p>He desarrollado mi propia infraestructura de servidores Linux, utilizando Docker, Nginx Proxy Manager y Cloudflare para alojar y gestionar diferentes servicios. Este proyecto me permite experimentar con redes, seguridad y administración de sistemas.</p>
				</article>
				<article>
					<h4>SUMEX Gráfica - Desarrollo web</h4>
					<p>Uno de mis primeros trabajos para clientes fue el desarrollo y despliegue de la página web de SUMEX Gráfica. Me encargué de la infraestructura, configuración del dominio, DNS, certificados SSL y publicación de la web mediante Docker y Cloudflare.</p>
				</article>
				<article>
					<h4>Monitorización de servidores Linux</h4>
					<p>He trabajado en la monitorización de servidores Linux y contenedores Docker, utilizando herramientas de terminal como btop para supervisar el consumo de recursos, procesos y rendimiento de los sistemas.</p>
				</article>
				<article>
					<h4>Servidor Minecraft Bedrock</h4>
					<p>He desplegado un servidor dedicado de Minecraft Bedrock sobre Linux, trabajando con Docker, configuración de red y administración remota. Este proyecto me ha permitido practicar el alojamiento de servicios multijugador.</p>
				</article>
				<article>
					<h4>Servidor dedicado de Valheim</h4>
					<p>Otro de mis proyectos ha sido el despliegue de un servidor dedicado de Valheim en mi propia infraestructura. He trabajado con la configuración del entorno Linux, la gestión de recursos y la conectividad necesaria para alojar partidas multijugador.</p>
				</article>
			</section>
			<section id="contacto">
				<h3>Contacto</h3>
				<p>Si quieres ponerte en contacto conmigo para hablar sobre algún proyecto, proponer una colaboración o intercambiar conocimientos sobre tecnología, estaré encantado de escucharte. Puedes encontrarme a través de STURMPROJEKT o conectar conmigo mediante mis perfiles de GitHub, LinkedIn e Instagram. Siempre estoy abierto a nuevas ideas, oportunidades y proyectos que me permitan seguir aprendiendo y creciendo profesionalmente.</p>
				<form>
					<label>Introduce tu nombre</label>
					<input name="nombre">
					<label>Introduce tu correo</label>
					<input name="correo">
					<label>Introduce tu mensaje</label>
					<textarea name="mensaje"></textarea>
					<input type="submit">
				</form>
			</section>
		</main>
		<footer></footer>
	</body>
</html>
```
**04-margin.html**
```html
<!doctype html>
<html lang="es">
	<head>
		<title>Lucas Andrés Griego</title>
		<meta charset="utf-8">
		<style>
			/* Todo lo que pongamos aqui dentro será CSS */
			body{
				background:skyblue;
			}
			header,main,footer{
				background:cornflowerblue;
				width:1000px;
				margin:auto;
				padding:30px;
			}
			img{
			width:30%;
			}
		</style>
	</head>
	<body>
	<!-- Esto es un comentario -->
		<header>
			<h1>Lucas Andrés Griego</h1>
			<h2>Propietario de Sturmprojekt</h2>
			<nav>
				<a href="#sobremi">Sobre mi</a>
				<a href="#miweb">Mi web</a>
				<a href="#formacion">Formación</a>
				<a href="#proyectos">Mis proyectos</a>
				<a href="#contacto">Contacto</a>
			</nav>
		</header>
		<main>
			<section id="sobremi">
				<h3>Sobre mi</h3>
				<img src="fotocarnet.jpg" alt="Foto de Lucas Andrés Griego">
				<p>Soy Lucas Andrés Griego, estudiante de Desarrollo de Aplicaciones Multiplataforma (DAM) y creador de STURMPROJEKT. Me apasionan la informática, la programación y la administración de sistemas Linux. Disfruto aprendiendo mediante la práctica, experimentando con servidores, contenedores Docker, desarrollo web y nuevas tecnologías. Compagino mis estudios con proyectos personales y trabajos para clientes, buscando mejorar mis conocimientos y adquirir experiencia real en el sector tecnológico.</p>
			</section>
			<section id="formacion">
				<h3>Mi formación</h3>
				<p>Actualmente estudio Desarrollo de Aplicaciones Multiplataforma (DAM), donde estoy ampliando mis conocimientos informáticos. Durante mi formación estudio materias como:</p>
				<!-- Aqui van las listas <ul> (lista desordenada, es decir, con viñetas.) y <li> (representa cada elemento de la lista.) -->
				<ul>
					<li>Programación</li>
					<li>Bases de datos</li>
					<li>Entornos de desarrollo</li>
				</ul>
			</section>
			<section id="miweb">
				<h3>Mi web</h3>
				<p>STURMPROJEKT es mi proyecto personal y profesional, nacido de mi interés por Linux, los servidores y el aprovechamiento de los recursos tecnológicos. Lo que comenzó como un laboratorio de experimentación con infraestructura auto hospedada ha evolucionado hacia un proyecto dedicado al desarrollo web, hosting, gestión de dominios, despliegue de aplicaciones y mantenimiento de servidores. En mi página puedes conocer los servicios que ofrezco, explorar mi infraestructura y descubrir algunos de los trabajos que he realizado.</p>
			</section>
			<section id="proyectos">
				<h3>Mis proyectos</h3><p>Me gusta desarrollar proyectos que me permitan aprender y solucionar problemas reales. Entre ellos destaca STURMPROJEKT, donde trabajo con infraestructura, alojamiento web y administración de sistemas. También experimento con servidores propios y comparto parte de mi aprendizaje y código en GitHub.</p>
				<article>
					<h4>STURMPROJEKT - Infraestructura propia</h4>
					<p>He desarrollado mi propia infraestructura de servidores Linux, utilizando Docker, Nginx Proxy Manager y Cloudflare para alojar y gestionar diferentes servicios. Este proyecto me permite experimentar con redes, seguridad y administración de sistemas.</p>
				</article>
				<article>
					<h4>SUMEX Gráfica - Desarrollo web</h4>
					<p>Uno de mis primeros trabajos para clientes fue el desarrollo y despliegue de la página web de SUMEX Gráfica. Me encargué de la infraestructura, configuración del dominio, DNS, certificados SSL y publicación de la web mediante Docker y Cloudflare.</p>
				</article>
				<article>
					<h4>Monitorización de servidores Linux</h4>
					<p>He trabajado en la monitorización de servidores Linux y contenedores Docker, utilizando herramientas de terminal como btop para supervisar el consumo de recursos, procesos y rendimiento de los sistemas.</p>
				</article>
				<article>
					<h4>Servidor Minecraft Bedrock</h4>
					<p>He desplegado un servidor dedicado de Minecraft Bedrock sobre Linux, trabajando con Docker, configuración de red y administración remota. Este proyecto me ha permitido practicar el alojamiento de servicios multijugador.</p>
				</article>
				<article>
					<h4>Servidor dedicado de Valheim</h4>
					<p>Otro de mis proyectos ha sido el despliegue de un servidor dedicado de Valheim en mi propia infraestructura. He trabajado con la configuración del entorno Linux, la gestión de recursos y la conectividad necesaria para alojar partidas multijugador.</p>
				</article>
			</section>
			<section id="contacto">
				<h3>Contacto</h3>
				<p>Si quieres ponerte en contacto conmigo para hablar sobre algún proyecto, proponer una colaboración o intercambiar conocimientos sobre tecnología, estaré encantado de escucharte. Puedes encontrarme a través de STURMPROJEKT o conectar conmigo mediante mis perfiles de GitHub, LinkedIn e Instagram. Siempre estoy abierto a nuevas ideas, oportunidades y proyectos que me permitan seguir aprendiendo y creciendo profesionalmente.</p>
				<form>
					<label>Introduce tu nombre</label>
					<input name="nombre">
					<label>Introduce tu correo</label>
					<input name="correo">
					<label>Introduce tu mensaje</label>
					<textarea name="mensaje"></textarea>
					<input type="submit">
				</form>
			</section>
		</main>
		<footer></footer>
	</body>
</html>
```
**05-font family.html**
```html
<!doctype html>
<html lang="es">
	<head>
		<title>Lucas Andrés Griego</title>
		<meta charset="utf-8">
		<style>
			/* Todo lo que pongamos aqui dentro será CSS */
			body{
				background:skyblue;
				font-family:Arial;
			}
			header,main,footer{
				background:cornflowerblue;
				width:1000px;
				margin:auto;
				padding:30px;
			}
			img{
				width:30%;
			}
			p{
				text-align:justify;
			}	
		</style>
	</head>
	<body>
	<!-- Esto es un comentario -->
		<header>
			<h1>Lucas Andrés Griego</h1>
			<h2>Propietario de Sturmprojekt</h2>
			<nav>
				<a href="#sobremi">Sobre mi</a>
				<a href="#miweb">Mi web</a>
				<a href="#formacion">Formación</a>
				<a href="#proyectos">Mis proyectos</a>
				<a href="#contacto">Contacto</a>
			</nav>
		</header>
		<main>
			<section id="sobremi">
				<h3>Sobre mi</h3>
				<img src="fotocarnet.jpg" alt="Foto de Lucas Andrés Griego">
				<p>Soy Lucas Andrés Griego, estudiante de Desarrollo de Aplicaciones Multiplataforma (DAM) y creador de STURMPROJEKT. Me apasionan la informática, la programación y la administración de sistemas Linux. Disfruto aprendiendo mediante la práctica, experimentando con servidores, contenedores Docker, desarrollo web y nuevas tecnologías. Compagino mis estudios con proyectos personales y trabajos para clientes, buscando mejorar mis conocimientos y adquirir experiencia real en el sector tecnológico.</p>
			</section>
			<section id="formacion">
				<h3>Mi formación</h3>
				<p>Actualmente estudio Desarrollo de Aplicaciones Multiplataforma (DAM), donde estoy ampliando mis conocimientos informáticos. Durante mi formación estudio materias como:</p>
				<!-- Aqui van las listas <ul> (lista desordenada, es decir, con viñetas.) y <li> (representa cada elemento de la lista.) -->
				<ul>
					<li>Programación</li>
					<li>Bases de datos</li>
					<li>Entornos de desarrollo</li>
				</ul>
			</section>
			<section id="miweb">
				<h3>Mi web</h3>
				<p>STURMPROJEKT es mi proyecto personal y profesional, nacido de mi interés por Linux, los servidores y el aprovechamiento de los recursos tecnológicos. Lo que comenzó como un laboratorio de experimentación con infraestructura auto hospedada ha evolucionado hacia un proyecto dedicado al desarrollo web, hosting, gestión de dominios, despliegue de aplicaciones y mantenimiento de servidores. En mi página puedes conocer los servicios que ofrezco, explorar mi infraestructura y descubrir algunos de los trabajos que he realizado.</p>
			</section>
			<section id="proyectos">
				<h3>Mis proyectos</h3><p>Me gusta desarrollar proyectos que me permitan aprender y solucionar problemas reales. Entre ellos destaca STURMPROJEKT, donde trabajo con infraestructura, alojamiento web y administración de sistemas. También experimento con servidores propios y comparto parte de mi aprendizaje y código en GitHub.</p>
				<article>
					<h4>STURMPROJEKT - Infraestructura propia</h4>
					<p>He desarrollado mi propia infraestructura de servidores Linux, utilizando Docker, Nginx Proxy Manager y Cloudflare para alojar y gestionar diferentes servicios. Este proyecto me permite experimentar con redes, seguridad y administración de sistemas.</p>
				</article>
				<article>
					<h4>SUMEX Gráfica - Desarrollo web</h4>
					<p>Uno de mis primeros trabajos para clientes fue el desarrollo y despliegue de la página web de SUMEX Gráfica. Me encargué de la infraestructura, configuración del dominio, DNS, certificados SSL y publicación de la web mediante Docker y Cloudflare.</p>
				</article>
				<article>
					<h4>Monitorización de servidores Linux</h4>
					<p>He trabajado en la monitorización de servidores Linux y contenedores Docker, utilizando herramientas de terminal como btop para supervisar el consumo de recursos, procesos y rendimiento de los sistemas.</p>
				</article>
				<article>
					<h4>Servidor Minecraft Bedrock</h4>
					<p>He desplegado un servidor dedicado de Minecraft Bedrock sobre Linux, trabajando con Docker, configuración de red y administración remota. Este proyecto me ha permitido practicar el alojamiento de servicios multijugador.</p>
				</article>
				<article>
					<h4>Servidor dedicado de Valheim</h4>
					<p>Otro de mis proyectos ha sido el despliegue de un servidor dedicado de Valheim en mi propia infraestructura. He trabajado con la configuración del entorno Linux, la gestión de recursos y la conectividad necesaria para alojar partidas multijugador.</p>
				</article>
			</section>
			<section id="contacto">
				<h3>Contacto</h3>
				<p>Si quieres ponerte en contacto conmigo para hablar sobre algún proyecto, proponer una colaboración o intercambiar conocimientos sobre tecnología, estaré encantado de escucharte. Puedes encontrarme a través de STURMPROJEKT o conectar conmigo mediante mis perfiles de GitHub, LinkedIn e Instagram. Siempre estoy abierto a nuevas ideas, oportunidades y proyectos que me permitan seguir aprendiendo y creciendo profesionalmente.</p>
				<form>
					<label>Introduce tu nombre</label>
					<input name="nombre">
					<label>Introduce tu correo</label>
					<input name="correo">
					<label>Introduce tu mensaje</label>
					<textarea name="mensaje"></textarea>
					<input type="submit">
				</form>
			</section>
		</main>
		<footer></footer>
	</body>
</html>
```
**06-Tamaño texto.html**
```html
<!doctype html>
<html lang="es">
	<head>
		<title>Lucas Andrés Griego</title>
		<meta charset="utf-8">
		<style>
			/* Todo lo que pongamos aqui dentro será CSS */
			body{
				background:skyblue;
				font-family:Arial;
			}
			header,main,footer{
				background:cornflowerblue;
				width:1000px;
				margin:auto;
				padding:30px;
			}
			img{
				width:30%;
			}
			p{
				text-align:justify;
			}
			h1{
				font-size:35px;
			}
			h2{
				font-size:16px;
			}
		</style>
	</head>
	<body>
	<!-- Esto es un comentario -->
		<header>
			<h1>Lucas Andrés Griego</h1>
			<h2>Propietario de Sturmprojekt</h2>
			<nav>
				<a href="#sobremi">Sobre mi</a>
				<a href="#miweb">Mi web</a>
				<a href="#formacion">Formación</a>
				<a href="#proyectos">Mis proyectos</a>
				<a href="#contacto">Contacto</a>
			</nav>
		</header>
		<main>
			<section id="sobremi">
				<h3>Sobre mi</h3>
				<img src="fotocarnet.jpg" alt="Foto de Lucas Andrés Griego">
				<p>Soy Lucas Andrés Griego, estudiante de Desarrollo de Aplicaciones Multiplataforma (DAM) y creador de STURMPROJEKT. Me apasionan la informática, la programación y la administración de sistemas Linux. Disfruto aprendiendo mediante la práctica, experimentando con servidores, contenedores Docker, desarrollo web y nuevas tecnologías. Compagino mis estudios con proyectos personales y trabajos para clientes, buscando mejorar mis conocimientos y adquirir experiencia real en el sector tecnológico.</p>
			</section>
			<section id="formacion">
				<h3>Mi formación</h3>
				<p>Actualmente estudio Desarrollo de Aplicaciones Multiplataforma (DAM), donde estoy ampliando mis conocimientos informáticos. Durante mi formación estudio materias como:</p>
				<!-- Aqui van las listas <ul> (lista desordenada, es decir, con viñetas.) y <li> (representa cada elemento de la lista.) -->
				<ul>
					<li>Programación</li>
					<li>Bases de datos</li>
					<li>Entornos de desarrollo</li>
				</ul>
			</section>
			<section id="miweb">
				<h3>Mi web</h3>
				<p>STURMPROJEKT es mi proyecto personal y profesional, nacido de mi interés por Linux, los servidores y el aprovechamiento de los recursos tecnológicos. Lo que comenzó como un laboratorio de experimentación con infraestructura auto hospedada ha evolucionado hacia un proyecto dedicado al desarrollo web, hosting, gestión de dominios, despliegue de aplicaciones y mantenimiento de servidores. En mi página puedes conocer los servicios que ofrezco, explorar mi infraestructura y descubrir algunos de los trabajos que he realizado.</p>
			</section>
			<section id="proyectos">
				<h3>Mis proyectos</h3><p>Me gusta desarrollar proyectos que me permitan aprender y solucionar problemas reales. Entre ellos destaca STURMPROJEKT, donde trabajo con infraestructura, alojamiento web y administración de sistemas. También experimento con servidores propios y comparto parte de mi aprendizaje y código en GitHub.</p>
				<article>
					<h4>STURMPROJEKT - Infraestructura propia</h4>
					<p>He desarrollado mi propia infraestructura de servidores Linux, utilizando Docker, Nginx Proxy Manager y Cloudflare para alojar y gestionar diferentes servicios. Este proyecto me permite experimentar con redes, seguridad y administración de sistemas.</p>
				</article>
				<article>
					<h4>SUMEX Gráfica - Desarrollo web</h4>
					<p>Uno de mis primeros trabajos para clientes fue el desarrollo y despliegue de la página web de SUMEX Gráfica. Me encargué de la infraestructura, configuración del dominio, DNS, certificados SSL y publicación de la web mediante Docker y Cloudflare.</p>
				</article>
				<article>
					<h4>Monitorización de servidores Linux</h4>
					<p>He trabajado en la monitorización de servidores Linux y contenedores Docker, utilizando herramientas de terminal como btop para supervisar el consumo de recursos, procesos y rendimiento de los sistemas.</p>
				</article>
				<article>
					<h4>Servidor Minecraft Bedrock</h4>
					<p>He desplegado un servidor dedicado de Minecraft Bedrock sobre Linux, trabajando con Docker, configuración de red y administración remota. Este proyecto me ha permitido practicar el alojamiento de servicios multijugador.</p>
				</article>
				<article>
					<h4>Servidor dedicado de Valheim</h4>
					<p>Otro de mis proyectos ha sido el despliegue de un servidor dedicado de Valheim en mi propia infraestructura. He trabajado con la configuración del entorno Linux, la gestión de recursos y la conectividad necesaria para alojar partidas multijugador.</p>
				</article>
			</section>
			<section id="contacto">
				<h3>Contacto</h3>
				<p>Si quieres ponerte en contacto conmigo para hablar sobre algún proyecto, proponer una colaboración o intercambiar conocimientos sobre tecnología, estaré encantado de escucharte. Puedes encontrarme a través de STURMPROJEKT o conectar conmigo mediante mis perfiles de GitHub, LinkedIn e Instagram. Siempre estoy abierto a nuevas ideas, oportunidades y proyectos que me permitan seguir aprendiendo y creciendo profesionalmente.</p>
				<form>
					<label>Introduce tu nombre</label>
					<input name="nombre">
					<label>Introduce tu correo</label>
					<input name="correo">
					<label>Introduce tu mensaje</label>
					<textarea name="mensaje"></textarea>
					<input type="submit">
				</form>
			</section>
		</main>
		<footer></footer>
	</body>
</html>
```
**07-Estilo del menu.html**
```html
<!doctype html>
<html lang="es">
	<head>
		<title>Lucas Andrés Griego</title>
		<meta charset="utf-8">
		<style>
			/* Todo lo que pongamos aqui dentro será CSS */
			body{
				background:skyblue;
				font-family:Arial;
			}
			header,main,footer{
				background:cornflowerblue;
				width:1000px;
				margin:auto;
				padding:30px;
			}
			img{
				width:30%;
			}
			p{
				text-align:justify;
			}
			h1{
				font-size:35px;
			}
			h2{
				font-size:16px;
			}
			a{
				background:royalblue;
				color:white;
				text-decoration:none;
				padding:5px 10px;
				font-size:11px;
			}
		</style>
	</head>
	<body>
	<!-- Esto es un comentario -->
		<header>
			<h1>Lucas Andrés Griego</h1>
			<h2>Propietario de Sturmprojekt</h2>
			<nav>
				<a href="#sobremi">Sobre mi</a>
				<a href="#miweb">Mi web</a>
				<a href="#formacion">Formación</a>
				<a href="#proyectos">Mis proyectos</a>
				<a href="#contacto">Contacto</a>
			</nav>
		</header>
		<main>
			<section id="sobremi">
				<h3>Sobre mi</h3>
				<img src="fotocarnet.jpg" alt="Foto de Lucas Andrés Griego">
				<p>Soy Lucas Andrés Griego, estudiante de Desarrollo de Aplicaciones Multiplataforma (DAM) y creador de STURMPROJEKT. Me apasionan la informática, la programación y la administración de sistemas Linux. Disfruto aprendiendo mediante la práctica, experimentando con servidores, contenedores Docker, desarrollo web y nuevas tecnologías. Compagino mis estudios con proyectos personales y trabajos para clientes, buscando mejorar mis conocimientos y adquirir experiencia real en el sector tecnológico.</p>
			</section>
			<section id="formacion">
				<h3>Mi formación</h3>
				<p>Actualmente estudio Desarrollo de Aplicaciones Multiplataforma (DAM), donde estoy ampliando mis conocimientos informáticos. Durante mi formación estudio materias como:</p>
				<!-- Aqui van las listas <ul> (lista desordenada, es decir, con viñetas.) y <li> (representa cada elemento de la lista.) -->
				<ul>
					<li>Programación</li>
					<li>Bases de datos</li>
					<li>Entornos de desarrollo</li>
				</ul>
			</section>
			<section id="miweb">
				<h3>Mi web</h3>
				<p>STURMPROJEKT es mi proyecto personal y profesional, nacido de mi interés por Linux, los servidores y el aprovechamiento de los recursos tecnológicos. Lo que comenzó como un laboratorio de experimentación con infraestructura auto hospedada ha evolucionado hacia un proyecto dedicado al desarrollo web, hosting, gestión de dominios, despliegue de aplicaciones y mantenimiento de servidores. En mi página puedes conocer los servicios que ofrezco, explorar mi infraestructura y descubrir algunos de los trabajos que he realizado.</p>
			</section>
			<section id="proyectos">
				<h3>Mis proyectos</h3><p>Me gusta desarrollar proyectos que me permitan aprender y solucionar problemas reales. Entre ellos destaca STURMPROJEKT, donde trabajo con infraestructura, alojamiento web y administración de sistemas. También experimento con servidores propios y comparto parte de mi aprendizaje y código en GitHub.</p>
				<article>
					<h4>STURMPROJEKT - Infraestructura propia</h4>
					<p>He desarrollado mi propia infraestructura de servidores Linux, utilizando Docker, Nginx Proxy Manager y Cloudflare para alojar y gestionar diferentes servicios. Este proyecto me permite experimentar con redes, seguridad y administración de sistemas.</p>
				</article>
				<article>
					<h4>SUMEX Gráfica - Desarrollo web</h4>
					<p>Uno de mis primeros trabajos para clientes fue el desarrollo y despliegue de la página web de SUMEX Gráfica. Me encargué de la infraestructura, configuración del dominio, DNS, certificados SSL y publicación de la web mediante Docker y Cloudflare.</p>
				</article>
				<article>
					<h4>Monitorización de servidores Linux</h4>
					<p>He trabajado en la monitorización de servidores Linux y contenedores Docker, utilizando herramientas de terminal como btop para supervisar el consumo de recursos, procesos y rendimiento de los sistemas.</p>
				</article>
				<article>
					<h4>Servidor Minecraft Bedrock</h4>
					<p>He desplegado un servidor dedicado de Minecraft Bedrock sobre Linux, trabajando con Docker, configuración de red y administración remota. Este proyecto me ha permitido practicar el alojamiento de servicios multijugador.</p>
				</article>
				<article>
					<h4>Servidor dedicado de Valheim</h4>
					<p>Otro de mis proyectos ha sido el despliegue de un servidor dedicado de Valheim en mi propia infraestructura. He trabajado con la configuración del entorno Linux, la gestión de recursos y la conectividad necesaria para alojar partidas multijugador.</p>
				</article>
			</section>
			<section id="contacto">
				<h3>Contacto</h3>
				<p>Si quieres ponerte en contacto conmigo para hablar sobre algún proyecto, proponer una colaboración o intercambiar conocimientos sobre tecnología, estaré encantado de escucharte. Puedes encontrarme a través de STURMPROJEKT o conectar conmigo mediante mis perfiles de GitHub, LinkedIn e Instagram. Siempre estoy abierto a nuevas ideas, oportunidades y proyectos que me permitan seguir aprendiendo y creciendo profesionalmente.</p>
				<form>
					<label>Introduce tu nombre</label>
					<input name="nombre">
					<label>Introduce tu correo</label>
					<input name="correo">
					<label>Introduce tu mensaje</label>
					<textarea name="mensaje"></textarea>
					<input type="submit">
				</form>
			</section>
		</main>
		<footer></footer>
	</body>
</html>
```
**08-br.html**
```html
<!doctype html>
<html lang="es">
	<head>
		<title>Lucas Andrés Griego</title>
		<meta charset="utf-8">
		<style>
			/* Todo lo que pongamos aqui dentro será CSS */
			body{
				background:skyblue;
				font-family:Arial;
			}
			header,main,footer{
				background:cornflowerblue;
				width:1000px;
				margin:auto;
				padding:30px;
			}
			img{
				width:30%;
			}
			p{
				text-align:justify;
			}
			h1{
				font-size:35px;
				margin:0px;
			}
			h2{
				font-size:16px;
			}
			a{
				background:royalblue;
				color:white;
				text-decoration:none;
				padding:5px 10px;
				font-size:11px;
			}
		</style>
	</head>
	<body>
	<!-- Esto es un comentario -->
		<header>
			<h1>Lucas Andrés Griego</h1>
			<h2>Propietario de Sturmprojekt</h2>
			<nav>
				<a href="#sobremi">Sobre mi</a>
				<a href="#miweb">Mi web</a>
				<a href="#formacion">Formación</a>
				<a href="#proyectos">Mis proyectos</a>
				<a href="#contacto">Contacto</a>
			</nav>
		</header>
		<main>
			<section id="sobremi">
				<h3>Sobre mi</h3>
				<img src="fotocarnet.jpg" alt="Foto de Lucas Andrés Griego">
				<p>Soy Lucas Andrés Griego, estudiante de Desarrollo de Aplicaciones Multiplataforma (DAM) y creador de STURMPROJEKT. Me apasionan la informática, la programación y la administración de sistemas Linux. Disfruto aprendiendo mediante la práctica, experimentando con servidores, contenedores Docker, desarrollo web y nuevas tecnologías. Compagino mis estudios con proyectos personales y trabajos para clientes, buscando mejorar mis conocimientos y adquirir experiencia real en el sector tecnológico.</p>
			</section>
			<section id="formacion">
				<h3>Mi formación</h3>
				<p>Actualmente estudio Desarrollo de Aplicaciones Multiplataforma (DAM), donde estoy ampliando mis conocimientos informáticos. Durante mi formación estudio materias como:</p>
				<!-- Aqui van las listas <ul> (lista desordenada, es decir, con viñetas.) y <li> (representa cada elemento de la lista.) -->
				<ul>
					<li>Programación</li>
					<li>Bases de datos</li>
					<li>Entornos de desarrollo</li>
				</ul>
			</section>
			<section id="miweb">
				<h3>Mi web</h3>
				<p>
					<br>STURMPROJEKT es mi proyecto personal y profesional, 
					<br>
					<br>nacido de mi interés por Linux, los servidores y el aprovechamiento de los recursos tecnológicos. 
					<br>
					<br>Lo que comenzó como un laboratorio de experimentación con infraestructura auto hospedada, 
					<br>
					<br>ha evolucionado hacia un proyecto dedicado al desarrollo web, hosting, gestión de dominios, 
					<br>
					<br>despliegue de aplicaciones y mantenimiento de servidores. 
					<br>
					<br>En mi página puedes conocer los servicios que ofrezco, 
					<br>
					<br>explorar mi infraestructura y descubrir algunos de los trabajos que he realizado.
				</p>
			</section>
			<section id="proyectos">
				<h3>Mis proyectos</h3><p>Me gusta desarrollar proyectos que me permitan aprender y solucionar problemas reales. Entre ellos destaca STURMPROJEKT, donde trabajo con infraestructura, alojamiento web y administración de sistemas. También experimento con servidores propios y comparto parte de mi aprendizaje y código en GitHub.</p>
				<article>
					<h4>STURMPROJEKT - Infraestructura propia</h4>
					<p>He desarrollado mi propia infraestructura de servidores Linux, utilizando Docker, Nginx Proxy Manager y Cloudflare para alojar y gestionar diferentes servicios. Este proyecto me permite experimentar con redes, seguridad y administración de sistemas.</p>
				</article>
				<article>
					<h4>SUMEX Gráfica - Desarrollo web</h4>
					<p>Uno de mis primeros trabajos para clientes fue el desarrollo y despliegue de la página web de SUMEX Gráfica. Me encargué de la infraestructura, configuración del dominio, DNS, certificados SSL y publicación de la web mediante Docker y Cloudflare.</p>
				</article>
				<article>
					<h4>Monitorización de servidores Linux</h4>
					<p>He trabajado en la monitorización de servidores Linux y contenedores Docker, utilizando herramientas de terminal como btop para supervisar el consumo de recursos, procesos y rendimiento de los sistemas.</p>
				</article>
				<article>
					<h4>Servidor Minecraft Bedrock</h4>
					<p>He desplegado un servidor dedicado de Minecraft Bedrock sobre Linux, trabajando con Docker, configuración de red y administración remota. Este proyecto me ha permitido practicar el alojamiento de servicios multijugador.</p>
				</article>
				<article>
					<h4>Servidor dedicado de Valheim</h4>
					<p>Otro de mis proyectos ha sido el despliegue de un servidor dedicado de Valheim en mi propia infraestructura. He trabajado con la configuración del entorno Linux, la gestión de recursos y la conectividad necesaria para alojar partidas multijugador.</p>
				</article>
			</section>
			<section id="contacto">
				<h3>Contacto</h3>
				<p>Si quieres ponerte en contacto conmigo para hablar sobre algún proyecto, proponer una colaboración o intercambiar conocimientos sobre tecnología, estaré encantado de escucharte. Puedes encontrarme a través de STURMPROJEKT o conectar conmigo mediante mis perfiles de GitHub, LinkedIn e Instagram. Siempre estoy abierto a nuevas ideas, oportunidades y proyectos que me permitan seguir aprendiendo y creciendo profesionalmente.</p>
				<form>
					<label>Introduce tu nombre</label>
					<input name="nombre">
					<label>Introduce tu correo</label>
					<input name="correo">
					<label>Introduce tu mensaje</label>
					<textarea name="mensaje"></textarea>
					<input type="submit">
				</form>
			</section>
		</main>
		<footer></footer>
	</body>
</html>
```
**09-negrita.html**
```html
<!doctype html>
<html lang="es">
	<head>
		<title>Lucas Andrés Griego</title>
		<meta charset="utf-8">
		<style>
			/* Todo lo que pongamos aqui dentro será CSS */
			body{
				background:skyblue;
				font-family:Arial;
			}
			header,main,footer{
				background:cornflowerblue;
				width:1000px;
				margin:auto;
				padding:30px;
			}
			img{
				width:30%;
			}
			p{
				text-align:justify;
			}
			h1{
				font-size:35px;
			}
			h2{
				font-size:16px;
			}
			a{
				background:royalblue;
				color:white;
				text-decoration:none;
				padding:5px 10px;
				font-size:11px;
			}
		</style>
	</head>
	<body>
	<!-- Esto es un comentario -->
		<header>
			<h1>Lucas Andrés Griego</h1>
			<h2>Propietario de Sturmprojekt</h2>
			<nav>
				<a href="#sobremi">Sobre mi</a>
				<a href="#miweb">Mi web</a>
				<a href="#formacion">Formación</a>
				<a href="#proyectos">Mis proyectos</a>
				<a href="#contacto">Contacto</a>
			</nav>
		</header>
		<main>
			<section id="sobremi">
				<h3>Sobre mi</h3>
				<img src="fotocarnet.jpg" alt="Foto de Lucas Andrés Griego">
				<p>Soy <b>Lucas Andrés Griego,</b> estudiante de Desarrollo de Aplicaciones Multiplataforma <b>(DAM)</b> y creador de STURMPROJEKT. Me apasionan la informática, la programación y la administración de sistemas Linux. Disfruto aprendiendo mediante la práctica, experimentando con servidores, contenedores Docker, desarrollo web y nuevas tecnologías. Compagino mis estudios con proyectos personales y trabajos para clientes, buscando mejorar mis conocimientos y adquirir experiencia real en el sector tecnológico.</p>
			</section>
			<section id="formacion">
				<h3>Mi formación</h3>
				<p>Actualmente estudio Desarrollo de Aplicaciones Multiplataforma (DAM), donde estoy ampliando mis conocimientos informáticos. Durante mi formación estudio materias como:</p>
				<!-- Aqui van las listas <ul> (lista desordenada, es decir, con viñetas.) y <li> (representa cada elemento de la lista.) -->
				<ul>
					<li>Programación</li>
					<li>Bases de datos</li>
					<li>Entornos de desarrollo</li>
				</ul>
			</section>
			<section id="miweb">
				<h3>Mi web</h3>
				<p>STURMPROJEKT es mi proyecto personal y profesional, nacido de mi interés por Linux, los servidores y el aprovechamiento de los recursos tecnológicos. Lo que comenzó como un laboratorio de experimentación con infraestructura auto hospedada ha evolucionado hacia un proyecto dedicado al desarrollo web, hosting, gestión de dominios, despliegue de aplicaciones y mantenimiento de servidores. En mi página puedes conocer los servicios que ofrezco, explorar mi infraestructura y descubrir algunos de los trabajos que he realizado.</p>
			</section>
			<section id="proyectos">
				<h3>Mis proyectos</h3><p>Me gusta desarrollar proyectos que me permitan aprender y solucionar problemas reales. Entre ellos destaca STURMPROJEKT, donde trabajo con infraestructura, alojamiento web y administración de sistemas. También experimento con servidores propios y comparto parte de mi aprendizaje y código en GitHub.</p>
				<article>
					<h4><b>STURMPROJEKT</b> - Infraestructura propia</h4>
					<p>He desarrollado mi propia infraestructura de servidores Linux, utilizando Docker, Nginx Proxy Manager y Cloudflare para alojar y gestionar diferentes servicios. Este proyecto me permite experimentar con redes, seguridad y administración de sistemas.</p>
				</article>
				<article>
					<h4>SUMEX Gráfica - Desarrollo web</h4>
					<p>Uno de mis primeros trabajos para clientes fue el desarrollo y despliegue de la página web de SUMEX Gráfica. Me encargué de la infraestructura, configuración del dominio, DNS, certificados SSL y publicación de la web mediante Docker y Cloudflare.</p>
				</article>
				<article>
					<h4>Monitorización de servidores Linux</h4>
					<p>He trabajado en la monitorización de servidores Linux y contenedores Docker, utilizando herramientas de terminal como btop para supervisar el consumo de recursos, procesos y rendimiento de los sistemas.</p>
				</article>
				<article>
					<h4>Servidor Minecraft Bedrock</h4>
					<p>He desplegado un servidor dedicado de Minecraft Bedrock sobre Linux, trabajando con Docker, configuración de red y administración remota. Este proyecto me ha permitido practicar el alojamiento de servicios multijugador.</p>
				</article>
				<article>
					<h4>Servidor dedicado de Valheim</h4>
					<p>Otro de mis proyectos ha sido el despliegue de un servidor dedicado de Valheim en mi propia infraestructura. He trabajado con la configuración del entorno Linux, la gestión de recursos y la conectividad necesaria para alojar partidas multijugador.</p>
				</article>
			</section>
			<section id="contacto">
				<h3>Contacto</h3>
				<p>Si quieres ponerte en contacto conmigo para hablar sobre algún proyecto, proponer una colaboración o intercambiar conocimientos sobre tecnología, estaré encantado de escucharte. Puedes encontrarme a través de STURMPROJEKT o conectar conmigo mediante mis perfiles de GitHub, LinkedIn e Instagram. Siempre estoy abierto a nuevas ideas, oportunidades y proyectos que me permitan seguir aprendiendo y creciendo profesionalmente.</p>
				<form>
					<label><b>Introduce tu nombre</b></label>
					<input name="nombre">
					<label><b>Introduce tu correo</b></label>
					<input name="correo">
					<label><b>Introduce tu mensaje</b></label>
					<textarea name="mensaje"></textarea>
					<input type="submit">
				</form>
			</section>
		</main>
		<footer></footer>
	</body>
</html>
```
**10-flex.html**
```html
<!doctype html>
<html lang="es">
	<head>
		<title>Lucas Andrés Griego</title>
		<meta charset="utf-8">
		<style>
			/* Todo lo que pongamos aqui dentro será CSS */
			body{
				background:skyblue;
				font-family:Arial;
			}
			header,main,footer{
				background:cornflowerblue;
				width:1000px;
				margin:auto;
				padding:30px;
			}
			img{
				width:30%;
			}
			p{
				text-align:justify;
			}
			h1{
				font-size:35px;
			}
			h2{
				font-size:16px;
			}
			a{
				background:royalblue;
				color:white;
				text-decoration:none;
				padding:5px 10px;
				font-size:11px;
			}
			/* FLEX para el form */
			form{
				display:flex;
				flex-direction:column;
				gap:10px;
			}
		</style>
	</head>
	<body>
	<!-- Esto es un comentario -->
		<header>
			<h1>Lucas Andrés Griego</h1>
			<h2>Propietario de Sturmprojekt</h2>
			<nav>
				<a href="#sobremi">Sobre mi</a>
				<a href="#miweb">Mi web</a>
				<a href="#formacion">Formación</a>
				<a href="#proyectos">Mis proyectos</a>
				<a href="#contacto">Contacto</a>
			</nav>
		</header>
		<main>
			<section id="sobremi">
				<h3>Sobre mi</h3>
				<img src="fotocarnet.jpg" alt="Foto de Lucas Andrés Griego">
				<p>Soy <b>Lucas Andrés Griego,</b> estudiante de Desarrollo de Aplicaciones Multiplataforma <b>(DAM)</b> y creador de STURMPROJEKT. Me apasionan la informática, la programación y la administración de sistemas Linux. Disfruto aprendiendo mediante la práctica, experimentando con servidores, contenedores Docker, desarrollo web y nuevas tecnologías. Compagino mis estudios con proyectos personales y trabajos para clientes, buscando mejorar mis conocimientos y adquirir experiencia real en el sector tecnológico.</p>
			</section>
			<section id="formacion">
				<h3>Mi formación</h3>
				<p>Actualmente estudio Desarrollo de Aplicaciones Multiplataforma (DAM), donde estoy ampliando mis conocimientos informáticos. Durante mi formación estudio materias como:</p>
				<!-- Aqui van las listas <ul> (lista desordenada, es decir, con viñetas.) y <li> (representa cada elemento de la lista.) -->
				<ul>
					<li>Programación</li>
					<li>Bases de datos</li>
					<li>Entornos de desarrollo</li>
				</ul>
			</section>
			<section id="miweb">
				<h3>Mi web</h3>
				<p><b>STURMPROJEKT</b> es mi proyecto personal y profesional, nacido de mi interés por Linux, los servidores y el aprovechamiento de los recursos tecnológicos. Lo que comenzó como un laboratorio de experimentación con infraestructura auto hospedada ha evolucionado hacia un proyecto dedicado al desarrollo web, hosting, gestión de dominios, despliegue de aplicaciones y mantenimiento de servidores. En mi página puedes conocer los servicios que ofrezco, explorar mi infraestructura y descubrir algunos de los trabajos que he realizado.</p>
			</section>
			<section id="proyectos">
				<h3>Mis proyectos</h3><p>Me gusta desarrollar proyectos que me permitan aprender y solucionar problemas reales. Entre ellos destaca STURMPROJEKT, donde trabajo con infraestructura, alojamiento web y administración de sistemas. También experimento con servidores propios y comparto parte de mi aprendizaje y código en GitHub.</p>
				<article>
					<h4>STURMPROJEKT - Infraestructura propia</h4>
					<p>He desarrollado mi propia infraestructura de servidores Linux, utilizando Docker, Nginx Proxy Manager y Cloudflare para alojar y gestionar diferentes servicios. Este proyecto me permite experimentar con redes, seguridad y administración de sistemas.</p>
				</article>
				<article>
					<h4>SUMEX Gráfica - Desarrollo web</h4>
					<p>Uno de mis primeros trabajos para clientes fue el desarrollo y despliegue de la página web de SUMEX Gráfica. Me encargué de la infraestructura, configuración del dominio, DNS, certificados SSL y publicación de la web mediante Docker y Cloudflare.</p>
				</article>
				<article>
					<h4>Monitorización de servidores Linux</h4>
					<p>He trabajado en la monitorización de servidores Linux y contenedores Docker, utilizando herramientas de terminal como btop para supervisar el consumo de recursos, procesos y rendimiento de los sistemas.</p>
				</article>
				<article>
					<h4>Servidor Minecraft Bedrock</h4>
					<p>He desplegado un servidor dedicado de Minecraft Bedrock sobre Linux, trabajando con Docker, configuración de red y administración remota. Este proyecto me ha permitido practicar el alojamiento de servicios multijugador.</p>
				</article>
				<article>
					<h4>Servidor dedicado de Valheim</h4>
					<p>Otro de mis proyectos ha sido el despliegue de un servidor dedicado de Valheim en mi propia infraestructura. He trabajado con la configuración del entorno Linux, la gestión de recursos y la conectividad necesaria para alojar partidas multijugador.</p>
				</article>
			</section>
			<section id="contacto">
				<h3>Contacto</h3>
				<p>Si quieres ponerte en contacto conmigo para hablar sobre algún proyecto, proponer una colaboración o intercambiar conocimientos sobre tecnología, estaré encantado de escucharte. Puedes encontrarme a través de STURMPROJEKT o conectar conmigo mediante mis perfiles de GitHub, LinkedIn e Instagram. Siempre estoy abierto a nuevas ideas, oportunidades y proyectos que me permitan seguir aprendiendo y creciendo profesionalmente.</p>
				<form>
					<label><b>Introduce tu nombre</b></label>
					<input name="nombre">
					<label><b>Introduce tu correo</b></label>
					<input name="correo">
					<label><b>Introduce tu mensaje</b></label>
					<textarea name="mensaje"></textarea>
					<input type="submit">
				</form>
			</section>
		</main>
		<footer></footer>
	</body>
</html>
```
**11-grid.html**
```html
<!doctype html>
<html lang="es">
	<head>
		<title>Lucas Andrés Griego</title>
		<meta charset="utf-8">
		<style>
			/* Todo lo que pongamos aqui dentro será CSS */
			body{
				background:skyblue;
				font-family:Arial;
			}
			header,main,footer{
				background:cornflowerblue;
				width:1000px;
				margin:auto;
				padding:30px;
			}
			img{
				width:30%;
			}
			p{
				text-align:justify;
			}
			h1{
				font-size:35px;
			}
			h2{
				font-size:16px;
			}
			a{
				background:royalblue;
				color:white;
				text-decoration:none;
				padding:5px 10px;
				font-size:11px;
			}
			/* FLEX para el form */
			form{
				display:flex;
				flex-direction:column;
				gap:10px;
			}
			/* GRID para proyectos */
			#proyectos{
				display:grid;
				grid-template-columns:repeat(3,1fr);
				margin:auto;
				justify-content: center;
				gap: 20px;
			}
		</style>
	</head>
	<body>
	<!-- Esto es un comentario -->
		<header>
			<h1>Lucas Andrés Griego</h1>
			<h2>Propietario de Sturmprojekt</h2>
			<nav>
				<a href="#sobremi">Sobre mi</a>
				<a href="#miweb">Mi web</a>
				<a href="#formacion">Formación</a>
				<a href="#proyectos">Mis proyectos</a>
				<a href="#contacto">Contacto</a>
			</nav>
		</header>
		<main>
			<section id="sobremi">
				<h3>Sobre mi</h3>
				<img src="fotocarnet.jpg" alt="Foto de Lucas Andrés Griego">
				<p>Soy <b>Lucas Andrés Griego,</b> estudiante de Desarrollo de Aplicaciones Multiplataforma <b>(DAM)</b> y creador de STURMPROJEKT. Me apasionan la informática, la programación y la administración de sistemas Linux. Disfruto aprendiendo mediante la práctica, experimentando con servidores, contenedores Docker, desarrollo web y nuevas tecnologías. Compagino mis estudios con proyectos personales y trabajos para clientes, buscando mejorar mis conocimientos y adquirir experiencia real en el sector tecnológico.</p>
			</section>
			<section id="formacion">
				<h3>Mi formación</h3>
				<p>Actualmente estudio Desarrollo de Aplicaciones Multiplataforma (DAM), donde estoy ampliando mis conocimientos informáticos. Durante mi formación estudio materias como:</p>
				<!-- Aqui van las listas <ul> (lista desordenada, es decir, con viñetas.) y <li> (representa cada elemento de la lista.) -->
				<ul>
					<li>Programación</li>
					<li>Bases de datos</li>
					<li>Entornos de desarrollo</li>
				</ul>
			</section>
			<section id="miweb">
				<h3>Mi web</h3>
				<p><b>STURMPROJEKT</b> es mi proyecto personal y profesional, nacido de mi interés por Linux, los servidores y el aprovechamiento de los recursos tecnológicos. Lo que comenzó como un laboratorio de experimentación con infraestructura auto hospedada ha evolucionado hacia un proyecto dedicado al desarrollo web, hosting, gestión de dominios, despliegue de aplicaciones y mantenimiento de servidores. En mi página puedes conocer los servicios que ofrezco, explorar mi infraestructura y descubrir algunos de los trabajos que he realizado.</p>
			</section>
			<section id="proyectos">
				<div>
					<h3>Mis proyectos</h3>
					<p>Me gusta desarrollar proyectos que me permitan aprender y solucionar problemas reales. Entre ellos destaca STURMPROJEKT, donde trabajo con infraestructura, alojamiento web y administración de sistemas. También experimento con servidores propios y comparto parte de mi aprendizaje y código en GitHub.</p>
				</div>
				<article>
					<h4>STURMPROJEKT</h4>
					<p>He desarrollado mi propia infraestructura de servidores Linux, utilizando Docker, Nginx Proxy Manager y Cloudflare para alojar y gestionar diferentes servicios. Este proyecto me permite experimentar con redes, seguridad y administración de sistemas.</p>
				</article>
				<article>
					<h4>SUMEX Gráfica - Desarrollo web</h4>
					<p>Uno de mis primeros trabajos para clientes fue el desarrollo y despliegue de la página web de SUMEX Gráfica. Me encargué de la infraestructura, configuración del dominio, DNS, certificados SSL y publicación de la web mediante Docker y Cloudflare.</p>
				</article>
				<article>
					<h4>Monitorización de servidores Linux</h4>
					<p>He trabajado en la monitorización de servidores Linux y contenedores Docker, utilizando herramientas de terminal como btop para supervisar el consumo de recursos, procesos y rendimiento de los sistemas.</p>
				</article>
				<article>
					<h4>Servidor Minecraft Bedrock</h4>
					<p>He desplegado un servidor dedicado de Minecraft Bedrock sobre Linux, trabajando con Docker, configuración de red y administración remota. Este proyecto me ha permitido practicar el alojamiento de servicios multijugador.</p>
				</article>
				<article>
					<h4>Servidor dedicado de Valheim</h4>
					<p>Otro de mis proyectos ha sido el despliegue de un servidor dedicado de Valheim en mi propia infraestructura. He trabajado con la configuración del entorno Linux, la gestión de recursos y la conectividad necesaria para alojar partidas multijugador.</p>
				</article>
			</section>
			<section id="contacto">
				<h3>Contacto</h3>
				<p>Si quieres ponerte en contacto conmigo para hablar sobre algún proyecto, proponer una colaboración o intercambiar conocimientos sobre tecnología, estaré encantado de escucharte. Puedes encontrarme a través de STURMPROJEKT o conectar conmigo mediante mis perfiles de GitHub, LinkedIn e Instagram. Siempre estoy abierto a nuevas ideas, oportunidades y proyectos que me permitan seguir aprendiendo y creciendo profesionalmente.</p>
				<form>
					<label><b>Introduce tu nombre</b></label>
					<input name="nombre">
					<label><b>Introduce tu correo</b></label>
					<input name="correo">
					<label><b>Introduce tu mensaje</b></label>
					<textarea name="mensaje"></textarea>
					<input type="submit">
				</form>
			</section>
		</main>
		<footer></footer>
	</body>
</html>
```
**12-footer.html**
```html
<!doctype html>
<html lang="es">
	<head>
		<title>Lucas Andrés Griego</title>
		<meta charset="utf-8">
		<style>
			/* Todo lo que pongamos aqui dentro será CSS */
			body{
				background:skyblue;
				font-family:Arial;
			}
			header,main,footer{
				background:cornflowerblue;
				width:1000px;
				margin:auto;
				padding:30px;
			}
			img{
				width:30%;
			}
			p{
				text-align:justify;
			}
			h1{
				font-size:35px;
			}
			h2{
				font-size:16px;
			}
			a{
				background:royalblue;
				color:white;
				text-decoration:none;
				padding:5px 10px;
				font-size:11px;
			}
			/* FLEX para el form */
			form{
				display:flex;
				flex-direction:column;
				gap:10px;
			}
			/* GRID para proyectos */
			#proyectos{
				display:grid;
				grid-template-columns:repeat(3,1fr);
				margin:auto;
				justify-content: center;
				gap: 20px;
			}
		</style>
	</head>
	<body>
	<!-- Esto es un comentario -->
		<header>
			<h1>Lucas Andrés Griego</h1>
			<h2>Propietario de Sturmprojekt</h2>
			<nav>
				<a href="#sobremi">Sobre mi</a>
				<a href="#miweb">Mi web</a>
				<a href="#formacion">Formación</a>
				<a href="#proyectos">Mis proyectos</a>
				<a href="#contacto">Contacto</a>
			</nav>
		</header>
		<main>
			<section id="sobremi">
				<h3>Sobre mi</h3>
				<img src="fotocarnet.jpg" alt="Foto de Lucas Andrés Griego">
				<p>Soy <b>Lucas Andrés Griego,</b> estudiante de Desarrollo de Aplicaciones Multiplataforma <b>(DAM)</b> y creador de STURMPROJEKT. Me apasionan la informática, la programación y la administración de sistemas Linux. Disfruto aprendiendo mediante la práctica, experimentando con servidores, contenedores Docker, desarrollo web y nuevas tecnologías. Compagino mis estudios con proyectos personales y trabajos para clientes, buscando mejorar mis conocimientos y adquirir experiencia real en el sector tecnológico.</p>
			</section>
			<section id="formacion">
				<h3>Mi formación</h3>
				<p>Actualmente estudio Desarrollo de Aplicaciones Multiplataforma (DAM), donde estoy ampliando mis conocimientos informáticos. Durante mi formación estudio materias como:</p>
				<!-- Aqui van las listas <ul> (lista desordenada, es decir, con viñetas.) y <li> (representa cada elemento de la lista.) -->
				<ul>
					<li>Programación</li>
					<li>Bases de datos</li>
					<li>Entornos de desarrollo</li>
				</ul>
			</section>
			<section id="miweb">
				<h3>Mi web</h3>
				<p><b>STURMPROJEKT</b> es mi proyecto personal y profesional, nacido de mi interés por Linux, los servidores y el aprovechamiento de los recursos tecnológicos. Lo que comenzó como un laboratorio de experimentación con infraestructura auto hospedada ha evolucionado hacia un proyecto dedicado al desarrollo web, hosting, gestión de dominios, despliegue de aplicaciones y mantenimiento de servidores. En mi página puedes conocer los servicios que ofrezco, explorar mi infraestructura y descubrir algunos de los trabajos que he realizado.</p>
			</section>
			<section id="proyectos">
				<div>
					<h3>Mis proyectos</h3>
					<p>Me gusta desarrollar proyectos que me permitan aprender y solucionar problemas reales. Entre ellos destaca STURMPROJEKT, donde trabajo con infraestructura, alojamiento web y administración de sistemas. También experimento con servidores propios y comparto parte de mi aprendizaje y código en GitHub.</p>
				</div>
				<article>
					<h4>STURMPROJEKT</h4>
					<p>He desarrollado mi propia infraestructura de servidores Linux, utilizando Docker, Nginx Proxy Manager y Cloudflare para alojar y gestionar diferentes servicios. Este proyecto me permite experimentar con redes, seguridad y administración de sistemas.</p>
				</article>
				<article>
					<h4>SUMEX Gráfica - Desarrollo web</h4>
					<p>Uno de mis primeros trabajos para clientes fue el desarrollo y despliegue de la página web de SUMEX Gráfica. Me encargué de la infraestructura, configuración del dominio, DNS, certificados SSL y publicación de la web mediante Docker y Cloudflare.</p>
				</article>
				<article>
					<h4>Monitorización de servidores Linux</h4>
					<p>He trabajado en la monitorización de servidores Linux y contenedores Docker, utilizando herramientas de terminal como btop para supervisar el consumo de recursos, procesos y rendimiento de los sistemas.</p>
				</article>
				<article>
					<h4>Servidor Minecraft Bedrock</h4>
					<p>He desplegado un servidor dedicado de Minecraft Bedrock sobre Linux, trabajando con Docker, configuración de red y administración remota. Este proyecto me ha permitido practicar el alojamiento de servicios multijugador.</p>
				</article>
				<article>
					<h4>Servidor dedicado de Valheim</h4>
					<p>Otro de mis proyectos ha sido el despliegue de un servidor dedicado de Valheim en mi propia infraestructura. He trabajado con la configuración del entorno Linux, la gestión de recursos y la conectividad necesaria para alojar partidas multijugador.</p>
				</article>
			</section>
			<section id="contacto">
				<h3>Contacto</h3>
				<p>Si quieres ponerte en contacto conmigo para hablar sobre algún proyecto, proponer una colaboración o intercambiar conocimientos sobre tecnología, estaré encantado de escucharte. Puedes encontrarme a través de STURMPROJEKT o conectar conmigo mediante mis perfiles de GitHub, LinkedIn e Instagram. Siempre estoy abierto a nuevas ideas, oportunidades y proyectos que me permitan seguir aprendiendo y creciendo profesionalmente.</p>
				<form>
					<label><b>Introduce tu nombre</b></label>
					<input name="nombre">
					<label><b>Introduce tu correo</b></label>
					<input name="correo">
					<label><b>Introduce tu mensaje</b></label>
					<textarea name="mensaje"></textarea>
					<input type="submit">
				</form>
			</section>
		</main>
		<footer>
			<p><b>(c) Sturmprojekt</b></p>
		</footer>
	</body>
</html>
```
**13-Ajusto fuente.html**
```html
<!doctype html>
<html lang="es">
	<head>
		<title>Lucas Andrés Griego</title>
		<meta charset="utf-8">
		<style>
			/* Todo lo que pongamos aqui dentro será CSS */
			body{
				background:skyblue;
				font-family:Arial;
			}
			header,main,footer{
				background:cornflowerblue;
				width:1000px;
				margin:auto;
				padding:30px;
			}
			img{
				width:30%;
			}
			p{
				text-align:justify;
				font-size:16px;
			}
			h1{
				font-size:35px;
			}
			h2{
				font-size:16px;
			}
			h1,h2,h3,h4,h5,h6{
			color:darkblue;
			}
			a{
				background:royalblue;
				color:white;
				text-decoration:none;
				padding:5px 10px;
				font-size:11px;
			}
			/* FLEX para el form */
			form{
				display:flex;
				flex-direction:column;
				gap:10px;
			}
			/* GRID para proyectos */
			#proyectos{
				display:grid;
				grid-template-columns:repeat(3,1fr);
				margin:auto;
				justify-content: center;
				gap: 20px;
			}
		</style>
	</head>
	<body>
	<!-- Esto es un comentario -->
		<header>
			<h1>Lucas Andrés Griego</h1>
			<h2>Propietario de Sturmprojekt</h2>
			<nav>
				<a href="#sobremi">Sobre mi</a>
				<a href="#miweb">Mi web</a>
				<a href="#formacion">Formación</a>
				<a href="#proyectos">Mis proyectos</a>
				<a href="#contacto">Contacto</a>
			</nav>
		</header>
		<main>
			<section id="sobremi">
				<h3>Sobre mi</h3>
				<img src="fotocarnet.jpg" alt="Foto de Lucas Andrés Griego">
				<p>Soy <b>Lucas Andrés Griego,</b> estudiante de Desarrollo de Aplicaciones Multiplataforma <b>(DAM)</b> y creador de STURMPROJEKT. Me apasionan la informática, la programación y la administración de sistemas Linux. Disfruto aprendiendo mediante la práctica, experimentando con servidores, contenedores Docker, desarrollo web y nuevas tecnologías. Compagino mis estudios con proyectos personales y trabajos para clientes, buscando mejorar mis conocimientos y adquirir experiencia real en el sector tecnológico.</p>
			</section>
			<section id="formacion">
				<h3>Mi formación</h3>
				<p>Actualmente estudio Desarrollo de Aplicaciones Multiplataforma (DAM), donde estoy ampliando mis conocimientos informáticos. Durante mi formación estudio materias como:</p>
				<!-- Aqui van las listas <ul> (lista desordenada, es decir, con viñetas.) y <li> (representa cada elemento de la lista.) -->
				<ul>
					<li>Programación</li>
					<li>Bases de datos</li>
					<li>Entornos de desarrollo</li>
				</ul>
			</section>
			<section id="miweb">
				<h3>Mi web</h3>
				<p><b>STURMPROJEKT</b> es mi proyecto personal y profesional, nacido de mi interés por Linux, los servidores y el aprovechamiento de los recursos tecnológicos. Lo que comenzó como un laboratorio de experimentación con infraestructura auto hospedada ha evolucionado hacia un proyecto dedicado al desarrollo web, hosting, gestión de dominios, despliegue de aplicaciones y mantenimiento de servidores. En mi página puedes conocer los servicios que ofrezco, explorar mi infraestructura y descubrir algunos de los trabajos que he realizado.</p>
			</section>
			<section id="proyectos">
				<div>
					<h3>Mis proyectos</h3>
					<p>Me gusta desarrollar proyectos que me permitan aprender y solucionar problemas reales. Entre ellos destaca STURMPROJEKT, donde trabajo con infraestructura, alojamiento web y administración de sistemas. También experimento con servidores propios y comparto parte de mi aprendizaje y código en GitHub.</p>
				</div>
				<article>
					<h4>STURMPROJEKT</h4>
					<p>He desarrollado mi propia infraestructura de servidores Linux, utilizando Docker, Nginx Proxy Manager y Cloudflare para alojar y gestionar diferentes servicios. Este proyecto me permite experimentar con redes, seguridad y administración de sistemas.</p>
				</article>
				<article>
					<h4>SUMEX Gráfica - Desarrollo web</h4>
					<p>Uno de mis primeros trabajos para clientes fue el desarrollo y despliegue de la página web de SUMEX Gráfica. Me encargué de la infraestructura, configuración del dominio, DNS, certificados SSL y publicación de la web mediante Docker y Cloudflare.</p>
				</article>
				<article>
					<h4>Monitorización de servidores Linux</h4>
					<p>He trabajado en la monitorización de servidores Linux y contenedores Docker, utilizando herramientas de terminal como btop para supervisar el consumo de recursos, procesos y rendimiento de los sistemas.</p>
				</article>
				<article>
					<h4>Servidor Minecraft Bedrock</h4>
					<p>He desplegado un servidor dedicado de Minecraft Bedrock sobre Linux, trabajando con Docker, configuración de red y administración remota. Este proyecto me ha permitido practicar el alojamiento de servicios multijugador.</p>
				</article>
				<article>
					<h4>Servidor dedicado de Valheim</h4>
					<p>Otro de mis proyectos ha sido el despliegue de un servidor dedicado de Valheim en mi propia infraestructura. He trabajado con la configuración del entorno Linux, la gestión de recursos y la conectividad necesaria para alojar partidas multijugador.</p>
				</article>
			</section>
			<section id="contacto">
				<h3>Contacto</h3>
				<p>Si quieres ponerte en contacto conmigo para hablar sobre algún proyecto, proponer una colaboración o intercambiar conocimientos sobre tecnología, estaré encantado de escucharte. Puedes encontrarme a través de STURMPROJEKT o conectar conmigo mediante mis perfiles de GitHub, LinkedIn e Instagram. Siempre estoy abierto a nuevas ideas, oportunidades y proyectos que me permitan seguir aprendiendo y creciendo profesionalmente.</p>
				<form>
					<label><b>Introduce tu nombre</b></label>
					<input name="nombre">
					<label><b>Introduce tu correo</b></label>
					<input name="correo">
					<label><b>Introduce tu mensaje</b></label>
					<textarea name="mensaje"></textarea>
					<input type="submit">
				</form>
			</section>
		</main>
		<footer>
			<p><b>(c) Sturmprojekt</b></p>
		</footer>
	</body>
</html>
```
**style.css**
```css
/* Estilos generales */

body {
    background: skyblue;
}

header, main, footer {
    background: cornflowerblue;
    width: 800px;
}

img {
    width: 50%;
}
```
### 06-Validación de documentos HTML y CSS
**01-Archivo validado.html**
```html
<!doctype html>
<html lang="es">
	<head>
		<title>Lucas Andrés Griego</title>
		<meta charset="utf-8">
		<link rel="stylesheet" href="style.css">
	</head>
	<body>
	<!-- Esto es un comentario -->
		<header>
			<h1>Lucas Andrés Griego</h1>
			<h2>Propietario de Sturmprojekt</h2>
			<nav>
				<a href="#sobremi">Sobre mi</a>
				<a href="#miweb">Mi web</a>
				<a href="#formacion">Formación</a>
				<a href="#proyectos">Mis proyectos</a>
				<a href="#contacto">Contacto</a>
			</nav>
		</header>
		<main>
			<section id="sobremi">
				<h3>Sobre mi</h3>
				<img src="fotocarnet.jpg" alt="Foto de Lucas Andrés Griego">
				<p>Soy <b>Lucas Andrés Griego,</b> estudiante de Desarrollo de Aplicaciones Multiplataforma <b>(DAM)</b> y creador de STURMPROJEKT. Me apasionan la informática, la programación y la administración de sistemas Linux. Disfruto aprendiendo mediante la práctica, experimentando con servidores, contenedores Docker, desarrollo web y nuevas tecnologías. Compagino mis estudios con proyectos personales y trabajos para clientes, buscando mejorar mis conocimientos y adquirir experiencia real en el sector tecnológico.</p>
			</section>
			<section id="formacion">
				<h3>Mi formación</h3>
				<p>Actualmente estudio Desarrollo de Aplicaciones Multiplataforma (DAM), donde estoy ampliando mis conocimientos informáticos. Durante mi formación estudio materias como:</p>
				<!-- Aqui van las listas <ul> (lista desordenada, es decir, con viñetas.) y <li> (representa cada elemento de la lista.) -->
				<ul>
					<li>Programación</li>
					<li>Bases de datos</li>
					<li>Entornos de desarrollo</li>
				</ul>
			</section>
			<section id="miweb">
				<h3>Mi web</h3>
				<p><b>STURMPROJEKT</b> es mi proyecto personal y profesional, nacido de mi interés por Linux, los servidores y el aprovechamiento de los recursos tecnológicos. Lo que comenzó como un laboratorio de experimentación con infraestructura auto hospedada ha evolucionado hacia un proyecto dedicado al desarrollo web, hosting, gestión de dominios, despliegue de aplicaciones y mantenimiento de servidores. En mi página puedes conocer los servicios que ofrezco, explorar mi infraestructura y descubrir algunos de los trabajos que he realizado.</p>
			</section>
			<section id="proyectos">
				<div>
					<h3>Mis proyectos</h3>
					<p>Me gusta desarrollar proyectos que me permitan aprender y solucionar problemas reales. Entre ellos destaca STURMPROJEKT, donde trabajo con infraestructura, alojamiento web y administración de sistemas. También experimento con servidores propios y comparto parte de mi aprendizaje y código en GitHub.</p>
				</div>
				<article>
					<h4>STURMPROJEKT</h4>
					<p>He desarrollado mi propia infraestructura de servidores Linux, utilizando Docker, Nginx Proxy Manager y Cloudflare para alojar y gestionar diferentes servicios. Este proyecto me permite experimentar con redes, seguridad y administración de sistemas.</p>
				</article>
				<article>
					<h4>SUMEX Gráfica - Desarrollo web</h4>
					<p>Uno de mis primeros trabajos para clientes fue el desarrollo y despliegue de la página web de SUMEX Gráfica. Me encargué de la infraestructura, configuración del dominio, DNS, certificados SSL y publicación de la web mediante Docker y Cloudflare.</p>
				</article>
				<article>
					<h4>Monitorización de servidores Linux</h4>
					<p>He trabajado en la monitorización de servidores Linux y contenedores Docker, utilizando herramientas de terminal como btop para supervisar el consumo de recursos, procesos y rendimiento de los sistemas.</p>
				</article>
				<article>
					<h4>Servidor Minecraft Bedrock</h4>
					<p>He desplegado un servidor dedicado de Minecraft Bedrock sobre Linux, trabajando con Docker, configuración de red y administración remota. Este proyecto me ha permitido practicar el alojamiento de servicios multijugador.</p>
				</article>
				<article>
					<h4>Servidor dedicado de Valheim</h4>
					<p>Otro de mis proyectos ha sido el despliegue de un servidor dedicado de Valheim en mi propia infraestructura. He trabajado con la configuración del entorno Linux, la gestión de recursos y la conectividad necesaria para alojar partidas multijugador.</p>
				</article>
			</section>
			<section id="contacto">
				<h3>Contacto</h3>
				<p>Si quieres ponerte en contacto conmigo para hablar sobre algún proyecto, proponer una colaboración o intercambiar conocimientos sobre tecnología, estaré encantado de escucharte. Puedes encontrarme a través de STURMPROJEKT o conectar conmigo mediante mis perfiles de GitHub, LinkedIn e Instagram. Siempre estoy abierto a nuevas ideas, oportunidades y proyectos que me permitan seguir aprendiendo y creciendo profesionalmente.</p>
				<form>
					<label><b>Introduce tu nombre</b></label>
					<input name="nombre">
					<label><b>Introduce tu correo</b></label>
					<input name="correo">
					<label><b>Introduce tu mensaje</b></label>
					<textarea name="mensaje"></textarea>
					<input type="submit">
				</form>
			</section>
		</main>
		<footer>
			<p><b>(c) Sturmprojekt</b></p>
		</footer>
	</body>
</html>
```
**style.css**
```css
/* Estilos generales */

			body{
				background:skyblue;
				font-family:Arial;
			}
			header,main,footer{
				background:cornflowerblue;
				width:1000px;
				margin:auto;
				padding:30px;
			}
			img{
				width:30%;
			}
			p{
				text-align:justify;
				font-size:16px;
			}
			h1{
				font-size:35px;
			}
			h2{
				font-size:16px;
			}
			h1,h2,h3,h4,h5,h6{
			color:darkblue;
			}
			a{
				background:royalblue;
				color:white;
				text-decoration:none;
				padding:5px 10px;
				font-size:11px;
			}
			/* FLEX para el form */
			form{
				display:flex;
				flex-direction:column;
				gap:10px;
			}
			/* GRID para proyectos */
			#proyectos{
				display:grid;
				grid-template-columns:repeat(3,1fr);
				margin:auto;
				justify-content: center;
				gap: 20px;
			}
```
## 02-Proyecto
**01-Archivo validado.html**
```html
<!doctype html>
<html lang="es">
	<head>
		<title>Lucas Andrés Griego</title>
		<meta charset="utf-8">
		<link rel="stylesheet" href="style.css">
	</head>
	<body>
	<!-- Esto es un comentario -->
		<header>
			<h1>Lucas Andrés Griego</h1>
			<h2>Propietario de Sturmprojekt</h2>
			<nav>
				<a href="#sobremi">Sobre mi</a>
				<a href="#miweb">Mi web</a>
				<a href="#formacion">Formación</a>
				<a href="#proyectos">Mis proyectos</a>
				<a href="#contacto">Contacto</a>
			</nav>
		</header>
		<main>
			<section id="sobremi">
				<h3>Sobre mi</h3>
				<img src="fotocarnet.jpg" alt="Foto de Lucas Andrés Griego">
				<p>Soy <b>Lucas Andrés Griego,</b> estudiante de Desarrollo de Aplicaciones Multiplataforma <b>(DAM)</b> y creador de STURMPROJEKT. Me apasionan la informática, la programación y la administración de sistemas Linux. Disfruto aprendiendo mediante la práctica, experimentando con servidores, contenedores Docker, desarrollo web y nuevas tecnologías. Compagino mis estudios con proyectos personales y trabajos para clientes, buscando mejorar mis conocimientos y adquirir experiencia real en el sector tecnológico.</p>
			</section>
			<section id="formacion">
				<h3>Mi formación</h3>
				<p>Actualmente estudio Desarrollo de Aplicaciones Multiplataforma (DAM), donde estoy ampliando mis conocimientos informáticos. Durante mi formación estudio materias como:</p>
				<!-- Aqui van las listas <ul> (lista desordenada, es decir, con viñetas.) y <li> (representa cada elemento de la lista.) -->
				<ul>
					<li>Programación</li>
					<li>Bases de datos</li>
					<li>Entornos de desarrollo</li>
				</ul>
			</section>
			<section id="miweb">
				<h3>Mi web</h3>
				<p><b>STURMPROJEKT</b> es mi proyecto personal y profesional, nacido de mi interés por Linux, los servidores y el aprovechamiento de los recursos tecnológicos. Lo que comenzó como un laboratorio de experimentación con infraestructura auto hospedada ha evolucionado hacia un proyecto dedicado al desarrollo web, hosting, gestión de dominios, despliegue de aplicaciones y mantenimiento de servidores. En mi página puedes conocer los servicios que ofrezco, explorar mi infraestructura y descubrir algunos de los trabajos que he realizado.</p>
			</section>
			<section id="proyectos">
				<div>
					<h3>Mis proyectos</h3>
					<p>Me gusta desarrollar proyectos que me permitan aprender y solucionar problemas reales. Entre ellos destaca STURMPROJEKT, donde trabajo con infraestructura, alojamiento web y administración de sistemas. También experimento con servidores propios y comparto parte de mi aprendizaje y código en GitHub.</p>
				</div>
				<article>
					<h4>STURMPROJEKT</h4>
					<p>He desarrollado mi propia infraestructura de servidores Linux, utilizando Docker, Nginx Proxy Manager y Cloudflare para alojar y gestionar diferentes servicios. Este proyecto me permite experimentar con redes, seguridad y administración de sistemas.</p>
				</article>
				<article>
					<h4>SUMEX Gráfica - Desarrollo web</h4>
					<p>Uno de mis primeros trabajos para clientes fue el desarrollo y despliegue de la página web de SUMEX Gráfica. Me encargué de la infraestructura, configuración del dominio, DNS, certificados SSL y publicación de la web mediante Docker y Cloudflare.</p>
				</article>
				<article>
					<h4>Monitorización de servidores Linux</h4>
					<p>He trabajado en la monitorización de servidores Linux y contenedores Docker, utilizando herramientas de terminal como btop para supervisar el consumo de recursos, procesos y rendimiento de los sistemas.</p>
				</article>
				<article>
					<h4>Servidor Minecraft Bedrock</h4>
					<p>He desplegado un servidor dedicado de Minecraft Bedrock sobre Linux, trabajando con Docker, configuración de red y administración remota. Este proyecto me ha permitido practicar el alojamiento de servicios multijugador.</p>
				</article>
				<article>
					<h4>Servidor dedicado de Valheim</h4>
					<p>Otro de mis proyectos ha sido el despliegue de un servidor dedicado de Valheim en mi propia infraestructura. He trabajado con la configuración del entorno Linux, la gestión de recursos y la conectividad necesaria para alojar partidas multijugador.</p>
				</article>
			</section>
			<section id="contacto">
				<h3>Contacto</h3>
				<p>Si quieres ponerte en contacto conmigo para hablar sobre algún proyecto, proponer una colaboración o intercambiar conocimientos sobre tecnología, estaré encantado de escucharte. Puedes encontrarme a través de STURMPROJEKT o conectar conmigo mediante mis perfiles de GitHub, LinkedIn e Instagram. Siempre estoy abierto a nuevas ideas, oportunidades y proyectos que me permitan seguir aprendiendo y creciendo profesionalmente.</p>
				<form>
					<label><b>Introduce tu nombre</b></label>
					<input name="nombre">
					<label><b>Introduce tu correo</b></label>
					<input name="correo">
					<label><b>Introduce tu mensaje</b></label>
					<textarea name="mensaje"></textarea>
					<input type="submit">
				</form>
			</section>
		</main>
		<footer>
			<p><b>(c) Sturmprojekt</b></p>
		</footer>
	</body>
</html>
```
**style.css**
```css
/* Estilos generales */

			body{
				background:skyblue;
				font-family:Arial;
			}
			header,main,footer{
				background:cornflowerblue;
				width:1000px;
				margin:auto;
				padding:30px;
			}
			img{
				width:30%;
			}
			p{
				text-align:justify;
				font-size:16px;
			}
			h1{
				font-size:35px;
			}
			h2{
				font-size:16px;
			}
			h1,h2,h3,h4,h5,h6{
			color:darkblue;
			}
			a{
				background:royalblue;
				color:white;
				text-decoration:none;
				padding:5px 10px;
				font-size:11px;
			}
			/* FLEX para el form */
			form{
				display:flex;
				flex-direction:column;
				gap:10px;
			}
			/* GRID para proyectos */
			#proyectos{
				display:grid;
				grid-template-columns:repeat(3,1fr);
				margin:auto;
				justify-content: center;
				gap: 20px;
			}
```
## 3-Resultado aprendizaje
**RA2.md**
```markdown
# Resultado de aprendizaje 2
**Resultado de aprendizaje**
Utiliza lenguajes de marcas para la transmisión y presentación de información a través de la web analizando la estructura de los documentos e identificando sus elementos.

Criterios de evaluación
a) Se han identificado y clasificado los lenguajes de marcas relacionados con la web y sus diferentes versiones y estándares.
En clases identicamos lenguajes de marcas como HTML5, CSS3, XML, etc.
Tabien utilizamos un validador para depurar los documentos.

b) Se ha analizado la estructura de un documento HTML e identificado las secciones que lo componen.
Efectivamente armamos el esqueleto de una pagina web, donde identificamos las etiquetas basicas como:
* head
* body
* main
* section
* article
* form
* footer

c) Se ha reconocido la funcionalidad de las principales etiquetas y los atributos del lenguaje HTML.
*Las etiquetas a y sus funciones:*
<head>: contiene información del documento, como el título, metadatos y enlaces a estilos. No es el contenido visible de la página.
<body>: contiene el contenido de la página que muestra el navegador.
<main>: identifica el contenido principal de la página.
<section>: agrupa contenido sobre un mismo tema, normalmente con un encabezado.
<article>: representa contenido independiente, como una noticia, publicación o reseña.
<form>: agrupa campos y controles para introducir y enviar datos.
<footer>: representa el pie de una página o de una sección, con información como autoría, enlaces o derechos de autor.

d) Se han establecido las semejanzas y diferencias entre las diferentes versiones de HTML.
Las versiones de HTML comparten las mismas semejanzas: estructurar el contenido de una página web mediante etiquetas, como títulos, párrafos, 
enlaces, imágenes y formularios. Se diferencian en las funciones disponibles y en las reglas para escribirlas.
Comparación:
			HTML 1.0	Muy básico: títulos, párrafos, listas y enlaces.
			HTML 2.0	Estandarizó las funciones iniciales e incorporó formularios.
			HTML 3.2	Añadió tablas y más posibilidades de presentación, como etiquetas para cambiar fuentes.
			HTML 4.01	Mejoró formularios y accesibilidad. Impulsó separar el contenido HTML del diseño mediante CSS.
			XHTML 1.0	Reformuló HTML 4 siguiendo reglas de XML: etiquetas en minúsculas, atributos entre comillas y elementos correctamente cerrados.
			HTML5		Incorporó etiquetas semánticas como <main>, <section> y <article>, además de audio, vídeo y nuevos controles de formulario.

e) Se han utilizado herramientas en la creación de documentos web.
En mi caso utilice como "herramientas" notepad ++, con este editor desarrolle los documentos, con tecnologías HTML5, Y CSS3.
Utilice el navegador Ecosia para visualizar los documentos, y el validador de w3 https://validator.w3.org/#validate_by_input. 

f) Se han identificado las ventajas que aporta la utilización de hojas de estilo.
Las hojas de estilo CSS aportan estas ventajas:
- Separan contenido y diseño: HTML estructura la información y CSS define su apariencia.
- Mantienen un diseño uniforme: varias páginas pueden compartir los mismos estilos.
- Facilitan el mantenimiento: modificar una hoja de estilos actualiza todas las páginas que la utilizan.
- Permiten diseños adaptables: ajustan la presentación a móviles, tabletas y ordenadores. 

g) Se han aplicado hojas de estilo.
Aplique estilo dentro del archivo html, y luego aplique estilo externo con el archivo "style.css" 
Conectado al html mediante la linea: <link rel="stylesheet" href="style.css">

h) Se han validado documentos HTML y CSS.
Como dije anteriormente, con el validador de w3, https://validator.w3.org/#validate_by_input, se valido el .html y el .css

i) Se han identificado las tecnologías en que se basa la sindicación de contenidos.
La sindicación de contenidos permite recibir las novedades de varias páginas web en un mismo lugar, sin entrar en cada una.
Por ejemplo: sigues tres blogs de tecnología. En vez de visitarlos para comprobar si publicaron algo, 
utilizas un lector de noticias que reúne sus nuevas publicaciones.
Cada blog ofrece un canal RSS.. de hecho me estoy planteando aplicar esto a mi pagina web.

j) Se han reconocido los ámbitos de aplicación de la sindicación de contenidos.
La sindicación de contenidos se utiliza en distintos ámbitos:
- Noticias: recibir titulares y novedades de varios periódicos.
- Blogs: seguir nuevas publicaciones sin visitar cada página.
- Pódcast: distribuir episodios nuevos a las aplicaciones de escucha mediante RSS.
- Educación: recibir recursos, actividades y avisos de cursos.
- Investigación: seguir artículos científicos y publicaciones de revistas.
- Empresas y comercios: difundir novedades, productos y ofertas.
- Empleo: recibir nuevas ofertas que coincidan con determinados intereses.
```
