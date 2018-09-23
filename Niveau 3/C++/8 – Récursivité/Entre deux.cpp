#include <iostream>

using namespace std;

void f(int n,int m){
   
   if (n==m){
      cout<<m<<' ';
   }
   else {
      cout<<n<<' ';
      f(n+1,m);
   }
}

int main(){
   
   int N,M;
   cin>>N>>M;
   f(N,M);

   return 0;
}