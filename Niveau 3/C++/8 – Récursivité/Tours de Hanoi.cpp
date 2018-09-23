#include <iostream>
using namespace std;

void deplacer(int n, int a,int b, int c){
      
      if (n==1) cout<<a<<" -> "<<c<<endl;
      else {
         deplacer(n-1,a,c,b);
         deplacer(1,a,b,c);
         deplacer(n-1,b,a,c); 
      }
} 

int main(){
   int N;
   cin>>N;
   deplacer(N,1,2,3);
   return 0;
}