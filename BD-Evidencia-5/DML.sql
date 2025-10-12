------------------------------
-- Practicas DML SMART HOME--
------------------------------

INSERT INTO Vivienda (Nombre, Direccion)
VALUES 
('Casa Carmin 1', 'Av. Pablo Bautista 2834'),
('Casa Carmin 2', 'Av. Simón Bautista 4321'),
('Casa Carmin 3', 'Av. Juan Carlos Bautista 3224'),
('Casa Moreno', 'Santa Rosa 5483'),
('Casa Pérez', 'Monseñor José Negro 5421');

INSERT INTO Usuario (Nombre, Apellido, Email, Nombre_rol, Contraseña) 
VALUES ('Alvaro', 'Carmin', 'alvarocarmin@gmail.com', 'ADMIN', '421384'),
('Lucia', 'Carmin', 'luciacarmin@gmail.com', 'USUARIO', '723456'),
('Lisandro', 'Carmin', 'lisandrocarmin@gmail.com', 'USUARIO', '421384'),
('Catalina', 'Moreno', 'catalinamoreno@gmail.com', 'ADMIN', '321347'),
('Juan', 'Perez', 'juanperez@gmail.com', 'ADMIN', '123543');

INSERT INTO Usuario_Vivienda (ID_usuario, ID_vivienda)
VALUES ('1', '1'), ('2', '2'),('3', '3'),('4', '4'),('5', '5');

INSERT INTO Ubicacion (Nombre_ubicacion, ID_vivienda)
VALUES 
('Cocina', 1),
('Living', 1),
('Entrada', 1),
('Comedor', 2),
('Patio', 3);

INSERT INTO Automatizacion (Accion, Estado)
VALUES 
('Modo Fiesta', 0),
('Modo Noche', 0);

INSERT INTO Dispositivo (Nombre, Marca, Modelo, Tipo, Estado, ID_usuario, ID_ubicacion, ID_automatizacion)
VALUES 
('Camara Entrada', 'Dahua', 'Cctv 1080p', 'CAMARA', 1, 1, 3, 2),
('Luz Living', 'Philips', 'Hue-A19', 'LUZ', 0, 1, 2, 1),
('Torre de Sonido Comedor', 'Noblex', 'MNT290', 'MUSICA', 0, 2, 4, 1),
('Camara Living', 'TP-Link', 'Tapo C210', 'CAMARA', 1, 1, 2, 2),
('Barra Móvil Láser Patio', 'Spark', 'BARRA LASER', 'MUSICA', 1, 3, 5, 1);

SELECT * FROM Vivienda;
SELECT * FROM Usuario;
SELECT * FROM Usuario_Vivienda;
SELECT * FROM Ubicacion;
SELECT * FROM Automatizacion;
SELECT * FROM Dispositivo;