#code
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def insert(self,data):
        new_node = node(data)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=new_node
            
    def delete(self,key):
        temp=self.head
        if temp is not None:
            if temp.data==key:
                self.head=temp.next
                temp=None
                return
        while(temp):
            if temp.data==key:
                break
            prev=temp
            temp=temp.next
        if temp==None:
            return
        prev.next=temp.next
        temp=None
            
    def print_ll(self):
        if self.head is None:
            print("EMPTY")
        else:
            while(self.head):
                print(self.head.data,end=" ")
                self.head=self.head.next
            print()
        


for _ in range(int(input())):
    read = LinkedList()
    unread = LinkedList()
    trash = LinkedList()
    n,q = map(int,input().split())
    query = list(map(int,input().split()))
    for i in range(1,n+1):
        unread.insert(i)
    for i in range(0,2*q,2):
        command = query[i]
        msg = query[i+1]
        if command==1:
            unread.delete(msg)
            read.insert(msg)
        elif command==2:
            read.delete(msg)
            trash.insert(msg)
        elif command==3:
            unread.delete(msg)
            trash.insert(msg)
        else:
            trash.delete(msg)
            read.insert(msg)
    
    unread.print_ll()
    read.print_ll()
    trash.print_ll()
        
        
