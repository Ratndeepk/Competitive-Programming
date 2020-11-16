#include<bits/stdc++.h>
using namespace std;
string reverseWord(string str){
  char t;
  int i=0;
  int j=str.size()-1;
  while(i<=j){
    t = str[i];
    str[i] = str[j];
    str[j] = t;
    i++;
    j--;
  }
  return str;
}
int main(){
  int t;
  cin>>t;
  while(t--){
    string s;
    cin>>s; 
    cout<<reverseWord(s)<<endl;
  }
  return 0;
}
