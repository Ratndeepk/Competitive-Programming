//https://practice.geeksforgeeks.org/problems/level-order-traversal/1

#include<bits/stdc++.h>
using namespace std;



vector<int> levelOrder(Node* node)
{
    vector <int > v;
    queue<Node*> w;
    w.push(node);
    while(!w.empty()){
        Node* temp =w.front();
        w.pop();
        v.push_back(temp->data);
        if(!temp->left && !temp->right) ; 
            
        else if(!temp ->left) {
            w.push (temp->right);
        }        
        else if(!temp->right){
            w.push(temp->left);
        }
        else {
            w.push(temp->left);
            w.push(temp->right);
        }
    }
    return v;
}
