#User function Template for python3

'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.arb=None
'''

def copyList(head):
    '''
    param: head:  head of linkedList to copy
    return: the head of the copied linked list the #output will be 1 if successfully copied
    '''
    copied = Node(head.data)
    temp=head.next
    prev=copied
    while temp:
        new=Node(temp.data)
        prev.next=new
        prev=new
        temp=temp.next
    temp=head
    temp2=copied
    while temp:
        if temp.arb:
            ctemp=copied
            while ctemp.data!=temp.arb.data:
                ctemp=ctemp.next
            temp2.arb=ctemp
        temp=temp.next
        temp2=temp2.next
            
    return copied


#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.arb=None
        
class LinkedList:
    def __init__(self):
        self.head = None

def insert(tail,data):
    tail.next=Node(data)
    return tail.next
    

def setarb(head,a,b):
    h=head
    i=1
    while i<a and h:
        h=h.next
        i+=1
    an=h
    
    h=head
    i=1
    while i<b and h:
        h=h.next
        i+=1
        
    if an:
        an.arb=h
        
def validation(head,res):
    
    while head and res:
        if id(head)==id(res):
            return
        
        #print(head.data,res.data,end=' ')
        if head.data != res.data:
            return
        
        if head.arb:
            if not res.arb:
                return
            
            #print(head.arb.data,res.arb.data)
            if head.arb.data != res.arb.data:
                return
            
        elif res.arb:
            return
        head=head.next
        res=res.next
        
    if not head and res:
        return
    elif head and not res:
        return
    
    return True


if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n,m = list(map(int, input().strip().split()))
        nodes = list(map(int, input().strip().split()))
        aarb = list(map(int, input().strip().split()))
        ll=LinkedList()
        ll.head=Node(nodes[0])
        tail=ll.head
        
        for x in nodes[1:]:
            tail=insert(tail,x)
        
        for i in range(0,len(aarb),2):
            setarb(ll.head,aarb[i],aarb[i+1])
        
        res=copyList(ll.head)
        if validation(ll.head,res):
            print(1)
        else:
            print(0)
# } Driver Code Ends