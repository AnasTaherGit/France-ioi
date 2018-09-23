#include <bits/stdc++.h>

using namespace std;

deque<int> Chiffres;;

int Assembly(int base1){
	int r=0;
	int n=Chiffres.size();
	for (int i=n-1;i>=0;i--){
		r+=Chiffres[i]*pow(base1,i);
	}

	return r;
}

void Disassembly(int r,int base2){
	Chiffres.clear();
	while (r!=0){
		Chiffres.push_front(r%base2);
		r/=base2;
	}
}

int main(int argc, char const *argv[])
{
	int base1,base2,C,N;
	cin>>base1>>base2>>C;
	for (int i=0;i<C;i++){
		cin>>N;
		Chiffres.push_front(N);
	}

	N=Assembly(base1);
	cout<<N<<endl;
	Disassembly(N,base2);

	int n=Chiffres.size();

	for(int i=0;i<n;i++){
		cout<<Chiffres[i]<<' ';
	}

	cout<<endl;

	return 0;
}