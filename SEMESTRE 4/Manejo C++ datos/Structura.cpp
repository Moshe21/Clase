#include<iostream>

using namespace std;

struct personas{
	int codigo;
	string nombre;
	string apellido;
	
};
int i;
personas datos[2];

int main(){
	
	for(i=0;i<=1;i++){
		
		cout<<"ingresa el codigo"<<endl;
		cin>>datos[i].codigo;
		cout<<"ingresa el nombre"<<endl;
		cin>>datos[i].nombre;
		cout<<"ingresa el apellido"<<endl;
		cin>>datos[i].apellido;
	}
	for(i=0;i<=1;i++){
	
	cout<<"codigo "<<datos[i].codigo<<endl;
	cout<<"nombre "<<datos[i].nombre<<endl;
	cout<<"apellido "<<datos[i].apellido<<endl;
	}
}
