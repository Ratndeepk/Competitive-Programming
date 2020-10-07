def merge(head_a,head_b):
    #code here
    head=None
    if head_a.data<head_b.data:
        head=head_a
        head_a=head_a.next
    else:
        head=head_b
        head_b=head_b.next
    temp=head 
    while(head_a or head_b):
        if head_a and head_b:
            if head_a.data<head_b.data:
                temp.next=head_a
                head_a=head_a.next
                temp=temp.next
            else:
                temp.next=head_b
                head_b=head_b.next
                temp=temp.next
        elif head_a is None:
            temp.next=head_b
            head_b=head_b.next
            temp=temp.next
        else:
            temp.next=head_a
            head_a=head_a.next
            temp=temp.next
    temp.next=None        
    return head
def mergeKLists(arr,N):
    # code here
    # return head of merged list
    if len(arr)==1:
        return arr[0]
    head = merge(arr[0],arr[1])
    if len(arr)==2:
        return head
    for i in range(2,N):
        head = merge(head,arr[i])
    return head
