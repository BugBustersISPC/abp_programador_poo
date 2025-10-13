-----------------------
-- Consultas Simples --
-----------------------

SELECT * FROM automatizacion;

SELECT Nombre, Tipo, Estado, ID_ubicacion, ID_automatizacion FROM dispositivo;

SELECT * FROM ubicacion;

SELECT Nombre, Apellido, Nombre_rol FROM usuario;

SELECT * FROM usuario_vivienda;

SELECT Nombre, Direccion FROM vivienda;

---------------------------
-- Consultas Multitablas --
---------------------------
SELECT vivienda.Nombre AS Vivienda, ubicacion.Nombre_ubicacion AS Ubicacion, dispositivo.Nombre AS Dispositivo, dispositivo.Tipo, dispositivo.Estado
FROM vivienda
INNER JOIN ubicacion ON vivienda.ID_vivienda = ubicacion.ID_vivienda
INNER JOIN dispositivo ON ubicacion.ID_ubicacion = dispositivo.ID_ubicacion
WHERE vivienda.ID_vivienda = 1;
-- Muestra todos los dispositivos de una casa

SELECT vivienda.Nombre AS Vivienda, vivienda.Direccion, ubicacion.Nombre_ubicacion AS Ubicacion, dispositivo.Nombre AS Camara, dispositivo.Marca, dispositivo.Modelo
FROM vivienda
INNER JOIN ubicacion ON vivienda.ID_vivienda = ubicacion.ID_vivienda
INNER JOIN dispositivo ON ubicacion.ID_ubicacion = dispositivo.ID_ubicacion
WHERE dispositivo.Tipo = 'CAMARA' AND vivienda.ID_vivienda = 1;
-- Un usuario puede ver todos sus dispositivos

SELECT dispositivo.Nombre AS Dispositivo, dispositivo.Tipo, ubicacion.Nombre_ubicacion AS Ubicacion, vivienda.Nombre AS Vivienda, automatizacion.Accion AS Modo_Automatico
FROM dispositivo
INNER JOIN ubicacion ON dispositivo.ID_ubicacion = ubicacion.ID_ubicacion
INNER JOIN vivienda ON ubicacion.ID_vivienda = vivienda.ID_vivienda
INNER JOIN automatizacion ON dispositivo.ID_automatizacion = automatizacion.ID_automatizacion
Where vivienda.ID_vivienda = 1;
-- Filtra todas las camaras de seguridad en una vivienda

SELECT vivienda.Nombre AS Vivienda, automatizacion.Accion AS Modo_Automatizacion, automatizacion.Estado
FROM vivienda
INNER JOIN ubicacion ON vivienda.ID_vivienda = ubicacion.ID_vivienda
INNER JOIN dispositivo ON ubicacion.ID_ubicacion = dispositivo.ID_ubicacion
INNER JOIN automatizacion ON dispositivo.ID_automatizacion = automatizacion.ID_automatizacion
WHERE vivienda.ID_vivienda = 1
GROUP BY vivienda.Nombre, automatizacion.Accion, automatizacion.Estado;
-- Muestra el estado de las automatizaciones en una vivienda

-----------------
-- Subonsultas --
-----------------
SELECT 
    vivienda.Nombre AS Vivienda,
    dispositivo.Nombre AS Dispositivo,
    dispositivo.Tipo,
    ubicacion.Nombre_ubicacion AS Ubicacion
FROM vivienda
JOIN ubicacion ON vivienda.ID_vivienda = ubicacion.ID_vivienda
JOIN dispositivo ON ubicacion.ID_ubicacion = dispositivo.ID_ubicacion
WHERE vivienda.ID_vivienda = (
    SELECT ubicacion2.ID_vivienda
    FROM ubicacion ubicacion2
    GROUP BY ubicacion2.ID_vivienda
    ORDER BY COUNT(ubicacion2.ID_ubicacion) DESC
    LIMIT 1
);
-- Mostrar todos los dispositivos de la vivienda con mas ubicaciones

SELECT usuario.Nombre, usuario.Apellido,
    COUNT(dispositivo.ID_dispositivo) AS Cantidad_Dispositivos
FROM usuario
JOIN dispositivo ON usuario.ID_usuario = dispositivo.ID_usuario
GROUP BY usuario.ID_usuario, usuario.Nombre, usuario.Apellido
HAVING COUNT(dispositivo.ID_dispositivo) > (
    SELECT AVG(DispositivosPorUsuario)
    FROM (
        SELECT COUNT(dispositivo2.ID_dispositivo) AS DispositivosPorUsuario
        FROM dispositivo dispositivo2
        GROUP BY dispositivo2.ID_usuario
    ) sub
);
-- Mostrar los usuarios con más dispositivos que el promedio general
