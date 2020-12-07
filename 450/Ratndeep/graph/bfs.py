from collections import defaultdict
def bfs(graph,x):
    visited=[False]*len(arr) 
    print(x,end=" ") 
    queue=[x] 
    visited[x]=True
    while queue:
        cur_node = queue.pop() 
        for i in graph[cur_node]:
            if visited[i]==False: 
                visited[i]=True 
                print(i,end=" ") 
                queue.insert(0,i) 
            

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

bfs(g.graph,0)   #starting bfs from 0