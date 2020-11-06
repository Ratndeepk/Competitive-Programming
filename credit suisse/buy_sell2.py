

n,d = map(int,input().split())
stock = list(map(int,input().split()))
for _ in range(d):
    x = int(input())
    mini=float("inf") 
    flag=0
    sell = float("inf")
    buy=float("-inf")
    for i in range(n-1):
        target = x+stock[i]
        if target in stock[i+1:]:
            j=i+1
            while j<n:
                if target==stock[j]:
                    flag=1
                    break
                j+=1 
            if stock[i] in stock[i+1:j]:
                k = i+1
                while k<j:
                    if stock[k]==stock[i]:
                        i=k
                        break 
                    k+=1

            if sell>i and mini>j-i:
                buy=i  
                sell=j 
                mini=j-i 
        else:
            continue 

    if flag==0:
        print(-1)
    else:
        print(buy+1,sell+1)

