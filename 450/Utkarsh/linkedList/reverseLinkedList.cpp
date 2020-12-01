//https://practice.geeksforgeeks.org/problems/reverse-a-linked-list/1
#include<bits/stdc++.h>
using namespace std;
 

// Should reverse list and return new head.
struct Node* reverseList(struct Node *head)
{
    Node * prev = NULL; 
    Node * current = head; 
    Node * nxt; 
    while (current != NULL) 
    { 
      nxt=current->next;
      current->next=prev;
      prev=current;
      current =nxt;

    }
    return prev; 
} 
