<?php

include "dbcon.php";


$fname=$_POST["fname"];
$lname=$_POST["lname"];
$city=$_POST["city"];

//DECLARACION DE LA CONSULTA
$insertsql="insert into student (fname,lname,city) values('$fname','$lname','$city')";
//ENVIO DE LA CONSULTA INSERCION
$res =mysqli_query($conx1,$insertsql);

//VALIDAR SI LA INFORMACION YA EXISTE
IF(mysqli_affected_rows($conx1) > 0){
    echo"La persona ya existe </br>";
  
}




//como se inserta una fila se debe validar si se inserta o no
if($res){
    echo("Inserted");
  
//es una buena practica cerrar la conexion
  mysqli_close($conx1);

  
// de
  
}
   header("Location: thanks.html");
?>