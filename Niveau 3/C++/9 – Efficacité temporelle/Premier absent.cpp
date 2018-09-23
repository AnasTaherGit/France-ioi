#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
	int N,P,LastAbsent=0;
	cin>>N>>P;
	bool Classe[P]={false};

	for (int i=0;i<P;i++){
		int temp;
		cin>>temp;
		if (temp<P) Classe[temp-1]=true;
		//else cout<<"ça depasse"<<endl;
		//cout<<Classe[temp-1]<<endl;
		if (i+1==N){
			printf("-1");
		}

		else{
			for (int j=LastAbsent;j<=i+1;j++){
				//cout<<Classe[j]<<endl;
				if (Classe[j]==false){
					printf("%d ", j+1);
					cout<<Classe[j]<<endl;
					LastAbsent=j;
					break;
				}
			}
		}
	}

	return 0;
}
