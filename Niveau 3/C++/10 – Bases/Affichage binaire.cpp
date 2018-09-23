#include <iostream>

using namespace std;

int BitLength(int n){
	int e=0;
	while (n!=0){
		n/=2;
		e++;
	}

	return e;
}

int power(int n,int e){
	int r=1;
	for (int k=1;k<=e;k++){
		r=r*n;
	}

	return r;
}

int main(int argc, char const *argv[])
{
	int N;
	cin>>N;
	if (N==0) printf("0");
	else{
		for (int s,i=BitLength(N)-1;i>=0;i--){
			s=power(2,i);
			// printf("%d\n", s);
			printf("%d",N/s );
			N%=s;
			// printf(" %d\n",N );
		}
	}
	return 0;
}