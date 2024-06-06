#include <iostream>

using namespace std;

int num=5;
int fac=1;

int factorial(int n){
	
	if(n==1){
		cout<<n;
		return 1;
		
	}else{
		
		cout<<vector[n]<<endl;
		
		fac=n+factorial(n-1);
	}	
	return fac;
}
int main(){
	
	
	cout<< "ingrese el numero a factorial"<<endl;
	cin>>num;
	//cout<<num<<"=! ";
	cout<<" = "<<factorial(num);
}
