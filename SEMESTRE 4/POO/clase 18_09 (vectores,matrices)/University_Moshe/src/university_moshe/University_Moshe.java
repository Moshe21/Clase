/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package university_moshe;
import java.util.Scanner; 
/**
 *
 * @author 304
 */
public class University_Moshe {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        System.out.println("Bienvanido A la UniMoshe");
        
        Scanner ingreso_data=new Scanner(System.in);

        String Info,Estud;
        int N_Info,N_Estud;
        int Cant_Info=0, Cant_Estud=0;
        String mat1[][];
        


        System.out.println("cuantos datos necesita: ");
        Cant_Estud=ingreso_data.nextInt();
        System.out.println("cuantos datos necesita: ");
        Cant_Info=ingreso_data.nextInt();


        mat1=new String[Cant_Estud][Cant_Info];

        for(N_Estud=0;N_Estud<=(Cant_Estud-1);N_Estud++){

            for(N_Info=0;N_Info<=(Cant_Info-1);N_Info++){
                System.out.println("Estudiante "+(N_Estud+1)+" ingrese dato "+(N_Info+1)+"  ingrese el dato:");
                mat1[N_Estud][N_Info]=ingreso_data.next();
            }
        }
            for(fila=0;fila<=(tfila-1);fila++){
            
                for(columna=0;columna<=(tcolumna-1);columna++){
                    
                    System.out.print(mat1[fila][columna]+"\t");
                    
                }
                System.out.println("");
           }
        
        
    }
    
}
