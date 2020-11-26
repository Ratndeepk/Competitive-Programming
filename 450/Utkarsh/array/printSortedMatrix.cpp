//https://practice.geeksforgeeks.org/problems/sorted-matrix/0#

#include <bits/stdc++.h>
using namespace std;
#define INF INT_MAX 

int a[100][100];
int n;
void extractMin(int i,int j){
    int res;
    int down=i+1<n?a[i+1][j]:INF;
    int right=j+1<n?a[i][j+1]:INF;
    if (down == INF && right == INF)
        return;
    if (down < right ) 
    { 
        a[i][j] = down; 
        a[i+1][j] = INF; 
        extractMin( i+1, j); 
    } 
    else
    { 
        a[i][j] = right; 
        a[i][j+1] = INF; 
        extractMin( i, j+1); 
    } 
}

void Solve(){
    cin>> n;
    for (int i =0;i<n ;i++)
        for(int j=0;j<n;j++)
            cin>>a[i][j];
    
    for(int i=0;i<n*n;i++){
        cout<<a[0][0]<<" ";
        extractMin(0,0);
  }
  cout<<endl;
}

int main() {
    int testcase=1;
    cin>>testcase;
    while(testcase--) Solve();
	return 0;
}