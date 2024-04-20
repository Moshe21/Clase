#include <iostream>
#include <stack>

using namespace std;


stack <int> pila1, pila2;
int dato,b_dato,sw=0;


int main(){



	for(int i=1;i<=4;i++){
	system("cls");
	cout<<"ingrese elemento numerico a la pila "<<endl;
	cin>>dato;
	pila1.push(dato);
	}
	cout<<"ingrese el elemento numerico a buscar "<<endl;
	cin>>b_dato;
	int a=pila1.size();
	
	for(int i=1;i<=a;i++){
		
		if(pila1.top()==b_dato){
			
			sw=1;
			
		}
		else{
			
			pila2.push(pila1.top());
			pila1.pop();
		}
		
		
 	}
 	
 	if(sw==0){
 		cout<< "NO HAY DATO BUSCADO "<<endl;
	 }
	 else{
	 	cout<< "el elemento se encuentra en la pila "<<endl;
	 }
	 cout<<"tamaño de la pila2  "<<pila2.size()<<endl;
	 
	 int b=pila2.size();
	 for(int i=1;i<=b;i++){
		
			pila1.push(pila2.top());
			pila2.pop();
			cout<<"cima de la pila 1 es "<<pila1.top()<<endl;
		}
	 cout<<"tamaño de la pila1  "<<pila1.size()<<"  cima de la pila1 es "<<pila1.top()<<endl;
	 
	 
}
