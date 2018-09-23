#include <bits/stdc++.h>

using namespace std;

typedef struct Produit {
	int parent;
}Produit;

void Initialisation(Produit* Reserve,int N){
	for (int i=0;i<N;i++){
		cin>>Reserve[i].parent;
	}
}

string find(int code,Produit* Reserve){
	string path=to_string(code);
	Produit currentProd=Reserve[code-1];
	while (currentProd.parent!=0){
		path=to_string(currentProd.parent)+' '+path;
		currentProd=Reserve[currentProd.parent-1];	
	}
	return path;
}

int main(int argc, char const *argv[])
{
	int N,R;
	cin>>N;
	Produit Reserve[N];
	Initialisation(Reserve,N);
	cin>>R;
	for (int i=0;i<R;i++){
		int code;
		cin>>code;
		string path=find(code,Reserve);
		cout<<path<<endl;
	}

	return 0;
}