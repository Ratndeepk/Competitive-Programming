a=list(map(int,input().split()))
n=len(a)-1
i=0
while i<n:
    a[i],a[n]=a[n],a[i]
    i +=1
    n -=1
print(a)


