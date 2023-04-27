
--1- Creacion de base de datos
create database Tu_cita_med;


--2- usar la base de datos

use Tu_cita_med;

-- 3- creaciobn de la tabla medico

create table medico(
codigo_med int identity,
nombre varchar(30),
dirección varchar(30),
teléfono varchar(10),
población varchar(20),
providencia varchar(20),
cod_postal varchar(8),
nif varchar(10),
num_seguridad varchar(11),
num_colegiatura varchar(12),
titular varchar(2),
primary key(codigo_med));
-- 4- creaciobn de la tabla empleados

create drop table empleados(
codigo_emp int identity,
nombre varchar(30),
dirección varchar(30),
teléfono varchar(10),
población varchar(20),
providencia varchar(20),
cod_postal varchar(8),
nif varchar(10),
num_seguridad varchar(11),
cargo varchar(30),
primary key(codigo_emp));-- 5- creaciobn de la tabla empleados

create table paciente(
codigo_pac int identity,
nombre varchar(30),
dirección varchar(30),
teléfono varchar(10),
cod_postal varchar(8),
nif varchar(10),
num_seguridad varchar(11),
med_responsable varchar(30),
primary key(codigo_pac));-- 6- creaciobn de la tabla horarioscreate table horario(
codigo_hor int identity,
fecha_ing datetime,
fecha_ret datetime,
codigo_med int,
primary key(codigo_hor));--7- union de tablas medico y horarioALTER TABLE  horario add CONSTRAINT FK_med_pac FOREIGN KEY (codigo_med) REFERENCES medico(codigo_med);-- 8- creacion de la tabla citascreate table citas(
codigo_citas int identity,
fecha_citas date,
codigo_pac int,
codigo_med int,
primary key(codigo_citas));--9- union de tablas medico, citas y pacientesALTER TABLE  citas add CONSTRAINT FK_cita_pac FOREIGN KEY (codigo_med) REFERENCES medico(codigo_med);ALTER TABLE  citas add CONSTRAINT FK_citas_pac FOREIGN KEY (codigo_pac) REFERENCES paciente(codigo_pac);-- 8- creacion de la tabla vacacionescreate table vacaciones(
codigo_vac int identity,
dias_vac varchar(2),
fecha_inicio date,
fecha_Fin date,
codigo_emp int,
codigo_med int,
primary key(codigo_vac));--9- union de tablas medico, vacaciones y empleadosALTER TABLE  vacaciones add CONSTRAINT FK_vac_med FOREIGN KEY (codigo_med) REFERENCES medico(codigo_med);--10- union de tablas medico y empleadosALTER TABLE empleados add  codigo_med int;ALTER TABLE empleados add CONSTRAINT FK_empl_med FOREIGN KEY (codigo_med) REFERENCES medico(codigo_med);--11- creacion procCREATE proc crear usuasrios@codigo_med int identity,
@nombre varchar(30),
@dirección varchar(30),
@teléfono varchar(10),
@población varchar(20),
@providencia varchar(20),
@qcod_postal varchar(8),
@nif varchar(10),
qnum_seguridad varchar(11),
@num_colegiatura varchar(12),
@titular varchar(2),
