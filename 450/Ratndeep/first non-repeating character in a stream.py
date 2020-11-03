class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        self.repeted=[None]*26
        for i in range(26):
            self.repeted[i]=Node(None)
    def add_node(self,x):
        new_node = Node(x)
        if self.head==None:
            self.head = new_node
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp
        self.repeted[ord(x)-97].next=new_node
    def remove_node(self,x):
        try:
            temp=self.head
            if temp.data==x:
                self.head=self.head.next
            else:
                while(temp.data!=x):
                    temp=temp.next
                if temp.next==None:
                    temp.prev.next=None
                else:
                    temp.next.prev=temp.prev
                    if temp.prev:
                        temp.prev.next=temp.next
        except:
            pass
    def rep(self,x):
        self.repeted[ord(x)-97].next=None
        self.remove_node(x)
    
    def printll(self):
        temp=self.head
        while(temp):
            print(temp.data,end = " ")
            temp=temp.next
        print()
for _ in range(int(input())):
    n = int(input())
    data = input().split()
    l = LinkedList()
    visited=[False]*26
    for i in range(n):
        if visited[ord(data[i])-97]==False:
            l.add_node(data[i])
            
            visited[ord(data[i])-97]=True
            if l.head:
                print(l.head.data,end=" ")
            else:
                print(-1,end=" ")
        else:
            l.rep(data[i])
            if l.head:
                print(l.head.data,end=" ")
            else:
                print(-1,end=" ")
    print()
            
            
    
