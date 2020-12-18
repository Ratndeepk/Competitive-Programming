def permutation(n,r):
    arr=[0]*(n+1) 
    arr[0]=1
    for i in range(1,n+1):
        arr[i]=arr[i-1]*i

    return arr[n]//arr[n-r]



n,r = map(int,input().split())
print(permutation(n,r))