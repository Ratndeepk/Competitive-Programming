class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    def append(self,x):
        node=Node(x)
        node.next=self.head
        self.head=node

    def reverse(self,node):
        if node.next==None:
            self.head=node
            return
        self.reverse(node.next)
        new_node=node.next
        new_node.next=node
        node.next=None

    def print_ll(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next
        print()
l = linkedlist()
my_list = list(map(int,input().split()))
for i in range(len(my_list)):
    l.append(my_list[i])
l.print_ll()
l.reverse(l.head)
l.print_ll()
