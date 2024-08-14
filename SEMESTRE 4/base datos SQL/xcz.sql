create database bdtest;
use bdtest;

create table tblibro(
id int auto_increment primary key,
titulo varchar(30),
autor varchar(30),
disponible bool
);

create table tblprestamo(
id int auto_increment primary key,
id_libro int,
fecha_prestamo date,
fecha_devolucion date,
foreign key (id_libro) references tblibros(id)
);

insert into tblibro (titulo, autor, disponible)
value("el rey leon","sanchez", true),
	  ("el barco","garcia",true),
      ("el tunel" , "perez",true);
      
select* from tblibro;
      
      
      
delimiter //
create procedure prestamo_realizado(
 in id_libro int,
 out mensaje varchar(30)
)


begin
	declare disponoble_actual boolean;
    select disponible into disponoble_actual from
    tblibro where id=id_libro;
    if disponoble_actual = true then 
      update tblibro set disponible = false where id=id_libro;
      
      
      insert into tblprestamo (id_libro,fecha_prestamo,fecha_devolucion)
      values (libro_id,curdate());
		
        set mensaje="Prestamo autorizado, devuelvalo pronto";
	else
		set mensaje="Prestamo NO autorizado, se encuentra en prestamo";
    end if;
end//

delimiter ;

call prestamo_realizado(2,@mensaje);
select @mensaje;