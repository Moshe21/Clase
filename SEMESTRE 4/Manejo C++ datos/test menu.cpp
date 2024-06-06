#include <iostream>
using namespace std;
 
int op=0;
bool mseguir=true;


int main(){
	
	menu();
	
}
int menu(){
	
	do{
	cout<<"Bienvenidos Menu Arboles"<<endl; 
	cout<<"1. Ingrese los elemento" <<endl;
	cout<<"2. Mostrar Dato"<<endl;
	cout<<"3. Recorrer Pre-orden"<<endl;
	cout<<"4. Recorrer In-orden"<<endl;
	cout<<"5. Recorrer Post-orden"<<endl;
	cout<<"6. SALIR" <<endl;
	cout<<"Escoja una Opcion" <<endl;
	cin>>op;
	
	switch(op){
		
		case 1: cout<<"Ingrese los elementos al arbol"<<endl;
				cin>>dato;
				insertar(arbol,dato);
				cout<<"\n\n";	
			break;
		case 2: cout<<"Mostrar Dato"<<endl;
					mostrar (arbol,contador);
					cout<<"\n\n";		
			break;
		case 2: cout<<"Mostrar Dato"<<endl;
			mostrar (arbol,contador);
			cout<<"\n\n";		
			break;
		case 3: cout<<"recorrido Pre-orde"<<endl;
			RecorrerPre-orden(arbol);
			cout<<"\n\n";
				
			break;
		case 4: cout<<"Recorrer In-orden"<<endl;
				RecorrerIn-orden (arbol);	
				cout<<"\n\n";	
			break;
		case 5: cout<<"Recorrer Post-orden"<<endl;
				mostrar (arbol);
				cout<<"\n\n";		
			break;
		case 6: mseguir=false;
			break;
	}
	system("pause");
	
	system("cls");
	
	
	}
	while (mseguir==true);
	
			
}
/*
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
*/


