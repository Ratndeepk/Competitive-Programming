#code https://practice.geeksforgeeks.org/problems/rearrange-characters/0
import math
for _ in range(int(input())):
    stg = list(input())
    limit = math.ceil(len(stg)/2)
    f=0
    for i in set(stg):
        if stg.count(i)>limit:
            f=1
            break
    
    if f:
        print(0)
    else:
        print(1)