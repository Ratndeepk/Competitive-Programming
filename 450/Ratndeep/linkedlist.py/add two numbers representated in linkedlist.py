

def reverse(head):
    prev=None
    temp=head 
    while(temp):
        next=temp.next
        temp.next=prev
        prev=temp
        temp=next
    return prev

def addLists(first, second):
    first=reverse(first) 
    second = reverse(second) 
    carry=0 
    temp=second
    
        
    if first.data+second.data<=9:
        head=Node(first.data+second.data)
    else:
        head=Node((first.data+second.data)%10)
        carry=1
        
    first=first.next
    second=second.next 
    while first and second:
        if first.data+second.data+carry<=9:
            node=Node(first.data+second.data+carry)
            node.next=head
            head=node
            carry=0
        else:
            node=Node((first.data+second.data+carry)%10)
            node.next=head
            head=node
            carry=1
        first=first.next
        second=second.next
    while first:
        if carry==0:
            node=Node(first.data) 
            node.next=head
            head=node
        else:
            if first.data+carry<=9:
                node=Node(first.data+carry)
                node.next=head
                head=node
                carry=0 
            else:
                node=Node((first.data+carry)%10)
                node.next=head
                head=node
                carry=1 
        first=first.next
    
    while second:
        if carry==0:
            node=Node(second.data) 
            node.next=head
            head=node
        else:
            if second.data+carry<=9:
                node=Node(second.data+carry)
                node.next=head
                head=node
                carry=0 
            else:
                node=Node((second.data+carry)%10)
                node.next=head
                head=node
                carry=1 
        second=second.next
        
    
    if carry==1:
        node=Node(1) 
        node.next=head
        head=node
    return head


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


def printList(n):
    while n:
        print(n.data,end='')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = list(map(int,input().split()))
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = list(map(int,input().split()))
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
       
         
        res = addLists(LL1.head, LL2.head)
        printList(res)
