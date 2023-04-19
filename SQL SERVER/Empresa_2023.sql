create database Empresa_2023;
use Empresa_2023;
-- Creación de la tabla Departamento


CREATE TABLE Departamento (
codDepto varchar (4) PRIMARY KEY,
nombreDpto varchar (20) NOT NULL,
ciudad varchar (15),
codDirector varchar (12));

-- Creación de la tabla empleados
if object_id('Empleado') is not null drop table Empleado;

CREATE TABLE Empleado (
nDIEmp VARCHAR( 12 ) NOT NULL PRIMARY KEY,
nomEmp VARCHAR( 30 ) NOT NULL ,
sexEmp CHAR( 1 ) NOT NULL CHECK (sexEmp IN ('F', 'M') ),
fecNac DATE NOT NULL ,
fecIncorporacion DATE NOT NULL,
salEmp FLOAT NOT NULL,
comisionE FLOAT NOT NULL,
cargoE VARCHAR( 15 ) NOT NULL,
jefeID VARCHAR( 12 ),
codDepto VARCHAR( 4 ) NOT NULL);

-- Declaración de las llaves foráneas
ALTER TABLE Empleado add CONSTRAINT FK_Empl FOREIGN KEY (jefeID) REFERENCES Empleado

ALTER TABLE Empleado add CONSTRAINT FK_Dpto FOREIGN KEY (codDepto) REFERENCES Departamento(codDepto);

--Inserción de datos en la tabla Departamento:
INSERT INTO Departamento (codDepto, nombreDpto, ciudad, codDirector) VALUES
('1000', 'GERENCIA',		'CALI',		'31.840.269'),
('1500', 'PRODUCCIÓN',		'CALI',		'16.211.383'),
('2000', 'VENTAS',			'CALI',		'31.178.144'),
('2100', 'VENTAS',			'POPAYAN',	'31.751.219'),
('2200', 'VENTAS',			'BUGA',		'768.782'),
('2300', 'VENTAS',			'CARTAGO',	'737.689'),
('3000', 'INVESTIGACIÓN',	'CALI',		'16.759.060'),
('3500', 'MERCADEO',		'CALI',		'22.222.222'),
('4000', 'MANTENIMIENTO',	'CALI',		'333.333.333'),
('4100', 'MANTENIMIENTO',	'POPAYAN',	'888.888'),
('4200', 'MANTENIMIENTO',	'BUGA',		'11.111.111'),		
('4300', 'MANTENIMIENTO',	'CARTAGO',	'444.444');

