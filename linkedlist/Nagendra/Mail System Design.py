#code

class Node:
    
    def __init__(self,value):
        self.data=value
        self.next=None

class LinkedList:
    
    def __init__(self):
        self.head=None
        
    def insert(self,data):
        new =Node(data)
        if self.head==None:
            self.head=new
   
        else:

            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=new
    
    def delete(self,data):
        
        if self.head !=None:
            if self.head.data==data:
                self.head=self.head.next
            else:
                temp1=self.head
                while(temp1):
                    if temp1.data==data:
                        break
                    prev=temp1
                    temp1=temp1.next
                if temp1==None:
                    return
                
                prev.next=temp1.next
            
    def traverse(self):
        temp1=self.head
        if not temp1:
            print('EMPTY')
        else:
            while(temp1):
                print(temp1.data,end=' ')
                temp1=temp1.next
            print()
            

for _ in range(int(input())):
    n,q = map(int, input().split())
    arr = list(map(int, input().split()))
    
    read=LinkedList()
    unread = LinkedList()
    trash = LinkedList()
    
    for i in range(1,n+1):
        unread.insert(i)
    
    for i in range(0,2*q,2):
        
        if arr[i]==1:
            unread.delete(arr[i+1])
            read.insert(arr[i+1])
            
        elif arr[i]==2:
            read.delete(arr[i+1])
            trash.insert(arr[i+1])
            
        elif arr[i]==3:
            unread.delete(arr[i+1])
            trash.insert(arr[i+1])
     
        elif arr[i]==4:
            trash.delete(arr[i+1])
            read.insert(arr[i+1])
   
            
    unread.traverse()
    read.traverse()
    trash.traverse()
   
        
            
    