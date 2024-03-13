#include <iostream>
using namespace std;
 
int op;
bool mseguir=true;
bool x=true;
int vector_cola[10];
int i;

int main(){
	
	do{
	
		cout<<"menu  Vector_cola"<<endl;
		cout<<"1. push "<<endl;
		cout<<"2. pop"<<endl;
		cout<<"3. front"<<endl;
		cout<<"4. back"<<endl;
		cout<<"5. mostra vector_cola"<<endl;
		cout<<"6. salir"<<endl;
		cout<<"ingresar la opcion:   ";
		cin>>op;
		
		
		
		
		switch(op){
			
			case 1:
				//push
			for(i=0;i<10;i++){
				
				if(vector_cola[i]!=0){
						
				//vector_cola[i]=vector_cola[i+1];
					
					
				}else if(x==true){ 
					
					cout<<"Ingrese el numero: "<<endl;
					cin>>vector_cola[i];
					x=false;
					
				}
				//cout<<x<<endl;;
			}
			x=true;
			break;	
//--------------------------------------------------------------------------------------
			case 2:
				// pop
				
				
				cout<<"dato elimindo "<<vector_cola[0]<<endl;
				vector_cola[0]=0;
				
				for(i=0;i<9;i++){
					
					//if(vector_cola[i]!=0)	{
					
					vector_cola[i]=vector_cola[i+1];
					//}
				//cout<<"---"<<vector_cola[1]<<endl;
				//cout<<vector_cola[i-1]<<endl;
				}
				
				//cout<<x<<endl;;
				
		
				break;
				
//--------------------------------------------------------------------------------------
			case 3:
				
						cout<<"dato front:  "<<vector_cola[0]<<endl;
			
				
				break;
			case 4:
				for(i=9;i>=0;i--){
					
					if(vector_cola[i]!=0){
						
				
					
					
					}else if(x==true){ 
						
						cout<<"dato BACK "<<vector_cola[i]<<endl;
						x=false;
						
					}
					
						
						
						
					
				}
				x=true;
			case 5:
				for(i=0;i<10;i++){
				
			
				
					if(vector_cola[i]!=0){
				
						cout<<vector_cola[i]<<endl;
					}
				}
					
				
				
				break;
			case 6:
				mseguir=false;
				break;
		
		}
		system("pause");
		system("cls");

		
	}
	while(mseguir==true);
	
}
