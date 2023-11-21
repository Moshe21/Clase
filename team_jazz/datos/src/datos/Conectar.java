/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package datos;
import java.sql.Connection;
import java.sql.DriverManager;

/**
 *
 * @author EdgarChamorro
 */
public class Conectar {
    Connection conn=null; 
    public Connection conexion(){
        try {
           Class.forName("com.mysql.cj.jdbc.Driver");
           conn=DriverManager.getConnection("jdbc:mysql://localhost/datos?useUnicode=true&useJDBCCompliantTimezoneShift=true&useLegacyDatetimeCode=false&serverTimezone=UTC","root","Moshe21");
        } catch (Exception e)
            {
               System.out.println(e.getMessage());
            }
          return conn;
        }


}
