from itertools import combinations
n,k = map(int,input().split())
variation = input().split()
count=0
comb = list(combinations("".join(variation),2))
print(comb)
for i,j in comb:
    if abs(int(i)-int(j))>=k:
        count+=1
print(count)
"""
for i in range(n):
    for j in range(i+1,n):
        if abs(variation[i]-variation[j])>=k:
            count+=1
print(count)
"""
