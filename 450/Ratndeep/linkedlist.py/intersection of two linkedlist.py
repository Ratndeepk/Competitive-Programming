"""
Intersection of Linkedlist
l1 = 1->2->3->2
l2 = 2->3->4

returns
l = 2->3
"""

def reverse(head):
    prev=None
    temp=head 
    while(temp):
        next=temp.next
        temp.next=prev
        prev=temp
        temp=next
    return prev

def findIntersection(head1,head2):
   
    dict={}  # store all data of linkedlist 1 in hash
    while(head1):
        if head1.data not in dict:
            dict[head1.data]=1
        else:
            dict[head1.data]+=1 
        head1=head1.next
    head=None  
    while(head2):
        try:
            if dict[head2.data]>=1: #if this data exist in hash add it in newly created linkedlist
                node=Node(head2.data)
                if head==None:
                    head=node
                else:
                    node.next=head
                    head=node 
                dict[head2.data]-=1
        except KeyError:
            pass 
        head2=head2.next
    return reverse(head)