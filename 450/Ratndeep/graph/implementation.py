from collections import defaultdict
nodes = list(map(int,input().split())) 
edges = int(input()) 
graph = defaultdict(list) 
for i in range(edges):
    a,b = map(int,input().split()) 
    
    #undirected graph
    graph[a].append(b) 
    graph[b].append(a) 

    #directed graph 
    graph[a].append(b) 


    #weighted edge 
    graph[a].append(b)
    graph[b].append(a) 

    matrix[a][b]=w 
    matrix[b][a]=w 
    
