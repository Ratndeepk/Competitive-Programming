#User function Template for python3

'''
*  g[]: adj list of the graph
*  N : number of vertices
'''
import queue
from collections import defaultdict
import sys
import io
import atexit


def bfs(g, N):
    # code here
    visited = [0]*N
    q = []
    visited[0] = 1
    res = [0, ]
    i = 0

    while(1):

        for j in g[i]:
            if visited[j] == 0:
                q.append(j)
                visited[j] = 1
        if len(q) == 0:
            return res
        else:
            i = q[0]
            res.append(i)
            q.pop(0)


#{
#  Driver Code Starts
#Initial Template for Python 3
#Contributed by : Nagendra 


#Graph Class:
class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):  # add directed edge from u to v.
        self.graph[u].append(v)


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        N, E = map(int, input().strip().split())
        g = Graph(N)
        edges = list(map(int, input().strip().split()))

        for i in range(0, len(edges), 2):
            u, v = edges[i], edges[i+1]
            g.addEdge(u, v)  # add a directed edge from u to v

        res = bfs(g.graph, N)  # print bfs of graph
        for i in range(len(res)):
            print(res[i], end=" ")
        print()

# } Driver Code Ends
