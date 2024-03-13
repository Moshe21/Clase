create  database Maquinaria;
use  Maquinaria;

create  table TblMaquinas (
CodM varchar(3) primary key,
Nombre  varchar(20),
precio_hora int
);

create table TblConductores  (
CodC varchar(3) primary key,
Nombre  varchar(20),
localidad varchar(20),
categoría int

);

create table   TblTrabajos(
CodC varchar(3),
CodM varchar(3),
CodP varchar(3),
fecha time,
Tiempos_minutos int
);

create table TblProyectos   (
CodP varchar(3) primary key,
Descrip  varchar(20),
localidad varchar(20),
Cliente varchar(20),
Telfono int
);

ALTER TABLE TblTrabajos
ADD CONSTRAINT fk_TblTrabajos_CodM
FOREIGN KEY (CodM) REFERENCES TblMaquinas(CodM);


alter table TblTrabajos
add constraint fk_TblTrabajos_CodP
foreign key (CodP) references TblProyectos(CodP);

ALTER TABLE TblTrabajos
ADD CONSTRAINT fk_TblTrabajos_CodC
FOREIGN KEY (CodC) REFERENCES TblConductores(CodC);


insert into TblMaquinas ;
