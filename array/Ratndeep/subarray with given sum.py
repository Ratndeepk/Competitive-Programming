#code
def subary(l,n,k):
    cur_sum=l[0]
    j=0
    i=1
    while i<n:
        
        cur_sum+=l[i]
        i+=1
        while cur_sum>k:
            cur_sum-=l[j]
            j+=1
        
        if cur_sum==k:
            return [j+1,i]
    return -1
for _ in range(int(input())):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    
    if subary(l,n,k)!=-1:
        print(*subary(l,n,k))
    else:
        print(-1)
