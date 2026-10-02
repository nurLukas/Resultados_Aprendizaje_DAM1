# Reporte de proyecto

## Información de generación

- **Fecha:** 2026-09-30 02:50:52 +0200
- **Usuario:** lucas
- **Equipo:** LUCAS
- **Sistema operativo:** Windows
- **Arquitectura:** x86_64
- **Directorio de ejecución:** `D:/Herramientas/jocarsa-generador-windows-x64`
- **Proyecto documentado:** `D:/DAM1 Resultados Aprendisaje/6-Sistemas informáticos/Unidad 2`
- **HMAC-SHA-256 de autenticidad:** `5b9b377852c3217df0d675e8e792688c3a67032f22365f3938b4669a6821c61a`

> El HMAC-SHA-256 se calcula sobre el documento completo usando un secreto incluido en el programa y 64 ceros en el propio campo del HMAC. El secreto no se escribe en el informe. Este mecanismo permite comprobar integridad y que el documento fue generado con el mismo secreto.

## Estructura del proyecto

```
D:/DAM1 Resultados Aprendisaje/6-Sistemas informáticos/Unidad 2
├── 1-Ejercicios
│   ├── 01-Evolución histórica y clasificación
│   │   ├── 01-Breve historia.md
│   │   └── 02-enlaces de susto.md
│   ├── 02-Funciones de un sistema operativo
│   │   └── 01-sistema de archivos.md
│   ├── 06-Procedimiento de instalación
│   │   ├── 00-Credenciales VM.md
│   │   ├── 01-Primero actualizamos.md
│   │   ├── 02-Operaciones de red.md
│   │   └── 03-Acceso remoto.md
│   ├── 08-Tecnologías de virtualización. Tipos
│   │   └── 01-virtualizacion.md
│   ├── 09-Consideraciones previas a la instalación de sistemas operativos libres y propietarios
│   │   ├── 01-requerimientos de hardware.md
│   │   ├── 02-requerimientos windows server.md
│   │   └── 03-comparacion.md
│   └── 12-Actualización y recuperación de sistemas operativos y aplicaciones
│       ├── 01-copia de seguridad.md
│       └── 02-copia de seguridad de los archivos.md
├── 2-Proyecto
│   └── 0-Ejercicio final de unidad 2.md
└── 3-Resultado de aprendizaje
    └── RA2.md
```

## Bases de datos SQLite

Esta sección documenta únicamente el esquema de las bases SQLite detectadas. No se vuelcan registros ni datos de usuario.

No se han encontrado bases SQLite con extensiones .db, .sqlite o .sqlite3.

## Código (intercalado)

