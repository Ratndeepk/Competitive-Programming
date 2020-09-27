import sys
sys.setrecursionlimit(100000)
def safe(i,j,n,m,island,visited):
    if i>=0 and j>=0 and i<n and j<m and island[i][j]==1 and visited[i][j]==False:
        return True
    return False

def dfs(island,n,m,visited,i,j):
    row=[-1, -1, -1,  0, 0,  1, 1, 1]
    col=[-1,  0,  1, -1, 1, -1, 0, 1]
    visited[i][j]=True
    for k in range(8):
        if safe(i+row[k],j+col[k],n,m,island,visited):
            dfs(island,n,m,visited,i+row[k],j+col[k])
        
def findIslands(A, N, M):
    #code here
    visited=[[False for i in range(M)]for i in range(N)]
    count=0
    for i in range(N):
        for j in range(M):
            if visited[i][j]==False and A[i][j]==1:
                dfs(A,N,M,visited,i,j)
                count+=1
    return count
