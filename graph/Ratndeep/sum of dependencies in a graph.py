from collections import defaultdict
for _ in range(int(input())):
    v,e = map(int,input().split())
    connections = list(map(int,input().split()))
    graph = defaultdict(list)
    for i in range(0,len(connections),2):
        graph[connections[i]].append(connections[i+1])
    count=0
    for key,value in graph.items():
        count+=len(value)
        
    print(count)
