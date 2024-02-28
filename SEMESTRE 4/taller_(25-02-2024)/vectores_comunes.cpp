#include <iostream>
using namespace std;

int vector_A[10] = {7,9,20,34,12,15,5,16,0,3};
int	vector_B[10] = {27,21,31,67,20,5,33,22,99};
int	vector_C[10] = {25,16,11,14,24,20,0,5,99};


int main() {
    
    cout << "Bienvenido al calculardora vector "<<endl;

    
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
     cout << endl;
    
    cout<<" los numeros comunes son: ";
    for(int i=0; i<10;i++){
    	for(int j=0; j<10;j++){
    	 	for(int k=0; k<10;k++){
    			if(vector_A[i]==vector_B[j] && vector_B[j]==vector_C[k]){
    				cout<<vector_A[i]<< " ";
				
				}		
			}
		}
	}
    cout << endl;
}
