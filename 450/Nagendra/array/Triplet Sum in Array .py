#code https://practice.geeksforgeeks.org/problems/triplet-sum-in-array/0
from collections import defaultdict
for _ in range(int(input())):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    dic = defaultdict(int)
    for i in arr:
        dic[i]+=1
    flag=0
    for i in range(n):
        for j in range(i+1,n):
            third = x-arr[i]-arr[j]
            if dic[third]>0:
                if (third==arr[i] and dic[arr[i]]==1) or (third==arr[j] and dic[arr[i]]==1):
                    continue
                if third==arr[i] and arr[i]==arr[j] and dic[arr[i]]==2:
                    continue
                flag=1
                break
        if flag==1:
            break
    if flag:
        print(1)
    else:
        print(0)