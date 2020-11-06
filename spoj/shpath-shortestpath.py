from collections import defaultdict

def dfs(graph,matrix,x,y,cost,initial_cost,visited):
    if x==y:
        return
    if cost[0]>initial_cost:
        cost[0]=initial_cost
        return 
    for i in graph[x]:
        
        if visited[i]==False:
            visited[i]=True
            cost[0]+=matrix[i][x]
            dfs(graph,matrix,i,y,cost,initial_cost,visited)
            return cost[0] 
        
    return cost[0]


def shortestpath(graph,matrix,x,y,n):
    initial_cost = matrix[x][y]
    
    for i in graph[x]:
        visited = [False]*n
        visited[x]=True
        initial_cost = min(initial_cost,dfs(graph,matrix,i,y,[matrix[i][x]],initial_cost,visited))
    return initial_cost

for _ in range(int(input())):
    n = int(input())
    country = {}
    graph = defaultdict(list)
    matrix = [[float("inf") for i in range(n)]for i in range(n)]
    for cities in range(n):
        country[input()]=cities
        
        for num_of_city in range(int(input())):
            
            # cities input
            y,w = map(int,input().split())
            
            # connecting cities
            graph[cities].append(y-1)
            
            # cost
            matrix[cities][y-1]=w 

    for cost in range(int(input())):
        
        # source & destination
        city1,city2 = map(str,input().split())
        
        # min cost
        print(shortestpath(graph,matrix,country[city1],country[city2],n))



