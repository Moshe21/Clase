#include <iostream>
#include <stack>
#include <queue>


using namespace std;

int vector1[10];
int dato;
stack <int> pila1;
queue <int> cola1;


int main(){
	
	for(int i=0;i<10;i++){
		
		cout<<"ingrese el dato a almacenar"<<endl;
		cin>>vector1[i];
		
	}	
	cout<<" el vector es el siguente"<<endl;
	for(int i=0;i<10;i++){
	
		cout<<vector1[i] <<"\t";
	}
	cout<<" "<<endl;
	for(int i=0;i<10;i++){
		
		if(vector1[i]<5){
		 	pila1.push(vector1[i]);
		 	cout<<"la pila fue "<<pila1.top()<<endl;
		 	
		}
		else if(vector1[i]>=5){
			cola1.push(vector1[i]);
			cout<<"la cola fue "<<cola1.back()<<endl;
		}
		
		
	}
	cout<<"la cantidad de elemento en la pila fue: "<<pila1.size()<<endl;
	cout<<"la cantidad de elemento en la cola fue: "<<cola1.size()<<endl;
	
}

