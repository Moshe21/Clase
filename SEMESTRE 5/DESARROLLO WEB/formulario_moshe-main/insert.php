<?php

include "dbcon.php";


$fname=$_POST["fname"];
$lname=$_POST["lname"];
$city=$_POST["city"];

//DECLARACION DE LA CONSULTA
$insertsql="insert into student (fname,lname,city) values('$fname','$lname','$city')";

$res =mysqli_query($conx1,$insertsql);

if($res){
    echo("Inserted");
  
//es una buena practica cerrar la conexion
  mysqli_close($conx1);

  
// de
  
}
   header("Location: thanks.html");
?>