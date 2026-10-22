1.-sudo mysql -u root -p
-- crea usuario nuevo con contraseña
-- creamos el nombre de usuario que querramos
CREATE USER 
'[tunombredeusuario]'@'[tuservidor]' IDENTIFIED BY '[tucontraseña]';

CREATE USER 'nurlucas'@'localhost' IDENTIFIED BY 'tame123';
@ = at (en)

# Comprobar el nivel de seguridad actual
SHOW VARIABLES LIKE 'validate_password%';
# Bajar la seguridad al nivel LOW
SET GLOBAL validate_password.policy = LOW;
SET GLOBAL validate_password.length = 7;

-- permite acceso a ese usuario
GRANT USAGE ON *.* TO '[tunombredeusuario]'@'[tuservidor]';
--[tuservidor] == localhost
-- La contraseña puede requerir Mayus, minus, numeros, caracteres, min len
GRANT USAGE ON *.* TO 'nurlukas'@'localhost';

-- quitale todos los limites que tenga
ALTER USER '[tunombredeusuario]'@'[tuservidor]' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

ALTER USER 'nurlukas'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

-- dale acceso a la base de datos empresadam
GRANT ALL PRIVILEGES ON [tubasededatos].* 
TO '[tunombredeusuario]'@'[tuservidor]';

GRANT ALL PRIVILEGES ON sturmprojekt.* 
TO 'nurlukas'@'localhost';
-- recarga la tabla de privilegios
FLUSH PRIVILEGES;