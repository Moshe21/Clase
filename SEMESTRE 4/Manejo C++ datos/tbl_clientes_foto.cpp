#include <iostream>

using namespace std;

struct Dclientes{
	int CodCli;
	string NomCli;
	string ApeCli;
	int cantidad_Fotos;
	int Valor_Unitario;

	
};

Dclientes dato[1];
int i;
int op;
bool mseguir=true;
int main(){
	
	do{
		
		cout<<"menu "<<endl;
		cout<< "1.ingresos de personal"<<endl;
		cout<<"2. mostra info"<<endl;
		cout<<"3. opcion "<<endl;
		cout<<"4. opcion"<<endl;
		cout<<"5. opcion"<<endl;
		cout<<"6. salir"<<endl;
		cout<<"ingresar la opcion"<<endl;
		cin>>op;
		
		switch(op){
			
			case 1: 
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
					
					break;
			case 2:
				
					for(int i=0;i<=1;i++){
						cout<<"el codigo CodCli "<<dato[i].CodCli<<endl;
						
						cout<<"ingrese el NomCli "<<dato[i].NomCli<<endl;
						
						cout<<"ingrese el ApeCli  "<<dato[i].ApeCli<<endl;
						
						cout<<"ingrese el cantidad_Fotos "<<dato[i].cantidad_Fotos<<endl;
						
						cout<<"ingrese el Valor_Unitario*Foto "<<dato[i].Valor_Unitario<<endl;
						
						}
						
					break;
					
			case 3:
					break;
					
			case 4: 
					break;
					
			case 5:
				
					break;
					
			case 6: mseguir=false;
		
					break;
				
		}
		
		system("pause");
		system("cls");
		
	
	}
	while(mseguir==true);
	//}
	
	//while(mseguir=true);
	
	
	
}

