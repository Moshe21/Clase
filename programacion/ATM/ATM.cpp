#include <stdio.h>


//Decalracion de funciones 
void deposit();
void balace();
void withdrawal();
int validate(int account_num_temp,int password_temp);
int x;
int i;

struct account_details{
	int account_no;
	int password;
	int amount;	
};



int account_num_temp;
int password_temp;
int amount_temp;


struct account_details s[3]={{25,54,0},{26,1234,0},{27,4987,0}};

//ejecucionb de funciones
int main(){
	
	while(1){
		
		int choice;
		printf("\"---BIENVENIDO A LA BANCA DEL SANTI---\n");
		printf("1. DEPOSIT\n2. WITHDRAWAL \n3. BALANCE ENQUIRY  \n4. EXIT/n ENTER YOUR CHOICE\t");	
		scanf("%d",&choice);
		
		switch (choice){
			case 1:{
				deposit();
				break;
			}
			case 2:{
				withdrawal();
				break;
			}
			case 3:{
				balace();
				break;
			}
			case 4:{
				printf("\n NO HAY SALIDA \n");
				exit(1);
				break;
			}
			default:
				printf("Enter a Valid choice\n");
		
		}
	
	
	}
}
int validate(int account_num_temp,int password_temp){

	for(i=0;i<3;i++){
		
		if(s[i].account_no==account_num_temp){
			if(s[i].password==password_temp){
				printf("SI ERES TU 'w' ");
				return i;
				break;
			}
		}
		else{
			printf("\n ERES UN FALSO Y TRAIDOR");
			exit(1);
		}
		
		
	}
	
return 0;
}

void deposit(){
	
	printf("\n Enter the account Number\t ");
	scanf("%d",&account_num_temp);
	printf(" Enter the amount to deposit\t");
	scanf("%d",&amount_temp);
	printf("\n Enter the password\t");
	scanf("%d",&password_temp);
	
	x=validate(account_num_temp,password_temp);
	
	s[x].amount+=amount_temp;
	printf("\n USD: %d have been successfully account ");
}

void balace(){
	
	printf("\n Enter the account number\t");
	scanf("%d",&account_num_temp);
	printf("\n Enter the password\t");
	scanf("%d",&password_temp);
	
	x=validate(account_num_temp,password_temp);
	
	printf("\n Your account No: %d contrains Rs%d",account_num_temp,s[x].amount);
	
}

void withdrawal(){
	
	printf("\n Enter the account Number\t ");
	scanf("%d",&account_num_temp);
	printf(" Enter the amount to deposit\t");
	scanf("%d",&amount_temp);
	printf("\n Enter the password\t");
	scanf("%d",&password_temp);
	
	x=validate(account_num_temp,password_temp);
	
	if(s[x].amount<amount_temp){
		printf("\n there is not chances");
	}
	
	else{
		s[x].amount-=amount_temp;
		printf("\n USD: %d have been successfully account ");
	}
}




