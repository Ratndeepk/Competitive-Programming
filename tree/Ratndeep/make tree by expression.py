def conv_util(l,s,e):
    n=None
    if s<e:
        n = Node(l[s])
        n.right=Node(l[e])
        
        n.left=conv_util(l,s+2,e-2)
    if s==e:
        n=Node(l[s])
    return n
     
    
    
def convert_expression(expression, i):
    #code here
    return conv_util(expression,i,len(expression)-1)
