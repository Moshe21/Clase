
--1- Creacion de base de datos
create database Tu_cita_med;


--2- usar la base de datos

use Tu_cita_med;

-- 3- creaciobn de la tabla medico

create table medico(
codigo_med int identity,
nombre varchar(30),
direcci�n varchar(30),
tel�fono varchar(10),
poblaci�n varchar(20),
providencia varchar(20),
cod_postal varchar(8),
nif varchar(10),
num_seguridad varchar(11),
num_colegiatura varchar(12),
titular varchar(2),
primary key(codigo_med)
-- 4- creaciobn de la tabla empleados

create drop table empleados(
codigo_emp int identity,
nombre varchar(30),
direcci�n varchar(30),
tel�fono varchar(10),
poblaci�n varchar(20),
providencia varchar(20),
cod_postal varchar(8),
nif varchar(10),
num_seguridad varchar(11),
cargo varchar(30),
primary key(codigo_emp)

create table paciente(
codigo_pac int identity,
nombre varchar(30),
direcci�n varchar(30),
tel�fono varchar(10),
cod_postal varchar(8),
nif varchar(10),
num_seguridad varchar(11),
med_responsable varchar(30),
primary key(codigo_pac)
codigo_hor int identity,
fecha_ing datetime,
fecha_ret datetime,
codigo_med int,
primary key(codigo_hor)
codigo_citas int identity,
fecha_citas date,
codigo_pac int,
codigo_med int,
primary key(codigo_citas)
codigo_vac int identity,
dias_vac varchar(2),
fecha_inicio date,
fecha_Fin date,
codigo_emp int,
codigo_med int,
primary key(codigo_vac)
@nombre varchar(30),
@direcci�n varchar(30),
@tel�fono varchar(10),
@poblaci�n varchar(20),
@providencia varchar(20),
@qcod_postal varchar(8),
@nif varchar(10),
qnum_seguridad varchar(11),
@num_colegiatura varchar(12),
@titular varchar(2),
