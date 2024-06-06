#include <iostream>


using namespace std;



/*int n=1;
int base=1, exponente=1; 

int numerofac;
int factorial (int n);
int fac=1;

*/
int op;
bool mseguir=true;
int num;
int repetir;
int vector[10];

int respuesta;


int potencia(int num, int repetir) {
    
    if (repetir == 0){
        return 1;
        }
    else{
    	respuesta=num*potencia(num,repetir-1);
    	
	}
     return respuesta;
}

int factorial(int num){
	
	if(num==1){
		cout<<num;
		return 1;
		
	}else{
		
		
		cout<<num<<" + ";
		respuesta=num+factorial(num-1);
	}	
	return respuesta;
}

int vector_1(int num){
	
	if(num==0){
		
		num=10;
		
	}else{
		
		cout<<"ingrese elemento["<<num<<"]"<<endl;
		cin>>vector[num];
		respuesta=vector_1(num-1);
	}
	cout<<endl;
	cout<<vector[num]<<"\t";	
	
	/*if(num==0){
		

		
	}else{
		
		cout<<vector[num]<<"\t";
		respuesta=vector_1(num-1);
	}	
	return respuesta;
	*/
}
/*int factorial (int n) {
	if (n==1)
	{
		cout<<n;
		
	}
	else {
		cout<<n<<"*";
		fac=n*factorial(n-1);
	
	}
	return fac;*/
int main() {

    

    do {
        cout<< "MENU"<<endl;
        cout<< "1. Elevar un numero a una potencia"<<endl;
        cout<< "2. Calcular la factorial de un numero"<<endl;
        cout<< "3. Imprimir un vector de 10 elementos utilizando recursividad"<<endl;
        cout<< "4. Ordenar un arreglo de enteros de menor a mayor"<<endl;
        cout<< "5. Invertir los números de un arreglo de enteros"<<endl;
        cout<< "6. Imprimir una matriz de 3x3 utilizando recursividad"<<endl;
        cout<< "7. Calcular el valor de la posicion Fibonacci usando recursividad"<<endl;
        cout<< "8. Verificar si una cadena es palindromo"<<endl;
        cout<< "9. Salir"<<endl;
        cout<< "Ingrese su opcion: "<<endl;
        cin>>op;

        switch (op) {
            case 1:
                cout << "Ingrese la numero: "<<endl;
                cin >> num;
                cout << "Ingrese el cuanto lo quiere potenciar: "<<endl;
                cin >> repetir;
                cout << "El resultado de " <<num << "^" << repetir << " es: " << potencia(num, repetir) << endl;
                break;
            case 2:
            	cout<<"Ingrese el numero a calcular la factorial"<<endl;
            	cin>>num;
            	cout<<"="<<factorial(num)<<endl;
                break;
                
            case 3:
            	num=10;
                vector_1(num);
            	break;
            	
            case 9:
            	mseguir=false;
				break;
        }
        	system("pause");
			system("cls");
			
    } while (mseguir==true);

}

	

