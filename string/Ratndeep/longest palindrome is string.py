#code
for _ in range(int(input())):
    a = input()
    x=""
    y=""
    i=0
    j=len(a)-1
    while i<j:
        m=i
        n=j
        if a[i]==a[j]:
            while m<n:
                print(m,n)
                if a[m]==a[n]:
                    x+=a[m]
                    y+=a[n]
                    m+=1
                    n-=1
                else:
                    i=m+1
                    j=n-1
                    x=""
                    y=""
                    break
            print(x,y)
        else:
            i+=1
            j-=1
    if len(x+y[::-1])>1:
        print(x+y[::-1])
    else:
        print(a[0])
