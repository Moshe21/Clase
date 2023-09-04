use programacion_bd
delimiter $
-- -------------------------------------------------------------------------------------------
/* CICLO LOOP

 se crea la tabla para almacenar los datos en tipo numerico
*/
-- se crea la tabla para almacenar los datos en tipo numerico
create table repiteme (solucion int);

-- creamos un menu para que despliengue las opciones que escoja el usuario
create procedure contador(in ing_dato int)
BEGIN		
declare Cantidad int;
declare i int default 0;
	SET Cantidad = ing_dato;
	myloop:LOOP
		SET i=i+1;
		IF i=Cantidad then
		leave myloop;
		END IF;
		SELECT i;
	END LOOP myloop;
END;
$
-- -------------------------------------------------------------------------------------------
/* CONDICIONAL IF

 se crea la tabla para almacenar los datos en tipo numerico
*/
create table respuesta( solucion varchar(30));
-- Creamos el procedimiento
create procedure she_lies
BEGIN		

-- decalramos la variables
declare ing_data varchar (2);
	SET ing_data = te_ama;
    -- creamos la codicion (para saber si te ama)
	if ing_data = "si" then
		INSERT INTO respuesta VALUES ("ella te ama");
		else
        INSERT INTO respuesta VALUES ("amiga date cuenta");
end if;
	SELECT * FROM respuesta;
END;


-- -------------------------------------------------------------------------------------------
/* CONDICIONAL CASE

 se crea la tabla para almacenar los datos en tipo numerico
*/
create table seleccion(solucion int);
-- se modifica la tabla para que acepte valores de textos
alter table seleccion modify column solucion varchar(6);
-- creamos un menu para que despliengue las opciones que escoja el usuario
create procedure menu_moshe (in ing_dato int)
BEGIN	
declare opcion int;
	SET opcion = ing_dato;
	case opcion 
		when 1 then insert into seleccion values ("play");
		when 2 then insert into seleccion values ("confi");
		when 3 then insert into seleccion values ("salir");
		else insert into seleccion values ("opcion invalida");
	end case;
	SELECT * FROM seleccion;
END;
