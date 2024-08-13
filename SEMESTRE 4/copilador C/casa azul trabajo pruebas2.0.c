#include<stdio.h>
void deposit();
void withdrawal();
void balance();
int validate(int account_numb_temp,int passwd_temp);
int i,x;
int account_numb_temp;
int amount_temp;
int passwd_temp;
struct account_details
{
	int account_no;
	int password;
	int amount;
};
struct account_details s[3]={{12343432,1234,0},{12343433,5678,0},{89877182,1098,0}};	
int main()
{
	while(1)
	{
		int choice;
		printf("\n---ATM MACHINE---\n");
		printf("1. DEPOSIT\n2. WITHDRAWAL\n3. BALANCE ENQUIRY\n4. EXIT\nEnter Your Choice\t");
		scanf("%d",&choice);
		switch(choice)
		{
			case 1:
			{
				deposit();
				break;	
			}
			case 2:
			{
				withdrawal();
				break;	
			}	
			case 3:
			{
				balance();
				break;		
			}
			case 4:
			{
				exit(1);	
			}
			default:
				printf("Enter a Valid choice\n");
		}	
	}		
}
