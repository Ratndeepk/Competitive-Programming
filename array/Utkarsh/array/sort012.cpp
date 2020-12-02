//https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1
#include <bits/stdc++.h>
using namespace std;


void swap(int* a, int* b) 
{ 
    int temp = *a; 
    *a = *b; 
    *b = temp; 
} 
void sort012(int a[], int n)
{
    int p=0,q=n-1;
    while(a[p]==0) p++;
    while(a[q]==2) q--;
    
    for(int i=p;i<=q;i)
    {
        if(a[i] == 0) swap(a[i++],a[p++]);
        else if(a[i] == 2) swap(a[i],a[q--]);
        else i++;
    }
}    
int main()
{
 ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
 srand(chrono::high_resolution_clock::now().time_since_epoch().count());

 int Testcase = 1;
 cin >> Testcase;

 while (Testcase--){
      int n;
      cin>>n;
      int a[n];
    for(int i=0;i<n;i++)
    cin>>a[i];  
    sort012(a,n);
    for(int i=0;i<n;i++)
        cout<<a[i]<<" ";
    cout<<endl;
 }
 return 0;
}
