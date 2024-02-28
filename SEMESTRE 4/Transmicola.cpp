#include <iostream>
#include <queue>

using namespace std;

queue <int> bus1;
queue <int> t1, t2,t3;
//int pax;
int op ;
int opt;
bool mseguir=true;

int main(){
	
	do{
	
		cout<<"menu  TRANSMICOLA"<<endl;
		cout<<"1. Insertar pasajero bus "<<endl;
		cout<<"2. Enviar pasajero del bus al torniquete"<<endl;
		cout<<"3. Retiro de pasajeros torniquete"<<endl;
		cout<<"4. Pasajeros total en el Bus"<<endl;
		cout<<"5. Pasajeros por torniquete"<<endl;
		cout<<"6. salir"<<endl;
		cout<<"ingresar la opcion"<<endl;
		cin>>op;
		
		
		
		
		switch(op){
			
			case 1:
				//cout<<"Ingrese pasajero: ";
				//cin>>pax;
				//	 bus1.push(pax);
				
				bus1.push(1);
				cout<<"cantida de pasajeros bus: "<< bus1.size()<<endl;
				//cout<<bus1.back()<<endl;
				break;


//--------------------------------------------------------------------------------------
			case 2:
				if(t1.size()< 3){
					t1.push(1);
				}
				else if(t2.size()<3){
					
					t2.push(1);
				}
				else{
					t3.push(1);
				}
				cout<<"cantida de pasajeros Torniquete 1: "<<t1.size()<<endl;
				cout<<"cantida de pasajeros Torniquete 2: "<<t2.size()<<endl;
				cout<<"cantida de pasajeros Torniquete 3: "<<t3.size()<<endl;
				//cout<<t1.back()<<endl;
				bus1.pop();
				cout<<"cantida de pasajeros bus: "<< bus1.size()<<endl;
				break;
				
//--------------------------------------------------------------------------------------
			case 3:
				
				cout<<"Retiro pasagero en Torniquete"<<endl;
				cout<<"1. Retiro pasajero del Torniquete 1"<<endl;
				cout<<"2. Retiro pasajero del Torniquete 2"<<endl;
				cout<<"3. Retiro pasajero del Torniquete 3"<<endl;
				cout<<"Seleccione el torniquete: ";
				cin>>opt;
				
				cout<<endl;
				
				
				switch(opt){
			
					case 1:
						t1.pop();
						cout<<"Se retiro pasajero del Torniquete 1"<<endl;
						cout<<"cantida de pasajeros Torniquete 1: "<<t1.size();
						cout<<endl;
						break;
					case 2:
						t2.pop();
						cout<<"Se retiro pasajero del Torniquete 2"<<endl;
						cout<<"cantida de pasajeros Torniquete 2:  "<<t2.size();
						cout<<endl;
						break;
					case 3:
						t3.pop();
						cout<<"Se retiro pasajero del Torniquete 3"<<endl;
						cout<<"cantida de pasajeros Torniquete 3:  "<<t3.size()<<endl;
						cout<<endl;
						break;
					
				}
						
						break;
			case 4:
				cout<<"cantida de pasajeros bus: "<< bus1.size()<<endl;
				break;
			case 5:
				
				cout<<"cantida de pasajeros Torniquete 1: "<<t1.size()<<endl;
				cout<<"cantida de pasajeros Torniquete 2: "<<t2.size()<<endl;
				cout<<"cantida de pasajeros Torniquete 3: "<<t3.size()<<endl;
				break;
			case 6:
				cout<<op<<endl;
				mseguir=false;
				break;
		
		}
		system("pause");
		system("cls");

		
	}
	while(mseguir==true);
	
}


