#include <iostream>
#include <fstream>

using namespace std;

ofstream archivo;
int cod, edad;
string nom,ape;
 
main(){
	
	archivo.open("datos.txt");
	for(int i=0;i<3;i++){
	
	cout<<"ingrese el codigo"<<endl;
	cin>>cod;
	cout<<"ingrese el nombre"<<endl;
	cin>>nom;
	cout<<"ingrese el apellido"<<endl;
	cin>>ape;
	cout<<"ingrese el edad"<<endl;
	cin>>edad;
	
	
	archivo<<cod<<","<<nom<<","<<ape<<","<<edad<<endl;
	system("cls");
	}
}
