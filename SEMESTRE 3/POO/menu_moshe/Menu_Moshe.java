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
        double valor1;
        
        Scanner teclado=new Scanner(System.in);
        
        System.out.println("digite su primer valor");
        valor1=teclado.nextInt();
        
        
        do{
            System.out.println("MENU PRINCIPAL");
            System.out.println("Indique aque lo quiere convertir");
            System.out.println("1 Pesos a Dolares");
//            System.out.println("2 Dolares a Pesos");
            System.out.println("3 Pesos a Euros");
            System.out.println("4 Euros a Pesos");
            System.out.println("5 Pesos a Libras Esterlinas");
            System.out.println("6 cc Esterlinas a Pesos");
            System.out.println("7 Salir");
            System.out.println("Seleccione opcion:");
            op=teclado.nextInt();
            
            switch(op){
                
                case 1:
                    System.out.println("Bienvenido Pesos a Dolares");
                    
                    break;
                    
                case 2:
                    System.out.println("Bienvenido Dolares a Pesos");
                    break;
                case 3:
                    System.out.println("Bienvenido Pesos a Euros");
                    break;
                case 4:
                    System.out.println("Bienvenido Euros a Pesos");
                    break;
                case 5:
                    System.out.println("Bienvenido Pesos a Libras Esterlinas");
                    break;
                case 6:
                    System.out.println("Bienvenido Libras Esterlinas a Pesos");
                    break;                     
                case 7: 
                    System.out.println("largate YA, y se Feliz :)");
                    mseguir=false;
                    break;
            }
            
            
            
        }while (mseguir==true);
        
        
        // TODO code application logic here
    }
    
}
