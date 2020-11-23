for _ in range(int(input())):
    row,col=map(int,input().split())
    in_matrix = list(map(int,input().split()))
    index=0
    matrix=[]
    for i in range(row):
        temp_row=[]
        for j in range(col):
            temp_row.append(in_matrix[index])
            index+=1
        matrix.append(temp_row)
        
    r,c=0,0
    while r<row and c<col:
        for i in range(c,col):
            print(matrix[r][i],end=" ")
        r+=1
        for i in range(r,row):
            print(matrix[i][col-1],end=" ")
        col-=1
        if r<row:
            for i in range(col-1,c-1,-1):
                print(matrix[row-1][i],end=" ")
            row-=1
        if c<col:
            for i in range(row-1,r-1,-1):
                print(matrix[i][c],end=" ")
            c+=1
    print()