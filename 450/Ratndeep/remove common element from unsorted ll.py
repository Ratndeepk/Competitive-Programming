def removeDuplicates(head):
    if head is None or head.next is None:
        return head

    hash=set() 

    walk = head
    hash.add(head.data)
    
    while walk.next is not None:
        
        if walk.next.data in hash:
            walk.next = walk.next.next
        
        else:
            hash.add(walk.next.data)
            walk = walk.next
    
    return head
