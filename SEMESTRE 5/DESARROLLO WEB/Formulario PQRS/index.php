<html>
 <head>
    <title> registro PQR</title>
 </head>
<body>
    <form action="inserta.php" method="POST">
     
    <table>
        <tr>
          <th>nombre del abonado</th>  
            <td>
              <input type="text" name="get_nombre" placeholder="ingresa tu nombre">
            </td>
        </tr>
          <tr>
            <th>apellido del abonado</th>
          <td>
            <input type="text" name="get_apellido" placeholder="ingresa tu apellido">
          </td>    
        </tr>
        <tr>
          <th>area</th>
            <select name="opcion_area">
              <option value ="soporte técnico">soporte técnico;  </option>
              <option value="cartera">cartera</option>
          
        </tr>

    </table>




    </form>   


</body>


</html>