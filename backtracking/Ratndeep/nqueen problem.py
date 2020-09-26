def safe(chess,row,col,n):
    for i in range(row):
        if chess[i][col]==1:
            return False
    temp=col-1
    for i in range(row-1,-1,-1):
        if temp==-1:
            break
        if chess[i][temp]==1:
            return False
        temp-=1
    temp = col+1
    for i in range(row-1,-1,-1):
        if temp==n:
            break
        if chess[i][temp]==1:
            
            return False
        temp+=1 
    return True
    
    
def nqueen(n,chess,row):
    if row>=n:
        return True
    for col in range(n):
        if safe(chess,row,col,n):
            
            chess[row][col]=1
            
            if nqueen(n,chess,row+1):
                return True
            
            chess[row][col]=0
            
    return False
        
for _ in range(int(input())):
    n = int(input())
    if n>1:
        
        chess = [[0 for i in range(n)]for i in range(n)]
        row=0
        if nqueen(n,chess,row):

            for i in chess:
                print(*i)
            
           
    else:
        print([1])
