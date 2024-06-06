#include <iostream>
using namespace std;

int vector_A[10],vector_B[10],vector_C[10];

int num_igual=0;

int main() {
    
    cout << "Bienvenido al calculardora vector "<<endl;
    
    cout << "ingrese los datos del Vector A: "<<endl;
    for (int i = 0; i < 10; ++i) {
    	cout << "digite Numero de la posicion " << i + 1 << ": ";
        cin >>vector_A[i];
        vector_comun[i]=vector_A[i];
    }
    cout << endl;
    
    
    cout << "ingrese los datos del Vector B: "<<endl;   
    for (int i = 0; i < 10; ++i) {
    	cout << "digite Numero de la posicion " << i + 1 << ": ";
        cin >>vector_B[i];
        vector_comun[i+10]=vector_B[i];
    }
    cout << endl;
    
    cout << "ingrese los datos del Vector C: "<<endl;  
        for (int i = 0; i < 10; i++) {
    	cout << "digite Numero de la posicion " << i + 1 << ": ";
        cin >>vector_C[i];
        vector_comun[i+20]=vector_C[i];
    }
    cout << endl;
    
    
     cout << "Vector A: ";
    for (int i = 0; i < 10; i++) {
        cout << vector_A[i] << " ";
    }
    cout << endl;
     
     cout << "Vector B: ";
    for (int i = 0; i < 10; i++) {
        cout << vector_B[i] << " ";
    }
    cout << endl;
        

      cout << "Vector C: ";
    for (int i = 0; i < 10; i++) {
        cout << vector_C[i] << " ";
    }
    
    for(int i=0; i<10;i++){
    	 for(int j=0; j<10;j++){
    	 	 for(int k=0; k<10;k++){
    			if(vector_A[i]==vector_A[i] &&)
	}
    cout << endl;
    
