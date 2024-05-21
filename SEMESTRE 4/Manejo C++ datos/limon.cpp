#include <iostream>
#include <cstdlib>

using namespace std;

int main() {
    // Definición de constantes y variables
    const int cant_pisos = 3;
    int asc_1[cant_pisos] = {0}; // Inicialización de ascensor 1
    int asc_2[cant_pisos] = {0}; // Inicialización de ascensor 2
    int cupo_1 = 0; // Inicialización de cupo de ascensor 1
    int cupo_2 = 0; // Inicialización de cupo de ascensor 2
    int Pisos[cant_pisos][cant_pisos] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};

    // Impresión inicial
    cout << "Estado inicial de los pisos:\n";
    for (int j = 0; j < cant_pisos; j++) {
        for (int i = 0; i < cant_pisos; i++) {
            cout << "  " << Pisos[j][i];
        }
        cout << endl;
    }

    // Ascensor 1 (bajando)
    cout << "\nAscensor 1 (bajando):\n";
    for (int j = 0; j < cant_pisos; j++) {
        for (int i = cant_pisos - 1; i >= 0; i--) {
            if (j != i && cupo_1 + Pisos[j][i] <= 6) {
                cupo_1 += Pisos[j][i];
                asc_1[i] += Pisos[j][i];
                Pisos[j][i] = 0;
            }
        }
        if (j == cant_pisos - 1) { // Si es la última iteración, manejar excepción descendente
            for (int i = cant_pisos - 1; i >= 0; i--) {
                if (j == i) { // Si j es igual a i, dejar la carga en el piso
                    cout << "Ascensor 1 deja " << Pisos[j][i] << " en el piso " << j + 1 << endl;
                    Pisos[j][i] = 0;
                }
            }
        }
    }

    // Ascensor 2 (subiendo)
    cout << "\nAscensor 2 (subiendo):\n";
    for (int j = cant_pisos - 1; j >= 0; j--) {
        for (int i = 0; i < cant_pisos; i++) {
            if (j != i && cupo_2 + Pisos[j][i] <= 6) {
                cupo_2 += Pisos[j][i];
                asc_2[i] += Pisos[j][i];
                Pisos[j][i] = 0;
            }
        }
        if (j == 0) { // Si es la última iteración, manejar excepción descendente
            for (int i = cant_pisos - 1; i >= 0; i--) {
                if (j == i) { // Si j es igual a i, dejar la carga en el piso
                    cout << "Ascensor 2 deja " << Pisos[j][i] << " en el piso " << j + 1 << endl;
                    Pisos[j][i] = 0;
                }
            }
        }
    }

    // Impresión final
    cout << "\nEstado final de los pisos:\n";
    for (int j = 0; j < cant_pisos; j++) {
        for (int i = 0; i < cant_pisos; i++) {
            cout << "  " << Pisos[j][i];
        }
        cout << endl;
    }

    // Total de carga en cada ascensor
    cout << "\nTotal carga en Ascensor 1: " << cupo_1 << endl;
    cout << "Carga por piso en Ascensor 1: ";
    for (int i = 0; i < cant_pisos; i++) {
        cout << asc_1[i] << " ";
    }
    cout << endl;

    cout << "Total carga en Ascensor 2: " << cupo_2 << endl;
    cout << "Carga por piso en Ascensor 2: ";
    for (int i = 0; i < cant_pisos; i++) {
        cout << asc_2[i] << " ";
    }
    cout << endl;

    return 0;
}

