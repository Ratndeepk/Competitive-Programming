#code https://practice.geeksforgeeks.org/problems/swap-and-maximize/0

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    max = 0
    
    for i in range(n//2):
        max -= 2*arr[i]
        max += 2*arr[n-i-1]
        
    
    print(max)