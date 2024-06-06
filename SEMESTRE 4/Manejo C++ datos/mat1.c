#include <iostream>

using namespace std;

int mat1[3][3];
int f;
int c;
int sumatoria;
 
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
	 cout<<sumatoria<<endl;
 }