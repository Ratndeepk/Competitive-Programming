#link https://practice.geeksforgeeks.org/problems/union-of-two-arrays/0#
from collections import defaultdict
for _ in range(int(input())):

    n, m = map(int, input().split())
    narr = list(map(int, input().split()))
    marr = list(map(int, input().split()))
    ndic = defaultdict(int)
    c = 0
    for i in narr:
        if ndic[i] != 1:
            ndic[i] = 1
            c += 1
    for j in marr:
        if ndic[j] != 1:
            ndic[j] = 1
            c += 1
    print(c)
