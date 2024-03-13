#include <iostream>

using namespace std;

int vector_mat[10];
int i=0;
int sum,rest,multi=1;
int promedio_mat;

int main(){

	
//	------------------------------------------------------------------------------
//	actividad 1
	cout<<"1.calculadora C++"<<endl;
	for (i=0;i<10;i++){
		
		cout<<"ingrese numero de de la posicion "<<i+1<<endl;
		cin>>vector_mat[i];
		
		sum=sum+vector_mat[i];
		rest=rest-vector_mat[i];
		multi=vector_mat[i]*multi;
		//sum=1+sum;
		//rest=rest-1;
		//multi=2*multi;
			 
	}
	cout<<"la suma de todos elementos de vector "<<sum<<endl;
	cout<<"la resta de todos elementos de vector "<<rest<<endl;
	cout<<"la multiplicacion de todos elementos de vector "<<multi<<endl;
//	------------------------------------------------------------------------------
//	actividad 2

	promedio_mat=sum/10;
		
	
	cout<<"-------------------------------------------------"<<endl;
	cout<<"2.Promedio C++"<<endl;
	cout<<"el promedio de todos elementos de vector "<<promedio_mat<<endl;





//	------------------------------------------------------------------------------
//	actividad 3
	cout<<"-------------------------------------------------"<<endl;
	cout<<"3.Notas C++"<<endl;
	
	int vector_nota[5];
	int nota;
	int promedio_nota;
	
	for(i=0;i<5;i++){
		cout<<"ingrese la nota "<<i+1<< " del estudiante"<<endl;
		cin>>vector_nota[i];
		nota=nota+vector_nota[i];	
	}
	promedio_nota=nota/5;
	
	//if deficiente
	if(promedio_nota<=5){
		cout<<"el estudiante fue deficiente con la nota "<<promedio_nota<<endl;
	}
	//if regular
	else if(promedio_nota<=10){
		cout<<"el estudiante fue regular con la nota "<<promedio_nota<<endl;
	}
	//if bueno
	
	else if(promedio_nota<=15){
		cout<<"el estudiante fue bueno con la nota "<<promedio_nota<<endl;
	}
	//if bueno
	else if(promedio_nota<20){
		cout<<"el estudiante fue excelente con la nota "<<promedio_nota<<endl;
	}
	//error de datos
	else{
		cout<<"error de datos ingresados"<<endl;	
	}
	



	
}
