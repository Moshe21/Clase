#include <iostream>
using namespace std;
 
int op=0;
bool mseguir=true;


int main(){
	
	do{
	cout<<"Bienvenidos Menu Supremo"<<endl; 
	cout<<"1. opcion 1" <<endl;
	cout<<"2. opcion 2"<<endl;
	cout<<"SALIR" <<endl;
	cout<<"Escoja una Opcion" <<endl;
	cin>>op;
	switch(op){
		
		case 1: cout<<"ingreso a la opcion 1"<<endl;
		
			break;
		case 2: cout<<"ingreso a la opcion 2"<<endl;
		
			break;
		case 3: mseguir=false;
			break;
	}
	system("pause");
	
	system("cls");
	
	
	}
	while (mseguir==true);
	
			
}
