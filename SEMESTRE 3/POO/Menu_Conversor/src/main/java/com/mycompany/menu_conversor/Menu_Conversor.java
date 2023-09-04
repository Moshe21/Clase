/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.menu_conversor;
import java.util.Scanner;
/**
 *
 * @author User
 */
public class Menu_Conversor {

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
            System.out.println("2 Dolares a Pesos");
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
                    op_1_Pesos_a_Dolares conversion_1=new op_1_Pesos_a_Dolares(valor1);
                    conversion_1.mostrar();
                    break;
                    
                case 2:
                    System.out.println("Bienvenido Dolares a Pesos");
                    op_2_Dolares_a_Pesos conversion_2=new op_2_Dolares_a_Pesos(valor1);
                    conversion_2.mostrar();
                    break;
                case 3:
                    System.out.println("Bienvenido Pesos a Euros");
                    op_3_Pesos_a_Euros conversion_3=new op_3_Pesos_a_Euros(valor1);
                    conversion_3.mostrar();
                    break;
                case 4:
                    System.out.println("Bienvenido Euros a Pesos");
                    op_4_Euros_a_Pesos conversion_4=new op_4_Euros_a_Pesos(valor1);
                    conversion_4.mostrar();
                    break;
                case 5:
                    System.out.println("Bienvenido Pesos a Libras Esterlinas");
                    op_5_Pesos_a_Libras_Esterlinas conversion_5=new op_5_Pesos_a_Libras_Esterlinas(valor1);
                    conversion_5.mostrar();
                    break;
                case 6:
                    System.out.println("Bienvenido Libras Esterlinas a Pesos");
                    op_6_Esterlinas_a_Pesos conversion_6=new op_6_Esterlinas_a_Pesos(valor1);
                    conversion_6.mostrar();
                    break;                     
                case 7: 
                    System.out.println("largate YA, y se Feliz :)");
                    mseguir=false;
                    break;
            }
            
            
            
        }while (mseguir==true);
        
        
        System.out.println("Hello World!");
        // TODO code application logic here
    }
        
    
}
