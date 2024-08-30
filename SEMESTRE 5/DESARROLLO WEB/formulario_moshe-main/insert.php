<?php

include "dbcon.php";

$fname=$_POST["fname"];
$lname=$_POST["lname"];
$city=$_POST["city"];

//DECLARACION DE LA CONSULTA
$insertsql="insert into student (fname,lname,city) 
values('$fname','$lname','$city')";

$res =mysqli_query($conx1,$insertsql);

?>