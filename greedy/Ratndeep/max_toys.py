for _ in range(int(input())):
    n,k = map(int,input().split())
    toys = list(map(int,input().split()))
    c=0
    toys.sort()
    i=0
    while i<n:
        if k-toys[i]>=0:
            k-=toys[i]
            i+=1
            c+=1
        else:
            break
    print(c)
