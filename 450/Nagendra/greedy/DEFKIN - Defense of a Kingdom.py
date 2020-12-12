https://www.spoj.com/problems/DEFKIN/
#incomplete
for _ in range(int(input())):
    w, h, n = map(int, input().split())
    cord = []
    for i in range(n):
        cord.append(list(map(int, input().split())))
    