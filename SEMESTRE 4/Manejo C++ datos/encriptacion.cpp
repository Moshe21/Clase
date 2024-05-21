#include <iostream>


using namespace std;

string alf={"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"};
string doi[26];
string letra[10];

string cadena;


int main(){
	
	cout<<" la letras es "<<endl;
	for(int i=0;i<26;i++){
		cout<<" "<<alf[i];
	}
/*	cout<<endl;
	cout<<" la encriptado 3 pasos es "<<endl;
		for(int i=0;i<26;i++){
			if((i+3)<26){
			cout<<" "<<alf[i+3];
			}else{
			cout<<" "<<alf[i-23];	
			}
	}*/
	cout<<endl;
	cout<<"la matriz encriptado 7 pasos es "<<endl;
		for(int i=0;i<26;i++){
			if((i+3)<26){
			doi[i]=alf[i+3];
			cout<<" "<<doi[i];
			}else{
			doi[i]=alf[i-22];
			cout<<" "<<doi[i];	
			}
	}
	cout<<endl;
	cout<<"la ingresa tu mensaje "<<endl;
	

	
		cin>>cadena;
	


	for(int j =0 ; j<10;j++){
	
		for(int i=0;i<26;i++){
			cout<<cadena[j];
			//if(alf[i]==cadena[j]){
				
				cout<<alf[i+3];
		//	}
			
		}
		
	}	
	

 
}
