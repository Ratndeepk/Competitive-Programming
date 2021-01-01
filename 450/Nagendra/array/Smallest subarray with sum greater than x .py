#code https://practice.geeksforgeeks.org/problems/smallest-subarray-with-sum-greater-than-x/0

for _ in range(int(input())):
    n, x = map(int, input().split())
    arr = list(map(int,input().split()))
    
    sum=0
    inti=0
    min=float('inf')
    c=0
    for i in range(n):
        sum+=arr[i]
        c+=1
        while sum>x:
            if min>c:
                min=c
            c-=1
            sum-=arr[inti]
            inti+=1
    print(min)
            
            