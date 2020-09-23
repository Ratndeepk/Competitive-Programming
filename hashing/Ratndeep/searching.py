def search(a,x):
    if x>=0:
        return has[x][0]==1
    else:
        return has[abs(x)][1]==1


def insert(a,n):
    for i in range(n):
        if a[i]>=0:
            has[a[i]][0]=1
        else:
            has[abs(a[i])][1]=1



array = list(map(int,input().split()))
x = int(input())
n = len(array)
has = [[0 for i in range(2)] for i in range(1000)]
insert(array,n)

print(search(array,x))
