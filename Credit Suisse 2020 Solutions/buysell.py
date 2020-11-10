n = int(input())
a = list(map(int,input().split()))



i = 0
money=0
while i<n-1:
    while i<n-1 and a[i]>=a[i+1]:
        i+=1
    if i==n-1:
        break
    buy_at=i
    i+=1
    while i<n and a[i]>=a[i-1]:
        i+=1
    sell_at=i-1
    money+=a[sell_at]-a[buy_at]

print(money)