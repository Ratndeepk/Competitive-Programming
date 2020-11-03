def findMid(head):
    if head is None:
        return None
    
    ptr1 = head
    ptr2 = head
    while(ptr2 is not None and ptr2.next is not None):
        ptr1 = ptr1.next
        # this pointer moves 1 nodes ahead everytime loop is run
        
        ptr2 = ptr2.next.next
        # this pointer moves 2 nodes ahead everytime loop is run
    
    return ptr1.data
    # since slow was moving with half speed, it is there at halfway point
