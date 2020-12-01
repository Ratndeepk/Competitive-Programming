arr = list(map(int,input().split()))
n = len(arr)

matrix = [[0 for i in range(n+1)] for i in range(n+1)] 


for i in range(1,n):
    for j in range(n):
        if i!=j:
            matrix[i][j] = sum(arr[:i])-sum(arr[i:])


for i in matrix:
    print(*i)