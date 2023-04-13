#include <stdio.h>

int main(){

	int num1,num2,num3;
	printf("ingrese su numero\n");	
	scanf(" %d %d %d",&num1,&num2,&num3);
	/**printf("%d\n",num1);
	printf("%d\n",num2);
	printf("%d\n",num3);
**/
	if(num1>num2 && num1>num3){
		printf("el numero %d mayor a numero %d",num1,num3);
	}
	else if(num2>num1 && num2>num3){
	
		printf("el numero %d mayor a numero %d",num2,num3);
	}
	else if(num3>num1 && num3>num2){
	
		printf("el numero %d mayor a numero %d",num3,num1);
	}
}
