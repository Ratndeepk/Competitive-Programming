//https://practice.geeksforgeeks.org/problems/middle-of-three2926/1

#include<bits/stdc++.h>
using namespace std;

// NO comparisons required at all
class Solution{
  public:
    int middle(int A, int B, int C){
        int maxi  = max(A,B)     , mini  = min(A,B);
        int maxii = max(maxi,C)  , minii = min(mini,C);
        return A+B+C-maxii-minii;
    }
};