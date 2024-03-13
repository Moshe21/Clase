#include <iostream>

using namespace std;

int i;
int num;
int factorial=1;
int main(){
	
	cout<<"numero a factorizar"<<endl;
	//cin>>num;
	num=5;
	
	cout<<num<<"!= ";
	for(i=num;i>0;i--){
		
		factorial=factorial*i;
		if(i==1){
			
			cout<<i;
		}else{
			
		cout<<i<<" x ";	
		}
		
		
		
	}
	cout<<" = "<<factorial<<endl;
	
}
