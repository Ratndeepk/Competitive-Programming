def KDistanceUtil(root,k,nodes):
    if root is None: 
        return 
    if k == 0: 
        nodes.append(root.data)
    else: 
        KDistanceUtil(root.left, k-1,nodes) 
        KDistanceUtil(root.right, k-1,nodes) 
        
def KDistance(root, k): 

    nodes = []
    KDistanceUtil(root,k,nodes)
    return nodes

