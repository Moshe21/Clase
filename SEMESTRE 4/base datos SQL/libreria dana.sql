create database prueba1;
use prueba1;

create table tblibros(
id int auto_increment  primary key,
titulo varchar (255), 
autor varchar(50),
disponible boolean
);

create table tblprestamos (
id int auto_increment primary key,
id_libro int,
fecha_prestamo date,
fecha_de_devolucion date,
foreign key(id_libro)references tblibros(id)
);
insert into tblibros(titulo,autor,disponible)
values ('el rey leon','sanchez',true),('el barco','garcia',true),('el avion','perez',true);

select*from tblibros;

delimiter //

create procedure sp_realizar_prestamo(
in libro_id int,
out mensaje varchar(255)
)

begin
declare disponible_actual boolean;
select disponible into disponible_actual from 
tblibros where id = libro_id;
if disponible_actual = true then 
update tblibros set disponible = false
where id = libro_id;
insert into tblprestamos ( id_libro,fecha_prestamo)
values(libro_id, curdate());
set mensaje = 'prestamo autorizado, devuelvalo pronto';
else set mensaje = 'prestamo no autorizado';
end if;
end //


delimiter ;

call sp_realizar_prestamo(1,@mensaje)
select @mensaje;