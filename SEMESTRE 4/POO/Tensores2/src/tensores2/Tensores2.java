/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package tensores2;
import java.util.Scanner;
/**
 *
 * @author 304
 */
public class Tensores2 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
            System.out.println("bienvenido a matrices");
            Scanner ingreso_data=new Scanner(System.in);
            
            int fila, columna=0;
            int tfila, tcolumna;
            int  mat1[][];
            int sumatoria=0,sumatoria_fila=0;
           
            
            System.out.println("Iingresa la fila: ");
            tfila=ingreso_data.nextInt();
            System.out.println("Iingresa la columna: ");
            tcolumna=ingreso_data.nextInt();
            
            mat1=new int[tfila][tcolumna];
            
            for(fila=0;fila<=(tfila-1);fila++){
            
                for(columna=0;columna<=(tcolumna-1);columna++){
                    System.out.println("fila "+(fila+1)+" Columna "+(columna+1)+"  ingrese el dato:");
                    mat1[fila][columna]=ingreso_data.nextInt();
                }
            }
           for(fila=0;fila<=(tfila-1);fila++){
            
                for(columna=0;columna<=(tcolumna-1);columna++){
                    
                    System.out.print(mat1[fila][columna]+"\t");
                    
                }
                System.out.println("");
           }
           for(fila=0;fila<=(tfila-1);fila++){
                sumatoria_fila=sumatoria+mat1[fila][columna];
                for(columna=0;columna<=(tcolumna-1);columna++){
                    sumatoria=sumatoria+mat1[fila][columna];
                }
           }
           System.out.println("la suma total seria: "+sumatoria);
        }
    }    
                    
            
            
            
            
        
        // TODO code application logic here

    

