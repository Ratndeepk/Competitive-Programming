#code
for _ in range(int(input())):
    m,n = map(int,input().split())
    matrix_l = list(map(int,input().split()))
    matrix=[]
    index=0
    for i in range(m):
        s_matrix=[]
        for j in range(n):
            s_matrix.append(matrix_l[index])
            index+=1
        matrix.append(s_matrix)
    row = 0
    col=0
 
    while row<m and col<n:
        for i  in range(col,n):
            print(matrix[row][i],end=" ")
        row+=1
        
        for i in range(row,m):
            print(matrix[i][n-1],end=" ")
        n-=1
        if row<m:
            for i  in range(n-1,col-1,-1):
                print(matrix[m-1][i],end=" ")
            m-=1
        if col<n:
            for i in range(m-1,row-1,-1):
                print(matrix[i][col],end=" ")
            col+=1
        
    print()
