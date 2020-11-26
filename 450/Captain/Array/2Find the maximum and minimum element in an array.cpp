#include<bits/stdc++.h>
using namespace std;

//struct used bcoz both elements are need to get in one loop and function should return both elements.
struct Pair{
    int min;
    int max;
};

struct Pair getMinMax(int arr[],int n){
    struct Pair s;
    s.min = INT_MAX;
    s.max = INT_MIN;
    for(int i=0;i<n;i++){
        if(arr[i]>s.max){
            s.max = arr[i];
        }
        if(arr[i]<s.min){
            s.min = arr[i];
        }
    }
    return s;
}
int main(){
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    struct Pair p1;
    p1 = getMinMax(arr,n);
    cout<<p1.min<<" "<<p1.max<<endl;
    return 0;
}
