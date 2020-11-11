import math 
n = int(input())
numbers = list(map(int,input().split()))


matrix = [[0 for i in range(n+1)] for i in range(n+1)]

index=n-1
for i in range(1,n):
    index1=0
    for j in range(1,n):
        matrix[i][j]=matrix[i-1][j-1]+(numbers[index1]*numbers[index])
        index1+=1
    index-=1 
    
sol = matrix[0][n]
print(sol)
index=n-1
for i in range(1,n):
    if sol<matrix[i][index]:
        sol=matrix[i][index]
    print(matrix[i][index])
    index-=1 


for i in matrix:
    print(*i)
print(sol) 


