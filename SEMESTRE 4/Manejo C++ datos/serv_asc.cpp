#include <iostream>
#include <stack>
#include <cstdlib>

using namespace std;
//stack <int> asc_1,asc_2;
//int Pisos[2]=[5,6];
int cant_pisos=3;


int main(){
		
	cout<<"servi_asc "<<endl;
	cout<<endl;
	
	
	//variables
	int asc_1[cant_pisos]={},
		asc_2[cant_pisos]={};
	int cupo_1,cupo_2;
	int per_pisos;
	int Pisos[cant_pisos]={};
	int desc=(cant_pisos-1);
	int asc=0;
		
	for(int j=0;j<cant_pisos;j++){			
		//for(int i=0;i<cant_pisos;i++){
			
		Pisos[j]= rand() % 2;
			
	//	}
	}
	
	
	
	
	//impresion inicial
		cout<<"inicios pisos :"<<endl;
		for(int i=0;i<cant_pisos;i++){
						
			for(int j=0;j<cant_pisos;j++){
				cout<<"  "<<Pisos[j];
				per_pisos=per_pisos+Pisos[j];
				}	
				
				//cout<<endl;
			
			cout<<" piso "<< i+1<<" es: "<<per_pisos<<endl;	
			per_pisos=0;
			}
			
		

	

	//cupo de ascensor 1
	for(int j=0;j<cant_pisos;j++){
		
			
		
			if(j==desc){		
				desc=desc-1;
				Pisos[j]=Pisos[j]+asc_1[j];
				cupo_1=cupo_1-1;
				
			}
			else if((cupo_1+Pisos[j])<=6){
			
			cupo_1=cupo_1+Pisos[j];
			
			asc_1[j]=asc_1[j]+Pisos[j];
			Pisos[j]=0;
			
			//cout << "Ascensor 1 deja " << Pisos[j][i] << " en el piso " << j+1 << endl;
			}

		
				
		
		//	cout<<endl;
		//	cout<<endl;
		

	}
	//cupo de ascensor 2
	for(int j=(cant_pisos-1);j>=0;j--){
	
			
			
			if(j==asc){	
				asc=asc+1;	
				Pisos[j]=Pisos[j]+asc_2[j];
				if(asc_2[j]<6){
						cupo_2=cupo_2-1;
						cout<<"se bajo pasajero: "<<j<<" cupo: "<<cupo_2<<endl;	
				}

		
			}	
			else if((cupo_2+Pisos[j])<=6){
			
				cupo_2=cupo_2+Pisos[j];
				asc_2[j]=asc_2[j]+Pisos[j];
				Pisos[j]=0;
				//cout<<"     "<<asc_2[i]<<endl;
				//cout << "Ascensor 2 subiendo " << Pisos[j][i] << " en el piso " << j+1  << endl;
				}
			
			
			
		//	cout<<endl;
		//		cout<<endl;
	}

		//cupo de pisos
		cout<<endl;
		cout<<"total cupo ascensor 1 es:  "<<cupo_1<<endl;
		cout<<"total cupo ascensor 2  es: "<<cupo_2<<endl;
			cout<<endl;
		//impresion final
		for(int i=0;i<cant_pisos;i++){			
			for(int j=0;j<cant_pisos;j++){
				cout<<"  "<<Pisos[j];
				per_pisos=per_pisos+Pisos[j];
				}	
				
				//cout<<endl;
			
			cout<<" piso "<< i+1<<" es: "<<per_pisos<<endl;	
			per_pisos=0;
		}
			cout<<endl;
		
		for(int i=0;i<cant_pisos;i++){
			
			if(asc_1[i]<0){
				cout<<"     "<<asc_1[i];
			}
			
			
			}	
			cout<<"     "<<endl;
		for(int i=0;i<cant_pisos;i++){
			
			if(asc_1[i]<0){
				cout<<"     "<<asc_2[i];
			}
		}		
	
		
	
		
		
	
}



	/*
	if(Pisos[3][]1){
	
	
		for(int i=0 ;i<2;i++){
			
		cout<<"ingrese personas de ascensor"<<endl;
		cin>>dato;
		asc_1.push(dato);
		}
	/*}
	else if(Piso==1){
	
		for(int b=0 ;b<2;b++){*/










