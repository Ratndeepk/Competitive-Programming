


#include<bits/stdc++.h>
using namespace std;
int t[100][100];
//memset(t,-1,sizeof(t));
int knapsack(int wt[],int val[],int W,int n)
{
	if(n==0 || W==0)
	{
		return 0;
	}
	if(t[n][W]!=0)
	{
		return t[n][W];
	}
	
	
	if( wt[n-1]<=W)
	{
		return t[n][W]= max(val[n-1]+knapsack(wt,val,W-wt[n-1],n-1),knapsack(wt,val,W,n-1));	
	}
	else if(wt[n-1]>W)
	{
		return t[n][W]=knapsack(wt,val,W,n-1);
	}
	
}

int main()
{
	int n;
	cin>>n;
	int wt[n+1];
	int val[n+1];
	
	for(int i=0;i<n;i++)
	{
		cin>>wt[i];
	}
	
	
	for(int i=0;i<n;i++)
	{
		cin>>val[i];
	}
	int W;
	cin>>W;
	
	int ans= knapsack(wt,val,W,n);
	
	cout<<ans<<endl;
	

	return 0;
}

