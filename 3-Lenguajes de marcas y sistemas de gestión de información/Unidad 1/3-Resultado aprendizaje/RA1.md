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