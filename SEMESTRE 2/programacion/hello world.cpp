#include <stdio.h>

int main (){
	
	while(1){
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
					exit(1);
				}
			default:
				printf("bi bu bi bu error vueleve a intentar");
		
		}	
	}			
}

menu_ing(){
	int opcion
	printf("INGRESAR \n Usuario");
	scanf("%d", opcion);
	printf("\n contraseña");
	scanf("%d", opcion);
	
}

 
