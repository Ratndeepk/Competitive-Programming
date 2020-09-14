for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c=[]
    for i in range(n):
        c.append([a[i],b[i]])
        
    c.sort(key=lambda x:x[1])
    t=1
    i=0
    j=1
    #print(c)
    while j<n:
        if c[i][1]<=c[j][0]:
            t+=1
            i=j
            j+=1
        else:
            j+=1
        
    print(t)
