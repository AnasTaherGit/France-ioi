#include <iostream>
#include <string>

using namespace std;

int lps(string S){
	int MaxLength=1;
	int start=0;
	int len=S.size();
	int low,high;

	for(int i=1;i<len;i++){
		low=i-1;
		high=i;

		while (low>=0 && high<len && S[low]==S[high]){

			if (high-low+1>MaxLength){
				start=low;
				MaxLength=high-low+1;
			}
			low--;
			high++;
		}

		low=i-1;
		high=i+1;
		while (low>=0 && high<len && S[low]==S[high]){

			if (high-low+1>MaxLength){
				start=low;
				MaxLength=high-low+1;
			}
			low--;
			high++;
		}

		//cout<<i<<endl;
	}

	return MaxLength;
}

int main(int argc, char const *argv[])
{
	string S;
	cin>>S;
	cout<<lps(S);
	return 0;
}



// A this algorithms has a time complexity of O(N^3) so it's no efficient 
/********************************************

bool is_palindrome(string s){
	int n=s.size();
	for (int i=0;i<n/2;i++){
		if (s[i]!=s[n-i-1]) return false;
	}
	return true;
}

int main(int argc, char const *argv[]){	

	int m=1;
	string s,S="mollakayakokomassa";
	//cin>>S;
	int N=S.size();
	for (int i=0;i<N;i++){
		for (int j = 1; j <= N-i; j++){
			s=S.substr(i,j);
			//cout<<s<<endl;
			if (is_palindrome(s)){
				if (j>m) m=j;
			}
		}
	}
	cout<<m<<endl;
	return 0;
}

******************************************/