//https://www.programiz.com/java-programming/examples/check-valid-shuffle-of-strings

#include<bits/stdc++.h>
using namespace std;

bool checkShuffle(string str, string str1, string str2)
{
if(str.length() != str1.length() + str2.length())
  return false;

int i=0,j=0,k=0;

for(k=0;k<str.length();k++)
{
  if( str[k] == str1[i] )  i++;
  else if (str[k] == str2[j]) j++;
  else return false;
}

if(i != str1.length()||j != str2.length())
return false;
else return true;
}

int main (){
  string str="X1Y2",str1="XY",str2="12";
  cout<<(checkShuffle(str,str1,str2)?"True":"False")<<endl;
}