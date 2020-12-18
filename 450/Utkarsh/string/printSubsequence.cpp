//https://www.geeksforgeeks.org/print-subsequences-string/

#include<bits/stdc++.h>
using namespace std;

// recursive program video reference(https://www.youtube.com/watch?v=KCEPvdLqlYI)
void printSubsequence(string input,string output)
{
  if(input.empty()) {
    cout<< output<<endl; 
    return;
  }
  printSubsequence(input.substr(1), output);
  printSubsequence(input.substr(1), output + input[0]);
}
int main (){
  string output="", input="abcd";
  printSubsequence(input , output);
}