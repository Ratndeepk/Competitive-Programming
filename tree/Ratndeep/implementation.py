class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Bt:
    def __init__(self):
        self.root=None

    def addnode(self,data):
        node = Node(data)
        if self.root is None:
            self.root=node
        else:
            cur_root=self.root
            while(cur_root):
                if node.data>cur_root.data:
                    if cur_root.right:
                        cur_root=cur_root.right
                    else:
                        cur_root.right=node
                        break
                else:
                    if cur_root.left:
                        cur_root=cur_root.left
                    else:
                        cur_root.left=node
                        break
    def printbt(self,root):
        if root.left:
            self.printbt(root.left)
        print(root.data,end=" ")
        if root.right:
            self.printbt(root.right)

    
    def levelOrder(self, root):
    # Code here
        queue=[]
        l=[]
        queue.append(root)
        while queue!=[]:
            l.append(queue[0].data)
            
            
            cur_root = queue.pop(0)
            if cur_root.left:
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)
            
        return l
sample_array = list(map(int,input().split()))
bt=Bt()
for i in range(len(sample_array)):
    bt.addnode(sample_array[i])

print("Inorder->")
bt.printbt(bt.root)
print()
print("Level order->")
print(*bt.levelOrder(bt.root))
l = bt.levelOrder(bt.root)
l.sort(reverse=True)
print(*l)
