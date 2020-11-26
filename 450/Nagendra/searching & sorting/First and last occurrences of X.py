#code https://practice.geeksforgeeks.org/problems/first-and-last-occurrences-of-x/0

# Binary Search

for _ in range(int(input())):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    lef, rig = 0, n-1
    f = 0
    while lef <= rig:
        m = lef+(rig-lef)//2
        if arr[m] == x:
            ind = m
            f = 1
            break
        elif arr[m] < x:
            lef = m+1
        else:
            rig = m-1
    if f == 0:
        print(-1)
    else:
        temp = ind
        while arr[temp] == x and temp >= 0:
            temp -= 1
        print(temp+1, end=' ')
        temp = ind
        while arr[temp] == x and temp < n:
            temp += 1
        print(temp-1)



#Linear search
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
