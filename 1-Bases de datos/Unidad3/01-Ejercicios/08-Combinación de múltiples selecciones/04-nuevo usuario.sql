-- Para usar tame123, debes reducir la política de contraseñas. Entra como administrador desde la terminal de Linux:
-- sudo mysql
-- Permite contraseñas sin exigir mayúsculas, números y símbolos.
-- SET GLOBAL validate_password.policy = LOW;
-- tame123 tiene siete caracteres.
-- SET GLOBAL validate_password.length = 7;


CREATE USER 'tiendazapatillas'@'localhost' IDENTIFIED BY 'tame123';

GRANT USAGE ON *.* TO 'tiendazapatillas'@'localhost';

ALTER USER 'tiendazapatillas'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON tiendazapatillas.* 
TO 'tiendazapatillas'@'localhost';

FLUSH PRIVILEGES;