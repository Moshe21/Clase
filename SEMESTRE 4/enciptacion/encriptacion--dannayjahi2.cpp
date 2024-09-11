#include <iostream>
using namespace std;

char alf[26] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
char cadena[100]; 

int main() {
   
    char doi[26];
    for (int i = 0; i < 26; i++) {
        doi[i] = alf[(i + 3) % 26];
    }

    
    cout << "Ingresa tu mensaje: ";
    cin.getline(cadena, 100);

    
    cout << "Mensaje encriptado: ";
    for (int j = 0; cadena[j] != '\0'; j++) {
        char c = cadena[j];
	
       if (c >= 'a' && c <= 'z') {
            int frase = c - 'a'; 
            char encritacion = doi[original_index]; 
            cout << encrypted_char;
        } else {
            cout << c;
        }
    }
    cout << endl;

    return 0;
}

