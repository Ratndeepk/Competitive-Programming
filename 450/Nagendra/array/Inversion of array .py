#User https://practice.geeksforgeeks.org/problems/inversion-of-array-1587115620/1
#incomplete
from collections import defaultdict
def inversionCount(a,n):
    # Your Code Here
    b=a[:]
    b.sort()
    if a==b:
        return 0
    
    dic=defaultdict(set)
    
    for i in range(n):
        dic[a[i]].add(i)
    c=0
    for i in range(n):
        
        if dic[b[i]] and i not in dic[b[i]]:
            c+=1
            remove = dic[b[i]].pop()
            # print(a, dic, remove)
            remove2 = dic[a[i]].pop()
            a[i], a[remove] = a[remove], a[i]
            dic[a[remove]].add(remove)
            # print(a, dic,remove2)

            
    return c
print(inversionCount([2,2,2], 3))