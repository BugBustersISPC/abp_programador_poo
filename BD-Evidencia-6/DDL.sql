INSERT INTO Vivienda (Nombre, Direccion)
VALUES 
('Casa Carmin 1', 'Av. Pablo Bautista 2834'),
('Casa Carmin 2', 'Av. Simón Bautista 4321'),
('Casa Carmin 3', 'Av. Juan Carlos Bautista 3224'),
('Casa Moreno', 'Santa Rosa 5483'),
('Casa Pérez', 'Monseñor José Negro 5421'),
('Casa Ruiz', 'Bv. Las Heras 1782'),
('Casa López', 'Belgrano 2045'),
('Casa Torres', 'Ituzaingó 3412'),
('Casa Giménez', 'Av. Rivadavia 5500'),
('Casa Sánchez', 'Av. Colón 1234');

INSERT INTO Usuario (Nombre, Apellido, Email, Nombre_rol, Contrasenia) 
VALUES 
('Alvaro', 'Carmin', 'alvarocarmin@gmail.com', 'ADMIN', '421384'),
('Lucia', 'Carmin', 'luciacarmin@gmail.com', 'USUARIO', '723456'),
('Lisandro', 'Carmin', 'lisandrocarmin@gmail.com', 'ADMIN', '421384'),
('Catalina', 'Moreno', 'catalinamoreno@gmail.com', 'USUARIO', '321347'),
('Juan', 'Perez', 'juanperez@gmail.com', 'ADMIN', '123543'),
('Mario', 'Ruiz', 'marioruiz@gmail.com', 'USUARIO', '654321'),
('Sofía', 'López', 'sofialopez@gmail.com', 'USUARIO', '908070'),
('Tomás', 'Torres', 'tomastorres@gmail.com', 'ADMIN', '202122'),
('Valentina', 'Giménez', 'valegimenez@gmail.com', 'USUARIO', '543210'),
('Martina', 'Sánchez', 'martinasanchez@gmail.com', 'ADMIN', '111111');

INSERT INTO Usuario_Vivienda (ID_usuario, ID_vivienda)
VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10);

INSERT INTO Ubicacion (Nombre_ubicacion, ID_vivienda)
VALUES 
('Cocina', 1),
('Living', 1),
('Entrada', 1),
('Comedor', 2),
('Patio', 3),
('Garage', 4),
('Baño', 5),
('Dormitorio Principal', 5),
('Lavadero', 7),
('Terraza', 8),
('Living', 9),
('Comedor', 10);

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
('Barra Móvil Láser Patio', 'Spark', 'BARRA LASER', 'MUSICA', 1, 3, 5, 1),
('Luz Terraza', 'Philips', 'Hue-B22', 'LUZ', 0, 8, 10, 1),
('Camara Garage', 'Xiaomi', 'Mi Motion', 'CAMARA', 1, 4, 6, 2),
('Camara Dormitorio', 'TP-Link', 'Tapo C210', 'CAMARA', 1, 5, 8, 2),
('Altavoz Cocina', 'JBL', 'Go3', 'MUSICA', 1, 1, 1, 1),
('Luz Baño', 'Osram', 'Smart+ E27', 'LUZ', 0, 5, 7, 2);