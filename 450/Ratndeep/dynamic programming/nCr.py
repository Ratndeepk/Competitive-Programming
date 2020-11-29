n,r = map(int,input().split())
combinations = [[0 for i in range(n+1)] for i in range(r+1)] 
combinations[0][0]=1 
for i in range(1,n+1):
    combinations[0][i]=1 
combinations[1][0]=1
for i in range(1,n+1):
    combinations[1][i]=i*combinations[1][i-1]  



for i in range(2,r+1):
    for j in range(i,n+1):
        fact = 1 
        combinations[i][j]=combinations[1][j]/(combinations[1][j-i]*combinations[1][i])

for i in combinations:
    print(*i)
print(combinations[r][n])