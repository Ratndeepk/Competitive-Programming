t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.insert(0,l.pop())
    print(*l,sep=' ')