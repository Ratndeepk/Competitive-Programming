def identical(r1,r2):
    if r1==None and r2==None:
        return True 
    if r1==None or r2==None:
        return False 

    return r1.data==r2.data and identical(r1.left,r2.left) and identical(r1.right,r2.right)
    
    
def prove(root1,root2):
    if root1==None and root2==None:
        return False
    if root1==None:
        return False 
    if root2==None:
        return True 

    if identical(root1,root2):
        return True 

    return prove(root1.left,root2) or prove(root1.right,root2)