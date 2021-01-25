
class Node:
    def __init__(self, val):
        self.left = None
        self.val = val
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end =' ')
        inorder(root.right)

def iterrative(root):

    stack = []
    curr = root
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr= stack.pop()
            print(curr.val, end=' ')
            curr = curr.right



root = Node(5)
root.left = Node(3)
root.left.left = Node(2)
root.left.right = Node(4)
root.right = Node(6)

print("Recursive---------------")
inorder(root)
print("\nIterative---------------")
iterrative(root)