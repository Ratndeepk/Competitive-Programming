//https://www.geeksforgeeks.org/permutation-coefficient/

#include<bits/stdc++.h>
using namespace std;

// in O(n) time ,O(1) space
int permutationCheck( int n , int k){
  int Ans= 1;
  for (int i = 0; i < k; i++ ) Ans *= ( n - i );
  return Ans;
}
// algorithm like seive of eratosthenes
int permutationCheck( int n, int k){
  int p[n+1][k+1];
  for(int i =0;i<=n ;i++)
    for( int j=0 ;j<= min (i, k) ;j++){
      if(j==0) a[i][j] = 1;
      else  P[i][j] = P[i-1][j] + (j*P[i-1][j-1]); 
      p[i][j+1] =0;
    }
    return p[n][k];
}