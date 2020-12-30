//https://practice.geeksforgeeks.org/problems/reverse-level-order-traversal/1#

#include<bits/stdc++.h>
using namespace std;

/*   
struct Node
{
    int data;
    Node* left;
    Node* right;
}; */


vector<int> reverseLevelOrder(Node *root)
{
  vector<int > v;
  queue < Node* > q;
  stack < Node* > s;
  q.push(root);
  while(!q.empty()){
      Node * temp = q.front(); q.pop();
    //   cout<< temp->data<<" ";
      s.push(temp);
      if(temp->right)       q.push(temp->right);
      if (temp->left)  q.push(temp->left);
  }
  while(!s.empty()){
      Node * temp = s.top();
      s.pop();
      if(temp)
      v.push_back(temp->data);
  }
  return v;
}