def cloneutil(node,k):
    if node==None:
        return
    head=Node(node.data)
    k[node]=head
    head.left=cloneutil(node.left,k)
    head.right=cloneutil(node.right,k)
    return head
    
def clonerandom(node,head,k):
    if node==None:
        return
    if node.random:
        head=k[node]
    clonerandom(node.left,head.left,k)
    clonerandom(node.right,head.right,k)
    
    
def cloneTree(node):
    k={}
    head=cloneutil(node,k)
    clonerandom(node,head,k)
    return head
