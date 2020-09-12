for i in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    i=n-1
    c=0
    print(l)
    while i>1:
        j=0
        k=i-1
        while j<k:
            if l[j]+l[k]>l[i]:
                k-=1
            elif l[j]+l[k]<l[i]:
                j+=1
            else:
                c+=1
                j+=1
                k-=1
        i-=1
                
    if c!=0:
        print(c)
    else:
        print(-1)
    
    
    
 
   
