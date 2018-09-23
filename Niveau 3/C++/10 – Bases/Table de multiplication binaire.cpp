#include <bits/stdc++.h>

using namespace std;

string convert(int x){
	string num="";
	while (x!=0){
		num=(char)(48+x%2)+num;
		x/=2;
	}

	return num;
}


int main(int argc, char const *argv[])
{
	string Table[15][15];

	int N;
	cin>>N;



	for (int i=0;i<15;i++){
		for(int j=0;j<15;j++){
			Table[i][j]=convert((i+1)*(j+1));
		}
		//cout<<endl;
	}

	for (int i=0;i<N;i++){
		for(int j=0;j<N;j++){
			cout<<Table[i][j]<<'\t';
		}
		cout<<endl;
	}


	return 0;
}