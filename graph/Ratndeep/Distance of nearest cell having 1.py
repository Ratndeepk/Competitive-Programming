from collections import defaultdict
def BFS(self, s): 
    visited = [False] * (len(self.graph)) 
    queue = [] 
    queue.append(s) 
    visited[s] = True
  
    while queue: 
        s = queue.pop(0) 
        print (s, end = " ") 
        for i in self.graph[s]: 
            if visited[i] == False: 
                queue.append(i) 
                visited[i] = True



def DFSutil(matrix,visited,row,col,x,y)
    x_axis = [0,0,1,-1,1,-1-1,1]
    y_axis = [1,-1,0,0,1,-1,1,-1]
    
    for i in range(8):
        new_x = x+x_axis[i]
        new_y = y+y_axis[i]
        if safe(new_x,new_y,visited,row,col):
            visited[new_x][new_y]=True
            if matrix[new_x][new_y]==1:
                return new_x,new_y
            
    
def DFS(matrix,row,col):
    visited = [[False for i in range(col)]for i in range(row)]
    graph = defaultdict(list)
    for i in range(row):
        for j in range(col):
            graph[i].append(j)
            x,y=DFSutil(matrix,visited,row,col,i,j)
            print(abs(i-x)+abs(j-y),end=" ")
    print()

for _ in range(int(input())):
    row,col = map(int,input().split())
    list_matrix = list(map(int,input().split())))
    index=0
    for i in range(row):
        temp_matrix=[]
        for j in range(col):
            temp_matrix.append(list_matrix[index])
            index+=1
        matrix.append(temp_matrix)
        
    DFS(matrix)
