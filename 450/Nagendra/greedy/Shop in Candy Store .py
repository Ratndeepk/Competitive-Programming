#coden https://practice.geeksforgeeks.org/problems/shop-in-candy-store/0

for _ in range(int(input())):
    n, k = map(int, input().split())
    price = list(map(int, input().split()))
    
    price.sort()
    minn = 0
    i, j = 0,n-1
    
    while i<=j:
        minn+=price[i] 
        j-=k
        i+=1
    
    price.sort(reverse=True)
    maxx=0
    i, j = 0,n-1
    
    while i<=j:
        maxx+=price[i] 
        j-=k
        i+=1
    print(minn,maxx)