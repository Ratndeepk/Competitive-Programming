# link https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1#
#pirm's-----------------------------
# Function to construct and return cost of MST for a graph
# represented using adjacency matrix representation
'''
V: nodes in graph
E: number of edges in graph
graph: adjacency matrix, graph[i][j]=weight, if edge exits , else float("inf").
'''
def spanningTree(V, E, graph):
    #code here
    minn = 999999
    #print(graph)
    for i in range(V):
        if minn > min(graph[i]):
            minn=min(graph[i])
            l=i
            r=graph[i].index(minn)
    min_cost = graph[l][r]
    near = [-1]*V
    for i in range(V):
        if graph[i][l]<graph[i][r]:
            near[i]=l
        else:
            near[i]=r
    near[l]=near[r]=-1
    #print(near,min_cost)
    for i in range(V-2):
        m=999999
        for j in range(V):
            if near[j]!=-1:
                if m>graph[j][near[j]]:
                    m= graph[j][near[j]]
                    l=near[j]
                    r=j
        min_cost+=m
        
        for k in range(V):
            if near[k]!=-1 and graph[k][near[k]] > graph[k][r]:
                near[k]= r
        near[r]=-1
        #print(near,min_cost,r)
    return min_cost
        
    
            



#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        info = list(map(int,input().strip().split()))
        graph = [[float("inf") for i in range(V)] for i in range(V)]
        for i in range(0,len(info),3):
            u,v,w = info[i]-1,info[i+1]-1,info[i+2]
            graph[u][v] = w
            graph[v][u] = w
        print(spanningTree(V,E,graph))
# } Driver Code Ends
