//https://practice.geeksforgeeks.org/problems/first-and-last-occurrences-of-x/1

#include <bits/stdc++.h>
using namespace std;

void firstAndLastX(int a[], int n, int x)
{
    if (binary_search(a, a + n, x) == 0) cout<<"-1";
    else cout<< lower_bound(a, a + n, x)-a <<" "<<upper_bound(a, a + n, x)-1-a;
}
int main()
{
    int T;
    cin >> T;
    while(T--)
    {
        int N, X;
        cin >> N >> X;
        int arr[N];
        for(int i = 0; i < N; i++)  
        cin >> arr[i];
        firstAndLastX(arr, N, X);
        cout << endl;
    }
    return 0;
}