//https://leetcode.com/problems/search-a-2d-matrix/

#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
    if(matrix.size()==0||matrix[0].size()==0)
        return false;
    
    int m=matrix.size();
    int n=matrix[0].size();
    int left =0;
    int right =m*n-1;
    int mid;
    while(left <= right){
        mid=(right-left)/2+left;
        if(matrix[mid/n][mid%n]==target)
            return true;
        else if (target<matrix[mid/n][mid%n])
            right=mid-1;
        else
            left=mid+1;
    }
        return false;
    }
};