# Unidad 2
## 1-Ejercicios
### 01-Evolución histórica y clasificación
**01-Breve historia.md**
```markdown
Windows
Linux
macOS

Android
iOS

Multipropósito - una misma máquina puede servir para varios fines
Máquina - hardware
Sistema operativo - maneja la máquina - abstrae la dificultad la máquina
y pone la máquina al servicio del programa

1969-1970 - lanzamiento el sistema operativo UNIX
Para supercomputadoras y mainframes
https://es.wikipedia.org/wiki/Unix

| Licencia UNIX (1975 aprox.)              | Precio entonces | Equivalente aprox. en dólares de 2026 |
| ---------------------------------------- | --------------: | ------------------------------------: |
| **Universidad / educación**              |        **$150** |                            **≈ $915** |
| **Licencia comercial con código fuente** |     **$20.000** |                        **≈ $121.900** |
| Licencia binaria para máquina adicional  |         ~$8.000 |                             ≈ $48.800 |


SSOO reservado para grandes empresas


Bill Gates, Paul Allen, Steve Ballmer - Microsoft - MS-DOS

| Sistema                  | Año de referencia |    Precio original | Equivalente aprox. en 2026 |
| ------------------------ | ----------------: | -----------------: | -------------------------: |
| **UNIX comercial**       |           1978-79 | **$20.000–25.000** |      **≈ $90.000–112.000** |
| **UNIX, CPU adicional**  |             ~1979 |  **$7.000–10.000** |       **≈ $31.000–45.000** |
| **PC-DOS 1.0 / MS-DOS**  |              1981 |            **$40** |                 **≈ $145** |
| CP/M-86, como referencia |           1981-82 |           **$240** |                 **≈ $850** |


Con MacOS

| Sistema operativo       | Año referencia |   Precio original aprox. | Equivalente aprox. 2026 | Tipo                                |
| ----------------------- | -------------: | -----------------------: | ----------------------: | ----------------------------------- |
| **UNIX comercial**      |        1978-79 |              **$20.000** |   **≈ $95.000–100.000** | Multiusuario, minicomputadores      |
| **Apple DOS 3.1**       |           1978 | **incluido con Disk II** |                       — | Apple II                            |
| **Apple Disk II + DOS** |           1978 |                 **$495** |            **≈ $2.500** | Unidad de disco + controlador + DOS |
| **PC-DOS 1.0**          |           1981 |                  **$40** |          **≈ $145–150** | IBM PC                              |
| **CP/M-86**             |           1981 |                 **$240** |          **≈ $870–900** | Microordenadores                    |


Linux = Un clon de UNIX, pero de software libre

```
**02-enlaces de susto.md**
```markdown
https://upload.wikimedia.org/wikipedia/commons/4/4c/Unix_history-simple_es.svg?utm_source=es.wikipedia.org&utm_campaign=imageinfo&utm_content=original

https://upload.wikimedia.org/wikipedia/commons/1/1b/Linux_Distribution_Timeline.svg?utm_source=es.wikipedia.org&utm_campaign=index&utm_content=original
```
### 02-Funciones de un sistema operativo
**01-sistema de archivos.md**
```markdown
Abrir consola: Ctrl + Alt + T   (en ubuntu desktop)

pwd = donde estoy ahora mismo
whoami = quien soy yo

ls = list = listado de directorios y archivos (dir)

ls -l = listado en forma de lista

cd = Change directory 
Relativa: con respecto a donde estoy
absoluta: a cualquier sitio directamente
cd Escritorio (entra en el escritorio)

clear = Limpia la pantalla (de terminal)

mkdir = make directory = Crea directorio

touch = crear archivo sin entrar en él

editores de texto = nano
nano clientes.txt
Control + O = guardar
Control + X = salir

cp = copy = cp [origen] [destino]

rm = remove

mv = mover = mv [origen] [destino]












```
### 06-Procedimiento de instalación
**00-Credenciales VM.md**
```markdown
# Credenciales VM Ubuntu Desktop 24.04 LTS 

* usuario: lucas95
* hostname: portatil
* contraseña: tame123$


# Credenciales VM Ubuntu Server 24.04 LTS

* Usuario:
* hostname:
* contraseña:
```
**01-Primero actualizamos.md**
```markdown

# sudo apt update

* sudo = super user do
* apt = gestor de paquetes de Debian
* update = actualizar paquetes, (repositorios)

# sudo apt upgrade

* actualizar los paquetes que tengan actualización

# sudo apt dist-upgrade 
Actualiza la version de distro, es como pasar de un windows 10 a windwos 11, 
No se recomienda nunca cambiar el SO con este comando, ya que es una forma sucia, deja archivos residuales del anterior SO
```
**02-Operaciones de red.md**
```markdown

1.- Cambio la configuracion de red de NAT a adaptador puente
2.- Reinicio -> sudo reboot


# Averiguar ip
instalamos una herramienta con el comando -> sudo apt install net-tools 

hacemos el comando -> ifconfig

# Instalar servidor apache
sudo apt install apache2

# Instalamos soporte para PHP
sudo apt install php


YA TENEMOS APACHE, PHP, Y MYSQL
```
**03-Acceso remoto.md**
```markdown

# Instalamos openssh-server

sudo apt install openssh-server


Me conecto de forma remota desde fuera, necesito estas 3 cosas:

1. La ip del servidor
2. El usuario con el que me quiero conectar
3. La contraseña del usuario

ssh lucas95@195.168.x.xx

```
### 08-Tecnologías de virtualización. Tipos
**01-virtualizacion.md**
```markdown

* Maquinas fisicas: 
El sistema está instalado en tu propia máquina

* Máquinas virtuales:
Software que simula otra máquina física
Crea una "burbuja".
A esa burbuja le hace creer que es un equipo físico
Le permite instalar una máquina dentro de otra máquina

A nivel de escritorio:
VirtualBox
VMware
Que disponen de interfaz gráfica de usuario

Virtualización en terminal
KVM - Qemu

Qemu también se usa para simular Windows en Linux - ejecutar programas sencillos en Linux

* Ventajas de las máquinas virtuales:
Aislamiento
Recuperación
Copias de seguridad

* Desventajas:
Penalización en el rendimiento
No acceso a los recursos físicos del sistema

Crear diferentes entornos te puede servir para diferentes proyectos
Porque cada proyecto puede tener sus propios requisitos

Docker
Alternativa a las máquinas virtuales
Crear unos contenedores (ballenas) 
Cada contenedor no es un entorno virtual completo
Si que es un espacio de trabajo donde en cada espacio puedes instalar tus propias librerias

```
### 09-Consideraciones previas a la instalación de sistemas operativos libres y propietarios
**01-requerimientos de hardware.md**
```markdown
| Requisito            | Windows 10                                     | Windows 11                                                                                      |
| -------------------- | ---------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| **Procesador**       | 1 GHz o superior                               | 1 GHz, 2 núcleos o más, 64 bits y CPU compatible                                                |
| **Arquitectura**     | 32 o 64 bits                                   | **Solo 64 bits**                                                                                |
| **RAM**              | 1 GB (32 bits) / 2 GB (64 bits)                | **4 GB**                                                                                        |
| **Almacenamiento**   | 32 GB*                                         | **64 GB**                                                                                       |
| **Firmware**         | BIOS o UEFI                                    | **UEFI + Secure Boot**                                                                          |
| **TPM**              | No requerido                                   | **TPM 2.0**                                                                                     |
| **Gráfica**          | DirectX 9 + WDDM 1.0                           | **DirectX 12 + WDDM 2.0**                                                                       |
| **Pantalla**         | 800 × 600                                      | >9", **720p**, 8 bits/canal                                                                     |
| **Internet**         | No imprescindible para instalación tradicional | Requerido en determinados escenarios de configuración                                           |
| **Cuenta Microsoft** | No necesariamente                              | Requerida oficialmente en la configuración inicial de ediciones de consumo en muchos escenarios |
```
**02-requerimientos windows server.md**
```markdown
A septiembre de 2026, la versión LTSC actual es **Windows Server 2025**, disponible en **Standard** y **Datacenter**. Windows Server 2022 sigue soportado, pero su soporte estándar termina el 13 de octubre de 2026. ([Microsoft Learn][1])

### Windows Server 2025: requisitos mínimos

Microsoft establece estos mínimos para Windows Server 2025/Windows Server moderno: ([Microsoft Learn][2])

| Componente          | Requisito mínimo                                                  |
| ------------------- | ----------------------------------------------------------------- |
| CPU                 | **64 bits, 1,4 GHz**                                              |
| Instrucciones CPU   | x64, NX/DEP, CMPXCHG16b, LAHF/SAHF, PrefetchW, **SSE4.2, POPCNT** |
| Virtualización CPU  | **SLAT (EPT/NPT)**                                                |
| RAM Server Core     | **2 GB**                                                          |
| RAM con escritorio  | **2 GB**, Microsoft recomienda 4 GB                               |
| Disco               | **32 GB** mínimo                                                  |
| Red                 | **Ethernet 1 Gbit/s**                                             |
| Bus de red          | PCI Express                                                       |
| RAM servidor físico | ECC o tecnología similar                                          |
| Arquitectura        | exclusivamente **64 bits**                                        |

Los 32 GB son un **mínimo absoluto** y Microsoft advierte que puede ser necesario bastante más espacio dependiendo de RAM, actualizaciones y funciones instaladas. ([Microsoft Learn][2])

### Licencia

Aquí está la gran diferencia respecto a Windows 10/11: **la licencia puede costar bastante más que el ordenador**.

Microsoft licencia Windows Server 2025 Standard y Datacenter **por núcleos**, con un mínimo habitual de **16 cores licenciados por servidor**; además hacen falta **CAL** para los usuarios/dispositivos que accedan al servidor. ([Microsoft][3])

Como referencia española actual, Microsoft vende directamente **Windows Server 2025 Standard, 16 cores + 10 CAL por 1.978 €**. ([Microsoft][4])

En canal OEM/distribución se encuentran precios inferiores; por ejemplo, una lista de distribución española mostraba aproximadamente **780 € para Standard 2025 OEM 16 cores** y unos **4.542 € para Datacenter OEM 16 cores**, antes de considerar las CAL necesarias. ([Ingram Micro][5])

La diferencia fundamental es que Standard está pensado para servidores físicos o poco virtualizados y permite, con el licenciamiento correspondiente, **2 máquinas virtuales**, mientras que Datacenter permite **VM ilimitadas** sobre el host correctamente licenciado. ([Microsoft][3])

### ¿Cuánto cuesta el ordenador mínimo?

Curiosamente, **muy poco** si hablamos literalmente de satisfacer los requisitos y no de montar un servidor empresarial certificado.

Por ejemplo, actualmente aparecen equipos reacondicionados como:

### [HP ProDesk 400 G5 Intel Core i5-9500T]()

*195,08 €*

por aproximadamente **195 €**, con un i5-9500T que está enormemente por encima del mínimo de CPU.

También aparecen equipos de escritorio alrededor de **180–260 €**:

### [Dell OptiPlex 3060]()

*179,00 €*

### [Lenovo ThinkCentre M70s]()

*183,68 €*

### [HP ProDesk 400 G6 i5-10500T]()

*257,75 €*

Por tanto, para explicarlo en clase, yo resumiría los órdenes de magnitud así:

| Concepto                                                  |                       Windows Server 2025 |
| --------------------------------------------------------- | ----------------------------------------: |
| Hardware mínimo teórico                                   |                            **~150–250 €** |
| Hardware básico razonable (8–16 GB + SSD)                 |                            **~200–400 €** |
| Licencia Standard OEM 16 cores                            |       **~780 €** como referencia de canal |
| Standard 16 cores + 10 CAL, Microsoft                     |                               **1.978 €** |
| Datacenter 16 cores OEM                                   |     **~4.500 €** como referencia de canal |
| **Servidor básico + Standard**                            | desde aproximadamente **1.000 €** con OEM |
| **Servidor básico + Standard + 10 CAL oficial Microsoft** |                  alrededor de **2.200 €** |

Hay una distinción didáctica importante: **un PC de 200 € puede superar los requisitos técnicos mínimos de Windows Server 2025, pero eso no lo convierte en un servidor empresarial adecuado**. Para producción normalmente buscaríamos ECC, almacenamiento redundante/RAID, fuente fiable o redundante, más RAM, copias de seguridad y hardware específicamente soportado. Microsoft además señala expresamente ECC o tecnología equivalente para despliegues físicos. ([Microsoft Learn][2])

Si quieres, puedo hacerte a continuación una **tabla Windows 10 → Windows 11 → Server 2016 → 2019 → 2022 → 2025**, con **RAM, CPU, disco, precio de licencia y precio aproximado del hardware mínimo**, que puede quedar muy bien como material de clase.

[1]: https://learn.microsoft.com/es-es/windows/release-health/windows-server-release-info?utm_source=chatgpt.com "Información de versión de Windows Server | Microsoft Learn"
[2]: https://learn.microsoft.com/es-es/windows-server/get-started/hardware-requirements?utm_source=chatgpt.com "Requisitos de hardware para Windows Server | Microsoft Learn"
[3]: https://www.microsoft.com/es-es/windows-server/pricing?utm_source=chatgpt.com "Precios y licencias de Windows Server 2025 | Microsoft"
[4]: https://www.microsoft.com/es-es/d/windows-server-2025-standard/dg7gmgf0wzrw?utm_source=chatgpt.com "Comprar una licencia de Windows Server 2025 Standard (16 núcleos) y 5 o 10 CAL | Microsoft Store"
[5]: https://now.ingrammicro.com/rs/340-MXL-245/images/ES_ListaPreciosSemanal_MSFT_Update.pdf?version=4&utm_source=chatgpt.com "| LISTA DE PRECIOS - válida desde el 30 de Junio hasta el 4 de Julio del 2025  |  |  |  |"
```
**03-comparacion.md**
```markdown
Sí. Para que la comparación sea homogénea, tomaría como referencia **Windows Server 2025 Standard**, **Ubuntu Server 24.04 LTS** y **Debian 13**, todos en instalación de servidor sin escritorio cuando sea posible. Los requisitos son los publicados por Microsoft, Canonical y Debian; no son necesariamente configuraciones recomendables para producción. ([Microsoft Learn][1])

### Comparativa general

| Característica                |     Windows Server 2025 |    Ubuntu Server 24.04 LTS |                 Debian 13 |
| ----------------------------- | ----------------------: | -------------------------: | ------------------------: |
| RAM mínima                    |                **2 GB** | **1,5 GB** instalación ISO | **512 MB** sin escritorio |
| RAM recomendada/base sugerida |     4 GB con escritorio |                  **3 GB+** |   **1 GB** sin escritorio |
| Disco mínimo                  |               **32 GB** |                   **5 GB** |                  **4 GB** |
| Disco sugerido                |                  >32 GB |                 **25 GB+** |      Depende del servicio |
| CPU                           |       x64 ≥ **1,4 GHz** |             amd64/ARM/etc. |   múltiples arquitecturas |
| Red mínima especificada       |   **1 Gbit/s Ethernet** |       depende del hardware |      depende del hardware |
| ECC para host físico          | Microsoft lo especifica |  No como requisito general | No como requisito general |
| Licencia SO                   |             **De pago** |                    **0 €** |                   **0 €** |
| CAL de usuarios/dispositivos  |                  **Sí** |                         No |                        No |
| Código abierto                |                      No |                         Sí |                        Sí |

Microsoft establece para Windows Server 2025 un procesador x64 de al menos 1,4 GHz, 2 GB de RAM y 32 GB de almacenamiento; además exige determinadas instrucciones modernas y especifica ECC o tecnología equivalente para despliegues físicos. ([Microsoft Learn][1]) Canonical publica para Ubuntu Server 24.04 LTS 1,5 GB de RAM y 5 GB de almacenamiento para instalación mediante ISO, aunque sugiere 3 GB y 25 GB respectivamente. ([Ubuntu][2]) Debian 13 publica para una instalación sin escritorio 512 MB de RAM mínima, 1 GB recomendada y 4 GB de disco. ([Debian][3])

### RAM mínima

Aquí Linux tiene una ventaja clara cuando interesa construir **VM pequeñas, servidores auxiliares o muchos contenedores/instancias**. Eso no significa que un servidor real deba funcionar con 512 MB: esos son mínimos del sistema operativo, no de Apache, bases de datos, aplicaciones, usuarios concurrentes, etc. ([Ubuntu][2])

### Almacenamiento mínimo

Esta diferencia es bastante significativa: **32 GB frente a 5 y 4 GB**. Microsoft, además, dice explícitamente que esos 32 GB deben considerarse un mínimo absoluto y que determinadas configuraciones requieren más espacio. Canonical recomienda en la práctica al menos 25 GB para Ubuntu Server. ([Microsoft Learn][1])

## El coste de licencia es donde aparece la gran diferencia

Ubuntu Server y Debian pueden instalarse y utilizarse sin pagar una licencia por servidor, CPU, core o usuario. Eso no significa que todo servicio empresarial asociado a Linux sea gratuito: Canonical, Red Hat, SUSE y otros venden soporte, gestión y servicios adicionales.

En Windows Server 2025, Microsoft utiliza licenciamiento basado en **núcleos**, y Standard y Datacenter requieren además **CAL para los usuarios o dispositivos que acceden al servidor**. ([Microsoft][4])

Como referencia oficial española especialmente fácil de comparar, Microsoft Store vende actualmente:

**Windows Server 2025 Standard, 16 cores + 10 CAL = 1.978 €**. ([Microsoft][5])

Esto necesita una pequeña precisión: **0 € significa coste de licencia del SO**, no coste total de propiedad igual a cero. Administración, mantenimiento, copias de seguridad, seguridad, energía, soporte y personal existen con ambos sistemas.

## Si tenemos 10 servidores

Aquí la diferencia se vuelve especialmente interesante didácticamente. Si suponemos, sólo como **ejemplo simplificado**, diez servidores independientes y aplicamos a cada uno el paquete Microsoft de 1.978 €, tendríamos:

En una infraestructura real no se debe multiplicar necesariamente así: Windows Server se licencia por cores y los derechos de virtualización cambian entre Standard y Datacenter. Standard incluye derechos para **2 máquinas virtuales** bajo las condiciones correspondientes, mientras que Datacenter proporciona virtualización ilimitada cuando el host está correctamente licenciado. ([Microsoft][4])

## ¿Y el hardware?

Aquí aparece un punto interesante: **no hace falta comprar hardware diferente por utilizar Linux o Windows**. Un servidor x86-64 moderno razonable puede ejecutar cualquiera de ellos. Lo que cambia es cuánto hardware consume el propio SO y qué hardware mínimo admite oficialmente.

Por ejemplo, para una máquina física económica podríamos plantear como **configuración didáctica**, no como mínimo oficial:

| Hardware                    |    Configuración razonable básica |
| --------------------------- | --------------------------------: |
| CPU                         |                  4–6 cores x86-64 |
| RAM                         |                         **16 GB** |
| Disco                       |               **500 GB NVMe/SSD** |
| Red                         |                         **1 GbE** |
| Precio orientativo hardware | **~300–600 €** PC/reacondicionado |
| SO Ubuntu/Debian            |                  **0 € licencia** |
| Windows Server              |   añadir licencia correspondiente |

Para producción empresarial, cambiaría completamente el planteamiento: ECC, RAID/almacenamiento redundante, copias, PSU adecuada o redundante, UPS, gestión remota, garantía, etc.

## Una comparación más completa para tus alumnos

Hay bastantes más dimensiones que RAM, disco y precio:

| Aspecto                | Windows Server 2025      | Linux Server                     |
| ---------------------- | ------------------------ | -------------------------------- |
| Licencia SO            | Comercial                | Normalmente libre                |
| Pago por usuarios      | CAL en muchos escenarios | No                               |
| Requisitos mínimos     | Mayores                  | Generalmente menores             |
| Instalación mínima     | Server Core              | Extremadamente reducida          |
| Administración gráfica | Muy desarrollada         | Opcional                         |
| Administración CLI     | PowerShell               | Bash + herramientas GNU          |
| Servidor web habitual  | IIS                      | Apache / Nginx                   |
| Directorio corporativo | Active Directory         | Samba/LDAP/FreeIPA, etc.         |
| Virtualización         | Hyper-V                  | KVM/QEMU, etc.                   |
| Contenedores           | Sí                       | Ecosistema Linux muy extendido   |
| Automatización         | PowerShell               | Shell/Python/Ansible/etc.        |
| Actualizaciones        | Windows Update           | Repositorios/gestor paquetes     |
| Acceso remoto típico   | RDP/PowerShell           | SSH                              |
| Coste de licencia base | Alto comparativamente    | 0 € en Debian/Ubuntu             |
| Soporte comercial      | Microsoft/partners       | Disponible según distribución    |
| Arquitecturas          | x64                      | x86-64, ARM y otras según distro |

Por tanto, para una **comparativa docente**, evitaría la conclusión simplista de “Linux es gratis y Windows es caro”. Lo interesante es mostrar que Windows Server combina **licencia por cores + CAL + integración especialmente directa con el ecosistema Microsoft**, mientras que Linux ofrece **menores requisitos mínimos, ausencia habitual de licencia por instancia/usuario y gran flexibilidad**, pudiendo contratar soporte empresarial aparte. Windows Server Standard y Datacenter también tienen diferencias importantes en derechos de virtualización. ([Microsoft][4])

[Requisitos oficiales de Windows Server 2025 — Microsoft Learn](https://learn.microsoft.com/es-es/windows-server/get-started/hardware-requirements?utm_source=chatgpt.com) · [Precios y licenciamiento de Windows Server 2025 — Microsoft](https://www.microsoft.com/es-es/windows-server/pricing?utm_source=chatgpt.com) · [Requisitos oficiales de Ubuntu Server](https://ubuntu.com/server/docs/reference/installation/system-requirements/?utm_source=chatgpt.com) · [Guía oficial de instalación de Debian 13](https://www.debian.org/releases/stable/amd64/?utm_source=chatgpt.com)

[1]: https://learn.microsoft.com/es-es/windows-server/get-started/hardware-requirements?utm_source=chatgpt.com "Requisitos de hardware para Windows Server | Microsoft Learn"
[2]: https://ubuntu.com/server/docs/reference/installation/system-requirements/?utm_source=chatgpt.com "System requirements - Ubuntu Server documentation"
[3]: https://www.debian.org/releases/trixie/riscv64/ch03s04.en.html?utm_source=chatgpt.com "3.4. Meeting Minimum Hardware Requirements"
[4]: https://www.microsoft.com/es-es/windows-server/pricing?utm_source=chatgpt.com "Precios y licencias de Windows Server 2025 | Microsoft"
[5]: https://www.microsoft.com/es-es/d/windows-server-2025-standard/dg7gmgf0wzrw?utm_source=chatgpt.com "Comprar una licencia de Windows Server 2025 Standard (16 núcleos) y 5 o 10 CAL | Microsoft Store"


RAM mínima del sistema servidor

GB de RAM según los requisitos publicados para instalaciones de servidor. Menor no significa necesariamente mejor rendimiento.

sistema	ram
Windows Server 2025	2
Ubuntu Server 24.04	1,5
Debian 13	0,5

Almacenamiento mínimo

Espacio mínimo publicado para el sistema base, en GB.

sistema	disco
Windows Server 2025	32
Ubuntu Server 24.04	5
Debian 13	4

Coste inicial de licencia del sistema operativo

Comparación usando como referencia el paquete oficial Microsoft Windows Server 2025 Standard de 16 núcleos + 10 CAL frente a distribuciones Linux sin coste de licencia.

sistema	precio
Windows Server 2025 Standard	1978
Ubuntu Server	0
Debian	0

Ejemplo simplificado: licencias para 10 servidores

Multiplicación ilustrativa de 10 × 1.978 € para Windows frente a distribuciones Linux sin coste de licencia.

sistema	precio
Windows Server 2025	19.780
Ubuntu Server	0
Debian	0
```
### 12-Actualización y recuperación de sistemas operativos y aplicaciones
**01-copia de seguridad.md**
```markdown
1.-Tenemos una base de datos llamada dam1;

2.-mysqldump -u root -p dam1 > backupdam1.sql

3.-mysqldump -u root -p dam1 > backupdam120260921.sql
```
**02-copia de seguridad de los archivos.md**
```markdown
sudo mkdir /home/lucas95/copias

Supongamos que tengo un proyecto en /var/www/html/lucas-tests

sudo cp -R /var/www/html/lucas-tests /home/lucas95/copias/
```
## 2-Proyecto
**0-Ejercicio final de unidad 2.md**
```markdown
# Trabajo final de unidad 2

## Resumen de lo realizado en las tutorias de la unidad 2

Hicimos una introducción a la segunda unidad de la asignatura "sistemas informáticos"
En la cual vimos estadisticas y datos precisos sobre diferentes sistemas informáticos, ya sea para ordenadores o servidores, y su cronologia.
Concluimos que Windows es el rey indiscutible para ordenadores, Linux manda en los servidores.
MACOS tiene precencia en los ordenadores, y en un pasado tambien incursiono en el ambito de los servidores. 
Concluimos tambien que vale mas la pena aprendernos en Ubuntu Server, distro de Linux, ya que al ser sofware gratuito, 
la gran mayoria de empresas del mundo trabajan con el, 
para sus aplicaciones, paginas webs, bases de datos, etc.
¿Porque eligen una distro de Linux? Basicamente porque además de funcionar muy bien, es un software gratuito, de codigo abierto.

Luego de ello, Analizamos diferntes tecnolocias de virtualizacion como Virtual Vox de Oracle, el cual es de codigo abierto. 
Tambien conocimos VMWare y alguna otra alternativa menos popular.
Hicimos un breve dialogo sobre la tecnologia Docker, esta tecologia similar a las maquinas virtuales, funciona como alternativa, y tiene algunas ventajas. 

Descargamos e instalamos Virtual Vox, para posteriormente, descargar e instalar Ubuntu Desktop versión 24.04 LTS.
Segun las instrucciones del profesor configuramos en la maquina virtual la cantidad de nucleos de procesamiento, asignamos RAM,
y espacio en la memoria del disco. para un funcionamiento óptimo.
El profesor nos explicó que posteriormente trabajaremos con Ubuntu Server 24.04 LTS

En una clase posterior hemos aprendido sobre sistemas de archivos en ubuntu, trabajando en la consola con diferentes comandos
basicos para la navegacion entre los directorios, 
Algunos comandos son: 

```
pwd = donde estoy ahora mismo
whoami = quien soy yo

