from collections import defaultdict

def cycleutil(v,graph,visited,parent):
    visited[v]=True 

    for i in graph[v]:
        if visited[i]==False:
            if cycleutil(i,graph,visited,v):
                return True 
        elif parent!=i:
            return True 
    return False
def cycle(graph):
    visited=[False]*len(arr) 
    for i in arr:
        if visited[i]==False:
            if cycleutil(i,graph,visited,i):
                return True 
    return False

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

print(cycle(g.graph))