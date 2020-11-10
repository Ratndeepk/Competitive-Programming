

# n trades m tries
n,m = map(int,input().split())

#profit probability
P = list(map(float,input().split()))

# profit chances
profit = list(map(float,input().split()))

#loss chances
loss = list(map(float,input().split()))

check_all  = [0]*n 

for i in range(n):
    check_all[i] = (P[i]*profit[i])-((1-P[i])*loss[i])

check_all.sort(reverse=True) 

answer=0
for i in range(m):
    if check_all[i]<0:
        break 
    answer+=check_all[i] 
if "." in str(answer)[-2]:
    answer=str(answer)+"0"
    print(answer)
else:
    print(round(answer,2))