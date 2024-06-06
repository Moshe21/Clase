#include <iostream>
#include <stack>
#include <cstdlib>

using namespace std;
//stack <int> asc_1,asc_2;
//int Pisos[2]=[5,6];
int cant_pisos=30;
string mseguir;
int viajes;

int main(){
		
	cout<<"servi_asc "<<endl;
	cout<<endl;
	
	
	//variables
	int asc_1[cant_pisos]={},
		asc_2[cant_pisos]={};
	int cupo_1,cupo_2;
	int per_pisos;
	int Pisos[cant_pisos][cant_pisos]={};
	int desc=(cant_pisos-1);

	int s=6;
	int asc=0;
		
	for(int j=0;j<cant_pisos;j++){			
		for(int i=0;i<cant_pisos;i++){
			
		Pisos[j][i]= rand() % 2;
			
		}
	}
	
	
//			do{
//		for(int x=0;x<10;x++){
	
	//impresion inicial
		cout<<"inicios pisos :"<<endl;
		for(int i=0;i<cant_pisos;i++){
						
			for(int j=0;j<cant_pisos;j++){
//				cout<<"  "<<Pisos[j][i];
				per_pisos=per_pisos+Pisos[j][i];
				}	
				
				//cout<<endl;
			
			cout<<" piso "<< i+1<<" es: "<<per_pisos<<endl;	
			per_pisos=0;
			}
			
		
			
		
				
			
				//cupo de ascensor 1
				for(int j=0;j<cant_pisos;j++){
					for(int i=0;i<cant_pisos;i++){
						
					
						if(i==desc){		
							desc=desc-1;
							Pisos[j][i]=Pisos[j][i]+asc_1[j];
							for(cupo_1;cupo_1<6;cupo_1--){
									
									cout<<"se bajo pasajero: "<<j<<" cupo: "<<cupo_1<<endl;	
							}
							
						}
						else if((cupo_1+Pisos[j][i])<=6){
						
						cupo_1=cupo_1+Pisos[j][i];
						
						asc_1[j]=asc_1[j]+Pisos[j][i];
						Pisos[j][i]=0;
						
						//cout << "Ascensor 1 deja " << Pisos[j][i] << " en el piso " << j+1 << endl;
						}
			
					
							
					}
					//	cout<<endl;
					//	cout<<endl;
					
			
				}
				//cupo de ascensor 2
				for(int j=(cant_pisos-1);j>=0;j--){
					for(int i=(cant_pisos-1);i>=0;i--){
						
						
						if(i==asc){	
							asc=asc+1;	
							Pisos[j][i]=Pisos[j][i]+asc_2[j];
							for(cupo_2;cupo_2<6;cupo_2--){
									
									cout<<"se bajo pasajero: "<<j<<" cupo: "<<cupo_2<<endl;	
							}
			
					
						}	
						else if((cupo_2+Pisos[j][i])<=6){
						
							cupo_2=cupo_2+Pisos[j][i];
							asc_2[j]=asc_2[j]+Pisos[j][i];
							Pisos[j][i]=0;
							//cout<<"     "<<asc_2[i]<<endl;
							//cout << "Ascensor 2 subiendo " << Pisos[j][i] << " en el piso " << j+1  << endl;
							}
						
						
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
//				cout<<"  "<<Pisos[j][i];
				per_pisos=per_pisos+Pisos[j][i];
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
		viajes=viajes+1;
				s=cupo_1;
				cout<<s<<endl;
//	}
//		cout<<viajes<<endl;
//		cout<<"otro viaje ";
//		cin>>mseguir;		
//	}
	
			
//			while (mseguir=="si");
	
		
		
	
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










