class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def push(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
        else:
            node.next=self.head
            self.head=node

    def print_ll(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next
        print()
    def make_last_node_head(self):
        temp=self.head.next
        temp1=self.head
        while(temp.next):
            temp1=temp1.next
            temp=temp.next
        temp1.next=None
        temp.next=self.head
        self.head=temp

ll = Linkedlist()
l = list(map(int,input().split()))
for i in range(len(l)):
    ll.push(l[i])
ll.print_ll()
ll.make_last_node_head()
ll.print_ll()
