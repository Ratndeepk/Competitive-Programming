//https://practice.geeksforgeeks.org/problems/intersection-of-two-sorted-linked-lists/1

#include<bits/stdc++.h>
using namespace std;

/* The structure of the Linked list Node is as follows:
struct Node
{
    int data;
    Node *next;
    Node(int val)
    {
        data=val;
        next=NULL;
    }
};
*/

Node* findIntersection(Node* head1, Node* head2)
{
    Node* p1= head1;
    Node* p2=head2;
    Node* head=NULL;
    Node* tail=NULL;
    while(p1!=NULL&&p2!=NULL){
        if  (p1->data < p2->data)
            p1=p1->next;
        else if (p1->data >p2->data)
            p2=p2->next;
        else
        {
            if(head==NULL)
                head = tail = new Node(p1->data);
            else {
                tail->next = new Node(p1->data);
                tail = tail->next;
            }
            p1 = p1->next;
            p2 = p2 ->next;
        }
    }
    return head;;
}