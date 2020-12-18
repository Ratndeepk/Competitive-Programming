#code https://practice.geeksforgeeks.org/problems/coin-piles/0

for _ in range(int(input())):
    n, k = map(int, input().split())
    pile = list(map(int, input().split()))
    
    minn = 0
    pile.sort()
    
    for i in range(1,n):
        if pile[i]>pile[0]+k:
            minn+=pile[i]-(pile[0]+k)
    # print(minn)       
    for i in range(n):
        temp=sum(pile[:(i+1)])
        for j  in range(i+1,n):
            if pile[j]>pile[i+1]+k:
                temp+=pile[j]-(pile[i+1]+k)
        if temp<minn:
            minn=temp
    print(minn)
            
            