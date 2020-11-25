def safe(chess,row,col,n,row_mat):
    if row_mat[row]==True:
        return False
    for i in range(col):
        if chess[row][i]==1:
            return False

    for i,j in zip([*range(row-1,-1,-1)],[*range(col-1,-1,-1)]):
        if chess[i][j]==1:
            return False
    for i,j in zip([*range(row+1,n)],[*range(col-1,-1,-1)]):
        if chess[i][j]==1:
            return False

    return True

def nqueen(n,chess,col,row_mat):
    if col==n:
        return True
    for row in range(n):
        if safe(chess,row,col,n,row_mat):
            
            chess[row][col]=1
            if col==0:
                row_mat[row]=True
            if nqueen(n,chess,col+1,row_mat):
                return True
            
            chess[row][col]=0
            if col==0:
                row_mat[row]=False
    return False

for _ in range(int(input())):
    n = int(input())
    if n>1:
        
        chess = [[0 for i in range(n)]for i in range(n)]
        col=0
        row_mat = [False]*n
        if nqueen(n,chess,col,row_mat):
            for i in chess:
                print(*i)
            print()
        
    else:
        print([1])