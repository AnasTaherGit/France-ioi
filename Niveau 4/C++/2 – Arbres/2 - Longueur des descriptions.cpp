#include <bits/stdc++.h>

using namespace std;

typedef struct Node {
	vector<int> next;
}Node;

void Initialisation(Node* Reserve,int N){
	int temp;
	for (int i=1;i<=N;i++){
		cin>>temp;
		Reserve[temp].next.push_back(i);
	}
}

int longuestPath(int n,Node* Reserve){
	Node p=Reserve[n];
	int longuest=1;
	if (p.next.empty()) return longuest;

	for (int i=0;i<(signed)p.next.size();i++){
		int nextLonguest=longuestPath(p.next[i],Reserve)+1;
		if (nextLonguest>longuest) longuest=nextLonguest;
	}

	return longuest;
}

int main(int argc, char const *argv[])
{
	int N;
	cin>>N;
	Node Reserve[N+1];
	Initialisation(Reserve,N);
	cout<<longuestPath(0,Reserve)-1;
	return 0;
}
