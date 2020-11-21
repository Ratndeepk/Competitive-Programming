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
    def levelorder(self,root):
        queue=[] 
        queue.append(root) 
        while queue!=[]:
            print(queue[0],end=" ") 
            cur_root=queue.pop() 
            if cur_root.left: 
                queue.append(cur_root.left) 
            if cur_root.right:
                queue.append(cur_root.right)  

        print() 

bt = BTree() 
data = list(map(int,input().split()))
for i in range(len(data)):
    bt.addNode(data[i]) 
bt.levelorder(bt.root) 

