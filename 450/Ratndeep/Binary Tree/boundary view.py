def addleft(root,a):
    if root:
        if root.left:
            #a.append(root.data) 
            print(root.data,end=" ")
            addleft(root.left,a) 
            
        if root.right:
            #a.append(root.data)
            print(root.data,end=" ")
            addleft(root.right,a)
            

def addleaf(root,a):
    if root: 
        addleaf(root.left,a)
        if root.left==None and root.right==None:
            #a.append(root.data)
            print(root.data,end=" ")
        addleaf(root.right,a)

def addright(root,a):
    if root:
        if root.right:
            
            addright(root.right,a) 
            #a.append(root.data) 
            print(root.data,end=" ")
        if root.left:
            
            addright(root.left,a) 
            #a.append(root.data)
            print(root.data,end=" ")
            
    
def printBoundaryView(root):
    #a=[root.data]
    a=[]
    print(root.data,end=" ")
    addleft(root.left,a)
    addleaf(root.left,a)
    addleaf(root.right,a)
    addright(root.right,a)
    
    return []