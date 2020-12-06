def lastnodehead(head):
    if head.next==None:
        return head 

    temp1=head    # send this pointer to second last node
    temp2 = head  # send this pointer to last node
    while temp1.next.next:
        temp1=temp1.next 
        temp2 = temp2.next 

    temp2=temp2.next 
    temp1.next=None # break link between last node and second last node
    temp2.next=head  # make next of last node point to head
    head=temp2  #make last node as head
    return head