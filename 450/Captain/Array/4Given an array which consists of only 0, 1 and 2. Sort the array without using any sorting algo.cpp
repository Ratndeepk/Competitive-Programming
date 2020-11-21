#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    int arr[n];
    int c0=0;
    int c1=0;
    int c2=0;
    for(int i=0;i<n;i++){
        cin>>arr[i];
        if(arr[i] == 0){
            c0++;
        }
        else if(arr[i] == 1){
            c1++;
        }
        else{
            c2++;
        }
    }
    int i=0;
    while(c0>0){
        arr[i] = 0;
        i++;
        c0--;
    }
    while(c1>0){
        arr[i] = 1;
        i++;
        c1--;
    }
    while(c2>0){
        arr[i] = 2;
        i++;
        c2--;
    }
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    
    
    return 0;
}
