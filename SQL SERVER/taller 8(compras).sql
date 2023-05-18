create database EducandoBD;
use EducandoBD;


create table solicitud(
N_solicitud varchar (4),
fecha date,
nombre varchar(40)
apellido varchar (40),
C_costos varchar(4)
C_presupuesto int,
primary key (N_solicitud)
);

create table item(
Item varchar (4),
N_producto varchar(40),
cantidad int,
U_medida varchar (40),
valor_U int,
valor_T int,

primary key (Item)
);

create table proveedor(
nit varchar(10),
nombre_p varchar(20),
