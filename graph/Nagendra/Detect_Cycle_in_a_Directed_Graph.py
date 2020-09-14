# Your task is to complete this function
# Function should return True/False or 1/0
# Graph(graph) is a defaultict of type List
# n is no of Vertices

from collections import defaultdict


def check(v, g, visited, rectrack):

    visited[v] = 1
    rectrack[v] = 1

    for i in graph[v]:
        if visited[i] == 0:
            if check(i, g, visited, rectrack) == True:
                return True
        elif rectrack[i] == 1:
            return True

    rectrack[v] = 0
    return False


def isCyclic(n, graph):
    # Code here
    visited = [0]*n
    rectrack = [0]*n

    for i in range(n):
        if visited[i] == 0:
            if check(i, graph, visited, rectrack) == True:
                return True
    return False


#{
#  Driver Code Starts


def creategraph(n, arr, graph):
    i = 0
    while i < 2 * e:
        graph[arr[i]].append(arr[i + 1])
        # graph[arr[i + 1]].append(arr[i])
        i += 2


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, e = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(e, arr, graph)
        if isCyclic(n, graph):
            print(1)
        else:
            print(0)
# } Driver Code Ends
