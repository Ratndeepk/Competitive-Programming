
def thatcolumn(x,y,matrix,cur_color,fin_color,col,row,visited):
    if y>=col or y<0:
        return
    if x>=row or x<0:
        return 
    if visited[x][y]==True:
        return
    if matrix[x][y]!=cur_color:
        return
    matrix[x][y]=fin_color
    visited[x][y]=True
    thatcolumn(x+1,y,matrix,cur_color,fin_color,col,row,visited)
    thatcolumn(x,y+1,matrix,cur_color,fin_color,col,row,visited)
    thatcolumn(x-1,y,matrix,cur_color,fin_color,col,row,visited)
    
    thatcolumn(x,y-1,matrix,cur_color,fin_color,col,row,visited)
        
def checkall(x,y,matrix,cur_color,fin_color,col,row,visited):
    thatcolumn(x,y,matrix,cur_color,fin_color,col,row,visited)
    
    
for _ in range(int(input())):
    row,col =   map(int,input().split())
    initial_list = list(map(int,input().split()))
    matrix=[]
    index=0
    visited = [[False for i in range(col)]for i in range(row)]
    for i in range(row):
        cur_row=[]
        for j in range(col):
            cur_row.append(initial_list[index])
            index+=1
        matrix.append(cur_row)
    for i in matrix:
        print(*i)
    print()
    x,y,fin_color = map(int,input().split())
    cur_color = matrix[x][y]
    checkall(x,y,matrix,cur_color,fin_color,col,row,visited)
    for i in matrix:
        print(*i)
    print()
    
    
