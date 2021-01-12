def howmany(n,k,box):
    suffix = [0]*n 
    for i in range(n-1,-1,-1):
        if i==n-1:
            suffix[i]=box[i] 
        else:
            suffix[i]=box[i]+suffix[i+1] 

    matrix = [[float("inf") for i in range(k+1) ] for i in range(n)] 

    for i in range(k,0,-1):
        if box[n-1]>=i:
            matrix[n-1][i]=box[n-1]

    for i in range(n-2,-1,-1):
        for j in range(k,0,-1):
            if box[i]>=k:
                matrix[i][j]=box[i] 
                continue 
            matrix[i][j] = min(matrix[i+1][j],matrix[i+1][j-box[i]]+box[i]) 
    
    for i in range(n-1,-1,-1):
        if suffix[i]-matrix[i][k]>=k:
            return n-i 
             
    return -1

for _ in range(int(input())):
    n,h = map(int,input().split())
    boxes = list(map(int,input().split()))
    boxes.sort()
    print(howmany(n,h,boxes))