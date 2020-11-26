#link https://practice.geeksforgeeks.org/problems/negative-weight-cycle/0#
from collections import defaultdict


def bellManFord(graph, src, v):

    dist = {i: float('inf') for i in range(v+1)}
    dist[src] = 0
    # print(dist,graph)

    for i in range(v-1):
        for u, v, w in graph:
            # print(u)
            cur = dist[u]+w
            if cur < dist[v]:
                dist[v] = cur
    for u, v, w in graph:
        cur = dist[u]+w
        if cur < dist[v]:
            return 1
    return 0


for _ in range(int(input())):
    v, e = map(int, input().split())
    # v,e=5,8
    graph = []
    t = list(map(int, input().split()))
    # print(t)
    for i in range(0, 3*e, 3):
        # print(i)
        graph.append(t[i:i+3])

    print(bellManFord(graph, 0, v))
