#include <iostream>

using namespace std;

int matriz[4][4];
int numero_b,cantidad_b;

int main() {

    cout << "Bienvenido al calculardora Matriz 4x4"<<endl;

    for (int f = 0; f <= 3; f++) {
        for (int c = 0; c <= 3; c++) {
            cout << "Numero del fila [" << f+1 << "] y la columna [" << c+1 << "]: ";
            cin >> matriz[f][c];
        }
    }

    cout << "Esta es la Matriz: " << endl;
    for (int f = 0; f <= 3; f++) {
        for (int c = 0; c <= 3; c++) {
            cout << matriz[f][c] << "\t";
        }
        cout << endl;
    }
    
    
    cout << "Ingrese el numero que desea buscar en la matriz: ";
    cin >> numero_b;
    
    
    for (int f = 0; f <= 3; f++) {
        for (int c = 0; c <= 3; c++) {
            if (matriz[f][c] == numero_b) {
            	cout << "Numero fue encontrado en la fila [" << f+1 << "] y la columna [" << c+1 << "]"<<endl;
            	cantidad_b +=1;;
            }
        }
    }
    
    cout<<"la cantidad de numero encontados fueron: "<<cantidad_b<<endl;

    /*if(cantidad_b<=0){
        cout<< "No se encontro numero buscado."<<endl;
    }   
*/

}
	
