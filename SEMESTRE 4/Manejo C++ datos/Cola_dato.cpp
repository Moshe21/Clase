#include <iostream>
#include <queue>

using namespace std;

queue <int> cola1;
int dato;
int main(){
	
	for(int i=1;i<=4;i++){
		
		cout<<"ingrese el dato de la cola"<<endl;
		cin>>dato;
		cola1.push(dato);
		
	}
	

	cout<<"cuantos datos hay en la cola "<<cola1.size()<<endl;
	cout<<"primer dato de la coLa es "<<cola1.front()<<endl;
	cout<<"ultimo dato de la cola es "<<cola1.back()<<endl;
	
	cola1.pop();
	cout<<"primer dato de la coLa es "<<cola1.front()<<endl;
	cout<<"ultimo dato de la cola es "<<cola1.back()<<endl;
	
}
