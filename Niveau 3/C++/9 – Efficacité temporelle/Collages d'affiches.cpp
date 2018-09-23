#include <iostream>
#include <vector>

using namespace std;

int main(){
   
   vector<int> A;
   int NbRequest,H,cpt;
   char R;
   cin>>NbRequest;
   
   for (int i=0;i<NbRequest;i++){
      cin>>R;
      if (R=='Q'){
         cout<<A.size()<<endl;
      }
      else{
         cin>>H;
         if (A.empty()){
            A.push_back(H);
         }
         else{
            cpt=A.size()-1;
            while (H>=A[cpt]){
               A.pop_back();
               cpt--;
               if (cpt==-1) break;
            }
            A.push_back(H);
         }
      }
   }

   return 0;
}