"""
Preorder Traversal in Binary Tree 

Root -> Left Child -> RightChild 

"""

# Recursive 
def preorder(root):
    if root==None:
        return 
    print(root.data,end=" ") 
    preorder(root.left) 
    preorder(root.right) 


# Iterative 

def preorder_i(root):
    stack=[] 
    stack.append(root) 
    while stack:
        top = stack.pop()
        print(top,end=" ") 
        if top.right:
            stack.append(top.right) 
        if top.left:
            stack.append(top.left)

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
preorder_i(bt.head)