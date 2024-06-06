#include <iostream>
#include <fstream>

using namespace std;

ifstream archivo;
string leerregistro;

int main(){
	
	archivo.open("datos.txt");
	if(archivo.fail())
	{
		cout<<"archivo no encontrado"<< endl;
		exit(0);
	}
	else
	{
		
		for(int i=0;i<3;i++){
		
		//while(archivo.eof()){
			archivo>>leerregistro;
			cout<<"dato del registro encontrado es:"<<leerregistro<<endl;
			
		}
		cout<<"fin"<<endl;
		archivo.close();
	}
}
