def safe(x,y,matrix):
    if x>=0 and y>=0 and x<row and y<col  and matrix[x][y]==1:
        return True
    return False
def dfsutil(matrix,row,col,x_axis,y_axis,x,y,count):
  
    for i in range(4):
        new_x = x+x_axis[i]
        new_y = y+y_axis[i]
        if safe(new_x,new_y,matrix):
            matrix[new_x][new_y]=2
            count+=1
            dfsutil(matrix,row,col,x_axis,y_axis,new_x,new_y,count)
            
    return count
    
def dfs(matrix,row,col):
    #visited = [[False for i in range(col)]for i in range(row)]
    x_axis = [1,-1,0,0]
    y_axis = [0,0,1,-1]
    count=0
    for i in range(row):
        for j in range(col):
            if matrix[i][j]==2:
                count=max(count,dfsutil(matrix,row,col,x_axis,y_axis,i,j,0))
                
    return count


for _ in range(int(input())):
    row,col = map(int,input().split())
    ini_list = list(map(int,input().split()))
    index=0
    matrix=[]
    for i in range(row):
        temp_list=[]
        for j in range(col):
            temp_list.append(ini_list[index])
            index+=1
        matrix.append(temp_list)
    
    count=dfs(matrix,row,col)
    flag=0
    for i in matrix:
        for j in i:
            if j==1:
                flag=1
                break
    
    if not flag:
        print(count)
    else:
        print(-1)

