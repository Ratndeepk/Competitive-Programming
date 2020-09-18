def util(node,visited,recstack):
    visited[node]=True
    recstack[node]=True
    for i in graph[node]:
        if visited[i]==False:
            if util(i,visited,recstack):
                return True
        elif recstack[i]==True:
            return True
    recstack[node]=False
    return False
    
    
    
def isCyclic(n, graph):
    visited=[False]*(n)
    recstack=[False]*(n)
    for i in range(n):
        if util(i,visited,recstack)==True:
            return 1
    return 0
