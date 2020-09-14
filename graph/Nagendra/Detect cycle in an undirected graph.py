#User function Template for python3
from collections import defaultdict
import sys
import io
import atexit


def check(g, n, visited, rectrack, parent):

    visited[n] = 1
    rectrack[n] = 1

    for adj in g[n]:
        if visited[adj] == 0:
            parent[adj] = n
            if check(g, adj, visited, rectrack, parent) == 1:
                return 1
        elif rectrack[adj] == 1 and adj != parent[n]:
            return 1

    rectrack[n] = 0
    return False


def isCyclic(g, n):
    '''
    :param g: given adjacency list representation of graph
    :param n: no of nodes in graph
    :return:  boolean (whether a cycle exits or not)
    '''
    # code here
    visited = [0]*n
    rectrack = [0]*n
    parent = [0]*n

    for i in range(n):
        if visited[i] == 0:
            if check(g, i, visited, rectrack, parent) == 1:
                return 1
    return 0


#{
#  Driver Code Starts
#Initial Template for Python 3

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
        print(isCyclic(g.graph, N))
# } Driver Code Ends
