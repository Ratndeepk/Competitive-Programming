for _ in range(int(input())):
    a,b = map(int, input().split())
    aeven = a//2
    aodd= a-aeven
    beven = b//2
    bodd = b-beven
    print(aeven*beven + aodd*bodd) 