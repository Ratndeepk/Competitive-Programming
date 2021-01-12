//https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/

#include<bits/stdc++.h>
using namespace std;

Node* insert(Node* root, int value)
{
    if(root&& root->data ==value) return root;
    if(!root) return  new Node(value);
    if(value > root->data ) root->right = insert(root->right,value);
    else root->left = insert (root->left, value);
    return root;
}