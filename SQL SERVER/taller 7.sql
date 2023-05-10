--===================================================================================================================================
--PRACTICA 5  Procedimientos Almacenados Parámetros de entrada.
--MOISES ZABALETA CRUZ 1033810224
--Email: MZABALETAC@ACADEMIA.USBBOG.EDU.CO
--================================================================================================================================


--Una empresa almacena los datos de sus empleados en una tabla llamada
--"empleados".


--1- Eliminamos la tabla, si existe y la creamos:

if object_id('empleados') is not null
 drop table empleados;

create table empleados(
 documento char(8),
 nombre varchar(20),
 apellido varchar(20),
 sueldo decimal(6,2),
 cantidadhijos tinyint,
 seccion varchar(20),
 primary key(documento));


--2- Ingrese algunos registros:

insert into empleados
values('22222222','Juan','Perez',300,2,'Contaduria');
insert into empleados
values('22333333','Luis','Lopez',300,0,'Contaduria');
insert into empleados values
('22444444','Marta','Perez',500,1,'Sistemas');
insert into empleados
values('22555555','Susana','Garcia',400,2,'Secretaria');
insert into empleados values('22666666','Jose
Maria','Morales',400,3,'Secretaria');


--3- Elimine el procedimiento llamado "pa_empleados_sueldo" si existe:

if object_id('pa_empleados_sueldo') is not null
 drop procedure pa_empleados_sueldo;

--4- Cree un procedimiento almacenado llamado "pa_empleados_sueldo" que
--seleccione los nombres,
--apellidos y sueldos de los empleados que tengan un sueldo superior o
--igual al enviado como
--parámetro.

CREATE proc  pa_empleados_sueldo
@sueldo decimal(6,2)
AS
SELECT nombre,apellido,sueldo
FROM Empleados
WHERE sueldo >=@sueldo;



--5- Ejecute el procedimiento creado anteriormente con distintos valores:

exec pa_empleados_sueldo 400;
exec pa_empleados_sueldo 500;


--6- Ejecute el procedimiento almacenado "pa_empleados_sueldo" sin
--parámetros.
--Mensaje de error.

exec pa_empleados_sueldo;


--7- Elimine el procedimiento almacenado "pa_empleados_actualizar_sueldo"
--si existe:

if object_id('pa_empleados_actualizar_sueldo') is not null
drop procedure pa_empleados_actualizar_sueldo;

--8- Cree un procedimiento almacenado llamado
--"pa_empleados_actualizar_sueldo" que actualice los
--sueldos iguales al enviado como primer parámetro con el valor enviado
--como segundo parámetro.

create proc pa_empleados_actualizar_sueldo
@sueldo decimal(6,2),
@sueldo_nuevo decimal(6,2)

AS
update empleados set sueldo=@sueldo_nuevo
where sueldo=@sueldo



--9- Ejecute el procedimiento creado anteriormente y verifique si se ha
--ejecutado correctamente:


exec pa_empleados_actualizar_sueldo 300,350;

select * from empleados;

--10- Ejecute el procedimiento "pa_empleados_actualizar_sueldo" enviando un
--solo parámetro.
--Error.

exec pa_empleados_actualizar_sueldo 350;

select * from empleados;


--11- Ejecute el procedimiento almacenado "pa_empleados_actualizar_sueldo"
--enviando en primer lugar el
--parámetro @sueldonuevo y en segundo lugar @sueldoanterior (parámetros por
--nombre).

exec pa_empleados_actualizar_sueldo @sueldo_nuevo=375, @sueldo=350;

--12- Verifique el cambio:

select * from empleados;


--13- Elimine el procedimiento almacenado "pa_sueldototal", si existe:

if object_id('pa_sueldototal') is not null
 drop procedure pa_sueldototal;


--14- Cree un procedimiento llamado "pa_sueldototal" que reciba el
--documento de un empleado y muestre
--su nombre, apellido y el sueldo total (resultado de la suma del sueldo y
--salario por hijo, que es de
--$200 si el sueldo es menor a $500 y $100, si el sueldo es mayor o igual a
--$500). Coloque como valor
--por defecto para el parámetro el patrón "%".

create proc  pa_sueldototal
@documento char(8)='%'

as
SELECT nombre,apellido, 
case 
	when sueldo<500 then sueldo+(cantidadhijos*200)
	else sueldo+(cantidadhijos*100)
	end as sueldo_total 

FROM Empleados
where documento like @documento;
go




--15- Ejecute el procedimiento anterior enviando diferentes valores:

exec pa_sueldototal '22333333';
exec pa_sueldototal '22444444';
exec pa_sueldototal '22666666';

--16- Ejecute el procedimiento sin enviar parámetro para que tome el valor
--por defecto.
--Muestra los 5 registros

create proc pa_sueldototal_todos
@documento char(8)='%'

as
SELECT nombre,apellido, 
case 
	when sueldo<500 then sueldo+(cantidadhijos*200)
	else sueldo+(cantidadhijos*100)
	end as sueldo_total 

FROM Empleados
where documento like @documento;
select *from empleados

go


exec pa_sueldototal_todos;
