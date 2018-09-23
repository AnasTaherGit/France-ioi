#include <iostream>

using namespace std;


char Sp[64][64]={' '};

void Sierpinski(int i,int j,int N){
   //cout<<i<<' '<<j<<endl;

   if (N==1){
      Sp[i][j]='#';
      //cout<<Sp[i][j]<<endl;
   }
   else{
      Sierpinski(i,j,N/2);
      Sierpinski(i+N/2,j,N/2);
      Sierpinski(i,j+N/2,N/2);
   }
}

int main()
{  
   int N ;
   cin>>N ;
   Sierpinski(0,0,N);
   ///*
   for (int i=0;i<N;i++){
      for (int j=0;j<N;j++){
         if (Sp[i][j]!='#'){
            cout<<' ';
         }
         else{
            cout<<Sp[i][j];
         }
      }
      
      cout<<endl;
   }
   //*/
   return 0;
}