def levelorder(root,dict,level):
    if root ==None:
        return 
    if level not in dict:
        dict[level]=[root.data] 
    else:
        dict[level].append(root.data) 
        
    levelorder(root.left,dict,level+1) 
    levelorder(root.right,dict,level+1) 
    
def zigZagTraversal(root):
    ans=[]
    dict={} 
    levelorder(root,dict,0)
    for i in sorted(dict):
        if i%2==0:
            ans.extend(dict[i]) 
        else:
            ans.extend(dict[i][::-1])
    return ans


""" 
Logic -> 

Do a level order traversal & add each level nodes in particular dict
now iterate over sorted dict whenever level is even take as it is,
but if its odd take in reverse order

"""