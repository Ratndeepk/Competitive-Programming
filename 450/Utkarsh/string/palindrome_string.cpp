//https://practice.geeksforgeeks.org/problems/palindrome-string0817/1
#include<bits/stdc++.h>
using namespace std;
//User function template for C++
class Solution{
public:	
	
	
	int isPlaindrome(string S)
	{
	    int n= S.length();
        for(int i=0;i<n/2;i++){
            if(S[i]!=S[n-i-1])
            return false;
        }
        return true;
    }

};