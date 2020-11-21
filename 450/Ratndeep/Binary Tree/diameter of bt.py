def height(root,dia):
    if root==None:
        return 0
    lh = height(root.left,dia)
    rh = height(root.right,dia)
    dia[0] = max(dia[0],lh+rh+1)
    return max(lh,rh)+1
def diameter(root):
    # Code here
    dia=[0]
    if root==None:
        return 0
    height(root,dia)
    
    return dia[0]



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
    
    

bt = BTree() 
data = list(map(int,input().split()))
for i in range(len(data)):
    bt.addNode(data[i]) 
print(diameter(bt.root))

