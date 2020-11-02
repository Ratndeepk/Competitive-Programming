def height(root):
    if root==None:
        return 0
    lh = height(root.left)
    rh = height(root.right)
    return max(lh,rh)+1
def diameter(root):
    # Code here
    if root==None:
        return 0
    lh = height(root.left)
    rh = height(root.right)
    
    ld = diameter(root.left)
    rd = diameter(root.right)
    return max(lh+rh+1,max(ld,rd))
