def dfsutil(v,N,g,visited,result):
    visited[v]=True
    result.append(v)
    for i in g[v]:
        if visited[i]==False:
            dfsutil(i,N,g,visited,result)
                
def dfs(g,N):
    visited=[False]*(max(g)+1)
    result=[]
    dfsutil(0,N,g,visited,result)
    # code here
    return result
