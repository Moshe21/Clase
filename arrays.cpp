#include<stdio.h>

int main(){
	int n;
	double arr[10];
	printf("coloque los numero que quiere ");
	scanf("%i",&n);
	
	for(int i=0;i<n;++i){
		for(int c=0;c<n;++c){
			printf("%d: ",c);
		}
		printf("ingrese su %d: ",i+1);
		scanf("%i",&arr[i]);
		/**printf("su numero es: %i",arr[i]);**/
	}
	return 0;
}
