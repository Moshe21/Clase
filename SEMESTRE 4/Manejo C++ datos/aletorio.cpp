#include <iostream>
#include <time.h>
#include <stdlib.h>


using namespace std;

int a;

main(){
	
	srand(time(NULL));
	cout<<"creacion de 10 numero entre 1 y 10"<<endl;
	for(int i=1;i<10;i++){
		
		a=1+rand()%(10);
		cout<<a<<endl;
	}
}
