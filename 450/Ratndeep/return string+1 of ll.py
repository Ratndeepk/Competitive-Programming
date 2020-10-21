def addOne(head):
    #Returns new head of linked List.
    st=""
    while(head):
        st+=str(head.data)
        head=head.next
    return int(st)+1
