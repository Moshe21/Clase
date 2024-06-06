/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ordenador_300;
import java.util.Scanner;
/**
 *
 * @author 304
 */
public class Ordenador_300 {
     /**
     * @param args the command line arguments
     */
    
    public static void main(String[] args) {
        // TODO code application logic here
       
        /* creacion los datos*/ 
     System.out.println("bienvenido a ordenador");
        
     Scanner ingreso_data=new Scanner(System.in);   
     

      
     int mat2[][]=new int[3][3];
      
     
           
                     
     for(int i=0;i<3;i++){

        for(int g=0 ;g<3;g++){
                System.out.println("fila "+(i)+" columna "+(g)+"  ingrese el dato:");
                mat2[i][g]=ingreso_data.nextInt();
            }
        }
        
        /* imprimir los datos*/
        for(int i = 0;i<3;i++){

            for(int g=0;g<3;g++){

                System.out.print(mat2[i][g]+"\t");
            }
            System.out.println("");
       }
        int dato_menor=mat2[1][1]; 
        int dato_mayor=mat2[1][1];
        /* ordenar datos los datos*/
        for(int i =0;i<3;i++){
 
            for(int g =0;g<3;g++){
                
                if(mat2[i][g]<dato_menor){
                
                    dato_menor=mat2[i][g];
                }
                if(mat2[i][g]>dato_mayor){
                
                    dato_mayor=mat2[i][g];
                }
                  
            }


       }

    
    System.out.println("dato menor es: "+dato_menor);
    System.out.println("dato mayor es: "+dato_mayor);
    }
    
    
}
