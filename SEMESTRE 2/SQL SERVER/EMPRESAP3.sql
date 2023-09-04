create database empresa_P3;
use empresa_P3;


CREATE TABLE categoria (
cat_id int PRIMARY KEY,
cat_nombre VARCHAR(30) NOT NULL,
cat_descripcion VARCHAR(50) NOT NULL,
cat_imagen image );


CREATE TABLE proveedor (
pro_id int PRIMARY KEY,
pro_cia VARCHAR(30) NOT NULL,
pro_titulo VARCHAR(50),
pro_dir VARCHAR(50),
pro_ciudad VARCHAR(40),
pro_region VARCHAR(30),
pro_codigoPostal VARCHAR(10),
pro_pais VARCHAR(30),
pro_tlf VARCHAR(60),
pro_fax VARCHAR(40),
pro_pagina VARCHAR(100) );CREATE TABLE articulo (
art_id int PRIMARY KEY,
art_nombre VARCHAR(30) NOT NULL,
pro_id int NOT NULL,
cat_id int NOT NULL,
art_cant_por_und int,
art_pu money NOT NULL,
art_stock int,
art_und_en_ordenes int,
art_nivel_para_ordenar int,
art_descontinuado bit,
FOREIGN KEY (pro_id) REFERENCES proveedor (pro_id),
FOREIGN KEY (cat_id) REFERENCES categoria (cat_id)); 

CREATE TABLE cliente (
cli_id int PRIMARY KEY,
cli_cc VARCHAR(30) NOT NULL,
cli_nom VARCHAR(50),
cli_dir VARCHAR(50),
cli_ciudad VARCHAR(40),
cli_region VARCHAR(30),
cli_codigoPostal VARCHAR(10),
cli_pais VARCHAR(30),
cli_tlf VARCHAR(60));


CREATE TABLE orden(
ord_id int PRIMARY KEY,
ord_num int NOT NULL,
ord_nom_item VARCHAR(50) NOT NULL,
ord_stock int NOT NULL,
cli_id int NOT NULL,
FOREIGN KEY (cli_id) REFERENCES cliente(cli_id));

CREATE TABLE info_orden (
inf_id int PRIMARY KEY,
inf_detalle VARCHAR(50),
ord_id int,
art_id int,
FOREIGN KEY (ord_id) REFERENCES orden(ord_id));
FOREIGN KEY (art_id) REFERENCES articulo(art_id));
);

--1. Realizar un procedimiento almacenado que devuelva los clientes
--(Customers) según el país (Country).

create proc datos_categoria
@cat_id int, 
@cat_nombre VARCHAR(30),
@cat_descripcion VARCHAR(50), 
@cat_imagen image
as
insert into categoria values
(@cat_id, 
@cat_nombre,
@cat_descripcion, 
@cat_imagen)

--1. Realizar un procedimiento almacenado que devuelva los clientes
--(Customers) según el país (Country).

create proc datos_cliente
@cli_pais VARCHAR(30)

as
select cli_nom,cli_pais
from cliente
where cli_pais=@cli_pais;

--2. Crear un procedimiento que determine la cantidad de clientes cuyo


CREATE PROCEDURE cant_cliente
 @cli_id int,
  @contador INT OUTPUT
AS
  SELECT @contador = COUNT(*) 
  FROM Cliente
  WHERE LEFT(cli_id, 1) = @cli_id ;

--3. Realizar un procedimiento que determine la cantidad de veces que un
--cliente está en la tabla ORDENES.


CREATE PROCEDURE pedido_Cliente
  @cli_id int,
  @contador INT OUTPUT
AS
  SELECT @contador = COUNT(*) 
  FROM Orden 
  WHERE cli_id = @cli_id;

 --4. Realizar un procedimiento que seleccione todos los registros de tabla
--Productos y Categorías a la vez.
CREATE PROCEDURE ProductosCategorias
AS
SELECT * FROM Articulo
FULL JOIN Categoria ON Articulo.cat_id = Categoria.cat_id;

EXEC ProductosCategorias

--5. Realizar un procedimiento que seleccione todos los productos que no
--corresponde a la categoría bebidas (1)
CREATE PROCEDURE NoBebidas
AS
  SELECT * FROM Articulo WHERE cat_id != 1;

  EXEC NoBebidas


--6. Realizar un procedimiento que obtenga la cantidad de registros que no
--corresponde a condimentos
CREATE PROCEDURE Prod_No_Condimentos
  @cantidad INT OUTPUT
AS

  SELECT @cantidad = COUNT(*) FROM Articulo WHERE cat_id <> 2;

  --7. Realizar un procedimiento que seleccionar todos los campos de los
--registros que no corresponden a categoría mariscos de la tabla
--productos.

CREATE PROCEDURE Prod_No_Mar
AS

  SELECT * FROM Articulo WHERE cat_id <> 3;

--8. Realizar un procedimiento que seleccionar los campos nombre del
--producto y precio (únicamente) de los productos diferentes a carnes.

  CREATE PROCEDURE Prod_No_Carne
AS

  SELECT art_nombre, art_pu FROM Articulo WHERE cat_id <> 4;

