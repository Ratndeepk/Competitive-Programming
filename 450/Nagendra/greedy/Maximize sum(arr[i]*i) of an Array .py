#code https://practice.geeksforgeeks.org/problems/maximize-arrii-of-an-array/0

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    
    summ =0 
    
    for i in range(n):
        summ=(summ+i*arr[i])%(10**9+7)
    print(summ)