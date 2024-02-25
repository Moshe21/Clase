#include <iostream>

using namespace std;

string matriz[3][3];
int numero_b,cantidad_b;

int main() {

    cout << "Bienvenido al calculardora Matriz 4x4"<<endl;

    for (int f = 0; f <= 3; f++) {
        for (int c = 0; c <= 3; c++) {
            cout << "Numero del fila [" << f+1 << "] y la columna [" << c+1 << "]: ";
            cin >> matriz[f][c];
        }
    }