ls = list = listado de directorios y archivos (dir)

ls -l = listado en forma de lista

cd = Change directory 
Relativa: con respecto a donde estoy
absoluta: a cualquier sitio directamente
cd Escritorio (entra en el escritorio)

clear = Limpia la pantalla (de terminal)

mkdir = make directory = Crea directorio

touch = crear archivo sin entrar en él

editores de texto = nano
nano clientes.txt
Control + O = guardar
Control + X = salir

cp = copy = cp [origen] [destino]

rm = remove

mv = mover = mv [origen] [destino]
```

tambien hemos configurado los ajustes de red, de la maquina virtual, 
cambiando la conexión de red de NAT a "adaptador puente"
Reiniciamos la VM para implementar cambios con el comando sudo reboot 

Actualizamos los indices con el comando sudo apt update

Luego actualizamos los paquetes disponibles con el comando sudo apt upgrade

instalamos una herramienta con el comando -> sudo apt install net-tools 
Con esas herramientas podemos hacer el comando ifconfig,
y obtener información entre esos datos nuestra ip actual

Instalamos un servidor apache con el comando sudo apt install apache2
Luego instalamos el soporte para php con sudo apt install php
Para el protocolo ssh lo instalamos con el comando sudo apt install openssh-server
Con el protocolo instalado y los 3 requerimientos necesarios,
nos conectamos a la maquina virtual, de forma remota.


Retomamos la teoria para hablar de los requerimientos minimos de Hardware,
que necesitan diferentes versiones de windows,
y otros sistemas operativos como Ubuntu, siempre hablando en maquinas fisicas.
Comparamos graficos que plasman la cuota mundial de uso de estos diferentes 
sistemas operativos, precios, etc.

Finalmente, tratamos sobre copias de seguridad, donde aprendimos los siguientes comandos, 
para realizarlas en nuestra base de datos de prueba.

```
2.-mysqldump -u root -p dam1 > backupdam1.sql

