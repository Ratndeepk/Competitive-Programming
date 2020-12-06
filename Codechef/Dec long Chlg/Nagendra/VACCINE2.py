import math
for _ in range(int(input())):
    n, d = map(int, input().split())
    arr = tuple(map(int,input().split()))
    risk = []
    helth = []
    minn=0
    for i in arr:
        if i>=80 or i<=9:
            risk.append(i)
        else:
            helth.append(i)
    minn = math.ceil(len(risk)/d) + math.ceil(len(helth)/d)
    print(minn)