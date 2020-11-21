def reverse_list(head):
    temp=head
    prev=None
    while(temp):
        next=temp.next
        temp.next=prev
        prev=temp
        temp=next
    return prev
def compute(head):
    #Your code here
    head=reverse_list(head)
    temp=head
    while(temp.next):
        if temp.data>temp.next.data:
            temp.next=temp.next.next
        else:
            temp=temp.next
    return reverse_list(head)
