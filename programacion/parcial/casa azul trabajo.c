#include <stdio.h>
#include <string.h>

// Importa las bibliotecas est�ndar para entrada/salida y manejo de cadenas.

//
int f=0;
const int i= 10;
const int M= 10;

// Declaraci�n de variables globales, 'f' es un contador, 'i' y 'M' son constantes.

void menu_ing();
void menu_reg();
void menu_prof();
void menu_estu();
void menu_ing_notas();
void menu_ver_notas();

// Declaraci�n de funciones que se definir�n m�s adelante.

//
int reg_nom_user;
int reg_pass_user;	
int pass_user ;
int nom_user ;
int ing_nota_1;
int ing_nota_2;
int ing_nota_3;

// Declaraci�n de variables globales, que se utilizar�n para almacenar informaci�n de los usuarios y las notas.

//
struct info_user{
 
	int reg_nom_user;
	int reg_pass_user;	
};

// Declaraci�n de una estructura para almacenar la informaci�n de cada usuario (nombre y contrase�a).

struct info_user I[i]={};
struct info_nota{
 
	int nota_1;
	int nota_2;
	int nota_3;
		
};

// Declaraci�n de una estructura para almacenar las notas de cada usuario.

struct info_nota N[i]={};

// Declaraci�n de un arreglo de estructuras para almacenar informaci�n de los usuarios y las notas.

int main (){
	
	// La funci�n principal del programa.

	while(1){
        int opcion;
		// Bucle que se ejecuta indefinidamente hasta que se elija la opci�n "3".
		// Se solicita al usuario que ingrese una opci�n (1, 2 o 3).
		printf("BIENVENIDOS AL COLEGIO \n      CASITA AZUL\n 1.INGRESAR\n 2.REGISTRASE\n 3.EXIT\n ingrese una opcion\t");
		scanf("%d",&opcion);
		
		switch(opcion){
		
			// Se utiliza un switch para determinar qu� funci�n se debe llamar en funci�n de la opci�n ingresada.
			// En caso de ingresar "1", se llama a la funci�n "menu_ing()".
			case 1:{
					menu_ing();
					break;
				}
			// En caso de ingresar "2", se llama a la funci�n "menu_reg()".
			case 2:{
					menu_reg();
					break;
				}
			// En caso de ingresar "3", se sale del bucle.
			case 3:{
					f=3;
				
				}
			// En caso de ingresar una opci�n inv�lida, se muestra un mensaje de error.
			default:
				printf("bi bu bi bu error vueleve a intentar");
		
		}	
	}
	
	// Mensaje final que se muestra al salir del bucle.
	printf("QUE TENGO UN BUEN DIA LES DESEA\n COLEGIO \n      CASITA AZUL ");
};

void menu_ing(){
	
	// Funci�n para manejar el ingreso al sistema.

	printf("INGRESAR \n Usuario");
	scanf("%d",&nom_user);
	
	printf("\n contrase�a");
	scanf("%d",&pass_user);
	
	// Se utiliza un bucle for para verificar las credenciales ingresadas.
	// Si se encuentran coincidencias, se llama a la funci�n correspondiente.
	// Si no se encuentran coincidencias, se muestra un mensaje de error.
	for(int j=0;j<3;j++){
            
    	if(reg_nom_user ==nom_user && reg_pass_user==pass_user){
    		
    		menu_prof();
    	}
    	if (reg_nom_user==nom_user && reg_pass_user==pass_user){
	    	
    		menu_estu();
	    }
	    else{
		printf("NO ESTAS REGISTRADO");
	    }
	
    }
}


void menu_prof(){
     
     while(f!=3){
     
        // Se inicializa una variable 'opcion' y se imprime un men�
        // para que el profesor elija una opci�n.
        
        int opcion;
		printf("BIENVENIDOS AL COLEGIO \n      CASITA AZUL\n 1.INGRESAR NOMBRE ESTUDIANTES\n 2.VER NOTAS DEL ESTUDIANTE \n 3.EXIT\n ingrese una opcion\t");
		scanf("%d",&opcion);
		
		// Dependiendo de la opci�n seleccionada, se ejecuta una funci�n
		// diferente. Si se ingresa la opci�n 1, se llama a la funci�n
		// 'menu_ing_notas'. Si se ingresa la opci�n 2, se llama a la
		// funci�n 'menu_ver_notas' y luego a 'menu_estu'. Si se ingresa
		// la opci�n 3, se sale del bucle.
		
		switch(opcion){
		
			case 1:{
                 
					menu_ing_notas();
					break;
				}
			case 2:{
					menu_ver_notas();
    				menu_estu();
				}
			case 3:{
					f=3;
				}
			default:
				printf("bi bu bi bu error vueleve a intentar");
		
		}	
	}    
     
}
//En resumen, esta funci�n muestra un men� al profesor con tres opciones 
//diferentes y ejecuta una acci�n dependiendo de la opci�n seleccionada. 
//El bucle se repetir� hasta que se seleccione la opci�n 3, 
//momento en el que se saldr� del bucle y se terminar� la funci�n.

