#include <iostream>

using namespace std;

int mat1[3][3];
int f;
int c;
int sumatoria;
int suma_Fila_1;
int suma_Fila_2;
int suma_Fila_3;
 
int main (){
 	
 	
 	for(f=0;f<=2;f++){
 		
 		for(c=0;c<=2;c++){
 		
			cout<<"ingrese el elemento ["<<f<<"]["<<c<<"]"<<endl;
			cin>>mat1[f][c] ;		
		 }
	 }
	 for(f=0;f<=2;f++){
 		
 		for(c=0;c<=2;c++){
 		
			cout<<mat1[f][c]<<"\t";
			
			sumatoria=sumatoria+mat1[f][c];
					
		 }
		 cout<<endl;
	 }
	 for(f=0;f<=2;f++){
 		
 		for(c=0;c<=2;c++){
 		
			cout<<mat1[f][c]<<"\t";
			
			sumatoria=suma_Fila_1+mat1[0][c];
			sumatoria=suma_Fila_2+mat1[1][c];
			sumatoria=suma_Fila_3+mat1[2][c];
					
		 }
		 cout<<endl;
	 }
	 
	 cout<<suma_Fila_1<<endl;
	 cout<<suma_Fila_2<<endl;
	 cout<<suma_Fila_3<<endl;
 }
