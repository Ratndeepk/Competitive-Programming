//https://practice.geeksforgeeks.org/problems/find-missing-and-repeating2512/1

#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
    int *findTwoElement(int *arr, int n) {
        int *a= new int(2);
        a[0]=0,a[1]=0;

        int shouldBe=0,butIs=0;
        for (int i = 0;i < n; i++) shouldBe ^= i+1;
        for (int i = 0;i < n; i++) butIs ^= arr[i];
        
        int temp = butIs ^ shouldBe;
        int setBit = temp & ~(temp-1);
        for(int i=0;i < n;i++){
           if(arr[i] & setBit) a[0] ^= arr[i];
           else a[1] ^= arr[i];
        }
        for (int i = 1; i <= n; i++) {
            if (i & setBit) a[0] ^= i;
            else  a[1] ^= i;
        }
        bool flag=1;
        for(int i = 0;i <n;i++) if(arr[i] == a[0]) flag=0;
        if(flag) swap(a[0],a[1]);
        return a;
    }
};