def merge(head1, head2):
    temp=None
    if head1==None:
        return head2
    if head2==None:
        return head1
    
    if head1.data<=head2.data:
        temp=head1
        temp.next=merge(head1.next,head2)
    else:
        temp=head2
        temp.next=merge(head1,head2.next)
    return temp
def mergeKLists(arr,N):
    # code here
    # return head of merged list
    if N==0:
        return 
    elif N==1:
        return heads[0]
    else:
        
        header=merge(heads[0],heads[1])
        for i in range(2,n):
            header=merge(header,heads[i])
        return header
