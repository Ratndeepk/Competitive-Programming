#include <iostream>
using namespace std;

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
	int t;
	cin>>t;
	while(t--) {
	    int n;
	    cin>>n;
	    int* arr = new int[n];
	    for(int i=1; i<n; i+=2) cin>>arr[i];
	    int a=n-1;
	    if(n%2 == 0) a=n-2;
	    for(int i=a; i>=0; i-=2) cin>>arr[i];
	    for(int i=0; i<n; i++) cout<<arr[i]<<" ";
	    cout<<endl;
	    delete[] arr;
	}
	return 0;
}
