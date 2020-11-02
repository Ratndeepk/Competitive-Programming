def mirror(root):
    # Code here
    if root==None:
        return
    mirror(root.left)
    mirror(root.right)
    temp=root.left
    root.left=root.right
    root.right=temp
