#include <iostream>
#include <vector>
using namespace std;

int v[1000];

void affichage(int l){
   for(int w=0;w<l;w++){
      cout<<v[w]<<' ';
   }
   cout<<endl;
}

void swap(int k){
   int temp;
   temp=v[k];
   v[k]=v[k-1];
   v[k-1]=temp;
}

int main(){
   int Nbv;
   cin>>Nbv;
   int min=1001;
   int index;
   vector<int> C;
   for (int i=0;i<Nbv;i++){
      cin>>v[i];
   }
   for (int i=0;i<Nbv-1;i++){
      //cout<<"i= "<<i<<endl;
      for (int j=i;j<Nbv;j++){
         if (v[j]<min){
            min=v[j];
            index=j;
         }
      }
      //cout<<"min= "<<min<<' '<<"index= "<<index<<endl;
      min=1001;
      for (int x=index;x>i;x--){
         C.push_back(v[x-1]);
         C.push_back(v[x]);
         swap(x);
         //affichage(Nbv);
      }
   }
   cout<<(int)(C.size())/2<<endl;
   for (int m=0;m<C.size();m=m+2){
      //cout<<m<<endl;
      cout<<C[m]<<' '<<C[m+1]<<endl;
   }
} 