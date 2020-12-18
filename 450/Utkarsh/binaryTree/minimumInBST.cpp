//https://practice.geeksforgeeks.org/problems/minimum-element-in-bst/1

#include<bits/stdc++.h>
using namespace std;

/*
struct Node {
    int data;
    Node* right;
    Node* left;

    Node(int x){
        data = x;
        right = NULL;
        left = NULL;
    }
};
*/

int minValue(Node* root)
{
    Node* temp =root;
    if(root==NULL) return -1;
    while(temp->left != NULL)
        temp=temp->left;
    return temp->data;
}