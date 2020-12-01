//https://practice.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/

#include<bits/stdc++.h>
using namespace std;

//User function template for C++

/* struct Node
  {
    int data;
    struct Node* next;
    
    Node(int x){
        data = x;
        next = NULL;
    }
  };*/
  
Node *reverse(Node *head) 
{ 
    Node * prev = NULL; 
    Node * current = head; 
    Node * next; 
    while (current != NULL) 
    { 
        next = current->next; 
        current->next = prev; 
        prev = current; 
        current = next; 
    } 
    return prev; 
} 
 
Node* addOne(Node *head) 
{
     head=reverse(head);
    
   Node* res = head; 
    Node *temp, *prev = NULL; 
 
    int carry = 1, sum; 
 
    while (head != NULL) 
    { 
        sum = carry + head->data; 
        carry = (sum >= 10)? 1 : 0; 
        sum = sum % 10; 
        head->data = sum; 
        temp = head; 
        head = head->next; 
    } 
    if (carry > 0) 
        temp->next = new Node(carry);
        
     head= res; 
    return reverse(head);
}
