create database vehiculo;
use vehiculo;
create  table peajes (
id_peajes int primary key auto_increment,
 ciudad Varchar(50), 
 tipo_de_vehiculo varchar (50), 
 precio int,
 entrado int,
 saliendo int,
 contador int,
 total_vehiculo int);


INSERT INTO peajes (Ciudad, Tipo_de_Vehiculo, Precio, entrado, saliendo,
 contador, total_vehiculo)
VALUES
('Bogotá', 'Vehículos familiares', 12000,0,0,0,0),
('Bogotá', 'Camión', 60000,0,0,0,0),
('Bogotá', 'Tracto Camión', 150000,0,0,0,0),
('Bogotá', 'Motos', 8500,0,0,0,0),
('Medellín', 'Vehículos familiares',  11000,0,0,0,0),
('Medellín', 'Camión', 50000,0,0,0,0),
('Medellín', 'Tracto Camión', 130000,0,0,0,0),
('Medellín', 'Motos', 6500,0,0,0,0),
('Cali', 'Vehículos familiares', 12500,0,0,0,0),
('Cali', 'Camión', 70000,0,0,0,0),
('Cali', 'Tracto Camión', 145000,0,0,0,0),
('Cali', 'Motos', 9000,0,0,0,0),
('Tunja', 'Vehículos familiares',11500,0,0,0,0),
('Tunja', 'Camión', 80000,0,0,0,0),
('Tunja', 'Tracto Camión', 170000,0,0,0,0),
('Tunja', 'Motos', 10000,0,0,0,0);

select *,contador*precio as total_vehiculo  from peajes where ciudad= "bogota";

select *,entrado*precio as total_vehiculo  from peajes;

select *,saliendo*precio as total_vehiculo  from peajes;

update peajes set total_vehiculo= contador*precio where ciudad = 'Bogotá'; 
                       

select * from peajes;


/*update peajes 
set contador=contador+1
where ciudad="Bogotá" and  tipo_de_vehiculo = 'Vehículos familiares';
*/
select * from peajes
where ciudad = "Medellìn";

create table registro_ingreso_peajes ( 
 id_registro int primary key,
 ciudad Varchar(50), 
 tipo_de_vehiculo varchar (50), 
 cantidad int,
 id_peajes int,
 CONSTRAINT id_peajes FOREIGN KEY (id_peajes)
 REFERENCES registro_ingreso_peajes(id_registro)
);

select Ciudad, id_peajes, Tipo_de_Vehiculo,precio* contador as total
from Peajes
where ciudad = ing_dato_profe ;

 
 

