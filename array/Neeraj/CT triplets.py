for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    ct=0
    m=arr[-1]
    c=set(arr)
    for i in range(n-2):
        for j in range(i+1,n-1):
            summ=arr[i]+arr[j]
            if summ>m:
                break
            elif s in c:
                ct+=1
    if ct!=0:
        print(count)
    else:
        print(-1)
                
