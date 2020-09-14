for _ in range(int(input())):
    n,k = map(int,input().split())
    piles = list(map(int,input().split()))
    piles.sort()
    i,z=0,0
    ans=float("inf")
    while i<n:
        j=n-1
        if i!=0:
            z=sum(piles[:i])
        while i<j:
            if piles[j]-piles[i]>k:
                z+=(piles[j]-piles[i])-k
                j-=1
            else:
                break
            
        ans=min(ans,z)
        i+=1
    print(ans)
