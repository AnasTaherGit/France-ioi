#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[])
{
	int entierConvertir,baseArrivee;
	int nbrChiffre=0;

	deque<int> v;

	cin>>entierConvertir>>baseArrivee;


	if (entierConvertir!=0){
		while (entierConvertir!=0){
			v.push_front(entierConvertir%baseArrivee);
			entierConvertir/=baseArrivee;
			nbrChiffre++;
		}

		cout<<nbrChiffre<<endl;

		for (auto x:v){
			cout<<x<<' ';
		}

		cout<<endl;
	}
	else cout<<1<<endl<<0;

	return 0;
}