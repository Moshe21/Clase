<html>
<head>
    
    <title>Registro</title>
</head>
<body>

    <form action="insert.php" method="POST">
        <table>
            <tr>
                <th>Nombre</th>
                <td>
                    <input type="text" name="fname" placeholder= "Tu nombre">
                    
                </td>
            </tr>

            <tr>
                <th>apellido</th>
                <td>
                    <input type="text" name="lname" placeholder= "Tu apellido">
                    
                </td>
            </tr>

             <tr>
                <th>Ciudad</th>
                <td>
                    <input type="text" name="city" placeholder= "Tu ciudad">
                    
                </td>
            </tr>




 <!--BOTONES--------------------------------------------------------------------------------
 
 -->
                <td>
                    <input type="submit" name="bsubmit" placeholder= "enviar">
                    
                </td>
            </tr> 

            <tr>
                <td>
                    <input type="reset" name="reniciar" placeholder= "ciudad">
                    
                </td>
            </tr>   


        </table>

    </form>
        <?php   





        ?>
</body>
</html>