# Reporte de proyecto

## Información de generación

- **Fecha:** 2026-10-20 15:46:35 +0200
- **Usuario:** lucas
- **Equipo:** LUCAS
- **Sistema operativo:** Windows
- **Arquitectura:** x86_64
- **Directorio de ejecución:** `D:/Herramientas/portables/jocarsa-generador-windows-x64`
- **Proyecto documentado:** `D:/Resultados Aprendizaje_DAM1/2-Entornos de desarrollo/Unidad 1`
- **HMAC-SHA-256 de autenticidad:** `277fc3ceb8d23b303c34ad46fd1d6fb0b3c5722d0783d5fc7b31471539c7c4e5`

> El HMAC-SHA-256 se calcula sobre el documento completo usando un secreto incluido en el programa y 64 ceros en el propio campo del HMAC. El secreto no se escribe en el informe. Este mecanismo permite comprobar integridad y que el documento fue generado con el mismo secreto.

## Estructura del proyecto

```
D:/Resultados Aprendizaje_DAM1/2-Entornos de desarrollo/Unidad 1
├── 01-Ejercicios
│   ├── 01-Concepto de programa informático
│   │   └── 01-Concepto e historia.md
│   ├── 03-Tipos de lenguajes de programación. Paradigmas
│   │   ├── 01-Clasificacion de los lengujes.md
│   │   ├── 02-Lenguajes de programación.md
│   │   └── 03-guerra de los navegadores.md
│   ├── 04-Características de los lenguajes más difundidos
│   │   ├── 01-lenguajes más difundidos.md
│   │   ├── 02-segmentación.md
│   │   └── 03-Mi historia.md
│   ├── 05-Fases del desarrollo de una aplicación análisis, diseño, codificación, pruebas, documentación, explotación y mantenimiento, entre otras
│   │   └── 01-Fases.md
│   └── 06-Proceso de obtención de código ejecutable a partir del código fuente; herramientas implicadas
│       ├── 01-lenguaje interpretado.py
│       ├── 02-hola mundo.c
│       ├── 03-como compilar.md
│       ├── 04-comando de compilacion.md
│       ├── 05-variables.c
│       ├── 06-flotante.c
│       ├── 07-char.c
│       ├── 08-strings.c
│       ├── 09-array de caracteres.c
│       ├── 10-operadores.c
│       ├── 11-comparadores.c
│       ├── 12-operadores booleanos.c
│       ├── 13-estructuras de seleccion.c
│       ├── 14-else.c
│       ├── 15-else if.c
│       ├── 16-repeticion.c
│       ├── 17-scanf.c
│       ├── 18-calculadora de iva.c
│       ├── 19-comentarios.c
│       ├── 20-ia.c
│       ├── char.exe
│       ├── flotante.exe
│       ├── hola.exe
│       └── variable.exe
├── 02-Proyecto
│   ├── 01-ingresos-web.c
│   ├── 01-ingresos-web.exe
│   ├── 02-entrada-webs.c
│   ├── 02-entrada-webs.exe
│   ├── 03-hosting.c
│   ├── 03-hosting.exe
│   ├── 04-dominios.c
│   ├── 04-dominios.exe
│   ├── 05-gastos.c
│   └── 05-gastos.exe
└── 03-Resultado de aprendizaje
    └── RA1.MD
```

## Bases de datos SQLite

Esta sección documenta únicamente el esquema de las bases SQLite detectadas. No se vuelcan registros ni datos de usuario.

No se han encontrado bases SQLite con extensiones .db, .sqlite o .sqlite3.

## Código (intercalado)

