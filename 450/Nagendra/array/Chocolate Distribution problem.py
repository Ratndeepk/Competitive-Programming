#code https://practice.geeksforgeeks.org/problems/chocolate-distribution-problem/0

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    
    arr.sort()
    min=float('inf')
    
    for i in range(n-m+1):
        if arr[i+m-1]-arr[i]<min:
            min=arr[i+m-1]-arr[i]
    print(min)