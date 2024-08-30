<?php

// declaracion de variables
$sever="7jk.h.filess.io";
$user="ServerMoshe_physicalno";
$pass="b0d735504a274566d1dc93860af71b821220adb3";
$dbname="ServerMoshe_physicalno";
$db_port="3307";


$conx1=mysqli_connect($sever,$user,$pass,$dbname,$db_port);

if(!$conx1){
    echo("Failled");
}
?>