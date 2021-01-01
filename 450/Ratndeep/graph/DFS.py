from collections import defaultdict
def dfsutil(node,graph,visited):
    visited[node]=True 
    print(node,end=" ")
    for i in graph[node]:
        if visited[i]==False:
            dfsutil(i,graph,visited) 
    
    
def dfs(graph):
    visited=[False]*len(arr) 

    dfsutil(0,graph,visited)
            

class Graph:
    def __init__(self):
        self.graph=defaultdict(list) 

    def addnode(self,u,v):
        self.graph[u].append(v) 
        self.graph[v].append(u)

g = Graph() 
arr = list(map(int,input().split())) 
q = int(input()) 
for i in range(q):
    u,v = map(int,input().split())
    g.addnode(u,v) 

dfs(g.graph)