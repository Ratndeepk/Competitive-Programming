from math import ceil, log2

def updatevalueutil(st,ss,se,i,diff,si):
    if i<ss or i>se:
        return
    st[si]=st[si]+diff
    if se!=ss:
        mid=(ss+se)//2
        updatevalueutil(st,ss,mid,i,diff,2*si+1)
        updatevalueutil(st,mid+1,se,i,diff,2*si+2)

def updatevalue(array,st,n,i,new_val):
    diff = new_val-array[i]
    array[i]=new_val

    upadtevalueutil(st,0,n-1,i,diff,0)

def getsumutil(st,ss,se,qs,qe,si):
    if qs<=ss and qe>=se:
        return st[si]
    if se<qs or ss>qe:
        return 0
    mid = (ss+se)//2
    return getsumutil(st,ss,mid,qs,qe,2*si+1)+getsumutil(st,mid+1,se,qs,qe,2*si+2)


def getsum(st,n,qs,qe):
    return getsumutil(st,0,n-1,qs,qe,0)

def constructutil(array,ss,se,st,si):
    if ss==se:
        st[si]=ar[ss]
        return ar[ss]
    mid = (ss+se)//2
    st[si]=constructutil(array,ss,mid,st,2*si+1)+constructutil(array,mid+1,se,st,2*si+2)

    return st[si]


def constructst(array,n):
    x = int(ceil(log2(n)))
    size = 2*int(2**x)-1
    st=[0]*size
    constructutil(array,0,n-1,st,0)
    return st

array=list(map(int,input().split()))
n=len(array)
st = constructst(array,n)

left,right=map(int,input().split())

print(getsum(st,n,left,right))

index,new_value = map(int,input().split())

updatevalue(array,st,n,index,new_value)
