//https://www.geeksforgeeks.org/a-program-to-check-if-strings-are-rotations-of-each-other/
#include<bits/stdc++.h>
using namespace std;

bool checkRotation(string  str1, string str2)
{
if(str1.length()!=str2.length())
  return false;
string temp=str1+str1;
return (temp.find(str2)!=string::npos);
}

int main()
{
  string str1="ABCDE";
  string str2="CDEAB";
  cout<<(checkRotation(str1,str2)?"True":"False");
}