INSERT INTO Empleado (nDIEmp, nomEmp, sexEmp, fecNac, fecIncorporacion, salEmp,
comisionE, cargoE, jefeID, codDepto)
VALUES
('31.840.269', 'María Rojas', 'F', '1959-01-15', '1990-05-16', 6250000, 1500000,'Gerente', NULL, '1000'),
('16.211.383', 'Luis Pérez', 'M', '1956-02-25', '2000-01-01', 5050000, 0,'Director', '31.840.269', '1500'),
('31.178.144', 'Rosa Angulo', 'F', '1957-03-15', '1998-08-16', 3250000, 3500000,'Jefe Ventas', '31.840.269', '2000'),
('16.759.060', 'Darío Casas', 'M', '1960-04-05', '1992-11-01', 4500000, 500000,'Investigador', '31.840.269', '3000'),
('22.222.222', 'Carla López', 'F', '1975-05-11', '2005-07-16', 4500000, 500000,'Jefe Mercadeo', '31.840.269', '3500'),
('22.222.333', 'Carlos Rozo', 'M', '1975-05-11', '2001-09-16', 750000, 500000,'Vigilante', '31.840.269', '3500') ,
('1.751.219', 'Melissa Roa', 'F', '1960-06-19', '2001-03-16', 2250000, 2500000,'Vendedor', '31.178.144', '2100'),
('768.782', 'Joaquín Rosas', 'M', '1947-07-07', '1990-05-16', 2250000, 2500000,'Vendedor', '31.178.144', '2200'),
('737.689', 'Mario Llano', 'M', '1945-08-30', '1990-05-16', 2250000, 2500000,'Vendedor', '31.178.144', '2300'),
('333.333.333', 'Elisa Rojas', 'F', '1979-09-28', '2004-06-01', 3000000, 1000000,'Jefe Mecánicos', '31.840.269', '4000'),
('888.888', 'Iván Duarte', 'M', '1955-08-12', '1998-05-16', 1050000, 200000,'Mecánico', '333.333.333', '4100'),
('11.111.111', 'Irene Díaz', 'F', '1979-09-28', '2004-06-01', 1050000, 200000,'Mecánico', '333.333.333', '4200'),
('444.444', 'Abel Gómez', 'M', '1939-12-24', '2000-10-01', 1050000, 200000,'Mecánico', '333.333.333', '4300'),
('1.130.222', 'José Giraldo', 'M', '1985-01-20', '2000-11-01', 1200000, 400000,'Asesor', '22.222.222', '3500'),
('19.709.802', 'William Daza', 'M', '1982-10-09', '1999-12-16', 2250000,1000000,'Investigador', '16.759.060', '3000'),
('31.174.099', 'Diana Solarte', 'F', '1957-11-19', '1990-05-16', 1250000, 500000,'Secretaria', '31.840.269', '1000'),
('1.130.777', 'Marcos Cortez', 'M', '1986-06-23', '2000-04-16', 2550000, 500000,'Mecánico', '333.333.333', '4000'),
('1.130.782', 'Antonio Gil', 'M', '1980-01-23', '2010-04-16', 850000, 1500000,'Técnico', '16.211.383', '1500'),
('333.333.334', 'Marisol Pulido', 'F', '1979-10-01', '1990-05-16', 3250000, 1000000,'Investigador', '16.759.060', '3000'),
('333.333.335', 'Ana Moreno', 'F', '1992-01-05', '2004-06-01', 1200000, 400000,'Secretaria', '16.759.060', '3000'),
('1.130.333', 'Pedro Blanco', 'M', '1987-10-28', '2000-10-01', 800000, 3000000,'Vendedor', '31.178.144', '2000'),
('1.130.444', 'Jesús Alfonso', 'M', '1988-03-14', '2000-10-01', 800000, 3500000,'Vendedor', '31.178.144', '2000'),
('333.333.336', 'Carolina Ríos', 'F', '1992-02-15', '2000-10-01', 1250000, 500000,'Secretaria', '16.211.383', '1500'),
('333.333.337', 'Edith Muñoz', 'F', '1992-03-31', '2000-10-01', 800000, 3600000,'Vendedor', '31.178.144', '2100'),
('1.130.555', 'Julián Mora', 'M', '1989-07-03', '2000-10-01', 800000, 3100000,'Vendedor', '31.178.144', '2200'),
('1.130.666', 'Manuel Millán', 'M', '1990-12-08', '2004-06-01', 800000, 3700000,'Vendedor', '31.178.144', '2300');

SELECT *
FROM Empleado;

SELECT *
FROM Departamento;

SELECT *
FROM Empleado
WHERE cargoE = 'Secretaria';

SELECT nomEmp, salEmp
FROM Empleado;

SELECT *
FROM Empleado
WHERE cargoE = 'Vendedor'
ORDER BY nomEmp;

SELECT nombreDpto
FROM Departamento;
SELECT DISTINCT nombreDpto
FROM Departamento;

SELECT DISTINCT nombreDpto
FROM Departamento
ORDER BY nombreDpto;

SELECT nombreDpto, ciudad
FROM Departamento
ORDER BY ciudad;

SELECT nombreDpto, ciudad
FROM Departamento
ORDER BY ciudad desc;

