use rcc;

create table tecnicos(
id int auto_increment,
nombre varchar(255),
cc int,
cuenta varchar(255),
banco varchar(255),
primary key(id)
);

show tables;

insert into tecnicos (nombre, cc, cuenta, banco) values 
('ROGER SUAREZ','10781141','0987654321','BANCOLOMBIA');

insert into tecnicos (nombre, cc, cuenta, banco) values 
('ROGER SUAREZ','10781141','3142142255','DAVIPLATA');

insert into tecnicos (nombre, cc, cuenta, banco) values 
('GUSTAVO PAREJO','1129581990','3209613583','DAVIPLATA');

select * from tecnicos;

select * from tecnicos where banco = 'DAVIPLATA';

create table seguimiento(
cliente varchar(255),
ot int,
gestor_rcc varchar(255)
);

select * from seguimiento;

select cliente from seguimiento where ot = 15966;

insert into seguimiento (cliente, ot, gestor_rcc) 
values ('BANCO DE BOGOTA',15966,'GABRIEL');

insert into seguimiento (cliente, ot, gestor_rcc) 
values ( 42394560,'BBVA','GABRIEL');

drop table seguimiento;