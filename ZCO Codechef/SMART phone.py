n = int(input())
a=[]
for i in range(n):
    a.append(int(input()))
a.sort()
k=n
for i in range(n):
    a[i]=a[i]*k 
    k-=1 
print(max(a))
