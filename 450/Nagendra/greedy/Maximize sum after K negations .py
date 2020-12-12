#code https://practice.geeksforgeeks.org/problems/maximize-sum-after-k-negations/0

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    arr.sort()
    i=0
    while k>0 and i<n:
        if arr[i]<0:
            arr[i]=-arr[i]
            
            k-=1
        i+=1
    if k%2 !=0:
        arr.sort()
        arr[0]= -arr[0]
    print(sum(arr))
            
        
