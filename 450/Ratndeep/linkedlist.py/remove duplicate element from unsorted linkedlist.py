"""
Given an unsorted linked list of N nodes. The task is to remove duplicate elements from this unsorted Linked List. 
When a value appears in multiple nodes, the node which appeared first should be kept, all others duplicates are to be removed.

Example 1:

Input:
N = 4
value[] = {5,2,2,4}
Output: 5 2 4
Explanation:Given linked list elements are
5->2->2->4, in which 2 is repeated only.
So, we will delete the extra repeated
elements 2 from the linked list and the
resultant linked list will contain 5->2->4
"""



def removeDuplicates(head):
    # code here
    # return head after editing list
    temp=head
    s=set() 
    s.add(temp.data)
    temp1=head
    temp=temp.next
    while(temp):
        if temp.data in s:
            temp1.next=temp.next 
            temp=temp1.next
        else:
            s.add(temp.data)
            temp1=temp1.next
            temp=temp.next
            
    return head