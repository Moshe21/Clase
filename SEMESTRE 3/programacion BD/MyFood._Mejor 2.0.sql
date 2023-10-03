CREATE DATABASE Myfood_Mejor;
use Myfood_mejor;

/*
-------------------------------------
 0. CREACION DE TABlAS 
-------------------------------------
*/
CREATE TABLE productos (
  idProducto INT PRIMARY KEY,
  idTipoProducto INT,
  nombreProducto VARCHAR(50),
  valorVenta INT,
  cantidad int);

CREATE TABLE vendedor(
	Cedula int primary key,
	idSucursal int, 
	salario varchar(45),
    comision int,
    ventas int);

CREATE TABLE FACTURA (
	id_Factura int primary key auto_increment ,
	idProducto int,
    idTipoProducto INT,
	nombreProducto VARCHAR(50),
    valorVenta int,
	iva int , 
	valor_con_iva int);
    

  
  CREATE TABLE Stock (
  idStock INT PRIMARY KEY auto_increment,
  idProducto INT ,
  idTipoProducto INT,
  nombreProducto VARCHAR(50),
  valorVenta INT,
  iva int ,
  valor_con_iva int,
  cantidad int);  
    



insert into Stock (idStock)
values (1);
insert into factura (id_Factura)
values (1);
/*
------------------------------
0.1 VISUALIZACION DE LAS TABLAS
--------------------------------
*/

select * from productos;

select * from vendedor;
select * from factura;

/*
-------------------------------------
1. Mantener actualizado el inventario una vez se realice una venta.
---------------------------------------------
            /*
1.1 CREAR UNA TABLA PARA INSERTAR EL SEGUIMIENTO
---------------------------------------------
*/

CREATE TABLE Seguimiento(
	usuario varchar(40),
    fecha datetime, 
    idUsuarios int,
    comentario text);
select * from Seguimiento;

/*
-------------------------------------
1.2 TRIGGER CREACION DE PRODUCTOS
-------------------------------------
*/

delimiter $
	create trigger Histora_Creacion_Producto
		after insert on productos
        for each row
        begin
			insert into Seguimiento(usuario,fecha, idUsuarios,comentario)
            value (user(),now(),idUsuarios,"Se creo un Producto nuevo");
		end
$
delimiter ;
/*
1.3 TRIGGER CAMBIOS LOCOS JEJE
-------------------------------------
*/

delimiter $
	create trigger Histora_Cambios
		after update on productos
        for each row
        begin
			insert into Seguimiento(usuario,fecha, idUsuarios,comentario)
            value (user(),now(),idUsuarios,"Hubo un cambio en los Productos");
		end
$
delimiter ;


/*
-------------------------------------
3.1Calcular el valor de la factura incluyendo el iva.

3.1INGRESAR DATOS 
-------------------------------------
*/

insert into productos value (1,0011,"MANZANAS",1000,10);
insert into productos value (2,0011,"PERAS",800,4);



select * from productos;
select * from stock;
select * from factura;



/*
-------------------------------------
3.2 TRIGGER INCLUIR IVA
-------------------------------------
*/


delimiter $
	create trigger incluir_iva 
		after insert on productos
        for each row
       begin
			insert into stock (
            idProducto,
            valorVenta,
            idTipoProducto,
            nombreProducto,
            iva, 
            valor_con_iva,
            cantidad)
            Select idProducto,
			valorVenta,
			idTipoProducto,
			nombreProducto,
			valorVenta*0.19 as iva,
			valorVenta+(valorVenta*0.19) as valor_con_iva,
			cantidad
            from productos
            where idProducto>0;
		end
$
delimiter ;

insert into productos value (003,0021,"APIO",500,20);
insert into productos value (004,0021,"CALABAZA",4000,34);
insert into productos value (005,0021,"BANANO",4000,40);
select * from stock;
select * from productos;
select * from Seguimiento;
/*
-------------------------------------
4.Informes de venta o de comisiones para empleados.
---------------------------------------------

-------------------------------------
4.1 Procedimiento de factura O venta
insert into productos value
-------------------------------------
*/
delimiter $
Create Procedure Crear_Factura (	
					in ing_nombreProducto varchar(50), 
                    in ing_cantidad int)
      BEGIN
		
		IF ing_cantidad<(select cantidad
						from stock
                        where ing_nombreProducto=nombreProducto)
		then
		update factura set
			idProducto=(SELECT idProducto
						from stock
                        where ing_nombreProducto=nombreProducto),
			valorVenta=(SELECT valorVenta
						from stock
                        where ing_nombreProducto=nombreProducto),
			idTipoProducto=(SELECT idTipoProducto
							from stock
							where ing_nombreProducto=nombreProducto),
			nombreProducto=(SELECT nombreProducto						
							from stock
							where ing_nombreProducto=nombreProducto),
			iva=(SELECT valorVenta
				from stock
				where ing_nombreProducto=nombreProducto)*0.19*ing_cantidad,
			valor_con_iva=iva+(SELECT valorVenta
				from stock
				where ing_nombreProducto=nombreProducto)*ing_cantidad
			where id_Factura=1;
		else
			SELECT comentario="no hubo compra" FROM Seguimiento
            where id_Factura=1;
		end if ;	
    END
$
delimiter ;
call Crear_Factura("MANZANA",10);
            
select * from factura;
select * from stock;        
select * from productos;
/*
-------------------------------------
4.2 TRIGGER Comision_De_Venta y registro de venta
-------------------------------------
*/

delimiter $
	create trigger Comision_De_Venta
		after update on factura
        for each row
        begin
				update vendedor 
				set comision=(SELECT valorVenta
						from stock
                        where valorVenta>100)*0.10
				where (SELECT valorVenta
						from stock
                        where valorVenta>100);
                
                Insert into Seguimiento(usuario,fecha, idUsuarios,comentario)
				value (user(),now(),idUsuarios,"Se vendio una factura");
					
		end
$
delimiter ;
select * from Seguimiento


