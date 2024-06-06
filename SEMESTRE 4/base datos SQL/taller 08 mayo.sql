create database taller_8_mayo;
use taller_8_mayo;

-- Procedimiento 1 Estudiantes

create table estudiantes(
id_estudiante int primary key auto_increment,
id_notas int,
nombre varchar (30),
foreign key (id_notas) references notas(id_notas)
);

create table notas(
id_notas int primary key auto_increment,
id_estudiante int,
notas int
);

INSERT INTO estudiantes (nombre) VALUES 
('Juan Pérez'),
('María González'),
('Carlos Rodríguez'),
('Ana Martínez'),
('Luisa Sánchez');



INSERT INTO notas (id_estudiante, notas) VALUES
(1, 85),
(1, 90),
(1, 88),
(2, 92),
(2, 89),
(2, 94),
(3, 78),
(3, 85),
(3, 80),
(4, 89),
(4, 92),
(4, 87),
(5, 95),
(5, 91),
(5, 93);



select sum(notas)/count(*) as promedio from notas where id_estudiante=id_estudiante;
select  notas from notas where id_estudiante=1;

delimiter //

create procedure calcular_promedio_notas(in id_estudiante int)
	
begin 	
	select sum(notas)/count(*) as promedio from notas where id_estudiante=id_estudiante;
end//
delimiter ;

call calcular_promedio_notas (2);

-- procedure de ingresar empleado con su departamento 


CREATE TABLE Empleados(
    id_Empleados INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(60),
    departamento VARCHAR(60)
);

DELIMITER //

CREATE PROCEDURE agregar_empleado(
    IN p_nombre VARCHAR(100),
    IN p_departamento VARCHAR(100)
)
BEGIN
    INSERT INTO Empleados (nombre, departamento) VALUES (p_nombre, p_departamento);
    SELECT * FROM Empleados;
END//

DELIMITER ;

call agregar_empleado ("andres","santander");


CREATE TABLE Producto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100)
);

CREATE TABLE Cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100)
);

CREATE TABLE Compras (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_producto varchar(30),
    nombre_cliente varchar(30),
    producto_id INT,
    cliente_id INT,
    cantidad INT,
    FOREIGN KEY (producto_id) REFERENCES Producto(id),
    FOREIGN KEY (cliente_id) REFERENCES Cliente(id)
);
INSERT INTO Producto (nombre) VALUES 
('Camisa'),
('Pantalón'),
('Zapatos');

INSERT INTO Cliente (nombre) VALUES 
('Juan Pérez'),
('María García'),
('Luis González');

DELIMITER //

CREATE PROCEDURE realizar_compra(
     IN nombre_producto VARCHAR(100),
    IN nombre_cliente VARCHAR(100),
    IN cantidad INT
)
BEGIN
    -- Insertar la compra en la tabla Compras
    INSERT INTO Compras (nombre_producto, nombre_cliente,cantidad) VALUES (nombre_producto, nombre_cliente, cantidad);

    -- Obtener los detalles de la compra insertada
    SELECT * from Compras;
END//

DELIMITER ;

CALL realizar_compra('Camisa', 'Juan Pérez', 2);
CALL realizar_compra('Pantalón', 'María García', 3);
CALL realizar_compra('Zapatos', 'Luis González', 1);




