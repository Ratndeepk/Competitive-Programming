#User function Template for python3

'''
g : adjacency list of graph
N : number of vertices

return a list containing the DFS traversal of the given graph
'''
from collections import defaultdict
import sys
import io
import atexit


def vis(g, v, visited, res):

    visited[v] = 1

    res.append(v)
    #print(res)
    for i in g[v]:
        if visited[i] == 0:
            vis(g, i, visited, res)


def dfs(g, N):

    # code here
    visited = [0]*N
    res = []
    vis(g, 0, visited, res)
    return res


#{
#  Driver Code Starts
#Initial Template for Python 3
sys.setrecursionlimit(10**6)

#Contributed by : Nagendra Jha

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
            g.addEdge(u, v)  # add an undirected edge from u to v
            g.addEdge(v, u)

        res = dfs(g.graph, N)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()

# } Driver Code Ends
