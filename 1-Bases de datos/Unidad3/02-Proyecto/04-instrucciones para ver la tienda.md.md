# Ver la tienda de Sturmprojekt desde Windows

Los archivos del proyecto se transfirieron desde Windows al servidor Ubuntu mediante FileZilla. 
La tienda se ejecuta en Ubuntu y se visualiza en el navegador de Windows mediante una conexión SSH.

## 1. Abrir la conexión desde Windows

en PowerShell 

ssh -L 5000:localhost:5000 nurlukas@IP_SERVIDOR (previamente investigue mi ip del servidor mediante el comando ifconfig, ya que la ip se actualiza constantemente)

ip ahora  mismo:192.168.1.29

La opción `-L 5000:localhost:5000` permite acceder desde el puerto 5000 de Windows al puerto 5000 de Ubuntu a través de SSH.

## 2. Entrar en la carpeta del proyecto en Ubuntu

Dentro de consola SSH, vamos a la carpeta donde transferiste los archivos con FileZilla:

cd "/ruta/de/la/carpeta"

Sustituye `/ruta/de/la/carpeta` por la ruta real de destino en Ubuntu, no por una ruta de Windows.

Comprueba que los archivos están presentes:

ls

Debe aparecer el archivo `03-tienda web.py`.

## 3. Comprobar la conexión con MySQL

connection = mysql.connector.connect(
    host='localhost',
    user='nurlukas',
    password='tame123',
    database='sturmprojekt'
)

Si lo corriges en Windows, vuelve a transferir el archivo actualizado mediante FileZilla.

`localhost` es correcto porque Python y MySQL se ejecutan en el mismo servidor Ubuntu. La contraseña de MySQL puede ser distinta de la contraseña SSH.

## 4. Iniciar la tienda

Desde la carpeta del proyecto, ejecuta:

python3 "03-tienda web.py"

Este comando se ejecuta en la terminal de Ubuntu, no dentro de la consola `mysql>`.

Para arrancar correctamente, Ubuntu debe tener disponibles Flask y MySQL Connector para Python, y MySQL debe estar funcionando con la base `sturmprojekt` y su tabla `servicios`.

Si la aplicación arranca, aparecerá un mensaje similar a:

Running on http://127.0.0.1:5000

## 5. Abrir la tienda en Windows

Abre el navegador de Windows y entra en:

[http://localhost:5000](http://localhost:5000)

La página mostrará el nombre, la descripción y el precio de los servicios almacenados en `sturmprojekt`.

Mantén abierta la conexión SSH y el programa Python mientras utilizas la tienda. No es necesario modificar el código para escuchar en todas las interfaces ni abrir el puerto 5000 del servidor: el acceso se realiza mediante el túnel SSH.

