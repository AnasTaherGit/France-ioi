#include <iostream>
#define L 101
#define C 101

using namespace std;

typedef struct point{
	int x;
	int y;
}point;


void get_middle(int tab[][C],point p1,point p2){

	int sumX=p1.x+p2.x;
	int sumY=p1.y+p2.y;
	if (sumX%2==0 && sumY%2==0){
		if (tab[sumX/2][sumY/2]==1){

			tab[sumX/2][sumY/2]=2;
			//cout<<sumX/2<<' '<<sumY/2<<' '<<tab[sumX/2][sumY/2]<<endl;
		}
	}
}


int main(int argc, char const *argv[])
{
	int tab[L][C]={0};
	point P[1000];
	point S;
	int NbPoints,N=0;
	cin>>NbPoints;

	for (int i=0;i<NbPoints;i++){
		cin>>P[i].x;
		cin>>P[i].y;
		tab[P[i].x][P[i].y]=1;
	}
	point p1,p2;
	for (int i=0;i<NbPoints;i++){
		p1=P[i];
		for (int j=0;j<NbPoints;j++){
			if (i!=j){
				p2=P[j];
				get_middle(tab,p1,p2);
			}

		}
	}
	for (int i=0;i<L;i++){
		for (int j=0;j<C;j++){
			if (tab[i][j]>1){ 
				N++;
				//cout<<i<<' '<<j<<' '<<tab[i][j]<<endl;
			}
		}
	}

	cout<<N;

	return 0;
}