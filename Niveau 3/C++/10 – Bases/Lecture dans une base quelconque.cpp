#include <iostream>
#include <math.h>

using namespace std;

int main(int argc, char const *argv[])
{
	long long Base,Nbchiffres,R=0,Chiffres;
	cin>>Base>>Nbchiffres;

	for (int i=Nbchiffres-1;i>=0;i--){
		cin>>Chiffres;
		R+=(Chiffres*pow(Base,i));
	}

	printf("%lld", R);

	return 0;
}