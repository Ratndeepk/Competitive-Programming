# This function should reverse linked list and return
# head of the modified linked list
def reverseList(head):
    # Code here
    temp=head
    prev=None
    while(temp):
        next=temp.next
        temp.next=prev
        prev=temp
        temp=next
        
    return prev