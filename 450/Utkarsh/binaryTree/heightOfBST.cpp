//https://practice.geeksforgeeks.org/problems/height-of-binary-tree/1

#include<bits/stdc++.h>
using namespace std;

class Solution{
    public:
    int height(struct Node* node){
        if(node == NULL) return 0;
        return 1+max(height(node->left),height(node->right)); 
    }
}; 