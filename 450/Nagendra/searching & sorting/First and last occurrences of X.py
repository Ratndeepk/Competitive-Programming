#code https://practice.geeksforgeeks.org/problems/first-and-last-occurrences-of-x/0

for _ in range(int(input())):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    f = 0
    ind = -1
    for i in range(n):
        if f == 0 and arr[i] == x:
            print(i, end=' ')
            f = 1
            ind = i
        elif arr[i] == x:
            ind = i
    if ind == -1:
        print(-1)
    else:
        print(ind)
