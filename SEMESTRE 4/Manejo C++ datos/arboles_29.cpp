#include <iostream>
using namespace std;
int i,j,dato,contador;
bool mseguir= true;
int op;
int b_nodo;
int cont;
int nivel_maximo;

//que almacena la ram(stock se crean las variables y en hib quedan los nodos )	
struct NodoA
{
	int dato;
	NodoA *der;
	NodoA *izq;
	
};



NodoA *arbol=NULL;

NodoA *crearNodo(int d)
{
	NodoA*nnodo=new NodoA();
	nnodo->dato=d;
	nnodo->der=NULL;
	nnodo->izq=NULL;
	
	return nnodo;
}

// opcion 1
void insertar (NodoA *& arbol,int d)
{
	if (arbol==NULL)
	{
		NodoA * nnodo=crearNodo(d);
		
		if(arbol == nnodo){
		
			cout<<"numero repetido"<<endl;
		
		}else{
			arbol=nnodo;
		
		}
		
		
	}
	else 
	{	
			int valorRaiz=arbol->dato;
				if (d<valorRaiz)
				{
					insertar(arbol->izq,d);
				}
				else
				{
					insertar(arbol->der,d);
				}
				
		
		
	}
}


// opcion 2
void mostrar(NodoA*arbol,int cont)
{
	if (arbol==NULL)
	{
		return;
	}
	
	else
	{
		mostrar(arbol->der,cont+1);
		for(int i= 0;i<cont;i++){
			cout<<"\t";		
			}
		cout<<arbol->dato<<"\n";
		mostrar(arbol->izq,cont+1);
	}
}
// opcion 3
void buscar_nodo(NodoA *&arbol){
	
	if(arbol==NULL){
	
	
	cout<<"  "<<cont; 
		return;
	}else{
		
			
			cont=cont+1;
		}
		
		
	buscar_nodo(arbol->izq);
	buscar_nodo(arbol->der);
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
void RecorrerPostorden(NodoA *&arbol){


	if(arbol==NULL){
	
		return;
	}else{
		
		RecorrerPostorden(arbol->izq);
		RecorrerPostorden(arbol->der);
		cout<<arbol->dato<<"\t";
	}
}




int menu(){
	
	do{
	cout<<"Bienvenidos Menu Arboles"<<endl; 
	cout<<"1. Ingrese los elemento" <<endl;
	cout<<"2. Mostrar Dato"<<endl;
	cout<<"3. buscar_nodo"<<endl;
	cout<<"4. nivel_arbol"<<endl;
	cout<<"5. Recorrer Postorden"<<endl;
	cout<<"6. SALIR" <<endl;
	cout<<"Escoja una Opcion" <<endl;
	cin>>op;
	
	switch(op){
		
		case 1: cout<<"Ingrese los elementos al arbol"<<endl;
				cin>>dato;
				insertar(arbol,dato);
				cout<<"\n\n";
				cout<<arbol;	
				system("cls");
			break;
		case 2: cout<<"Mostrar Dato"<<endl;
				mostrar(arbol,contador);
				cout<<"nivel de arbol es: "<<contador;
				cout<<"\n\n";		
			break;
		case 3: cout<<"Buscar un nodo dentro del árbol"<<endl;
				cout<<"ingrese el nodo a buscar"<<endl;
				cin>>b_nodo;
				buscar_nodo(arbol);
				cout<<"\n\n";
			break;
		case 4: cout<<"nivel de nodo"<<endl;
				nivel_arbol(arbol,cont,nivel_maximo);	
				cout<<"nivel de arbol es: "<<contador;
				cout<<"\n\n";	
			break;
		case 5: cout<<"Recorrer Postorden"<<endl;
				RecorrerPostorden(arbol);
				cout<<"\n\n";		
			break;
		case 6: mseguir=false;
			break;
	}
	system("pause");
	
//	system("cls");
	
	
	}
	while (mseguir==true);
	
			
}

	

int main ()
{
	menu();		
	
}
