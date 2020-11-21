Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #code

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def add_node(self,x):
        new_node=Node(x)
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=new_node
    def conversion(self,node):
        if node.next==None:
            return node
        temp=node
        temp1 = node.next
        while(temp1):
            if temp.data%2==0:
                temp=temp.next
                temp1=temp1.next
            elif temp.data%2!=0 and temp1.data%2==0:
                temp.data,temp1.data=temp1.data,temp.data
                temp=temp.next
                temp1=temp1.next
            else:
                temp1=temp1.next
        return node
for _ in range(int(input())):
    n = int(input())
    old = list(map(int,input().split()))
    l = LinkedList()
    for i in range(n):
        l.add_node(old[i])
    head = l.conversion(l.head)
    while(head):
        print(head.data,end=" ")
        head=head.next
    print()