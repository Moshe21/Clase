
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

create table empleados(
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
primary key(codigo_pac));-- 6- creaciobn de la tabla horarioscreate  table horario(
codigo_hor int identity,
fecha_ing datetime,
fecha_ret datetime,
primary key(codigo_hor));--7- union de tablas ALTER TABLE  horario add CONSTRAINT FK_med_pac FOREIGN KEY (codDepto) REFERENCES Departamento(codDepto);