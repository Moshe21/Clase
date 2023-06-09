CREATE DATABASE SISTEMA_VENTAS

CREATE TABLE CLIENTE(CUIT INT PRIMARY KEY NOT NULL,
					NOMBRE VARCHAR(30),
					TELEFONO INT, 
					DIRECCION VARCHAR(60))

ALTER TABLE CLIENTE ADD NRO_FACTURA INT

ALTER TABLE CLIENTE ADD
					CONSTRAINT FK_CLIENTE_VENTAS  
					FOREIGN KEY(NRO_FACTURA)
					REFERENCES VENTA(NRO_FACTURA);

CREATE TABLE VENTA(NRO_FACTURA INT PRIMARY KEY NOT NULL,
					DESCUENTO INT,
					FECHA DATE, 
					MONTOFINAL INT )

CREATE TABLE PRODUCTO(ID_PRODUCTO INT PRIMARY KEY NOT NULL,
					NOMBRE VARCHAR (30),
					STOCK INT, 
					PRECIO INT)

CREATE TABLE PROVEEDOR(CUIT INT PRIMARY KEY NOT NULL,
					NOMBRE VARCHAR (30),
					WEB VARCHAR (90), 
					TELEFONO INT)

ALTER TABLE PROVEEDOR ADD ID_PRODUCTO INT

ALTER TABLE PROVEEDOR ADD
					CONSTRAINT FK_PROVEEDOR_PRODUCTO  
					FOREIGN KEY(ID_PRODUCTO)
					REFERENCES PRODUCTO(ID_PRODUCTO);


CREATE TABLE CATEGORIA(ID_CATEGORIA INT PRIMARY KEY NOT NULL,
					NOMBRE VARCHAR (30),
					DESCRIPCION CHAR)

ALTER TABLE CATEGORIA ADD ID_PRODUCTO INT

ALTER TABLE CATEGORIA ADD
					CONSTRAINT FK_CATEGORIA_PRODUCTO  
					FOREIGN KEY(ID_PRODUCTO)
					REFERENCES PRODUCTO(ID_PRODUCTO);

CREATE TABLE PARTICIPA(ID_PARTICIPA INT PRIMARY KEY NOT NULL)

ALTER TABLE PARTICIPA ADD PRECIO_UNIDAD INT,
							MONTOTOTALPRODUCTO INT, 
							CANTIDAD_VTA_UNIDAD INT
					
ALTER TABLE PARTICIPA ADD NRO_FACTURA INT
ALTER TABLE PARTICIPA ADD ID_PRODUCTO INT

ALTER TABLE PARTICIPA ADD
					CONSTRAINT FK_PARTICIPA_VENTAS  
					FOREIGN KEY(NRO_FACTURA)
					REFERENCES VENTA(NRO_FACTURA);