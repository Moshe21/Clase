create database taller_final;
use taller_final;
create table clientes (idcliente int primary key auto_increment, nomcliente varchar(50));
create table articulos (idarticulo int primary key auto_increment, nomarticulo varchar(100));
create table vendedores (idvendedores int primary key auto_increment, nomvendedor varchar(50));
create table fac_gen (idfactura int primary key auto_increment, fecha datetime, idcliente int, idvendedores int, 
 constraint fk_cliente foreign key (idcliente)references clientes(idcliente),constraint fk_vendedor foreign key 
 (idvendedores) references vendedores (idvendedores));
 create table fac_det (idfacturas int primary key auto_increment, idarticulo int, cantidad int, vlr_unit int,
 vlr_iva int, valor_vta int, constraint fk_articulo foreign key (idarticulo) references articulos (idarticulo));
 
 delimiter //
 create  procedure ing_clientes (
 nomcliente varchar (50))
 begin
     insert into clientes (nomcliente) value (nomcliente);
	
end //

delimiter ;

call ing_clientes ("Jahaira");
call ing_clientes ("Moises");
call ing_clientes ("Danna");
select * from clientes;







 delimiter //
 create procedure ing_articulos (
 nomarticulo varchar (100))
 begin
     insert into articulos (nomarticulo) value (nomarticulo);
	
end //

delimiter ;

call ing_articulos ("tablet");
call ing_articulos ("Celular");
call ing_articulos ("Televisores");
select * from articulos;



delimiter //
 create procedure ing_vendedor (
 nomvendedor varchar (100))
 begin
     insert into vendedores (nomvendedor) value (nomvendedor);
	
end //

delimiter ;


call ing_vendedor ("cristian");
select * from vendedores; 
-- delete from vendedores where idvendedores =2;




delimiter //
 create procedure ing_fac_gen(
 id_cliente int,
 id_vendedores int)
 begin
     insert into fac_gen (fecha,Idcliente,idvendedores) value (NOW(),id_cliente,id_vendedores);
	
end //

delimiter ;

 call ing_fac_gen (1,2);
 
 select * from fac_gen;




delimiter //
 create procedure ing_fac_det(
 id_articulo int,
 cantidad int,
 vlr_unit int
 )
 begin
     insert into fac_det (idarticulo,cantidad,vlr_unit,vlr_iva,valor_vta) value (id_articulo,cantidad,vlr_unit,vlr_unit*0.19,vlr_unit*1.19);
	
end //

delimiter ;
call ing_fac_det (1,20,180000);
select * from fac_det;


delimiter //
 create procedure cant_vent()
 begin
     select idarticulo, cantidad, vlr_unit, cantidad * vlr_unit as totalvendido,sum() as total from fac_det where idarticulo=idarticulo;
	
end //

delimiter ;
call cant_vent();


DELIMITER //

CREATE PROCEDURE TotalVentas()
BEGIN
    SELECT SUM(valor_vta) AS TotalDeVentas FROM fac_det;
END //

DELIMITER ;
CALL TotalVentas();






drop PROCEDURE TotalVentas_Cliente
DELIMITER //
CREATE PROCEDURE TotalVentas_Cliente(
    in ing_idcliente INT
)
BEGIN
    SELECT 
        idcliente, 
        SUM(fac_det.valor_vta) AS TotalDeVentas
    FROM 
        fac_gen
    JOIN 
        fac_det ON idfactura = idfactura
    WHERE 
        fac_gen.idcliente = ing_idcliente
        GROUP BY 
        fac_gen.idcliente;
END //
DELIMITER ;

CALL TotalVentas_Cliente(2);




drop PROCEDURE TotalVentas_vendedor
DELIMITER //
CREATE PROCEDURE TotalVentas_vendedor(
    in ing_idvendedores INT
)
BEGIN
    SELECT 
        idvendedores, 
        SUM(fac_det.valor_vta) AS TotalDeVentas
    FROM 
        fac_gen
    JOIN 
        fac_det ON idfactura = idfactura
    WHERE 
        fac_gen.idvendedores = ing_idvendedores
        GROUP BY 
        fac_gen.idvendedores;
END //
DELIMITER ;


call TotalVentas_vendedor(2);

-- ---------------------------------------


-- -----------------------------------
DELIMITER //
CREATE PROCEDURE promedioVentas()
BEGIN
    SELECT AVG(valor_vta) AS PromedioDeVentas FROM fac_det;
END //

DELIMITER ;

CALL promedioVentas();






drop PROCEDURE promedioVentas_Cliente
DELIMITER //
CREATE PROCEDURE promedioVentas_Cliente(
    in ing_idcliente INT
)
BEGIN
    SELECT 
        idcliente, 
        AVG(fac_det.valor_vta) AS PromedioDeVentas
    FROM 
        fac_gen
    JOIN 
        fac_det ON idfactura = idfactura
    WHERE 
        fac_gen.idcliente = ing_idcliente
        GROUP BY 
        fac_gen.idcliente;
END //
DELIMITER ;

CALL promedioVentas_Cliente(3);




drop PROCEDURE promedioVentas_vendedor
DELIMITER //
CREATE PROCEDURE promedioVentas_vendedor(
    in ing_idvendedores INT
)
BEGIN
    SELECT 
        idvendedores, 
        AVG(fac_det.valor_vta) AS PromedioDeVentas
    FROM 
        fac_gen
    JOIN 
        fac_det ON idfactura = idfactura
    WHERE 
        fac_gen.idvendedores = ing_idvendedores
        GROUP BY 
        fac_gen.idvendedores;
END //
DELIMITER ;


call promedioVentas_vendedor(2);








/*
insert into fac_gen (fecha,Idcliente,idvendedores) value (NOW (),
							(SELECT idcliente FROM clientes where idcliente=idcliente),
                            (SELECT idvendedores FROM clientesvendedores where idvendedores=idvendedores));
                            */