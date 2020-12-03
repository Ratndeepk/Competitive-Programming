//https://www.techiedelight.com/preorder-tree-traversal-iterative-recursive/

#include<bits/stdc++.h>
using namespace std;
//preorder traversal  recursive function 
void preorder(Node *root)
{
      if (root == nullptr)
        return;
    cout << root->data << " ";
    preorder(root->left);
    preorder(root->right);
}

// preorder traversal iterative funciton
void preorderIterative(Node *root)
{
    // return if tree is empty
    if (root == nullptr)
       return;
 
    // create an empty stack and push root node
    stack<Node*> stack;
    stack.push(root);
 
    // loop till stack is empty
    while (!stack.empty())
    {
        // pop a node from the stack and print it
        Node *curr = stack.top();
        stack.pop();
 
        cout << curr->data << " ";
 
        // push right child of popped node to the stack
        if (curr->right)
            stack.push(curr->right);
 
        // push left child of popped node to the stack
        if (curr->left)
            stack.push(curr->left);
 
        // important note - right child is pushed first so that left child
        // is processed first (FIFO order)
    }
}


