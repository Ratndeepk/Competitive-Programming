def copyList(head):
    new_head=Node(head.data)
    dic={}
    dic[head]=new_head
    h=head.next
    c=new_head
    
    while(h):
        d=Node(h.data)
        c.next=d
        dic[h]=d
        h=h.next
        c=d
    
    h=head
    c=new_head
    while(h):
        if h.arb:
            c.arb=dic[h.arb]
        h=h.next
        c=c.next
    return new_head
