def safe(row,col,visited):
    if row>=0 and col>=0 and row<n and col<m and visited[row][col]==False and matrix[row][col]=="X":
        return True
    return False

def dfs(visited,matrix,row,col):
    x_axis=[1,0,-1,0]
    y_axis =[0,1,0,-1]
    visited[row][col]=True
    for i in range(4):
        if safe(row+x_axis[i],col+y_axis[i],visited):
            dfs(visited,matrix,row+x_axis[i],col+y_axis[i])
    


for i in range(int(input())):
    n,m=map(int,input().split())
    string_array = input().split()
    matrix=[]
    for i in range(n):
        for j in string_array:
            matrix.append(list(j))
    visited = [[False for i in range(m)] for j in range(n)]
    count=0
    for i in range(n):
        for j in range(m):
            if visited[i][j]==False and matrix[i][j]=="X":
                dfs(visited,matrix,i,j)
                count+=1
    print(count)
