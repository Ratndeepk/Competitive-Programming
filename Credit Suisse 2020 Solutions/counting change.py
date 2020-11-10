def solution(S,m,n):
    table = [[0 for x in range(m)] for x in range(n+1)]

    for i in range(m):
        table[0][i]=1
    
    for i in range(1,n+1):
        for j in range(m):
            if i-S[j]>=0:
                x = table[i-S[j]][j] 
            else:
                x=0 

            if j>=1:
                y=table[i][j-1]
            else:
                y=0 

            table[i][j]=x+y 

    return table[n][m-1]


x,n = map(int,input().split())
coins = list(map(int,input().split()))

print(solution(coins,n,x))