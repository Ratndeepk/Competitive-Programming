def height(root,dia):
    if root==None:
        return 0
    lh = height(root.left,dia)
    rh = height(root.right,dia)
    dia[0] = max(dia[0],lh+rh+1)
    return max(lh,rh)+1
def diameter(root):
    # Code here
    dia=[0]
    if root==None:
        return 0
    height(root,dia)
    
    return dia[0]
