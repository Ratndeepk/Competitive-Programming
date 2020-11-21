def removeTheLoop(head):
    ##Your code here
    if detectloop(head)==0:
        return 
    
    one=head
    two=head
    while(one and two and two.next):
        one=one.next
        two=two.next.next
        #print(one.data,two.data)
        if one==two:
            f=one
            break
    #print(f.data)
    
    temp=head
    while(temp!=f):
        if temp.next==f.next:
            #print(temp.next.data,f.next.data)
            f.next=None
            break
        else:
            temp=temp.next
            f=f.next
    return True