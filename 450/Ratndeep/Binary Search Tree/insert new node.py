def insert(root, Key):
    node=Node(Key) 
    if root==None:
        return node 
    while(root):
        if root.data==Key:
            break
        if root.data>Key:
            if root.left:
                root=root.left
                
            else:
                root.left=node
                break
        else:
            if root.right:
                root=root.right
            else:
                root.right=node 
                break