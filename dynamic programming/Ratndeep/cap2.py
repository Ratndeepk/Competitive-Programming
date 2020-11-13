n = int(input())
numbers = list(map(int,input().split()))


matrix = [[0 for i in range(n)] for i in range(n)]


for i in range(n):
    for j in range(i+1,n):
        if i!=j:
            matrix[i][j]=numbers[i]*numbers[j]


sol = float("-inf")
for i in range(n-1):
    index=i
    cur_sol=0
    for j in range(n-1,-1,-1):
        if cur_sol+matrix[index][j]>cur_sol:
            cur_sol+=matrix[index][j]
        index+=1 
        if index>=n:
            break
    if sol<cur_sol:
        sol=cur_sol
for i in range(n-1):
    index=i
    cur_sol=0
    for j in range(n-2,-1,-1):
        if cur_sol+matrix[index][j]>cur_sol:
            cur_sol+=matrix[index][j]
        index+=1 
        if index>=n:
            break
    if sol<cur_sol:
        sol=cur_sol
cur_sol=[]
for i in matrix:
    cur_sol.extend(i)
print(max(max(cur_sol),sol))