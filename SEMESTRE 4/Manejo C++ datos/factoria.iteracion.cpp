#include <iostream>

using namespace std;

int num;
int factorial(int n){
	
	if(n==0){
		return 1;
	}else{
		
		n=n*factorial(n-1);
	}	
	return n;
}


int main(){
	
	
	cout<< "ingrese el numero a factorial"<<endl;
	cin>>num;
	cout<<factorial(num);
	
	
}