SELECT nomEmp, cargoE
FROM Empleado
ORDER BY salEmp;

SELECT nomEmp, cargoE, salEmp
FROM Empleado
ORDER BY cargoE, salEmp;

SELECT nomEmp, cargoE
FROM Empleado
ORDER BY cargoE DESC;

SELECT nomEmp, salEmp, comisionE
FROM Empleado
WHERE codDepto = '2000';

SELECT nomEmp, salEmp, comisionE
FROM Empleado
WHERE codDepto = '2000'
ORDER BY comisionE;

SELECT comisionE
FROM Empleado;


--16-
SELECT DISTINCT comisionE
FROM Empleado
ORDER BY comisionE;

--17- 
SELECT DISTINCT salEmp
FROM Empleado
ORDER BY salEmp;

--18 Obtener el valor total a pagar que resulta de sumar a los empleados del
--departamento 3000 una
--bonificación de $500.000, en orden alfabético del empleado
SELECT nomEmp, salEmp, 'Pago Total = $', salEmp+500000
FROM Empleado
WHERE codDepto = '3000';

--19- 
SELECT nDIEmp, nomEmp, salEmp, comisionE
FROM Empleado
WHERE comisionE > salEmp;

--20- -- Listar los empleados cuya comisión es menor o igual que el 30% de su sueldo
SELECT nDIEmp, nomEmp, salEmp, comisionE
FROM Empleado
WHERE comisionE <= salEmp*0.30

--21- --Listado donde para cada fila, figure Nombre y Cargo antes del
 --valor respectivo para cada empleado
SELECT 'Nombre: ', nomEmp, 'Cargo: ', cargoE
FROM Empleado;

--22 -- Hallar el salario y la comisión de aquellos empleados cuyo número de
 -- documento de identidad es superior al '19.709.802'
SELECT nDIEmp, nomEmp, salEmp,
comisionE
FROM Empleado
WHERE nDIEmp > '19.709.802';


--23- -- Listar los empleados cuyo salario es menor o igual que el 40% de su comisión
SELECT nomEmp, salEmp, comisionE
FROM Empleado
WHERE salEmp <= comisionE*0.40;

--24- -- Listar los empleados cuyo salario es menor o igual que el 40% de su comisión
SELECT JZ.nomEmp, JZ.cargoE
FROM (SELECT *
 FROM Empleado
 WHERE nomEmp> 'J' AND nomEmp <'z')
 JZ
ORDER BY nomEmp;

--25- --Listar el salario, la comisión, el salario total (salario + comisión),
--documento
 -- de identidad del empleado y nombre, de aquellos empleados que tienen comisión
 -- superior a $1.000.000, ordenar el informe por el número del documento de
--identidad
SELECT nDIEmp, nomEmp, salEmp, comisionE, (salEmp+comisionE) as total
FROM Empleado
WHERE comisionE > 1000000
ORDER BY nDIEmp;

--26- -- Obtener un listado similar al anterior, pero de aquellos empleados que NO
--tienen comisión
SELECT nDIEmp, nomEmp, salEmp, comisionE, (salEmp+comisionE) as total
FROM Empleado
WHERE comisionE = 0
ORDER BY nDIEmp;

--27- --Hallar el nombre de los empleados que tienen un salario superior a $1.000.000,
--y tienen como jefe al
 -- empleado con documento de identidad '31.840.269'
SELECT nomEmp, salEmp
FROM Empleado
WHERE salEmp > 1000000 AND jefeID = '31.840.269';

--28- --Hallar el conjunto complementario del resultado del ejercicio anterior
SELECT nomEmp,salEmp,jefeID
FROM Empleado
WHERE salEmp <= 1000000 AND jefeID = '31.840.269';

--29 ???????----

--30- -- Hallar los empleados cuyo nombre no contiene la cadena MA
SELECT nomEmp
FROM Empleado
WHERE nomEmp LIKE 'Ma%';

