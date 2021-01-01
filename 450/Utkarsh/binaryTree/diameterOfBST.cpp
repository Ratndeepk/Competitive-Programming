//https://practice.geeksforgeeks.org/problems/diameter-of-binary-tree/1

#include<bits/stdc++.h>
using namespace std;

int H(struct Node* node){
        if(node == NULL) return 0;
        return 1+max(H(node->left),H(node->right)); 
}
    
/* Computes the diameter of binary tree with given root.  */
int diameter(Node* root) {
    if(root == NULL ) return 0;
    return 
        max({
            diameter(root->left),
            diameter(root->right),
            H(root->right)+H(root->left)
        });
}