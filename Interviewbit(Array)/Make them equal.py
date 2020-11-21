import math
from math import log2
from heapq import heappush,heappop,heapify
def solve(a):
    t=[]
    new_a=a[:]
    heapify(new_a)
    mi=heappop(new_a)
    count=0
    for i in range(len(a)):
        
            
        if a[i]!=mi:
            count+=round(log2(a[i]//mi))
            print(a[i],"=",count)
            t.append(count)
    
    return count,t
a = list(map(int,input().split()))
count,t=solve(a)
print("count1",count)

count=0
print()
j=[]

for i in range(len(a)):
    x=a[i]
    if a[i]!=min(a):
        while(x>min(a)):
            x//=2
            count+=1
        print(a[i],"=",count)
        j.append(count)
print("count2",count)
for i in range(len(a)-1):
    print(j[i]-t[i],end=" ")
