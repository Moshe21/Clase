/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package mvc;
import modelo.Modelo;
import vista.Vista;
import controlador.Controlador;
/**
 *
 * @author 304-1
 */
public class Mvc {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
       Modelo mod= new Modelo();
       Vista view= new Vista();
       Controlador control=new Controlador(view,mod);
       control.iniciar();
       view.setVisible(true);
        
    }
    
}
