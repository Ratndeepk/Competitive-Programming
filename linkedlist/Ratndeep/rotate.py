def rotateList(head, k):
    # code here
    t=k-1
    temp=head
    while(k):
        temp=temp.next
        k-=1
    temp1=head
    
    while(t):
        temp1=temp1.next
        t-=1
    temp1.next=None
    temp2=temp
    if temp2!=None:
        while(temp2.next):
            temp2=temp2.next
        temp2.next=head
        return temp
    else:
        return head
