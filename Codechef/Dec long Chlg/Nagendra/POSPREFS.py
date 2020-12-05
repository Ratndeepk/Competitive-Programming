for _ in range(int(input())):
    n, k = map(int, input().split())

    diff = n-k
    lis = [i for i in range(1,n+1)]
    i=0
    while diff >0 and i<n-1:
        # print('..............')
        lis[i]= -lis[i]
        # print(sum(lis[:i+2]), lis)
        if sum(lis[:i+2])<=0:
            lis[i] = -lis[i]
            diff+=1
        i+=1
        diff-=1
        # print(lis)
    i=n-1
    while diff >0 and i>=0:
        if lis[i]>0:
            lis[i] = -lis[i]
            diff-=1
        i-=1
        
    print(*lis)