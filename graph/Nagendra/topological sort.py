def dfsutil(v, visit, graph, s):
    visit[v] = True
    for i in graph[v]:
        if visit[i]==False:
            dfsutil(i, visit, graph, s)
    s.insert(0,v)
    
def topoSort(n, graph):
    # Code here
    visit=[False]*n
    s=[]
    for i in range(n):
        if visit[i] is False:
            dfsutil(i, visit, graph, s)
<<<<<<< HEAD
    return s[::-1]
=======
    return s
>>>>>>> bbe2857a8d8fc597f39d3771b698af78daffaf05
