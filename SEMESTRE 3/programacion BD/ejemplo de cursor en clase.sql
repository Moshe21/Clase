create database clases;
use clases;

create table usuario(
	id int auto_increment primary key,
    nombre varchar (20),
    edad int,
	comentario varchar(40)
);


delimiter //
create procedure Tu_categoria_edad(
	in ing_nombre varchar (20),
    in ing_edad int)
	begin
		
        if ing_edad<18 then		
			insert into usuario (nombre, edad,comentario) value (ing_nombre,ing_edad,"Estas !Puberto¡");
			select * from usuario;
		elseif ing_edad>18 then
			insert into usuario (nombre, edad,comentario) value (ing_nombre,ing_edad,"eres un adulto");
			select * from usuario;
		elseif ing_edad>65 then
			insert into usuario (nombre, edad,comentario) value (ing_nombre,ing_edad,"Esta viejo hermano");
			select * from usuario;
		end if;
		
	end//
delimiter ; 
    call Tu_categoria_edad ("cristina",19);

create table info_usuario(
cedula int primary key,
nombre varchar (20),
correo varchar(50)
);


insert into info_usuario(cedula,nombre,correo) 
						value 	(1234567890, 'John Doe', 'john@example.com'),
								(9876543210, 'Jane Smith', 'jane@example.com'),
								(4567891230, 'Alice Johnson', 'alice@example.com'),
								(7891234560, 'Bob Williams', 'bob@example.com'),
								(3216549870, 'Eva Davis', 'eva@example.com'),
								(6543217890, 'Mike Brown', 'mike@example.com'),
								(1472583690, 'Sara Wilson', 'sara@example.com'),
								(2583691470, 'David Lee', 'david@example.com'),
								(3691472580, 'Emily White', 'emily@example.com'),
								(9517538520, 'Chris Martin', 'chris@example.com');
 
 select * from info_usuario;
delimiter //
 CREATE PROCEDURE Busca_Correo ( 
		INOUT emailList varchar(4000))
        
BEGIN
	DECLARE finished INTEGER DEFAULT 0; 	
    DECLARE emailAddress varchar(50) DEFAULT "";
	-- declaracion cursor email 
	DECLARE curEmail 
		CURSOR FOR SELECT correo FROM info_usuario;  
        -- declaracion NOT FOUND  
        DECLARE CONTINUE HANDLER 
			FOR NOT FOUND SET finished = 1;
	OPEN curEmail;
	ciclo_correo: LOOP
		FETCH curEmail INTO emailAddress;
		IF finished = 1 
			THEN LEAVE ciclo_correo;
		END IF;
		-- construir email list
		SET emailList = CONCAT(emailAddress, ";", emailList); 
	END LOOP ciclo_correo;
	CLOSE curEmail;
end//

select correo from info_usuario;
set @emailList="";
call Busca_correo (@emailList);
select @emailList; 