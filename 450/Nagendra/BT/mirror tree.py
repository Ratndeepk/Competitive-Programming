#incomplete

class Node:
    def __init__(self,val):
        self.left=None
        self.val = val
        self.right = None

def mirror(root):

    from collections import deque
    if root:
        q = deque()
        q.append(root)
        mroot = None
        while q:
            a = q.pop()
            if mroot==None:
                mroot = Node(q.val)
                new = mroot
            new.left = Node(q.val)
            if a.left:
                q.append(a.left)
            if a.right:
                q.append(a.right)
            



    return root







def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

root = Node(5)
root.left = Node(3)
root.left.left = Node(2)
root.left.right = Node(4)
root.right = Node(6)

mirror = mirror(root)
inorder(mirror)


