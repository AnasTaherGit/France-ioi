#include <iostream>
#include <math.h>

using namespace std;


int main(int argc, char const *argv[]){
	string N;
	long long R=0,n;
	cin>>N;
	n=N.size();
	//printf("%lld\n", N);
	for (int i = 0; i < n; ++i){
		//printf("%c\t", N[n-i-1]);
		if (N[n-i-1]=='1'){
			R+=pow(2,i);
		}
	}
	printf("%lld",R);
	return 0;
}