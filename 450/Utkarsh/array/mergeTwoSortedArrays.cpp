//https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays5135/1

#include<bits/stdc++.h>
using namespace std;

// literally 4 lines of code
  void merge4LOC(int arr1[], int arr2[], int n, int m){
    int j = 0, i = n-1;
    while(j < m && i > -1 && arr2[j] < arr1[i])
      swap(arr2[j++],arr1[i--]);
    sort(arr1,arr1+n);
    sort(arr2,arr2+m);
  }

// Gap method Or shell sort method
class Solution{
public:
	int nextGap(int gap) {
	    if (gap <= 1) return 0;
	    return (gap / 2) + (gap % 2);
	}
	
public:
	void merge(int arr1[], int arr2[], int n, int m) {
	    
	    int i, j, gap = n + m;
	    for (gap = nextGap(gap); gap > 0; gap = nextGap(gap)) {
	        cout<<gap<<" : \n";
	        for (i = 0; i + gap < n; i++)
	            if (arr1[i] > arr1[i + gap]) swap(arr1[i], arr1[i + gap]);

	        for (j = gap > n ? gap - n : 0; i < n && j < m; i++, j++)
	            if (arr1[i] > arr2[j]) swap(arr1[i], arr2[j]);

	        if (j < m) {

	            for (j = 0; j + gap < m; j++)
	                if (arr2[j] > arr2[j + gap]) swap(arr2[j], arr2[j + gap]);
	        }
	    }
    
    }
};
