def detectLoop(head):
    #code here
    temp=head
    temp1=head
    while(temp1 and temp and temp1.next):
        temp=temp.next
        temp1=temp1.next.next
        if temp==temp1:
            return True
    return False