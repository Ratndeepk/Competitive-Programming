from collections import defaultdict
nodes = list(map(int,input().split())) 
edges = int(input()) 
graph = defaultdict(list) 
matrix = [[0 for i in range(nodes)] for i in range(nodes)]
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

