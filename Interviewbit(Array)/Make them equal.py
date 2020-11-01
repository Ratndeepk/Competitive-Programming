def solve(a):
    mi = min(a)
    count=0
    for i in range(len(a)):
        count+=math.floor(log2(a[i]//mi))
    return count
a = list(map(int,input().split()))
print(solve(a))
