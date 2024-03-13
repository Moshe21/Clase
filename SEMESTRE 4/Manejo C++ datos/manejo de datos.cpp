#include <iostream>
#include <stack>

using namespace std;
stack <int> pila1;

int main(){
	
	//pila1.push(1);
	//pila1.push(9);
	//pila1.push(3);
	
	cout<<"tamaño de la pila es "<< pila1.size()<<endl;
	cout<<"estado de la pila es "<< pila1.empty()<<endl;
	cout<<"cima  de la pila es "<< pila1.top()<<endl;
	
	
	
	cout<<"cima  de la pila es "<< pila1.top()<<endl;
	
	if( pila1.empty()==0){
		
		cout<<"tiene datos la pila "<<endl;
	}else{
		
		cout<<"la pila  esta vacia"<<endl;
	}
}