void menu_ing_notas(){

     // Se pide al usuario que ingrese un nombre de usuario y una
     // contrase�a, y se almacenan en las variables 'nom_user' y
     // 'pass_user'.
     
     printf("INGRESAR \n Usuario");
	scanf("%d",&nom_user);
	
	printf("\n contrase�a");
    scanf("%d",&pass_user);
	
    // Se realiza un bucle 'for' que se repetir� tres veces. Dentro
    // del bucle, se verifica si el nombre de usuario y la contrase�a
    // ingresados coinciden con los almacenados en la estructura 'I'.
    
	for(int j=0;j<3;j++){
        if(reg_nom_user==nom_user && reg_pass_user==pass_user){
    		
            // Si las credenciales son correctas, se le pide al profesor
            // que ingrese las notas del estudiante, y se suman a las
            // notas almacenadas en la estructura 'N'.
            
    		printf("Nota 1: \n");
	        scanf("%d",&ing_nota_1);
            N[i].nota_1+=ing_nota_1;
	
    		printf("Nota 2: \n");
    		scanf("%d",&ing_nota_2);
            N[i].nota_2+=ing_nota_2;
	
    		printf("Nota 3: \n");
    		scanf("%d",&ing_nota_3);
            N[i].nota_3+=ing_nota_3;

            
	    }
	    else{
	    
            // Si las credenciales son incorrectas, se imprime un mensaje
            // de error.
            
		    printf("NO ESTAS REGISTRADO");
	    }
    } 
}
  
void menu_ver_notas(){  
//Este es un fragmento de c�digo en lenguaje C++ que define 
//una funci�n llamada "menu_ver_notas".

    printf("INGRESAR \n Usuario");
	scanf("%d",&nom_user);
//La funci�n recorre un arreglo de usuarios y 
//compara el nombre de usuario ingresado con los nombres 
//de usuario almacenados en el arreglo.
	
	printf("\n contrase�a");
    scanf("%d",&pass_user);
	
	for(int j=0;j<3;j++){
        if(reg_nom_user==nom_user && reg_pass_user==pass_user){                                                          	if(I[j].reg_nom_user[i]==nom_user[i]){
 //Si encuentra un usuario con el mismo nombre de usuario,
//muestra las notas correspondientes a ese usuario.

    		printf("Nota 1: \n %d",N[i].nota_1);
            printf("Nota 2: \n %d",N[i].nota_2);
            printf("Nota 3: \n %d",N[i].nota_3);
	    	}
		}
	    else{
		printf("NO ESTAS REGISTRADO");
//Si no encuentra un usuario con el mismo nombre de usuario, 
//muestra el mensaje "NO ESTAS REGISTRADO".
	    }
    }     
}



void menu_estu(){
     //Este es un fragmento de c�digo en lenguaje 
     //C++ que define una funci�n llamada "menu_estu".
     printf("hola querido estudiante");
     //La funci�n muestra un mensaje de bienvenida y 
     //muestra un men� con varias opciones para el usuario.
     while(f!=3){
     //Luego, utiliza un bucle "while" para repetir 
     //el men� hasta que el usuario seleccione la opci�n de "EXIT".
        int opcion;
		printf("BIENVENIDOS AL COLEGIO \n      CASITA AZUL\n 1.VER NOTAS DEL ESTUDIANTE\n 2.VER PROMEDIO DE NOTAS \n 3.VER NOTAS MAS ALTA \n 4.EXIT\n ingrese una opcion\t");
		scanf("%d",&opcion);
		
		switch(opcion){
	
		
			case 1:{
                 //muestra las notas correspondientes a ese usuario.
                 printf("Nota 1: \n %d",N[i].nota_1);
                 printf("Nota 2: \n %d",N[i].nota_2);
                 printf("Nota 3: \n %d",N[i].nota_3);
                 break;
                 
				}
			case 2:{
                 int promedio=(N[i].nota_1+N[i].nota_2+N[i].nota_3)/3;
				 printf("Nota 3: \n %d",promedio);
				 break;
				}
			case 3:{
				if(N[i]nota_1>N[i]nota_2){
                   printf("Nota 1: \n %d",N[i].nota_1);                     
                   }
                   if else(N[i]nota_2>N[i]nota_3){
                       printf("Nota 2: \n %d",N[i].nota_2); 
                   }
                   else{
                       printf("Nota 3: \n %d",N[i].nota_3); 
                   }
              }
			case 4:{
			        f=4;
				
			     }
			default:
				printf("bi bu bi bu error vueleve a intentar");
		
		}	
	}    
    
    //dependiendo de la opci�n seleccionada por el usuario, la funci�n 
    //muestra las notas correspondientes al usuario, el promedio de las notas
    //o la nota m�s alta del estudiante ,Para cada opci�n, 
    //se utiliza la estructura de control "switch" para realizar diferentes
    //acciones en funci�n de la opci�n seleccionada por el usuario.
    //La funci�n tambi�n define una variable "f" que se utiliza para 
    //salir del bucle "while" cuando se selecciona la opci�n de "EXIT".
    
    
    
     
}
void menu_reg(){
//La funci�n permite al usuario registrar un nuevo usuario y contrase�a 
//en el sistema.

    	printf("INGRESAR \n Usuario");
    	scanf("%d",&reg_nom_user);
//Luego, utiliza la funci�n "scanf" para leer el nombre de usuario 
//ingresado por el usuario y lo guarda en una variable llamada 
//"reg_nom_user".
    	I[i].nom_user[i]+=reg_nom_user;
//A continuaci�n, el nombre de usuario se agrega al arreglo 
de nombres de usuario almacenado en la estructura "I" en la posici�n "i".                	
    	printf("\n contrase�a");
    	scanf("%d",&reg_pass_user[]);
    	I[i].pass_user[i]+=reg_pass_user;
                	
    	i+=1;
                	
//La contrase�a se agrega al arreglo de contrase�as almacenado 
//en la estructura "I" en la posici�n "i".	
//Finalmente, la funci�n incrementa la variable "i" en 1 para 
//que el pr�ximo usuario se registre en la siguiente posici�n del arreglo.
}
