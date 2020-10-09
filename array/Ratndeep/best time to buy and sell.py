def check(i,a):
    j=i+1
    print(i,j)
    while a[j]>a[i]:
        j+=1
    print(i,j)
    return a[j-1]-a[i],j
prices=[7,1,5,3,6,4]
n = len(prices)
max_profit = 0
i=0
while i<n:
    j=i+1
 
    k=i
    while j<n and prices[j]>prices[k]:
        j+=1
        k+=1
    
    profit= prices[j-1]-prices[i]
    i=j
    max_profit+=profit
print(max_profit)
