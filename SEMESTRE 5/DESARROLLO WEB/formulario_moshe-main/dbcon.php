<?php

// declaracion de variables
$sever="sql.freedb.tech";
$user="freedb_ADMIN_MOSHE7";
$pass="UzQ&d?gpTQ6q@k*";
$dbname="freedb_My_server_moshe";
$db_port="3306";


$conx1=mysqli_connect($sever,$user,$pass,$dbname,$db_port);

if(!$conx1){
    echo("Failled");
}
?>