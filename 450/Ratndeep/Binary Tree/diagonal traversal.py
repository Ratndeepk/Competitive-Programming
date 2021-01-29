def preorder(root,dict,count):
    if root==None:
        return 
    if count not in dict:
        dict[count]=[root.data] 
    else:
        dict[count].append(root.data) 
        
    preorder(root.left,dict,count+1) 
    preorder(root.right,dict,count)
def diagonal(root):
    dict={}
    count=0
    
    preorder(root,dict,count)
    a=[] 
    for i in sorted(dict):
        a.extend(dict[i]) 
        
    return a


    
    