
#include <stdio.h>
#include <string.h>
#define i 6

void menu_ing();
void menu_reg();
void menu_prof();
void menu_estu();

char reg_nom_user[];
char reg_pass_user[];	
char pass_user [];
char nom_user [];


struct info_user{
 
	char reg_nom_user[i];
	char reg_pass_user[i];	
}I[i];

int main (){
	int f;
	
	while(f!=3){
        int opcion;
		printf("BIENVENIDOS AL COLEGIO \n      CASITA AZUL\n 1.INGRESAR\n 2.REGISTRASE\n 3.EXIT\n ingrese una opcion\t");
		scanf("%d",opcion);
		
		switch(opcion){
	
		
			case 1:{
					menu_ing();
					break;
				}
			case 2:{
					menu_reg();
					break;
				}
			case 3:{
					f=3;
				
				}
			default:
				printf("bi bu bi bu error vueleve a intentar");
		
		}	
	}
	
	printf("QUE TENGO UN BUEN DIA LES DESEA\n COLEGIO \n      CASITA AZUL ");

				
};

void menu_ing(){
	
	printf("INGRESAR \n Usuario");
	scanf("%d",nom_user[i]);
	
	printf("\n contraseña");
	scanf("%d", pass_user[i]);
	
	for(int j=0;j<i;j++){
            
    	if(I[j].reg_nom_user[i]==nom_user[i] && I[j].reg_pass_user[50]==pass_user[50]){
    		
    		menu_prof();
    	}
    	if else(I[i].reg_nom_user[50]==nom_user[50] && I[i].reg_pass_user[50]==pass_user[50]){
    		printf("hola querido estudiante");
    		menu_estu();
	    }
	    else{
		printf("NO ESTAS REGISTRADO");
	    }
	
    }
}

void menu_reg(){
	
	printf("INGRESAR \n Usuario");
	scanf("%d",nom_user[]);
	I[i].reg_nom_user=nom_user[];
	
	printf("\n contraseña");
	scanf("%d", pass_user);
	I[i].reg_pass_user=pass_user;
	
	i++;
}

void menu_profe(){
	
	printf("Bienvenido querido profesor\n 1.INGRESAR\n 2.REGISTRASE\n 3.EXIT\n ingrese una opcion\t");
	printf("INGRESAR \n Usuario del estudiante");
	scanf("%d",nom_user[]);
	
	if(I[i].reg_nom_user==nom_user[]){
		
		printf("INGRESAR \n Usuario");
		scanf("%d",nom_user[]);
		I[i].reg_nom_user=nom_user[];
	}

	
	printf("\n contraseña");
	scanf("%d", pass_user[]);
}
// me quede verificancion de  profe  meter las calificaciones - estudiantes

