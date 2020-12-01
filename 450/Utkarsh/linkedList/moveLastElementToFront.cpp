//https://www.geeksforgeeks.org/move-last-element-to-front-of-a-given-linked-list/

#include<bits/stdc++.h>
using namespace std;

//function to return head pointer
Node moveToFront(Node *head){
  Node secLast=NULL;
  Node last= head;
  while(last->next!=NULL){
    secLast=last;
    last=last->next;
  }
  secLast->next=NULL;
  last->next=head;
  return last;
}