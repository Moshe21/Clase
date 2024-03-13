#include <iostream>
#include <stack>

using namespace std;
stack <int> pila;
int op, dato;
bool mseguir=true;



int main(){

	do{
		
		cout<<"menu  manejaos de pila"<<endl;
		cout<< "1.insertar elementos"<<endl;
		cout<<"2. mostrar la cima"<<endl;
		cout<<"3. eliminar elemento"<<endl;
		cout<<"4. tamaño"<<endl;
		cout<<"5. estado"<<endl;
		cout<<"6. salir"<<endl;
		cout<<"ingresar la opcion"<<endl;
		cin>>op;
		
		switch(op){
			
			case 1: cout<<"ingrese el dato"<<endl;
					cin>>dato;
					pila.push(dato);
					break;
			case 2:cout<<"el dato mas reciente fue: "<<pila.top()<<endl;
					break;
					
			case 3: if(pila.empty()==1){
					cout<<"no hay datos para eliminar "<<pila.top()<<endl;
					}
					else{
					cout<<"el dato mas reciente fue: "<<pila.top()<<endl;
					pila.pop();
					cout<<"el dato fue eliminado"<<endl;}
					break;
					
			case 4: cout<<"la cantidad de elementos fue: "<<pila.size()<<endl;
					break;
					
			case 5:
				if(pila.empty()==0){
					cout<<"hay datos en la pila"<<endl;
					cout<<""<<endl;
					}
				else{
					
					cout<<"la pila no tiene datos"<<endl; 
					cout<<""<<endl;
				}
					break;
					
			case 6: mseguir=false;
		
					break;
				
		}
		system("pause");
		system("cls");
		
	
	}
	while(mseguir==true);
}
