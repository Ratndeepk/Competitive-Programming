from collections import defaultdict
def cycleutil(node,graph,visited,stack):
    visited[node]=True 
    stack[node]=True 
    
    for i in graph[node]:
        if visited[i]==False:
            if cycleutil(i,graph,visited,stack)==True:
                return True 
        elif stack[i]==True:
            return True 
    stack[node]=False
    return False 
    
    
def cycle(graph):
    visited=[False]*len(arr) 
    stack=[False]*len(arr) 
    for i in arr:
        if visited[i]==False:
            if cycleutil(i,graph,visited,stack):
                return True 
    return False
            

class Graph:
    def __init__(self):
        self.graph=defaultdict(list) 

    def addnode(self,u,v):
        self.graph[u].append(v) 
        

g = Graph() 
arr = list(map(int,input().split())) 
q = int(input()) 
for i in range(q):
    u,v = map(int,input().split())
    g.addnode(u,v) 

print(cycle(g.graph))