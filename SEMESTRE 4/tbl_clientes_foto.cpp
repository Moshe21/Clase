#include <iostream>

using namespace std;

struct Dclientes{
	int CodCli;
	string NomCli;
	string ApeCli;
	int cantidad_Fotos;
	int Valor_Unitario;
	
};

Dclientes dato[2];
int i;
int main(){
	
	//do(){
		for(i=0;i<=1;i++){
		
		cout<<"ingrese el Codigo "<<endl;
		cin>> dato[i].CodCli;
		cout<<"ingrese el Nombre "<<endl;
		cin>> dato[i].NomCli;
		cout<<"ingrese el Apellido"<<endl;
		cin>> dato[i].ApeCli;
		cout<<"ingrese el cantidad de Fotos"<<endl;
		cin>> dato[i].cantidad_Fotos;
		cout<<"ingrese el Valor Unitario"<<endl;
		cin>> dato[i].Valor_Unitario;
	}
	for(int i=0;i<=1;i++){
		cout<<"el codigo CodCli "<<dato[i].CodCli<<endl;
		
		cout<<"ingrese el NomCli "<<dato[i].NomCli<<endl;
		
		cout<<"ingrese el ApeCli  "<<dato[i].ApeCli<<endl;
		
		cout<<"ingrese el cantidad_Fotos "<<dato[i].cantidad_Fotos<<endl;
		
		cout<<"ingrese el Valor_Unitario*Foto "<<dato[i].Valor_Unitario<<endl;
		
	}
	//}
	
	//while(mseguir=true);
	
	
	
}

