#recursive
def postorder(root):
    if root==None:
        return 
    postorder(root.left) 
    postorder(root.right) 
    print(root.data,end=" ") 

def postOrder(root):
    stack=[root] 
    sol=[]
    while stack:
        top=stack.pop()
        sol.append(top.data) 
        if top.left:
            stack.append(top.left) 
        if top.right:
            stack.append(top.right) 
    return sol[::-1]   

 
    
    
    
class Node:
    def __init__(self,data):
        self.data=data 
        self.left=None 
        self.right=None 

class BTree:
    def __init__(self):
        self.head=None 

    def addNode(self,data): 
        node = Node(data) 
        root=self.head
        if root==None:
            self.head=node 
        else:
            while(root):
                if root.data<node.data:
                    if root.right==None:
                        root.right = node 
                        break 
                    else: 
                        root=root.right 
                else: 
                    if root.left==None: 
                        root.left=node 
                        break 
                    else: 
                        root=root.left 
        
    

bt = BTree() 
data = list(map(int,input().split()))
for i in range(len(data)):
    bt.addNode(data[i])  
postorder(bt.head)