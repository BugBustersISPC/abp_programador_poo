----------------------------
-- Practicas DDL SMARTHOME--
----------------------------

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

INSERT INTO Usuario (Nombre, Apellido, Email, Nombre_rol, Contrasenia)
VALUES 
('Alvaro', 'Carmin', 'alvarocarmin@gmail.com', 'ADMIN', '421384'),
('Lucia', 'Carmin', 'luciacarmin@gmail.com', 'USUARIO', '723456'),
('Lisandro', 'Carmin', 'lisandrocarmin@gmail.com', 'USUARIO', '421384'),
('Catalina', 'Moreno', 'catalinamoreno@gmail.com', 'USUARIO', '321347'),
('Juan', 'Perez', 'juanperez@gmail.com', 'ADMIN', '123543');

INSERT INTO Usuario_Vivienda (ID_usuario, ID_vivienda)
VALUES 
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

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
('Camara Entrada', 'Dahua', 'Cctv 1080p', 'CAMARA', 1, 1, 3, 1),
('Luz Living', 'Philips', 'Hue-A19', 'LUZ', 0, 1, 2, 2),
('Torre de Sonido Comedor', 'Noblex', 'MNT290', 'MUSICA', 0, 2, 4, 1),
('Camara Living', 'TP-Link', 'Tapo C210', 'CAMARA', 1, 1, 2, 2),
('Barra Móvil Láser Patio', 'Spark', 'BARRA LASER', 'MUSICA', 1, 3, 5, 1);

SELECT * FROM Vivienda;
SELECT * FROM Usuario;
SELECT * FROM Usuario_Vivienda;
SELECT * FROM Ubicacion;
SELECT * FROM Automatizacion;
SELECT * FROM Dispositivo;