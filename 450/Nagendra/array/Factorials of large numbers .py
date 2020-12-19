#code https://practice.geeksforgeeks.org/problems/factorials-of-large-numbers/0

for _ in range(int(input())):
    n = int(input())
    fac=1
    
    while n>0:
        fac*=n
        n=n-1
    print(fac)
