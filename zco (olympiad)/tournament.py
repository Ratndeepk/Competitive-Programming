from itertools import combinations
strength = list(map(int,input().split()))
money=0
n = len(strength)
l = [str(i) for i in range(len(strength))]
comb = list(combinations("".join(l),2))
print(comb)
for i,j in comb:
    print(i,j)
    money+=abs(strength[int(i)]-strength[int(j)])
print(money)
