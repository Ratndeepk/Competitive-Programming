n = int(input())
strength = list(map(int,input().split()))
money=0

for i in range(n-1):
    for j in range(i+1,n):
        money+=abs(strength[i]-strength[j])
print(money)
