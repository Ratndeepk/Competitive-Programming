#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--) {
	    int n;
	    cin>>n;
	    int num = 1;
	    int* arr = new int[n-1];
	    for(int i=0; i<n-1; i++) {
	        cin>>arr[i];
	    }
	    sort(arr,arr+n-1);
	    for(int i=0; i<n-1; i++) {
	        if(arr[i] != num) {
	            break;
	        }
	        num++;
	    }
	    cout<<num<<endl;
	    
	}
	return 0;
}
