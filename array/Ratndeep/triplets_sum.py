for i in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    count=0
    max_a=l[-1]
    c = set(l)
    for i in range(n-2):
        for j in range(i+1,n-1):
            s = l[i]+l[j]
            if s>max_a:
                break
            elif s in c:
                count+=1
    if count!=0:
        print(count)
    else:
        print(-1)
    
    
    
 
   
#ratndeep
# O(n2)
# https://practice.geeksforgeeks.org/problems/count-the-triplets/0
