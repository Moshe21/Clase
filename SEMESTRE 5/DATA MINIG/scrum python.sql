create database python_clase;
use python_clase;

-- C create
create table mesa_dato(
id int auto_increment primary key,
nomb varchar(50),
cel int
);


-- R realy
select * from mesa_dato;

-- U update 
insert into mesa_dato value(200,"hello world",1234567);

-- D dalete
delete from mesa_dato
where
id= 100;