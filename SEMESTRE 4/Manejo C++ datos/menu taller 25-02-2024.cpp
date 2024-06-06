#include <iostream>
using namespace std;
int op, dato;
bool mseguir=true;

//-------------------------------------------------------
int vector_1[10];
int promedio_par,suma_impar,num_promedio;
double resultado_p, resutado_s;
//-------------------------------------------------------
int matriz_1[4][4];
int numero_b,cantidad_b;
//-------------------------------------------------------
string matriz_2[3][3];

//-------------------------------------------------------
int vector_A[10] = {7,9,20,34,12,15,5,16,0,3};
int	vector_B[10] = {27,21,31,67,20,5,33,22,99};
int	vector_C[10] = {25,16,11,14,24,20,0,5,99};
					
//-------------------------------------------------------					




int main(){

	do{
		
		cout<<"menu  manejaos de pila"<<endl;
		cout<<"1. suma promedio "<<endl;
		cout<<"2. buscador matriz "<<endl;
		cout<<"3. matriz inversa "<<endl;
		cout<<"4. vectores comunes"<<endl;
		cout<<"5. salir"<<endl;
		cout<<"ingresar la opcion"<<endl;
		cin>>op;
		
		switch(op){
			
			case 1: 
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
					
					break;
			case 2:
					    cout << "Bienvenido al calculardora Matriz 4x4"<<endl;
					
					    for (int f = 0; f <= 3; f++) {
					        for (int c = 0; c <= 3; c++) {
					            cout << "Numero del fila [" << f+1 << "] y la columna [" << c+1 << "]: ";
					            cin >> matriz_1[f][c];
					        }
					    }
					
					    cout << "Esta es la Matriz: " << endl;
					    for (int f = 0; f <= 3; f++) {
					        for (int c = 0; c <= 3; c++) {
					            cout << matriz_1[f][c] << "\t";
					        }
					        cout << endl;
					    }
					    
					    
					    cout << "Ingrese el numero que desea buscar en la matriz: ";
					    cin >> numero_b;
					    
					    
					    for (int f = 0; f <= 3; f++) {
					        for (int c = 0; c <= 3; c++) {
					            if (matriz_1[f][c] == numero_b) {
					            	cout << "Numero fue encontrado en la fila [" << f+1 << "] y la columna [" << c+1 << "]"<<endl;
					            	cantidad_b +=1;
					            }
					        }
					    }
					    
					    cout<<"la cantidad de numero encontados fueron: "<<cantidad_b<<endl;

				
					break;
					
			case 3: 
					    cout << "Bienvenido al calculardora Matriz 4x4"<<endl;
					
					    for (int f = 0; f <3; f++) {
					        for (int c = 0; c < 3; c++) {
					            cout << "Numero del fila [" << f+1 << "] y la columna [" << c+1 << "]: ";
					            cin >> matriz_2[f][c];
					        }
					    }
					    
					    cout << "Esta es la Matriz original: " << endl;
					    for (int f = 0; f < 3; f++) {
					        for (int c = 0; c < 3; c++) {
					            cout << matriz_2[f][c] << "\t";
					        }
					        cout << endl;
					    }
					    cout << "Esta es la Matriz inversa " << endl;
					    for (int f = 0; f < 3; f++) {
					        for (int c = 0; c < 3; c++) {
					            cout << matriz_2[c][f] << "\t";
					        }
					        cout << endl;
					    }
					    break;
					
			case 4: 
 
					    cout << "Bienvenido al calculardora vector "<<endl;
					
					    
					     cout << "Vector A: ";
					    for (int i = 0; i < 10; i++) {
					        cout << vector_A[i] << " ";
					    }
					    cout << endl;
					     
					     cout << "Vector B: ";
					    for (int i = 0; i < 10; i++) {
					        cout << vector_B[i] << " ";
					    }
					    cout << endl;
					        
					
					      cout << "Vector C: ";
					    for (int i = 0; i < 10; i++) {
					        cout << vector_C[i] << " ";
					    }
					     cout << endl;
					    
					    cout<<" los numeros comunes son: ";
					    for(int i=0; i<10;i++){
					    	for(int j=0; j<10;j++){
					    	 	for(int k=0; k<10;k++){
					    			if(vector_A[i]==vector_B[j] && vector_B[j]==vector_C[k]){
					    				cout<<vector_A[i]<< " ";
									
									}		
								}
							}
						}
					    cout << endl;
			
			
					break;
					
			case 5:
				mseguir=false;
		
					break;
				
		}
		system("pause");
		system("cls");
		
	
	}
	while(mseguir==true);
}
