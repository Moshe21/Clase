/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package menu_moshe;
import java.util.Scanner;


/**
 *
 * @author 304
 */
public class Menu_Moshe {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        int op;
        boolean mseguir=true;
        
        Scanner teclado=new Scanner(System.in);
        
        do{
            System.out.println("MENU PRINCIPAL");
            System.out.println("1.Pesos a Dolares");
            System.out.println("2.e");
            System.out.println("3.opcion 3");
            System.out.println("4.Salir");
            System.out.println("Seleccione opcion:");
            op=teclado.nextInt();
            
            switch(op){
                
                case 1:
                    System.out.println("ingreso opcion 1");
                    break;
                    
                case 2:
                    System.out.println("ingreso opcion 2");
                    break;
                    
                case 3:
                    System.out.println("ingreso opcion 3");
                    break;
                case 4: 
                    System.out.println("largate YA");
                    mseguir=false;
                    break;
            }
            
            
            
        }while (mseguir==true);
        
        
        // TODO code application logic here
    }
    
}