--31- --Obtener los nombres de los departamentos que no sean 'VENTAS','INVESTIGACIÓN',
--ni 'MANTENIMIENTO',
 -- ordenados por ciudad.
SELECT nombreDpto, ciudad
FROM Departamento
WHERE nombreDpto NOT IN ('VENTAS',
'INVESTIGACIÓN','MANTENIMIENTO')
ORDER BY ciudad;

--32- --Obtener el nombre y el departamento de los empleados con cargo SECRETARIA OVENDEDOR,
 -- que no trabajan en el departamento de 'PRODUCCION', cuyo salario es superior a $1.000.000,
 -- ordenados por fecha de incorporación
SELECT E.nomEmp, E. cargoE, D.nombreDpto
FROM Departamento D, Empleado E
WHERE cargoE NOT IN ('Secretaria',
'Vendedor') AND
salEmp > 1000000 AND
E.coddepto = D.coddepto AND
E.coddepto NOT IN
(SELECT F.coddepto
FROM Departamento F
WHERE F.nombredpto='PRODUCCIÓN');

--33,34????

--35- --Obtener los nombres, salarios y comisiones de los empleados que reciben un
--salario situado entre la
 --mitad de la comisión la propia comisión
SELECT nomEmp, salEmp, comisionE
FROM Empleado
WHERE salEmp >= comisionE/2 AND salEmp <= comisionE ;

--36- --Suponga que la empresa va a aplicar un reajuste salarial del 7%. Listar los
--nombres de los empleados,
 -- su salario actual y su nuevo salario, indicando para cada uno de ellos si
--tiene o no comisión
SELECT nomEmp, salEmp, (salEmp*0.07),
comisionE
FROM Empleado;

--37- --Obtener la información disponible del empleado cuyo número de documento de
--identidad
SELECT nDIEmp, nomEmp
FROM Empleado
WHERE
nDIEmp IN ('31.178.144', '16.759.060','1.751.219', '768.782',
'737.689','19.709.802', '31.174.099','1.130.782');

--38- --Entregar un listado de todos los empleados ordenado por su departamento, y
--alfabético
 --dentro del departamento
SELECT nDIEmp, nomEmp, codDepto
FROM Empleado
ORDER BY codDepto, nomEmp;

--39- --Entregar el salario más alto de la empresa.
SELECT nomEmp, salEmp
FROM Empleado
WHERE salEmp IN
(SELECT MAX(salEmp)
FROM Empleado);


--40- -- Entregar el total a pagar por comisiones, y el número de empleados que las
--reciben
SELECT count (nDIEmp), sum (comisionE)
FROM Empleado
WHERE comisionE > 0;

--========================================================================
--PRACTICA 3 DE LENGUAJE ESTRUCTURADO SQL
--MOISES ZABALETA CRUZ
--1033810224
--Email: MZABALETAC@ACADEMIA.USBBOG.EDU.CO

-- Consulta 1: Obtener los datos completos de los empleados.
SELECT *
FROM Empleado;

Consulta 1: Obtener los datos completos de los empleados.

-- Consulta 2: Obtener los datos completos de los departamentos.
SELECT *
FROM Departamento;

-- Consulta 3: Obtener los datos de los empleados con cargo secretaria.
SELECT *
FROM Empleado
WHERE cargoE IN ('Secretaria');

-- Consulta 4: Obtener el nombre y salario de los empleados..
SELECT nomEmp,salEmp
FROM Empleado;

-- Consulta 5: Obtener los datos de los empleados vendedores, ordenado por nombre.
SELECT *
FROM Empleado
WHERE cargoE IN ('vendedor')
ORDER BY nomEmp;

-- Consulta 6:Listar el nombre de los departamentos
SELECT DISTINCT ciudad
FROM Departamento;

-- Consulta 7:Listar los salarios y comisiones de los empleados del departamento 2000, ordenado por comisión.
SELECT *
FROM EMPLEADO;