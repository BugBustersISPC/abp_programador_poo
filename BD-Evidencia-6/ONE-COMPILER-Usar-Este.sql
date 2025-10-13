CREATE TABLE Usuario (
    ID_usuario INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(30) NOT NULL,
    Apellido VARCHAR(30) NOT NULL,
    Email VARCHAR(40) NOT NULL UNIQUE,
    Nombre_rol ENUM('USUARIO', 'ADMIN') NOT NULL,
    Contrasenia VARCHAR(100) NOT NULL
);

CREATE TABLE Vivienda (
    ID_vivienda INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(30) NOT NULL,
    Direccion VARCHAR(50) NOT NULL
);

CREATE TABLE Usuario_Vivienda (
    ID_usuario INT NOT NULL,
    ID_vivienda INT NOT NULL,
    PRIMARY KEY (ID_usuario, ID_vivienda),
    FOREIGN KEY (ID_usuario) REFERENCES Usuario(ID_usuario),
    FOREIGN KEY (ID_vivienda) REFERENCES Vivienda(ID_vivienda)
);

CREATE TABLE Ubicacion (
    ID_ubicacion INT PRIMARY KEY AUTO_INCREMENT,
    Nombre_ubicacion VARCHAR(30) NOT NULL,
    ID_vivienda INT NOT NULL,
    FOREIGN KEY (ID_vivienda) REFERENCES Vivienda(ID_vivienda)
);

CREATE TABLE Automatizacion (
    ID_automatizacion INT PRIMARY KEY AUTO_INCREMENT,
    Accion VARCHAR(30) NOT NULL,
    Estado TINYINT(1) NOT NULL
);

CREATE TABLE Dispositivo (
    ID_dispositivo INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(25) NOT NULL,
    Marca VARCHAR(15),
    Modelo VARCHAR(25),
    Tipo ENUM('LUZ', 'CAMARA', 'MUSICA') NOT NULL,
    Estado TINYINT(1) NOT NULL,
    ID_usuario INT NOT NULL,
    ID_ubicacion INT NOT NULL,
    ID_automatizacion INT,
    FOREIGN KEY (ID_usuario) REFERENCES Usuario(ID_usuario),
    FOREIGN KEY (ID_ubicacion) REFERENCES Ubicacion(ID_ubicacion),
    FOREIGN KEY (ID_automatizacion) REFERENCES Automatizacion(ID_automatizacion)
);

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


SELECT * FROM automatizacion;

SELECT Nombre, Tipo, Estado, ID_ubicacion, ID_automatizacion FROM dispositivo;

SELECT * FROM ubicacion;

SELECT Nombre, Apellido, Nombre_rol FROM usuario;

SELECT * FROM usuario_vivienda;

SELECT Nombre, Direccion FROM vivienda;

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

SELECT * FROM Vivienda;
SELECT * FROM Usuario;
SELECT * FROM Usuario_Vivienda;
SELECT * FROM Ubicacion;
SELECT * FROM Automatizacion;
SELECT * FROM Dispositivo;