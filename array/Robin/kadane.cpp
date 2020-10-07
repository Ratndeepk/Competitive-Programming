#include <iostream>
using namespace std;

int getMaxElement(int arr[], int n) {
    int maxNum = arr[0];
    for(int i=1; i<n; i++) {
        if(arr[i] > maxNum){
            maxNum = arr[i];
        }
    }
    return maxNum;
}

int getMaxSumArray(int arr[], int n) {
    int maxNum = getMaxElement(arr, n);
    if(maxNum <= 0) return maxNum;
    //cout<<"Max Element : "<<maxSum<<endl;
    int curSum = 0;
    int maxSum = 0;
    for(int i=0; i<n; i++) {
        curSum = curSum+arr[i] > 0 ? curSum+arr[i] : 0;
        if(curSum > maxSum) maxSum = curSum;
    }
    return maxSum;
}

int main() {
	int t;
	cin>>t;
	while(t--) {
	    int n;
	    cin>>n;
	    int* arr = new int[n];
	    for(int i=0; i<n; i++) cin>>arr[i];
	    int maxSum = getMaxSumArray(arr, n);
	    cout<<maxSum<<endl;
	    delete[] arr;
	}
	return 0;
}
