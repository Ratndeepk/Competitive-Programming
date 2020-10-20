def removeDuplicates(head):
    #code here
    cur=head
    while(cur.next):
        if cur.data==cur.next.data:
            cur.next=cur.next.next
            
        else:
            cur=cur.next
