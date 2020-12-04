d1, v1, d2, v2, p = map(int, input().split())
summ=0
c=0
if d1!=1 or d2 !=1:
    c+=min(d1,d2)-1
while summ<p:
    if d1<d2:
        summ+=v1
        d1+=1
    elif d1>d2:
        summ+=v2
        d2+=1
    else:
        summ = summ+v1+v2
    c+=1
print(c)