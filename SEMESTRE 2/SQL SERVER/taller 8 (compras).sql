-=================================================================================================================================== 
--PRACTICA 8 DE LENGUAJE ESTRUCTURADO SQL ("Educando S.A")
--MOISES ZABALETA CRUZ
--1033810224
--Email: MZABALETAC@ACADEMIA.USBBOG.EDU.CO
--================================================================================================================================ 

create database EducandoBD2;
use EducandoBD2;

create table Item(
N_item varchar (4),
Nom_producto varchar(40),
cantidad int,
U_medida varchar (40),
V_unidad int,
V_total int,

primary key (N_item)
);

create table proveedor(
N_pedido varchar(10),
nit varchar(10),
Nom_proveedor varchar(20),
F_orden date,
T_orden int,
F_entrega date,
N_item varchar (4),
primary key (n_pedido)
);

-- aprobada por el Director Financiero

create table factura(
N_factura varchar(10),
N_Entrada varchar(10),
F_factura date,
N_pedido varchar(10),
N_item varchar (4),
primary Key (N_factura)
);


create table solicitud(
N_solicitud varchar (10),
T_solicitud int,
F_solicitud date,
nombre varchar(40),
apellido varchar (40),
cargo varchar(60),
C_costos int,
C_presupuesto int,
T_salida int,
F_salida date,
T_entrega int,
F_entrega date,
direccion varchar(60),
N_pedido varchar(10),
N_item varchar (4),
primary key (N_solicitud)
);

alter table proveedor	
	add constraint fk_proveedor_item
	foreign key (N_item) 
	references  item(N_item);

alter table factura	
	add constraint fk_factura_item
	foreign key (N_item) 
	references  item(N_item);

alter table solicitud	
	add constraint fk_solicitud_proveedor
	foreign key (N_pedido) 
	references  proveedor(N_pedido);

alter table solicitud	
	add constraint fk_solicitud_item
	foreign key (N_item) 
	references  item(N_item);



