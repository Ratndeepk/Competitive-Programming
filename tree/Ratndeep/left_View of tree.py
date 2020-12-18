def LeftView(root):
    if root is None:
        
        return
    print(root.data,end=" ")
    if root.left==None:
        if root.right:
            LeftView(root.right)
    LeftView(root.left)
