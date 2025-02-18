/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package tensor_suma;
import java.util.Scanner;
/**
 *
 * @author 304
 */
public class Tensor_suma {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        System.out.println("bienvenido a matrices");
            Scanner ingreso_data=new Scanner(System.in);
            
            int fila, columna;
            int tfila, tcolumna;
            int  mat1[][],mat2[][],mat3[][];
            
            
             System.out.println("Iingresa la fila: ");
            tfila=ingreso_data.nextInt();
            System.out.println("Iingresa la columna: ");
            tcolumna=ingreso_data.nextInt();
            
            mat1=new int[tfila][tcolumna];
            mat2=new int[tfila][tcolumna];
            mat3=new int[tfila][tcolumna];
            
            for(fila=0;fila<=(tfila-1);fila++){
                for(columna=0;columna<=(tcolumna-1);columna++){
                    System.out.println("matriz 1 fila "+(fila+1)+" Columna "+(columna+1)+"  ingrese el dato:");
                    mat1[fila][columna]=ingreso_data.nextInt();
                }
            }   
            for(fila=0;fila<=(tfila-1);fila++){
            
                for(columna=0;columna<=(tcolumna-1);columna++){
                
                    System.out.print(mat1[fila][columna]+"\t");
                
                }
                System.out.println("");
            }
     
            System.out.println("");
            
            //---------------------------------------------------------
            
            for(fila=0;fila<=(tfila-1);fila++){
                for(columna=0;columna<=(tcolumna-1);columna++){
                    System.out.println("matriz 2 fila "+(fila+1)+" Columna "+(columna+1)+"  ingrese el dato:");
                    mat2[fila][columna]=ingreso_data.nextInt();
                }
            }  
            
            for(fila=0;fila<=(tfila-1);fila++){
            
                for(columna=0;columna<=(tcolumna-1);columna++){
                
                    System.out.print(mat2[fila][columna]+"\t");
                
                }
                System.out.println("");
            }
            System.out.println("");
            



            //---------------------------------------------------------
            
            for(fila=0;fila<=(tfila-1);fila++){
                for(columna=0;columna<=(tcolumna-1);columna++){
                    mat3[fila][columna]=mat1[fila][columna]+mat2[fila][columna];
                }
            } 
            
            for(fila=0;fila<=(tfila-1);fila++){
            
                for(columna=0;columna<=(tcolumna-1);columna++){
                
                    System.out.print(mat3[fila][columna]+"\t");
                
                }
                System.out.println("");
            }
            System.out.println("");
    }
    
}
