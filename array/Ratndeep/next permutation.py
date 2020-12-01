#https://practice.geeksforgeeks.org/problems/next-permutation/0#
def check(arr,n):
    small=arr[-1]
    for i in range(n-2,-1,-1):
        if arr[i]<small:
            break 
        else:
            small=arr[i]
    
    if i==-1:
        arr.sort()
        return arr 

    

    cur_small=i+1
    
    for k in range(i+2,n):
        if arr[k]<arr[cur_small] and arr[k]>arr[i]:
            cur_small=k

    arr[i],arr[cur_small]=arr[cur_small],arr[i] 
    
    arr[i+1:]=sorted(arr[i+1:])
    return arr

for _ in range(int(input())): 
    n = int(input())
    arr = list(map(int,input().split()))
    print(*check(arr,n))

    