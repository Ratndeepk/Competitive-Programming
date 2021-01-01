//https://practice.geeksforgeeks.org/problems/longest-repeating-subsequence/

#include <bits/stdc++.h>
using namespace std;

void Solve (){
    int n ;
    cin>>n ;
    char s[n];
    for(int i =0;i<n ;i++) cin>> s[i];
    int ans[n+1][n+1];
    for(int i =0 ;i <=n ;i++ )
        for(int j =0; j<=n ;j++){
            if( !i | !j)  ans[i][j] = 0;
            else  if (s[i-1] != s[j-1] || i == j ) ans[i][j] = max(ans[i][j-1] , ans[i-1][j]);
            else  ans [i][j] = ans[i-1][j-1] + 1;
        }
	cout<<ans[n][n]<<endl;
}
int main (){
    int testCase =1;
    cin>>testCase;
    while(testCase--) Solve();
    return 0;
}