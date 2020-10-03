from collections import defaultdict
# Graph (adj) is a default dict of type list
# V is the number of vertices in the graph
stack=[]

def dfs(v,visited,graph):
    visited[v]=True
    for i in graph[v]:
        if visited[i]==False:
            dfs(i,visited,graph)
    stack.append(v)  

def dfst(v,visit,grapht):
    visit[v]=True
    for i in grapht[v]:
        if visit[i]==False:
            dfst(i,visit,grapht)
            

def countSCCs (adj, V):
    visited=[False]*V
    for i in range(V):
        if visited[i]==False:
            dfs(i,visited,adj)

    #graph transpose
    grapht=defaultdict(list)
    for i in range(V):
        for j in graph[i]:
            grapht[j].append(i)


    visit=[False]*V
    count=0
    while stack:
        i = stack.pop()
        if visit[i]==False:
            dfst(i,visit,grapht)
            count+=1
    return count
