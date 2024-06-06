#include <iostream>
using namespace std;

int dato, contador = 0;
bool mseguir = true;
int op;
int b_nodo = 0;
int cont = 0;
int nivel_maximo = 0;
int nivel= 0;
int peso;
int hojas; 
int ramas;
int cont_izquierda = 0;
int cont_derecha = 0;

struct NodoA {
    int dato;
    NodoA* der;
    NodoA* izq;
};

NodoA* arbol = NULL;

NodoA* crearNodo(int d) {
    NodoA* nnodo = new NodoA();
    nnodo->dato = d;
    nnodo->der = NULL;
    nnodo->izq = NULL;
    return nnodo;
}

// opcion 1
void insertar(NodoA*& arbol, int d) {
    if (arbol == NULL) {
        NodoA* nnodo = crearNodo(d);
        arbol = nnodo;
    } else {
        if (arbol->dato == d) {
            cout << "Lo siento el numero " << d << " ya existe en el árbol." << endl;
            return;
        }
        int valorRaiz = arbol->dato;
        if (d < valorRaiz) {
            insertar(arbol->der, d);
        } else {
            insertar(arbol->izq, d);
        }
    }
}

// opcion 2
void mostrar(NodoA* arbol, int cont) {
    if (arbol == NULL) {
        return;
    } else {
        mostrar(arbol->der, cont + 1);
        for (int i = 0; i < cont; i++) {
            cout << "\t";
        }
        cout << arbol->dato << "\n";
        mostrar(arbol->izq, cont + 1);
    }
}

// opcion 3
void buscar_nodo(NodoA* arbol, int b_nodo, int nivel, int& cont_izquierda, int& cont_derecha) {
    if (arbol == NULL) {
        return;
    } else {
        if (arbol->dato == b_nodo) {
            cout << "El nodo " << b_nodo << " se encontró en el nivel " << nivel << endl;
            cout << "Número de veces que fue a la izquierda: " << cont_izquierda << endl;
            cout << "Número de veces que fue a la derecha: " << cont_derecha << endl;
            return;
        }
        cont_izquierda += (arbol->izq != NULL);
        cont_derecha += (arbol->der != NULL);
    }

    buscar_nodo(arbol->izq, b_nodo, nivel+ 1, cont_izquierda, cont_derecha);
    buscar_nodo(arbol->der, b_nodo, nivel+ 1, cont_izquierda, cont_derecha);
}



// opcion 4
void nivel_arbol(NodoA* arbol, int cont, int& nivel_maximo) {
    if (arbol == NULL) {
        if (cont > nivel_maximo) {
            nivel_maximo = cont;
        }
        return;
    } else {
        nivel_arbol(arbol->izq, cont + 1, nivel_maximo);
        nivel_arbol(arbol->der, cont + 1, nivel_maximo);
    }
}

// opcion 5
void RecorrerPostorden(NodoA*& arbol) {
    if (arbol == NULL) {
        return;
    } else {
        RecorrerPostorden(arbol->izq);
        RecorrerPostorden(arbol->der);
        cout << arbol->dato << "\t";
    }
}

// opcion 6
int peso_arbol(NodoA* arbol) {
    if (arbol == NULL) {
        return 0;
    } else {
        int altura_izquierda = peso_arbol(arbol->izq);
        int altura_derecha = peso_arbol(arbol->der);
        return 1 + max(altura_izquierda, altura_derecha);
    }
}

// opcion 7
bool es_arbol_lleno(NodoA* arbol) {
    if (arbol == NULL) {
        return true;
    }
    if ((arbol->izq == NULL && arbol->der == NULL) || (arbol->izq != NULL && arbol->der != NULL)) {
        return es_arbol_lleno(arbol->izq) && es_arbol_lleno(arbol->der);
    }
    return false;
}

// opcion 8
int contar_ramas(NodoA* arbol) {
    if (arbol == NULL) {
        return 0;
    }
    if (arbol->izq == NULL && arbol->der == NULL) {
        return 1;
    }
    return contar_ramas(arbol->izq) + contar_ramas(arbol->der);
}

int contar_hojas(NodoA* arbol) {
    if (arbol == NULL) {
        return 0;
    }
    if (arbol->izq == NULL && arbol->der == NULL) {
        return 1;
    }
    return contar_hojas(arbol->izq) + contar_hojas(arbol->der);
}

