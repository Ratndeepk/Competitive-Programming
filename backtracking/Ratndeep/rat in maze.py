n = 4
def safe(x,y,maze):
    if x<n and y<n and maze[x][y]==1:
        return True
    return False


def solve(maze,x,y,sol,dx,dy):
    if x==dx and y==dy and maze[x][y]==1:
        sol[x][y]=1
        return True
    if safe(x,y,maze):
        sol[x][y]=1
        if solve(maze,x+1,y,sol,dx,dy):
            return True
        if solve(maze,x,y+1,sol,dx,dy):
            return True
        sol[x][y]=0
        return False


maze = [[1,0,0,0],[1,1,0,1],[0,1,0,1],[1,1,1,1]]
dx=int(input())
dy=int(input())
sol = [[0 for i in range(4)]for i in range(4)]
if solve(maze,0,0,sol,dx,dy):
    for i in sol:
        print(*i)
else:
    print("Not possible")
