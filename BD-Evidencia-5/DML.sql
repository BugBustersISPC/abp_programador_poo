------------------------------
-- Practicas DML SMART HOME--
------------------------------

INSERT INTO vivienda (direccion) 
VALUES ('Av. Pablo Bautista 2834'),
('Av. Simon Bautista 4321'),
('Av. Juan Carlos Bautista 3224'),
('Santa Rosa 5483'),
('Mon señor Jose Negro 5421');

INSERT INTO usuario (Nombre, Apellido, Email, Nombre_rol, Contraseña) 
VALUES ('Alvaro', 'Carmin', 'alvarocarmin@gmail.com', 'Admin', '421384'),
('Lucia', 'Carmin', 'luciacarmin@gmail.com', 'Usuario', '723456'),
('Lisandro', 'Carmin', 'lisandrocarmin@gmail.com', 'Dueño', '421384'),
('Catalina', 'Moreno', 'catalinamoreno@gmail.com', 'Usuario', '321347'),
('Juan', 'Perez', 'juanperez@gmail.com', 'Admin', '123543');

INSERT INTO usuario_Vivienda (ID_usuario, ID_vivienda)
VALUES ('1', '1'), ('2', '2'),('3', '3'),('4', '4'),('5', '5');

INSERT INTO Ubicacion (nombre_ubicacion, ID_vivienda)
VALUES ('Cocina', 1), ('Living', 1), ('Entrada', 1), ('Comedor', 2), ('Patio', 3);

INSERT INTO Tipo_Dispositivo (descripcion)
Values ('Camara'), ('Luz'), ('Equipo de Musica'); 

INSERT INTO Dispositivo (Nombre, Marca, Modelo, Estado, ID_tipo, ID_usuario, ID_ubicacion)
VALUES ('Camara Entrada', 'Dahua', 'Cctv 1080p', True, 1, 1, 1),
('Luz Living', 'Philips', 'Hue-A19', False, 2, 1, 1),
('Torre de Sonido Comedor', 'Noblex', 'MNT290', False, 3, 2, 2),
('Camara living', 'TP-Link', 'Tapo C210', True, 1, 1, 1),
('Barra Móvil Láser Patio', 'Spark', 'BARRA LASER', True, 3, 3, 3);

INSERT INTO automatizacion (accion, estado)
VALUES ('modo fiesta', '0'), ('modo noche', '0');

INSERT INTO registro_acciones (id_dispositivo,descripcion_accion,fecha_hora,id_automatizacion)
VALUES 
(1, 'Encendido por sensor de movimiento', '2025-09-14 20:45:00', 1),
(2, 'Apagado automático por inactividad', '2025-09-14 21:00:00', 2),
(3, 'Activación por modo noche', '2025-09-14 22:15:00', 2);

SELECT * FROM vivienda;
SELECT * FROM usuario;
SELECT * FROM usuario_Vivienda;
SELECT * FROM Ubicacion;
SELECT * FROM Tipo_Dispositivo;
SELECT * FROM Dispositivo;
SELECT * FROM automatizacion;
SELECT * FROM registro_acciones;