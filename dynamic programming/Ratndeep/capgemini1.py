import math 
n = int(input())
numbers = list(map(int,input().split()))


matrix = [[0 for i in range(n)] for i in range(n)]


for i in range(n):
    for j in range(n):
        if i!=j:
            matrix[i][j]=numbers[i]*numbers[j]


sol = float("-inf")
for i in range(n-1):
    index=i
    cur_sol=0
    for j in range(n-1,-1,-1):
        #print(matrix[index][j])
        cur_sol+=matrix[index][j]
        index+=1 

        if index>=math.ceil(n/2):
            break
    if sol<cur_sol:
        sol=cur_sol

"""
for i in range(n-1):
    index=0
    cur_sol=0
    for j in range(n-2,-1,-1):
        print(matrix[index][j])
        cur_sol+=matrix[index][j]
        index+=1 

        if index>=((n-1)/2):
            break
    if sol<cur_sol:
        sol=cur_sol
"""
flag=0
for j in range(n-2,0,-1):
    index=j 
    cur_sol=0 
    
    
        
    for i in range((n//2)-flag):
        #print(i,index)
        #print(matrix[i][index])
        cur_sol+=matrix[i][index]
        index-=1
    flag+=1
    if sol<cur_sol:
        sol=cur_sol


print(sol)