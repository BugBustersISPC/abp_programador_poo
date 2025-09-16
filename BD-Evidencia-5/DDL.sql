----------------------------
-- Practicas DDL SMARTHOME--
----------------------------

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
    Estado TINYINT(1) NOT NULL,
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
    estado TINYINT(1) NOT NULL
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
