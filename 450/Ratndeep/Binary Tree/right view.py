
def height(root):
    if root==None:
        return 1 
    return max(height(root.left),height(root.right))+1
def rightview(root,v,a,level):
    if root==None:
        return
    if v[level]==False:
        a.append(root.data) 
        v[level]=True
    rightview(root.right,v,a,level+1) 
    rightview(root.left,v,a,level+1)


    
def rightView(root):
    a=[]
    x = height(root)
    v=[False]*x
    rightview(root,v,a,0)
    return a
