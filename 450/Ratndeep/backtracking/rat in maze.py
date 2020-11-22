def safe(visited,x,y):
    if x>=0 and y>=0 and x<n and y<n and visited[x][y]==False and arr[x][y]==1:
        return True
    return False
    
def find(arr,visited,x,y,x_axis,y_axis,n):
    if x==n-1 and y==n-1:
        return True
    for i in range(4):
        cur_x = x+x_axis[i]
        cur_y = y+y_axis[i] 
        if safe(visited,cur_x,cur_y):
            visited[cur_x][cur_y]=True
            if find(arr,visited,cur_x,cur_y,x_axis,y_axis,n):
                return True
    return False
            
    
def findPath(arr, n):
    # code here
    visited=[[False for i in range(n)] for i in range(n)] 
    x_axis = [1,-1,0,0]
    y_axis = [0,0,1,-1] 
    if find(arr,visited,0,0,x_axis,y_axis,n):
        print("YES")
    else:
        print("NO")


n = int(input()) 
arr=[] 
for i in range(n):
    arr.append(list(map(int,input().split()))) 

findPath(arr,n)
