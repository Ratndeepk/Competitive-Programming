def bstutil(root,min_v,max_v):
    if root is None:
        return True
    if root.data>=min_v and root.data<max_v and bstutil(root.left,min_v,root.data) and bstutil(root.right,root.data,max_v):
        return True
    return False
def isBST(root):
    return bstutil(root,-float("inf"),float("inf"))
