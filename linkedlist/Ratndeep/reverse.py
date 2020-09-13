def reverseList(self):
    # Code here
    if self.head is None:
        return None
    temp=self.head
    prev=None
    while(temp):
        Next = temp.next
        temp.next=prev
        prev=temp
        temp=Next
    self.head=prev
