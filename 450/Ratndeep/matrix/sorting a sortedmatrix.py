for _ in range(int(input())):
    n = int(input())
    matrix=[]
    for i in range(n):
        matrix.append(list(map(int,input().split())))
        
    #flaten the n-d matrix
    sol=[]
    for i in matrix:
        sol.extend(i)
    sol.sort()
    print(*sol)