# Unidad 1
## 01-Ejercicios
### 01-Concepto de programa informático
**01-Concepto e historia.md**
```markdown
Los computadores se basan en procesadores que mueven información 
Un procesador es una calculadora programable

Quiere decir esto que no realiza una tarea única, sino que puede realizar multitud de tareas

Una secuencia de instrucciones (a día de hoy, palabras escritas en un documento digital), 
que se convertirán en operaciones físicas del procesador
```
### 03-Tipos de lenguajes de programación. Paradigmas
**01-Clasificacion de los lengujes.md**
```markdown
Según el paradigma (imperativos, funcionales, orientados a objetos)

Según el nivel (bajo nivel,asm, c, nivel intermedio, java Csharp, alto nivel, python, js)

Horizontales (transversales), verticales (especializados)

Ámbito generales (python), específicos (PHP)

| Criterio                       | Categoría                    | Ejemplos                                       |
| ------------------------------ | ---------------------------- | ---------------------------------------------- |
| **Según paradigma**            | Imperativos / procedurales   | C, Pascal, BASIC, Fortran                      |
|                                | Orientados a objetos         | Java, C#, C++, Kotlin, Swift                   |
|                                | Funcionales                  | Haskell, Lisp, Clojure, F#, Erlang, Elixir     |
|                                | Multiparadigma               | Python, JavaScript, C++, Rust, Scala           |
| **Según nivel de abstracción** | Bajo nivel                   | Ensamblador (ASM), código máquina              |
|                                | Intermedio                   | C, C++, Rust                                   |
|                                | Alto nivel                   | Java, C#, Python, JavaScript, PHP, Ruby        |
| **Según transversalidad**      | Horizontales / transversales | C, C++, Java, C#, Python, JavaScript           |
|                                | Verticales / especializados  | R, MATLAB, SQL, Solidity, Verilog, VHDL        |
| **Según ámbito de aplicación** | Propósito general            | C, C++, Java, C#, Python, JavaScript, Go, Rust |
|                                | Propósito específico         | PHP, SQL, R, MATLAB, Solidity, Bash, Verilog   |
```
**02-Lenguajes de programación.md**
```markdown
Código máquina (ceros y  unos)
Es el lenguaje nativo de cada procesador
No es nada cómodo que un ser humano programe en lenguaje máquina

Ensamblador - assembly - asm
Conjunto de instrucciones mnemónicas para realizar operaciones con el procesador
Muy bajo nivel
Se usa para tener mucho control
Muy específico de sectores como la electrónica o robótica

C - 1969-1872
Bajo nivel 
Imperativo, fácil de aprender
Pensado para que "cualquier" persona pueda programar

C++ 1984
Bjarne Strrfsafsadfsd
Toma el lenguaje C y lo aumenta con programación orientada a objetos

Python 1991
Lenguaje de muy alta nivel, muy abstraido, muy fácil
Pensado para que todo el mundo pueda programar

Java
Lenguaje estrictamente orientado a objetos
Pensado directamente para crear software empresarial

Csharp 1998 - Microsoft tiene envidia de Java
Y Crea su propio Java llamado C#

JavaScript creado en 1995
Para apoyar la web (web dinámica)
Hoy en día juega un rol imprescindible en internet








```
**03-guerra de los navegadores.md**
```markdown
1991 Se crea la WWW


1995 Microsoft lanza windwos 95 con capacidades multimedia
	Pentium MMX
	
1995 
```
### 04-Características de los lenguajes más difundidos
**01-lenguajes más difundidos.md**
```markdown
https://www.tiobe.com/tiobe-index/

Python - Lenguaje crecimiento
C - Muy viejo, muy confiable, muy solido, alto rendimiento, duro
C++ - Hermano mayor de C - C con clases
Java - Fantástico, en declive
C# - Como Java pero de Microsoft
Javascript - Nicho web, dominante web
Visual Basic - lenguaje a extinguir de Microsoft
SQL - Lenguaje para bases de datos
R - Lenguaje para estadística - Python le está comiendo
Rust - Se está poniendo de moda, más seguro que C
Fortran Formula Translator - 1956


```
**02-segmentación.md**
```markdown
| Lenguaje       | Propósito general |     Web | Escritorio | IA / ML |   Datos |   Móvil | Sistemas / embebido | Videojuegos |
| -------------- | ----------------: | ------: | ---------: | ------: | ------: | ------: | ------------------: | ----------: |
| **Python**     |           **28%** |      9% |         6% | **62%** | **45%** |      1% |                  2% |          3% |
| **JavaScript** |                9% | **30%** |         8% |      5% |      3% |      8% |                  1% |          5% |
| **TypeScript** |               12% | **34%** |        10% |      7% |      2% |     10% |                  1% |          4% |
| **Java**       |           **16%** |      9% |         7% |      3% |      7% |      9% |                  3% |          4% |
| **C#**         |               12% |      6% |    **25%** |      2% |      4% |      4% |                  3% |     **31%** |
| **C++**        |                8% |      1% |    **20%** |     10% |      2% |      2% |             **30%** |     **35%** |
| **C**          |                5% |       — |         4% |      2% |      1% |       — |             **43%** |          6% |
| **PHP**        |                3% |      8% |          — |       — |       — |       — |                   — |           — |
| **Go**         |                4% |      3% |         3% |      2% |      2% |       — |                  8% |          1% |
| **Rust**       |                3% |     <1% |         3% |      3% |      1% |      1% |                  9% |          4% |
| **Kotlin**     |                 — |       — |         3% |       — |       — | **31%** |                   — |          1% |
| **Swift**      |                 — |       — |         5% |       — |       — | **28%** |                   — |          1% |
| **Dart**       |                 — |       — |         3% |       — |       — |  **7%** |                   — |          1% |
| **R**          |                 — |       — |          — |      3% | **24%** |       — |                   — |           — |
| **SQL***       |                 — |       — |          — |       — |  **9%** |       — |                   — |           — |
| **Otros**      |                 — |     ~0% |         3% |      1% |     ~0% |     ~0% |                 ~0% |          4% |
```
**03-Mi historia.md**
```markdown
Años 90 - Java - C - HTML
2000 - Toolbook 4.0 - Visual Basic Script
2001 - Macromedia Director - Lingo
2003 - Macromedia Flash - ActionScript 2.0
2005 - Adobe Flash MX - ActionScript 3.0 POO
2007 - Apple iPhone - incompatible con Flash - Javascript
2010 - Android empieza abandonar Flash - Javascript

Tomé una decisión:
Usar lenguajes libres, no propietarios, no controlables por una empresa

HTML, CSS, JS, Python, SQL, PHP, ...

COBOL - Para la banca - nicho
```
### 05-Fases del desarrollo de una aplicación análisis, diseño, codificación, pruebas, documentación, explotación y mantenimiento, entre otras
**01-Fases.md**
```markdown
análisis:
Estudiamos el mundo real
Las necesidades de los usuarios
Si acaso esas necesidades se pueden resolver con programas
Si acaso ese programa está en nuestras manos
Por lo tanto si es viable y conveniente desarrollar

diseño:
Planificar la aplicación que quiero hacer
No me meto a picar código, sino que dedico unas horas a decidir
y a seleccionar tecnologías y a esbozar

codificación:
Te sientas y programas todo aquello que sale de la fase de diseño

pruebas:
Ningun programa sale bien a la primera
Pruebas el código que has desarrollado
Si falla vuelves a iterar, y desarrollas hasta un punto de lanzamiento

documentación, 
Creas la documentación para el usuario, desarrollador
Explicas cómo funciona tu programa
Tienes que explicar cómo funciona tu desarrollo

explotación y mantenimiento
Ponerlo en marcha
Mantenerlo, reportarán fallos - correctivo
Ampliarlo - evolutivos

Tu programa llegará a un fin de vida útil
Será más operativo crear un programa nuevo que mantener el antiguo
```
### 06-Proceso de obtención de código ejecutable a partir del código fuente; herramientas implicadas
**01-lenguaje interpretado.py**
```python
print("Hola mundo")
```
**02-hola mundo.c**
```c
#include <stdio.h>

int main(){
	printf("Hola mundo en C\n");
  return 0;
}
```
**03-como compilar.md**
```markdown
Linux: Linux ya incluye muchas herramientas de compilación:
gcc

Windows: 
Podéis descargar un entorno de compilación desde:
https://sourceforge.net/projects/mingw/files/
```
**04-comando de compilacion.md**
```markdown
1.-Abrir una terminal en la misma carpeta que está el archivo
2.-Poner: gcc [tuarchivo.c] -o [tuejecutable]
```
**05-variables.c**
```c
#include <stdio.h>

int main(){
	int edad = 48;
	printf("Que sepais que tengo %i años \n",edad);
  return 0;
}
```
**06-flotante.c**
```c
#include <stdio.h>

int main(){
	float altura = 1.72;
	printf("Que sepais que mido %f metros \n",altura);
  return 0;
}
```
**07-char.c**
```c
#include <stdio.h>

int main(){
	char inicial = 'L';
	printf("Que sepais que mi inicial es %c  \n",inicial);
  return 0;
}
```
**08-strings.c**
```c
#include <stdio.h>

int main(){
	char inicial = 'Lucas de Sturmprojekt';
	printf("Que sepais que soy %c  \n",inicial);
  return 0;
}
```
**09-array de caracteres.c**
```c
#include <stdio.h>

int main(){
	char nombre[] = "nurLukas";
	printf("Que sepais que mi nombre es %s  \n",nombre);
  return 0;
}
```
**10-operadores.c**
```c
#include <stdio.h>

int main(){
	float resultado;
  resultado = 4 + 3;
	printf("%f \n",resultado);
  
  resultado = 4 - 3;
	printf("%f \n",resultado);
  
  resultado = 4 * 3;
	printf("%f \n",resultado);
  
  resultado = 4 / 3;
	printf("%f \n",resultado);
  
  resultado = 4 % 3;
	printf("%f \n",resultado);
  return 0;
}
```
**11-comparadores.c**
```c
#include <stdio.h>
#include <stdbool.h>

int main(){
	bool resultado;
  resultado = 4 < 3;
	printf("%d \n",resultado);
  
  resultado = 4 > 3;
	printf("%d \n",resultado);
  
  resultado = 4 <= 3;
	printf("%d \n",resultado);
  
  resultado = 4 >= 3;
	printf("%d \n",resultado);
  
  resultado = 4 == 3;
	printf("%d \n",resultado);
  
  resultado = 4 != 3;
	printf("%d \n",resultado);
  return 0;
}
```
**12-operadores booleanos.c**
```c
#include <stdio.h>
#include <stdbool.h>

int main(){
	bool resultado;
  resultado = 4 == 4 && 3 == 3 && 2 == 2;
	printf("%d \n",resultado);
  
  resultado = 4 == 4 && 3 == 3 && 2 == 1;
	printf("%d \n",resultado);
  
  resultado = 4 == 4 || 3 == 3 || 2 == 2;
	printf("%d \n",resultado);
  
  resultado = 4 == 4 || 3 == 3 || 2 == 1;
	printf("%d \n",resultado);
  
  resultado = 4 == 4 || 3 == 2 || 2 == 1;
	printf("%d \n",resultado);
  
  resultado = 4 == 3 || 3 == 2 || 2 == 1;
	printf("%d \n",resultado);
  
  
  return 0;
}
```
**13-estructuras de seleccion.c**
```c
#include <stdio.h>

int main(){
	int edad = 48;
  if(edad < 10){
  	printf("eres un niño \n");
  }
  
  return 0;
}
```
**14-else.c**
```c
#include <stdio.h>

int main(){
	int edad = 48;
  if(edad < 10){
  	printf("eres un niño \n");
  }else{
  	printf("ya no eres un niño \n");
  }
  
  return 0;
}
```
**15-else if.c**
```c
#include <stdio.h>

int main(){
	int edad = 48;
  if(edad < 10){
  	printf("eres un niño \n");
  }else if(edad >= 10 && edad < 20){
  	printf("eres un adolescente \n");
  }else if(edad >= 20 && edad < 30){
  	printf("eres un joven \n");
  }else if(edad >= 30 && edad < 40){
  	printf("eres un adulto \n");
  }else{
  	printf("eres ya muy mayor \n");
  }
  
  return 0;
}
```
**16-repeticion.c**
```c
#include <stdio.h>

int main(){
	
  int dia;
  for(dia = 1;dia<31;dia++){
  	printf("Hoy es el dia %i del mes \n",dia);
  }
  return 0;
}
```
**17-scanf.c**
```c
#include <stdio.h>

int main(){
    int num;
    printf("Ingrese un numero: ");
    scanf("%d", &num);
    printf("El numero ingresado es: %d\n", num);
    return 0;
}
```
**18-calculadora de iva.c**
```c
#include <stdio.h>

int main(){
    int base;
    printf("Introduce una base: ");
    scanf("%d", &base);
    float iva;
    iva = base*0.21;
    float total = base + iva;
    printf("La base de cálculo es: %d\n", base);
    printf("El total del IVA es: %f\n", iva);
    printf("El total de la factura es: %f\n", total);
    return 0;
}
```
**19-comentarios.c**
```c
/*
	Programa calculadora de IVA
  v0.1 por Jose Vicente Carratala
*/
#include <stdio.h>

int main(){
		// Primero declaro variables
    int base;
    float iva;
    float total;
    
    // Ahora el usuario introduce datos
    printf("Introduce una base: ");
    scanf("%d", &base);
    
    // Ahora realizo cálculos
    iva = base*0.21;
    total = base + iva;
    
    // Y por último muestro resultados
    printf("La base de cálculo es: %d\n", base);
    printf("El total del IVA es: %f\n", iva);
    printf("El total de la factura es: %f\n", total);
    return 0;
}
```
**20-ia.c**
```c
/*
    Programa calculadora de IVA
    v0.2 por Jose Vicente Carratala
*/

#include <stdio.h>

int main(){

    // ================================
    // DECLARACIÓN DE VARIABLES
    // ================================

    float base;
    float iva;
    float total;

    // ================================
    // LIMPIAMOS LA PANTALLA
    // ================================

    printf("\033[2J");

    // Colocamos el cursor arriba a la izquierda
    printf("\033[1;1H");


    // ================================
    // CABECERA
    // ================================

    // Fondo azul + texto blanco + negrita
    printf("\033[44;97;1m");
    printf("                                                    \n");
    printf("              CALCULADORA DE IVA v0.2              \n");
    printf("              Jose Vicente Carratala               \n");
    printf("                                                    \n");
    printf("\033[0m");


    // ================================
    // ENTRADA DE DATOS
    // ================================

    printf("\n");

    printf("\033[1;36m");
    printf("+--------------------------------------------------+\n");
    printf("|               ENTRADA DE DATOS                   |\n");
    printf("+--------------------------------------------------+\n");
    printf("\033[0m");

    printf("\n");

    printf("  Introduce la base imponible: ");

    // Color amarillo para lo que escriba el usuario
    printf("\033[1;33m");
    scanf("%f", &base);
    printf("\033[0m");


    // ================================
    // CÁLCULOS
    // ================================

    iva = base * 0.21;
    total = base + iva;


    // ================================
    // RESULTADOS
    // ================================

    printf("\n");

    printf("\033[1;32m");
    printf("+--------------------------------------------------+\n");
    printf("|                    RESULTADO                     |\n");
    printf("+--------------------------------------------------+\n");
    printf("\033[0m");

    printf("|                                                  |\n");

    printf("|  Base imponible:        %10.2f euros        |\n", base);
    printf("|  IVA (21%%):             %10.2f euros        |\n", iva);

    printf("|                                                  |\n");

    printf("\033[1;32m");
    printf("+--------------------------------------------------+\n");
    printf("|  TOTAL:                 %10.2f euros        |\n", total);
    printf("+--------------------------------------------------+\n");
    printf("\033[0m");


    // ================================
    // EXPLICACIÓN DIDÁCTICA
    // ================================

    printf("\n");

    printf("\033[1;35m");
    printf("COMO SE HA CALCULADO\n");
    printf("====================\n");
    printf("\033[0m");

    printf("IVA   = %.2f x 0.21 = %.2f\n", base, iva);
    printf("TOTAL = %.2f + %.2f = %.2f\n", base, iva, total);


    // ================================
    // DESPEDIDA
    // ================================

    printf("\n");
    printf("\033[90m");
    printf("Pulsa ENTER para finalizar...");
    printf("\033[0m");

    getchar();
    getchar();

    return 0;
}
```
## 02-Proyecto
**01-ingresos-web.c**
```c
/*
    Calculadora STURMPROJEKT
    Version 0.1 - Ingresos por paginas web
*/

#include <stdio.h>

int main(){
    // Declaro las variables
    int webs = 3;
    float precioWeb = 250;
    float ingresos;

    // Calculo los ingresos
    ingresos = webs * precioWeb;

    // Muestro los resultados
    printf("CALCULADORA STURMPROJEKT\n");
    printf("Webs vendidas: %i\n", webs);
    printf("Precio por web: %.2f euros\n", precioWeb);
    printf("Ingresos: %.2f euros\n", ingresos);

    return 0;
}
```
**02-entrada-webs.c**
```c
/*
    Calculadora STURMPROJEKT
    Version 0.2 - Entrada de datos por teclado
*/

#include <stdio.h>

int main(){
    // Declaro las variables
    int webs;
    float precioWeb = 250;
    float ingresos;

    // Pido los datos
    printf("CALCULADORA STURMPROJEKT\n");
    printf("Cuantas webs has vendido este mes? ");
    scanf("%i", &webs);

    // Calculo los ingresos
    ingresos = webs * precioWeb;

    // Muestro los resultados
    printf("Webs vendidas: %i\n", webs);
    printf("Precio por web: %.2f euros\n", precioWeb);
    printf("Ingresos del mes por webs: %.2f euros\n", ingresos);

    return 0;
}
```
**03-hosting.c**
```c
/*
    Calculadora STURMPROJEKT
    Version 0.3 - Webs y hosting
*/

#include <stdio.h>

int main(){
    // Declaro las variables
    int webs;
    int clientesHosting;
    float precioWeb = 250;
    float precioHosting = 35;
    float ingresosWebs;
    float ingresosHosting;
    float ingresosMes;

    // Pido los datos
    printf("CALCULADORA STURMPROJEKT\n");

    printf("Cuantas webs has vendido este mes? ");
    scanf("%i", &webs);

    printf("Cuantos clientes de hosting tienes este mes? ");
    scanf("%i", &clientesHosting);

    // Calculo los ingresos
    ingresosWebs = webs * precioWeb;
    ingresosHosting = clientesHosting * precioHosting;
    ingresosMes = ingresosWebs + ingresosHosting;

    // Muestro los resultados
    printf("\nINGRESOS DEL MES\n");
    printf("Desarrollo de webs: %.2f euros\n", ingresosWebs);
    printf("Hosting y mantenimiento: %.2f euros\n", ingresosHosting);
    printf("Total: %.2f euros\n", ingresosMes);

    return 0;
}
```
**04-dominios.c**
```c
/*
    Calculadora STURMPROJEKT
    Version 0.4 - Webs, hosting y dominios
*/

#include <stdio.h>

int main(){
    // Declaro las variables
    int webs;
    int clientesHosting;
    int dominiosCobrados;

    float precioWeb = 250;
    float precioHosting = 35;
    float precioDominio = 35;

    float ingresosWebs;
    float ingresosHosting;
    float ingresosDominios;
    float ingresosMes;

    // Pido los datos
    printf("CALCULADORA STURMPROJEKT\n");

    printf("Cuantas webs has vendido este mes? ");
    scanf("%i", &webs);

    printf("Cuantos clientes de hosting tienes este mes? ");
    scanf("%i", &clientesHosting);

    printf("Cuantos servicios anuales de dominio has cobrado este mes? ");
    scanf("%i", &dominiosCobrados);

    // Calculo los ingresos
    ingresosWebs = webs * precioWeb;
    ingresosHosting = clientesHosting * precioHosting;
    ingresosDominios = dominiosCobrados * precioDominio;

    ingresosMes = ingresosWebs + ingresosHosting + ingresosDominios;

    // Muestro los resultados
    printf("\nINGRESOS DEL MES\n");
    printf("Desarrollo de webs: %.2f euros\n", ingresosWebs);
    printf("Hosting y mantenimiento: %.2f euros\n", ingresosHosting);
    printf("Servicios de dominio: %.2f euros\n", ingresosDominios);
    printf("Total: %.2f euros\n", ingresosMes);

    return 0;
}
```
**05-gastos.c**
```c
/*
    Calculadora STURMPROJEKT
    Version 0.5 - Ingresos y gastos del mes
	
	
	Tengo que decir que tuve dificultades con programación en C, la ia me ayudo bastante además de depurando el codigo, 
	me oriento, y me ayudo a entender los conceptops y a hacer las variables correctamente 
	y comentar de forma precisa los bloques de codigo
*/

#include <stdio.h>

int main(){
    // Declaro las variables
    int webs;
    int clientesHosting;
    int dominiosCobrados;

    float precioWeb = 250;
    float precioHosting = 35;
    float precioDominio = 35;

    float electricidad = 10;
    float internet = 15;
    float gptPlus = 23;
    float costeDominio = 15;

    float ingresosWebs;
    float ingresosHosting;
    float ingresosDominios;
    float ingresosMes;
    float gastosDominios;
    float gastosMes;
    float resultadoMes;

    // Pido los datos
    printf("CALCULADORA STURMPROJEKT\n");

    printf("Cuantas webs has vendido este mes? ");
    scanf("%i", &webs);

    printf("Cuantos clientes de hosting tienes este mes? ");
    scanf("%i", &clientesHosting);

    printf("Cuantos servicios anuales de dominio has cobrado este mes? ");
    scanf("%i", &dominiosCobrados);

    // Calculo los ingresos
    ingresosWebs = webs * precioWeb;
    ingresosHosting = clientesHosting * precioHosting;
    ingresosDominios = dominiosCobrados * precioDominio;

    ingresosMes = ingresosWebs + ingresosHosting + ingresosDominios;

    // Calculo los gastos y el resultado
    gastosDominios = dominiosCobrados * costeDominio;
    gastosMes = electricidad + internet + gptPlus + gastosDominios;
    resultadoMes = ingresosMes - gastosMes;

    // Muestro los resultados
    printf("\nRESUMEN DEL MES\n");
    printf("Ingresos por webs: %.2f euros\n", ingresosWebs);
    printf("Ingresos por hosting: %.2f euros\n", ingresosHosting);
    printf("Ingresos por dominios: %.2f euros\n", ingresosDominios);
    printf("Ingresos totales: %.2f euros\n", ingresosMes);

    printf("\nElectricidad: %.2f euros\n", electricidad);
    printf("Internet: %.2f euros\n", internet);
    printf("GPT Plus: %.2f euros\n", gptPlus);
    printf("Gastos de dominios: %.2f euros\n", gastosDominios);
    printf("Gastos totales: %.2f euros\n", gastosMes);

    printf("\nResultado del mes: %.2f euros\n", resultadoMes);

    // Indico si hay ganancias o perdidas
    if(resultadoMes > 0){
        printf("Hay ganancias.\n");
    }else if(resultadoMes < 0){
        printf("Hay perdidas.\n");
    }else{
        printf("Los ingresos y los gastos son iguales.\n");
    }

    return 0;
}
```
## 03-Resultado de aprendizaje
**RA1.MD**
```markdown
# Resultado de aprendizaje 1
## Resultado de aprendizaje

Reconoce los elementos y herramientas que intervienen en el desarrollo de un programa informático, 
analizando sus características y las fases en las que actúan hasta llegar a su puesta en funcionamiento.

*Criterios de evaluación*
a) Se ha reconocido la relación de los programas con los componentes del sistema informático: memoria, procesador, periféricos, entre otros.
Un programa informático, es un conjunto de instrucciones que permiten realizar una o más tareas.
Para funcionar necesita de los componente fisicos del ordenador, (hardware), y los servicios del S.O.
Hardaware:
- Procesador: ejecuta las instrucciones y realiza operaciones aritméticas, lógicas y de control.
- Memoria RAM: almacena temporalmente las instrucciones y los datos utilizados durante la ejecución.
- Almacenamiento: conserva los programas y sus archivos aunque se apague el equipo.
- Periféricos de entrada: permiten introducir datos, como el teclado o el ratón.
- Periféricos de salida: muestran los resultados, como la pantalla o la impresora.
- Sistema operativo: gestiona los recursos y facilita el acceso del programa a los dispositivos.

b) Se han identificado las fases de desarrollo de una aplicación informática.
Fases de desarrollo de una aplicación informática:
- Análisis: Identificar necesidades, requisitos y viabilidad.
- Diseño: Definir la estructura, los datos, las operaciones y la interacción.
- Codificación: Escribir el programa en un lenguaje de programación.
- Pruebas: Comprobar el cumplimiento de los requisitos y detectar errores.
- Documentación: Explicar el uso, la instalación y el funcionamiento interno.
- Implantación y explotación: Instalar la aplicación y utilizarla en su entorno real.
- Mantenimiento: Corregir errores y adaptar o ampliar el programa.

c) Se han diferenciado los conceptos de código fuente, objeto y ejecutable.
- El *código fuente* es el texto escrito por el programador. Por ejemplo: un archivo .c contiene instrucciones, declaraciones y funciones.
- El *objeto* es el resultado de compilar código fuente, en una compilación se contiene instrucciones máquina y suele almacenarse en archivos .o o .obj.
- El *ejecutable* se obtiene mediante el enlazado de los archivos objeto y las bibliotecas necesarias, tiene un formato que permite al sistema operativo cargarlo e iniciar su ejecución.

d) Se han reconocido las características de la generación de código intermedio para su ejecución en máquinas virtuales.
En clase hemos trabajado con programas escritos en C y Python. Estos ejemplos permiten distinguir diferentes formas de ejecutar un programa.
- En C utilizamos el compilador GCC mediante un comando, este proceso genera un ejecutable.
- En Python lo ejecutamos mediante el intérprete de Python, sin generar manualmente un ejecutable.

e) Se han clasificado los lenguajes de programación, identificando sus características.
Clasificación de los lenguajes de programación:
- Según el nivel de abstracción
	. Bajor nivel
	. Medio nivel
	. Alto nivel

- Según el paradigma
	. Imperativo
	. Orientado a objetos
	. Declarativo
	. Multiparadigma

f) Se ha evaluado la funcionalidad ofrecida por las herramientas utilizadas en el desarrollo de software.
Herramientas utilizadas en el desarrollo de software:
- Entorno de desarrollo integrado, o IDE: IDE Python
- Compilador: GCC
- Enlazador: GCC ademas de compilar, enlaza el "codigo objeto" con las bibliotecas/dependencias necesarias.
- Depurador: yo utilice Chat GPT para depurar.
- Control de versiones: Identifico en mi código la version ej: "v0.2", tambien utilizo Github desktop

g) Se han identificado las características y escenarios de uso de las metodologías ágiles de desarrollo de software.
Las metodologías ágiles consisten en desarrollar un programa mediante pequeñas mejoras sucesivas, 
comprobando los resultados y adaptándolo a las necesidades del usuario.
En los ejercicios de clase, la calculadora de IVA muestra una evolución: 
primero permite introducir una base y calcular el resultado; después aparecen versiones con comentarios, 
una presentación más elaborada y una explicación de los cálculos.

Este ejemplo permite entender algunas características del desarrollo ágil:
- Desarrollo incremental: añadir funcionalidades poco a poco.
- Pruebas frecuentes: comprobar que los cálculos funcionan después de cada modificación.
- Adaptación a cambios: modificar el programa si cambian las necesidades.
- Revisión con el usuario: mostrar una versión funcional y recoger sus sugerencias.
```
