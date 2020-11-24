//https://leetcode.com/problems/count-and-say/

#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    string solve(string str){
        string newstr;
        for(int i=0 ;i<str.size();i++){
           int  count=1;
            while( str[i] == str[i+1] && i + 1 < str.size())
               count++,i++;
            
            newstr += to_string(count)+str[i];
        }
        return newstr;
    }
    string countAndSay(int n) {
        string str="1";
        if(n==1) return str;
        for(int i=2;i<=n;i++)
            str=solve(str);
        return str;
    }
};