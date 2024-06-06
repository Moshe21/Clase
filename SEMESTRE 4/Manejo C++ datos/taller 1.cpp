#include <iostream>
using namespace std;


int vector_1[10];
int promedio_par,suma_impar,num_promedio;
double resultado_p, resutado_s;

int main() {
    
    cout << "Bienvenido al calculardora vector "<<endl;
    for (int i = 0; i < 10; ++i) {
    	cout << "digite Numero de la posicion " << i + 1 << ": ";
        cin >>vector_1[i];
    }

   
    cout << "Vector:" << endl;
    for (int i = 0; i < 10; ++i) {
        cout << vector_1[i] << " ";
    }
    cout << endl;

  


    for (int i = 0; i < 10; ++i) {
        if (vector_1[i] % 2 == 0) {
            promedio_par += vector_1[i];
            num_promedio++;
        } else {
            suma_impar += vector_1[i];
        }
    }
    if (num_promedio > 0) {
        resultado_p = promedio_par / num_promedio;
    } else {
        resultado_p = 0; 
    }
    

    
    cout << "Promedio de los numeros pares: " << resultado_p << endl;
    cout << "Sumatoria de los numeros impares: " << suma_impar << endl;
}

