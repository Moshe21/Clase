#include <iostream>
using namespace std;

char alf[26] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
char cadena[100];
int normal ; 

int main() {
   
    char doi[26];
    for(int i=0;i<26;i++){
			if((i+3)<26){
			doi[i]=alf[i+3];
			
			}else{
			doi[i]=alf[i-22];
				
			}
	}

    
    cout << "Ingresa tu mensaje: ";
    cin>>cadena;

    
    cout << "Mensaje encriptado: ";
    for (int j = 0; cadena[j] != '\0'; j++) {
        char longitud = cadena[j];
       
        if (longitud >= 'a' && longitud <= 'z') {
            normal = longitud - 'a'; 
            char encriptacion = doi[normal]; 
            cout << encriptacion;
    	}
    }
    cout << endl;

    return 0;
}


