def intersetPoint(head_a,head_b):
    #code here
    while(head_a):
        head_a.data=str(head_a.data)
        head_a=head_a.next
    while(head_b):
        if type(head_b.data)==str:
            return head_b.data
        head_b=head_b.next
    return -1

"""
def getSize(head):
    ret = 0
    while head is not None:
        head = head.next
        ret+=1
    return ret

def intersetPoint(head1,head2):
    n1 = getSize(head1)
    n2 = getSize(head2)
    
    while n1>n2:
        head1 = head1.next
        n1-=1
        # if list1 is longer, we ignore some of its starting
        # elements till it has as many elements as list2
    
    while n2>n1:
        head2 = head2.next
        n2-=1
        # if list2 is longer, we ignore some of its starting
        # elements till it has as many elements as list1
    
    while head1 != head2:
        head1 = head1.next
        head2 = head2.next
        # now we simple traverse ahead till we get the
        # intersection point, if there is none, this loop
        # will break when both pointers point at NULL

    if head1 is not None:
        return head1.data
    return -1

"""
