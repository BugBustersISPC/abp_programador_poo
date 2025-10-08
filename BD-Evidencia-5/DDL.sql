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