# Your task is to complete this function
# Function should return Topologically Sorted List
# Graph(adj) is a defaultict of type List
# n is no of edges
def topsortutil(stack,adj,m,v):
    v[m]=True
    for i in adj[m]:
        if v[i]==False:
            topsortutil(stack,adj,i,v)
    stack.insert(0,m)



def topoSort(n, adj):
    # Code here
    stack=[]
    v= [False]*n
    for i in range(n):
        if v[i]==False:
            topsortutil(stack,adj,i,v)
    return stack
