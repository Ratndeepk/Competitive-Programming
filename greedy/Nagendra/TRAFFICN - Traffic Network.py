from collections import defaultdict
import heapq

def djikstra(sr,dist,graph):

    dist[sr] = 0
    min_dist = [(0, sr)]
    visited = set()

    while min_dist:
        cur_dist, cur = heapq.heappop(min_dist)
        if cur in visited:
            continue
        visited.add(cur)
        for neighbor in graph[cur]:
            if neighbor in visited:
                continue
            this_dist = cur_dist + graph[cur][neighbor]
            if this_dist < dist[neighbor]:
                dist[neighbor] = this_dist
                heapq.heappush(min_dist, (this_dist, neighbor))


for _ in range(int(input())):
    n, m, k, s, t = map(int, input().split())
    graph = defaultdict(dict)
    rgraph = defaultdict(dict)
    for i in range(m):
        d, c, l = map(int, input().split())
        graph[d][c] = l
        rgraph[c][d]=l

    dist = {i: float('inf') for i in range(1, n+1)}
    rdist = {i: float('inf') for i in range(1, n+1)}
    djikstra(s,dist,graph)
    djikstra(t,rdist,rgraph)
    fmin_dist=float('inf')               
    for i in range(k):
        u, v, j = map(int, input().split())
        fmin_dist = min(dist[t], min(fmin_dist, j+min(dist[u]+rdist[v], dist[v]+rdist[u])))
            
    if fmin_dist == float('inf'):
        print('-1')
    else:
        print(fmin_dist)
