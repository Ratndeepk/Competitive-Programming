# Recursive Approach

def reverse(a,start,end):
    if start>=end:
        return
    a[start],a[end]=a[end],a[start]
    reverse(a,start+1,end-1)
a=list(map(int,input().split()))
end=len(a)-1
reverse(a,0,end)
print(a)
