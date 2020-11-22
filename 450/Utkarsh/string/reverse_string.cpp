//https://practice.geeksforgeeks.org/problems/reverse-a-string/1
#include<bits/stdc++.h>
using namespace std;
string reverseWord(string str){
    int n = str.length();
    char c;
    for(int i = 0; i < n/2 ; i++){
        c=str[i];
        str[i]=str[n-1-i];
        str[n-i-1]=c;
    }
    return str;
}