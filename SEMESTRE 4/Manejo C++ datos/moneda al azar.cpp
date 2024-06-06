#include <iostream>
#include <time.h>
#include <stdlib.h>

using namespace std;

int moneda;
string seguir;

main (){
	
	srand(time(NULL));
	

		do{
		cout<<"creacion de dados al azar"<<endl;
		moneda=1+rand()%(2);
		
		
		if(moneda == 2){
		cout<<"salio cara"<<endl;
		}else{
		cout<<"salio sello"<<endl;
		}
		
		cout<<"quiere seguir"<<endl;
		cout<<"si / no"<<endl;
		cin>>seguir;
		system("cls");
		if(seguir=="si"){
			seguir="si";
		}else if(seguir=="no"){
			cout<<"saliste del sistema"<<endl;
			seguir="no";
		}else{
			cout<<"no entendi"<<endl;
			seguir="no";
		}
		}while(seguir=="si");
		
	
	
		
}