// opcion 9

void RecorrerPreorden(NodoA *&arbol){
	
	if(arbol==NULL){
	
		return;
	}else{
		
		cout<<arbol->dato<<"\t";
	}	
	RecorrerPreorden(arbol->izq);
	RecorrerPreorden(arbol->der);
}

void RecorrerInorden(NodoA *&arbol){


	if(arbol==NULL){
	
		return;
	}else{
		
		RecorrerInorden(arbol->izq);
		cout<<arbol->dato<<"\t";
		RecorrerInorden(arbol->der);
	}
}
/*
void RecorrerPostorden(NodoA *&arbol){

	if(arbol==NULL){
	
		return;
	}else{
		
		RecorrerPostorden(arbol->izq);
		RecorrerPostorden(arbol->der);
		cout<<arbol->dato<<"\t";
	}
}

*/
int menu() {
    do {
        cout << "Bienvenidos Menu Arboles" << endl;
        cout << "1. Ingrese los elementos" << endl;
        cout << "2. Mostrar Dato" << endl;
        cout << "3. Buscar nodo" << endl;
        cout << "4. Nivel del arbol" << endl;
        cout << "5. Peso del arbol" << endl;
        cout << "6. Arbol binario lleno o no" << endl;
        cout << "7. Cuantas ramas y hojas" << endl;
        cout << "8.recorridos preorden, inorden, postorden " << endl;
        cout << "0. SALIR" << endl;
        cout << "Escoja una Opcion" << endl;
        cin >> op;

        switch (op) {
            case 1:
                cout << "Ingrese los elementos al arbol" << endl;
                cin >> dato;
                insertar(arbol, dato);
                cout << "\n\n";
                system("pause");
                system("cls");
                break;
            case 2:
                cout << "Mostrar Dato" << endl;
                mostrar(arbol, contador);
                cout << "nivel de arbol es: " << contador << endl;
                cout << "\n\n";
                system("pause");
                
                break;
			case 3:
					{
					    cout << "Buscar un nodo dentro del árbol" << endl;
					    int b_nodo;
					    cout << "Ingrese el nodo a buscar: ";
					    cin >> b_nodo;
					
					    int cont_izquierda = 0;
					    int cont_derecha = 0;
					    buscar_nodo(arbol, b_nodo, 1, cont_izquierda, cont_derecha);
				
					    system("pause");
					    system("cls");
					}
					break;

			    
            case 4:
                cout << "Nivel del arbol" << endl;
                nivel_arbol(arbol, 0, nivel_maximo);
                cout << "Nivel maximo del arbol: " << nivel_maximo << endl;
                cout << "\n\n";
                system("pause");
                system("cls");
                break;
            case 5:
                cout << "Calcular el peso del árbol" << endl;
			    peso = peso_arbol(arbol);
			    cout << "El peso del árbol es: " << peso << endl;
			    cout << "\n\n";
			    system("pause");
			    system("cls");
                break;
            case 6:
				if (es_arbol_lleno(arbol)) {
			        cout << "El árbol es un árbol binario lleno." << endl;
			    } else {
			        cout << "El árbol no es un árbol binario lleno." << endl;
			    }
			    cout << "\n\n";
			    system("pause");
			    system("cls");
		    break;
		    
			case 7:
			    ramas = contar_ramas(arbol);
			    hojas = contar_hojas(arbol);
			    cout << "El árbol tiene " << ramas << " ramas." << endl;
			    cout << "El árbol tiene " << hojas << " hojas." << endl;
			    cout << "\n\n";
			    system("pause");
			    system("cls");
			    break;
			case 8:
			    cout << "recorrido Preorden" << endl;
			    RecorrerPreorden(arbol);
			    cout << "\n\n";
			
			    cout << "Recorrer Inorden" << endl;
			    RecorrerInorden(arbol);
			    cout << "\n\n";
			
			   	cout<<"Recorrer Postorden"<<endl;
				RecorrerPostorden(arbol);
				cout<<"\n\n";		
				break;
			    
		case 0:
		    mseguir = false;
		    break;
		
			}
		} while (mseguir);

    		return 0;
	
}
int main() {
    menu();
}

