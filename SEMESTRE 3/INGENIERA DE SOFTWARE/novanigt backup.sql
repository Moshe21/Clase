create database NOVANIGHT;
use NOVANIGHT;


------------CREACION DE TABLAS----------------------------------------------------------------------------------------

CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY,
    dni INT,
    nombre CHAR(60),
    direccion CHAR(60),
    telefono INT,
    fecha_nacimiento DATE
);

CREATE TABLE producto (
    id_producto INT PRIMARY KEY,
    codigo_producto INT,
    nombre CHAR(60),
    costo_unitario FLOAT,
    id_proveedor INT
);

CREATE TABLE proveedor (
    id_proveedor INT PRIMARY KEY,
    dni INT,
    nombre CHAR(60),
    direccion CHAR(60),
    telefono INT,
    ciudad CHAR(60),
    tipo_producto CHAR(60)
);

CREATE TABLE empleado (
    id_empleado INT PRIMARY KEY,
    nif INT,
    nombre VARCHAR(60),
    cargo VARCHAR(60),
    direccion VARCHAR(60),
    telefono INT
);
CREATE TABLE ventas (
    idventas INT PRIMARY KEY,
    cantidad INT,
    descuento INT,
    total_venta DECIMAL(10, 2),
    fecha DATE,
	id_empleado int,
	id_cliente int,
	id_producto int
);

-----------INGRESO DE DATOS-------------------------------------------------------------------------------------------

CREATE PROCEDURE insertarcliente
    @id_cliente INT,
    @dni INT,
    @nombre CHAR(60),
    @direccion CHAR(60),
    @telefono INT,
    @fecha_nacimiento DATE
AS
BEGIN
    INSERT INTO clientes (id_cliente, dni, nombre, direccion, telefono, fecha_nacimiento)
    VALUES (@id_cliente, @dni, @nombre, @direccion, @telefono, @fecha_nacimiento)
END
exec insertarcliente 01,1000,'samuel','sancipriano',3023315,'1990-05-15'
EXEC insertarcliente 101, 123456789, 'Juan Pérez', 'Calle Principal', 555123, '1990-05-15'
EXEC insertarcliente 2, 2000, 'Laura', 'Calle Principal 789', 5558889, '1993-06-25'

----------------------------------------------------------------------------------------------------------------------
CREATE PROCEDURE insertarProducto
    @id_producto INT,
    @codigo_producto INT,
    @nombre CHAR(60),
    @costo_unitario FLOAT,
    @id_proveedor INT
AS
BEGIN
    INSERT INTO producto (id_producto, codigo_producto, nombre, costo_unitario, id_proveedor)
    VALUES (@id_producto, @codigo_producto, @nombre, @costo_unitario, @id_proveedor)
END

EXEC InsertarProducto 1, 5, 'UNDIFONOS', 500.00,1
EXEC InsertarProducto 2, 3,'PROCTETOR DE CELULAR', 250.00,2

----------------------------------------------------------------------------------------------------------------------
CREATE PROCEDURE InsertarProveedor
    @id_proveedor INT,
    @dni INT,
    @nombre CHAR(60),
    @direccion CHAR(60),
    @telefono INT,
    @ciudad CHAR(60),
    @tipo_producto CHAR(60)
AS
BEGIN
    INSERT INTO proveedor (id_proveedor, dni, nombre, direccion, telefono, ciudad, tipo_producto)
    VALUES (@id_proveedor, @dni, @nombre, @direccion, @telefono, @ciudad, @tipo_producto)
END

EXEC InsertarProveedor 1, 123456789, 'Proveedor A', 'Calle Principal 123', 55517, 'Ciudad A', 'Ropa'
EXEC InsertarProveedor 2, 852396, 'Proveedor B', 'Calle 60 #42 - 13', 31427845, 'Ciudad B', 'AUDIFONOS'
EXEC InsertarProveedor 3, 456789123, 'Proveedor C', 'Calle Secundaria 789', 55543, 'Ciudad C', 'Muebles'
EXEC InsertarProveedor 4, 123456789, 'Proveedor A', 'Calle Principal 123', 55517, 'Ciudad A', 'Ropa'

----------------------------------------------------------------------------------------------------------------------
CREATE PROCEDURE InsertarEmpleado
    @id_empleado INT,
    @nif INT,
    @nombre VARCHAR(60),
    @cargo VARCHAR(60),
    @direccion VARCHAR(60),
    @telefono INT
AS
BEGIN
    INSERT INTO empleado (id_empleado, nif, nombre, cargo, direccion, telefono)
    VALUES (@id_empleado, @nif, @nombre, @cargo, @direccion, @telefono)
END

EXEC InsertarEmpleado 1, 123456789, 'Juan Pérez', 'Gerente', 'Calle Principal 123', 34567
EXEC InsertarEmpleado 2, 123456789, 'falso Juan Pérez', 'falso Gerente', 'falso Calle Principal 123', 34567
EXEC InsertarEmpleado 3, 456789123, 'Carlos Ramírez', 'Vendedor', 'Calle Secundaria 789', 21098

----------------------------------------------------------------------------------------------------------------------
CREATE PROCEDURE InsertarVenta
    @idventas INT,
    @cantidad INT,
    @descuento INT,
    @total_venta DECIMAL(10, 2),
    @fecha DATE,
    @id_empleado INT,
    @id_cliente INT,
    @id_producto INT
AS
BEGIN
    INSERT INTO ventas (idventas, cantidad, descuento, total_venta, fecha, id_empleado, id_cliente, id_producto)
    VALUES (@idventas, @cantidad, @descuento, @total_venta, @fecha, @id_empleado, @id_cliente, @id_producto)
END


EXEC InsertarVenta 1, 5, 10, 500.00, '2023-05-10', 1, 1, 1
EXEC InsertarVenta 2, 3, 5, 250.00, '2023-05-10', 2, 3, 2


----------------------------------------------------------------------------------------------------------------------
CREATE PROCEDURE sp_VerEmpleados
AS
BEGIN
    SELECT *
    FROM empleado;
END
 
 exec sp_VerEmpleados

 
----------------------------------------------------------------------------------------------------------------------

 CREATE PROCEDURE sp_ProveedorPorLetra
    @letra CHAR(1)
AS
BEGIN
    SELECT *
    FROM proveedor
    WHERE direccion LIKE @letra + '%';
END


exec sp_ProveedorPorLetra 'C'

drop procedure sp_ProveedorPorLetra
----------------------------------------------------------------------------------------------------------------------



CREATE PROCEDURE sp_DireccionPorDirreccion
    @direccion VARCHAR(60)
AS
BEGIN
       SELECT direccion
   FROM proveedor

    WHERE direccion LIKE  '%';
END


exec sp_DireccionPorDirreccion 'f'


drop procedure sp_DireccionPorDirreccion

----------------------------------------------------------------------------------------------------------------------
CREATE PROCEDURE sp_BorrarEmpleado
    @id_empleado INT
AS
    BEGIN
        DELETE FROM empleado WHERE id_empleado = @id_empleado;
       
    END


exec sp_BorrarEmpleado 2

exec sp_VerEmpleados
----------------------------------------------------------------------------------------------------------------------