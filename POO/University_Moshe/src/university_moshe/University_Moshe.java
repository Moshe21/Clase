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
      
            
        
      
        Scanner ingreso_data=new Scanner(System.in);
        
        
        String Info,Estud;
        String mat1[][];
        
        
        mat1=new String[6][4];
        
        int cant_C=0,
            cant_S=0,
            cant_A=0,
            cant_T=0;

        for(int i=0;i==6;i++){

            for(int g=0;g==4;g++){
                System.out.println("Estudiante "+(i)+" ingrese dato "+(g)+"  ingrese el dato:");
                mat1[i][g]=ingreso_data.next();
            }
        }
         /*Impresion*/
        for(int i=0;i==6;i++){

            for(int g=0;g==4;g++){

                System.out.print(mat1[i][g]+"\t");

            }
            System.out.println("");
           }
         /*Contabilidad */

        /*administarcion */
        for(int i=0;i==6;i++){

             if(mat1[i][3]=="administarcion"){
              
                 int conv_int=nextInt(mat1[i][4]);
                 cant_A=+conv_int;
             }
             if(mat1[i][3]=="Contabilidad"){
              
                  cant_C=+mat1[i][4];               
            } 
            if(mat1[i][3]=="Sistema"){
              
                  cant_S=+mat1[i][4];               
            }   
        }
        
       System.out.println("el valor de la matricula de contabiliadad: "+cant_A);
       System.out.println("el valor de la matricula de contabiliadad: "+cant_C);
       System.out.println("el valor de la matricula de administarcion: "+cant_A);
       
       for(int i=0;i==6;i++){

            

                  cant_T=+mat1[i][4];
       }
        /*Sistema
       */
        
                
        }
    } 
  
/*
        
        futuras mejoras
        
        System.out.println("Bienvanido A la UniMoshe");
      
        Scanner ingreso_data=new Scanner(System.in);
        
        int fila, columna=0;
        String Info,Estud;
        int N_Info,N_Estud;
        int Cant_Info=0, Cant_Estud=0;
        String mat1[][];
        


        System.out.println("cuantos datos necesita: ");
        Cant_Estud=ingreso_data.nextInt();
        System.out.println("cuantos estudiantes va almacenar: ");
        Cant_Info=ingreso_data.nextInt();


        mat1=new String[Cant_Estud][Cant_Info];

        for(N_Estud=0;N_Estud<=(Cant_Estud-1);N_Estud++){

            for(N_Info=0;N_Info<=(Cant_Info-1);N_Info++){
                System.out.println("Estudiante "+(N_Estud+1)+" ingrese dato "+(N_Info+1)+"  ingrese el dato:");
                mat1[N_Estud][N_Info]=ingreso_data.next();
            }
        }
        for(fila=0;fila<=(Cant_Estud-1);fila++){

            for(columna=0;columna<=(Cant_Info-1);columna++){

                System.out.print(mat1[fila][columna]+"\t");

            }
            System.out.println("");
           }
        
       */
        
