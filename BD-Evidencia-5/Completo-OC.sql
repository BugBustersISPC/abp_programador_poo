CREATE TABLE Usuario (
    ID_usuario INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(30) NOT NULL,
    Apellido VARCHAR(30) NOT NULL,
    Email VARCHAR(40) NOT NULL UNIQUE,
    Nombre_rol VARCHAR(15) NOT NULL,
    Contraseña VARCHAR(20)
);

CREATE TABLE Vivienda (
    ID_vivienda INT PRIMARY KEY AUTO_INCREMENT,
    Direccion VARCHAR(30) NOT NULL
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
    nombre_ubicacion VARCHAR(20) NOT NULL,
    ID_vivienda INT NOT NULL,
    FOREIGN KEY (ID_vivienda) REFERENCES Vivienda(ID_vivienda)
);

CREATE TABLE Tipo_Dispositivo(
    ID_tipo INT PRIMARY KEY AUTO_INCREMENT,
    descripcion VARCHAR(50) NOT NULL
);

CREATE TABLE Dispositivo(
    ID_dispositivo INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(25) NOT NULL,
    Marca VARCHAR(15),
    Modelo VARCHAR(25),
    Estado TINYINT NOT NULL,
    ID_tipo INT NOT NULL,
    ID_usuario INT NOT NULL,
    ID_ubicacion INT NOT NULL,
    FOREIGN KEY(ID_tipo) REFERENCES Tipo_Dispositivo(ID_tipo),
    FOREIGN KEY(ID_usuario) REFERENCES Usuario(ID_usuario),
    FOREIGN KEY(ID_ubicacion) REFERENCES Ubicacion(ID_ubicacion)
);

CREATE TABLE Automatizacion(
    ID_automatizacion INT PRIMARY KEY AUTO_INCREMENT,
    accion VARCHAR(30) NOT NULL,
    estado TINYINT NOT NULL
);

CREATE TABLE Registro_Acciones(
    ID_acciones INT PRIMARY KEY AUTO_INCREMENT,
    ID_dispositivo INT NOT NULL,
    descripcion_accion VARCHAR(40),
    fecha_hora DATETIME NOT NULL DEFAULT NOW(),
    ID_automatizacion INT NOT NULL,
    FOREIGN KEY(ID_dispositivo) REFERENCES Dispositivo(ID_dispositivo),
    FOREIGN KEY(ID_automatizacion) REFERENCES Automatizacion(ID_automatizacion)
);

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