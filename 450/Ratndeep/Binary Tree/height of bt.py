

class Node:
    def __init__(self,data):
        self.data=data 
        self.left=None 
        self.right=None 

class BTree:
    def __init__(self):
        self.root=None 


    def addNode(self,data): 
        node = Node(data) 

        while(root):
            if root.data>node.data:
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
    def height(root):
        if root==None:
            return 0
        lh = height(root.left)
        rh = height(root.right)
        return max(lh,rh)+1 
    

bt = BTree() 
data = list(map(int,input().split()))
for i in range(len(data)):
    bt.addNode(data[i]) 
print(bt.height(bt.root))

