#link https://practice.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one/0#

#code
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    b = arr.pop()
    if n > 1:
        print(b, *arr)
    else:
        print(b)
