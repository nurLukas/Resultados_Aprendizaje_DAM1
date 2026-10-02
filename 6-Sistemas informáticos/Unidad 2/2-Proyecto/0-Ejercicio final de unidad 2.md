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
