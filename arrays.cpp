#include<stdio.h>

int main(){
	int n;
	double arr[10];
	printf("coloque los numero que quiere ");
	scanf("%i",&n);
	
	for(int i=0;i<n;++i){
		printf("%d",i);
		scanf("%lf",&arr[i]);
		printf("su numero es: %d"&arr[i])
	}
	return 0;
}
