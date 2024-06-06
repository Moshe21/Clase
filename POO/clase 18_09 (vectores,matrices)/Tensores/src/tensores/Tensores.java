/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package tensores;
import java.util.Scanner
/**
 *
 * @author 304
 */
public class Tensores {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner ingreso=new Scanner(System.in);
        
        //declaracion de vector
        int V1[];
        // decalracion de variables
        int tamano;
        int i;
        int acumulador=0;
        int num_escogido;
        int sw=0;
        
      //ingreso de tamaño de vector
        System.out.print("ingrese el tamaño del vector:  ");
        tamano=ingreso.nextInt();
   
        
        V1=new int [tamano];
        
        //ciclo para ingresar los valores de las posiciones de el vector
        for (i=0;i<=(tamano-1);i++){
            
          

            //Ingreso de datos
            System.out.println("ingrese el dato de valor: ");
            V1[i]=ingreso.nextInt();
            
        }
        //impresion de datos del vector
         for (i=0;i<=(tamano-1);i++){
             System.out.print(V1[i]+", ");
             acumulador=acumulador+V1[i];
            
         }
         System.out.println("sumatoria de lso elementos son: "+acumulador); 
         
         
        //----------------------------------------------------
        //Ingreso de dato a buscar
        System.out.print("ingrese el dato a buscar: ");
        num_escogido=ingreso.nextInt();
        
         for (i=0;i<=(tamano-1);i++){
             if(V1[i]==num_escogido){
                 sw=1;
                  System.out.println("el valor existe, es: "+V1[i]+ " y esta en la posicion "+(i+1));
             }
         }
         if(sw==0){
         
             System.out.println("No existe ese valor");
         }
         
         System.out.println("FIN.....");
    }
    
}

