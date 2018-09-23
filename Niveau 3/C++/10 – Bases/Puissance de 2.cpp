#include <iostream>

using namespace std;

int power(int n,int e){
	int r=1;
	for (int i=1;i<=e;i++){
		r=r*n;
	}

	return r;
}

int main(int argc, char const *argv[])
{
	int N,e=0;
	cin>>N;
	while (N!=0){
		N/=2;
		e++;
	}

	printf("%d\n",power(2,e-1));

	return 0;
}