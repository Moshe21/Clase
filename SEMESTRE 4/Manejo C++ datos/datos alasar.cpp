#include <iostream>
#include <time.h>
#include <stdlib.h>

using namespace std;

int dado_1,dado_2;

main (){
	
	srand(time(NULL));
	cout<<"creacion de dados al azar"<<endl;
	
		
		dado_1=1+rand()%(6);
		dado_2=1+rand()%(6);
		
		if(dado_1 == dado_2){
		cout<<"el numero fue un par, felicitaciones"<<endl;
		}else{
		cout<<"los dados no fueron pares"<<endl;
		}
		cout<<"el Resultado de los dados fue"<<endl;
		cout<<"   "<<dado_1<<"  "<<dado_2<<endl;
		
}
