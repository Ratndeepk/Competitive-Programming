from collections import defaultdict

def safe(row,col,visited):
    if row>=0 and col>=0 and row<n and col<m and visited[row][col]==False and final_matrix[row][col]==1:
        return True
    return False

def dfs(visited,matrix,row,col,size):
    x_axis = [-1, -1, -1, 0, 0, 1, 1, 1]  
    y_axis = [-1, 0, 1, -1, 1, -1, 0, 1] 
    visited[row][col]=True
    for move in range(8):
        if safe(row+x_axis[move],col+y_axis[move],visited):
            size[0]+=1
            new_row=row+x_axis[move]
            new_col=col+y_axis[move]
            dfs(visited,matrix,new_row,new_col,size)
            
    

for _ in range(int(input())):
    graph = defaultdict(list)
    n,m = map(int,input().split())
    matrix = list(map(int,input().split()))
    final_matrix=[]
    col=0
    for i in range(n):
        case_row=[]
        for j in range(m):
            case_row.append(matrix[col])
            col+=1
        final_matrix.append(case_row)
    max_size=-999999999999999999999
    visited=[[False for i in range(m)] for i in range(n)]
    for row in range(n):
        for col in range(m):
            
            if visited[row][col]==False and final_matrix[row][col]==1:
                size=[1]
                dfs(visited,matrix,row,col,size)
                max_size=max(max_size,size[0])
    print(max_size)
    
    
        
