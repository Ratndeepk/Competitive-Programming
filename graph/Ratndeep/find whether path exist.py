#code
def safe(x,y,matrix,visited):
    if x<n and y<n and x>=0 and y>=0 and visited[x][y]==False:
        print(x,y,matrix[x][y])
        if matrix[x][y]==3 or matrix[x][y]==2:
            
            return True
    return False

def findpath(matrix,x,y,move_x,move_y,dest_x,dest_y):
    if source_x==dest_x and source_y==dest_y:
       return True
    
    for i in range(4):
        print(x,y)
        new_x=x+move_x[i]
        new_y=y+move_y[i]
        print(new_x,new_y,"moves=",move_x[i],move_y[i])
        if safe(new_x,new_y,matrix,visited):
            visited[new_x][new_y]=True
            if matrix[new_x][new_y]==2:
                return True
            
            if findpath(matrix,new_x,new_y,move_x,move_y,dest_x,dest_y):
                return True
            
            return False
for _ in range(int(input())):
    n = int(input())
    list_matrix = list(map(int,input().split()))
    cursor=0
    matrix=[]
    visited = [[False for i in range(n)]for i in range(n)]
    for i in range(n):
        h_matrix=[]
        for j in range(n):
            h_matrix.append(list_matrix[cursor])
            if list_matrix[cursor]==1:
                source_x=i
                source_y=j
            if list_matrix[cursor]==2:
                dest_x=i
                dest_y=j
            
            cursor+=1
        matrix.append(h_matrix)
    move_x = [1,0,0,-1]
    move_y = [0,1,-1,0]
    
    for i in matrix:
        print(*i)
    if findpath(matrix,source_x,source_y,move_x,move_y,dest_x,dest_y):
        print(1)
    else:
        print(0)