3.-mysqldump -u root -p dam1 > backupdam120260921.sql

# para archivos
sudo mkdir -> + (ruta para la carpeta) Crea una carpeta
sudo cp -R -> + (ruta de la carpeta para copiar el archivo) para copiar un archivo en dicha carpeta
```

Lucas Andrés Griego
DAM1
```
## 3-Resultado de aprendizaje
**RA2.md**
```markdown
# Resultado de aprendizaje 2
**Resultado de aprendizaje**
Instala sistemas operativos planificando el proceso e interpretando documentación técnica.

**Criterios de evaluación**
a) Se han identificado los elementos funcionales de un sistema informático.
a) A lo largo de la unidad aprendimos sobre Hardware y Software, con todo lo que engloba para un sistema informático

b) Se han analizado las características, funciones y arquitectura de un sistema operativo.
b) Comprobamos parte por parte los componente del Hardware, como por ejemplo, placa madre, memoria RAM, unidad de almacenamiento, 
Fuente de alimentacion, perifericos de entrada y salida. etc abordando la funcion que cumple cada componente, y donde se ubica.

c) Se han comparado sistemas operativos en base a sus requisitos, características, campos de aplicación y licencias de uso.
c) Efectivamente, hemos visto historia, graficos comparativos, precios, requisitos minimos ya sea para sistemas operativos 
de ordenadores y para servidores, comprobando la cuota de consumo/popularidad de estos SO de en una tabla cronologica,
Analizando los altibajos de su utilizacion mundial.

d) Se ha planificado el proceso de la instalación de sistemas operativos.
d) Paso a paso hemos descargado el Software necesario para montar la maquina virtual con el SO que solicito el docente,
Comprobando versiones de SO, actualizando sus indices, y paquetes de datos. 

e) Se han instalado y actualizado sistemas operativos libres y propietarios.
e) Como se dijo en el pundo (d) de la consigna, se instalo y actualizo el sistema, con los comandos especificos que demando el docente.
dichos comandos estan especificados en el archivo del trabajo final de unidad.

f) Se han aplicado técnicas de actualización y recuperación del sistema.
f) Una vez tuvimos lista la maquina virtual, con el sistema operativo funcionando, y todos sus sistemas actualizados
Aprendimos a tecnicas de recuperacion mediante copias de seguridad y backup, los comandos de los cuales estan detallados
en el archivo del trabajo final de unidad.

g) Se han utilizado tecnologías de virtualización para instalar y probar sistemas operativos.
g)Instalamos Virtual Vox, un Software de Oracle, de código libre, y en el probamos Ubuntu Desktop

h) Se han instalado, desinstalado y actualizado aplicaciones.
h) Instalamos y actualizamos aplicaciones como net-tools, openssh, apache2, y php.
Los comandos de dichas instalaciones estan detallados en el trabajo final de unidad, y en elos ejercicios de subunidad que corresponda.

i) Se han documentado los procesos realizados.
i) Todos los procesos realizados paso a paso, fueron documentados al detalle en archivos formato .md. 
Estos archivos corresponden a cada subunidad de la unidad 2.

Lucas Ezequiel Andrés Griego
DAM1
Sistemas informáticos unidad 2
```
