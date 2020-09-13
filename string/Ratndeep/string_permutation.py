def curse(a,l,r,c):
    if l==r:
        c+=1
    for i in range(len(a)):
        a[l],a[i]=a[i],a[l]
        curse(a,l+1,r,c)
        a[l],a[i]=a[i],a[l]
    return c
    



a = input().split()
c=0
print(curse(a,0,len(a)-1,c))
