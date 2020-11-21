def isHeap(root):
    
    if root.left is None and root.right is None:
        return True
    if root.right is None:
        if root.data>=root.left.data:
            return isHeap(root.left)
        else:
            return False
    else:
        if root.data>=root.left.data and root.data>=root.right.data:
            return isHeap(root.left) and isHeap(root.right)
        else:
            return False
