/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package getset;

import java.util.HashSet;
import java.util.Set;

/**
 *
 * @Moshe Zabaleta Cruz
 */
public class Getset {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        String nombre_1="marcela";
        String apellido_1="sanchez";
        int edad_1=45;
        
        
        Datochs personas=new  Datochs(nombre_1,apellido_1,edad_1);
        personas.mostra();
        
        personas.setNombre("camilo");
        
        personas.mostra();
        
    
    
    
    }
    
}
