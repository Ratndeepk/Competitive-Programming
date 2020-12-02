
def inorder(root):
    if root==None:
        return
    inorder(root.left) 
    print(root.data,end=" ") 
    inorder(root.right) 



def inorder(root):
    if root==None:
        return
    inorder(root.left) 
    print(root.data,end=" ") 
    inorder(root.right) 


def inorder_rec(root1):
    stack=[]
    root=root1
    while(stack or root):
        if root:
            stack.append(root)
            root=root.left
        else:
            root=stack.pop()
            print(root.data,end=" ")
            root=root.right
            

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
inorder(bt.head)
inorder_rec(bt.head)





