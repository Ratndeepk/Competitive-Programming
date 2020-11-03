def getNthfromEnd(head,n):
    #code here
    count=0
    temp=head
    while(temp):
        count+=1
        temp=temp.next
    if n>count:
        return -1
    count=count-n
    temp=head
    
    while(count):
        temp=temp.next
        count-=1
    return temp.data
