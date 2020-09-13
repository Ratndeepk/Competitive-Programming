class Node:

    def __init__(self,data):
        self.data=data
        self.next=None

    def set_data(self,data):
        self.data=data
    
    def get_data(self):
        return self.data
    
    def set_next(self,next):
        self.next=next

    def get_next(self):
        return self.next

class LinkedList:

    def __init__(self):
        self.head=None

    def set_head(self,head):
        self.head=head

    def get_head(self):
        return self.head

    def traverse(self):
        temp=self.head

        while(temp):
            print(temp.data, end="-->")
            temp=temp.next
        
ll=LinkedList()
while(1):
    ch=int(input("\nEnter\n 1 to insert\n 2 to traverse\n 3 to exit\n"))

    if ch==1:
        
        new=Node(int(input("enter node value ")))
        if ll.get_head()==None:
            ll.set_head(new)
        else:
            temp=ll.get_head()
            
            while(temp.next):
                temp=temp.next
            temp.next=new 

    elif ch==2:
        ll.traverse()
    elif ch==3:
        break
        
            
