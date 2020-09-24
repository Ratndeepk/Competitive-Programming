#insertion sort

arrray = list(map(int,input().split()))
n = len(array)

for i in range(1,n):
    key = arrray[i]
    j=i-1
    while j>=0 and key<arrray[j]:
        arrray[j+1]=arrray[j]
        j-=1
    arrray[j+1]=key


print(*arrray)
