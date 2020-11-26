class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

        
class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,newdata):
        new_node=Node(newdata)
        if self.head is None:
            self.head=new_node
            return 
        temp=self.head
        
        while(temp.next):
            temp=temp.next
        temp.next=new_node


    def first_node_of_loop(self,node):
        
        # finding the position where fast=slow
        slow=self.head 
        fast = self.head 
        while(True):
            slow = slow.next 
            fast = fast.next.next
            if slow==fast:
                break 

        #starting from head move fast & cur_node until they are equal
        cur_node=self.head 
        while(cur_node!=fast):
            fast=fast.next 
            cur_node=cur_node.next 
        return cur_node 


                
    
arr = list(map(int,input().split()))
l = LinkedList()
for i in range(lenn(arr)):
    l.append(arr[i]) 

print(l.first_node_of_loop(l.head))
