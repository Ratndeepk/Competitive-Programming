


def reverse(head):
    prev=None
    temp=head 
    while(temp):
        next=temp.next
        temp.next=prev
        prev=temp
        temp=next
    return prev
    
def addOne(head):
  
    head=reverse(head)  # reverse ll 456 becomes 654
    
    carry=0
    temp=head
    if temp.data<9:   # 6<9
        temp.data+=1 
        head=reverse(head)  #reverse again 754 becomes 457 
        return head 
    else:                   # but if it was 659
        carry=1 
        temp.data=0         # 956 becoms 056
        temp=temp.next 
        while(temp):
            if temp.data<9:         #056 becomes 066 
                temp.data+=carry      
                head=reverse(head) 
                return head 
            else:
                carry=1          # but if it was 899 
                temp.data=0      # it becomes 998 -> 098 -> 009 then we reverse it 
            temp=temp.next
        
        n = Node(1)     #but if it was 999 -> 099 -> 009 -> 0001 reverse and return 
        temp=head 
        while(temp.next):
            temp=temp.next
        temp.next=n
        head=reverse(head) 
        return head



class Node:
    def __init__(self, data):  
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

 
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

def PrintList(head):
    while head:
        print(head.data,end='')
        head = head.next

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        
        num = input()
        ll = LinkedList() 
        for digit in num:
            ll.insert(int(digit))  
        
        resHead = addOne(ll.head)
        PrintList(resHead)
        print()


