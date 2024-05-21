#include <iostream>
using namespace std;
int i,j,dato,contador;
bool mseguir= true;
int op;
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

void insertar (NodoA *& arbol,int d)
{
	if (arbol==NULL)
	{
		NodoA * nnodo=crearNodo(d);
		arbol=nnodo;
		
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
	cout<<"3. Recorrer Preorden"<<endl;
	cout<<"4. Recorrer Inorden"<<endl;
	cout<<"5. Recorrer Postorden"<<endl;
	cout<<"6. SALIR" <<endl;
	cout<<"Escoja una Opcion" <<endl;
	cin>>op;
	
	switch(op){
		
		case 1: cout<<"Ingrese los elementos al arbol"<<endl;
				cin>>dato;
				insertar(arbol,dato);
				cout<<"\n\n";	
				system("cls");
			break;
		case 2: cout<<"Mostrar Dato"<<endl;
				mostrar(arbol,contador);
				cout<<"\n\n";		
			break;
		case 3: cout<<"recorrido Preorde"<<endl;
				RecorrerPreorden(arbol);
				cout<<"\n\n";
			break;
		case 4: cout<<"Recorrer Inorden"<<endl;
				RecorrerInorden(arbol);	
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
