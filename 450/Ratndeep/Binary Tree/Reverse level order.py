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
    
    def reverseLevelOrder(self,root):
   
        stack=[]
        queue=[root]
        while queue!=[]:
            stack.insert(0,queue[0].data)
            cur_root=queue.pop(0)
            if cur_root.right:
                queue.append(cur_root.right)
            if cur_root.left:
                queue.append(cur_root.left)
        return stack

bt = BTree() 
data = list(map(int,input().split()))
for i in range(len(data)):
    bt.addNode(data[i]) 
print(*bt.reverseLevelOrder(bt.root))

