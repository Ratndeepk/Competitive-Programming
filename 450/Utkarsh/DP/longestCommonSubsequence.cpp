//https://leetcode.com/problems/longest-common-subsequence/solution/

#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int ans[text1.size()+1][text2.size()+1];
        for(int i =0;i<=text1.size();i++)
            for(int j =0;j<=text2.size() ;j++){
                if( j==0 || i== 0) ans[i][j] = 0;
                else if (text1[i-1] == text2[j-1]) ans[i][j] = 1+ ans[i-1][j-1];
                else ans[i][j] = max(ans[i-1][j], ans[i][j-1]);
            }
        return ans[text1.size()][text2.size()];
    }
};