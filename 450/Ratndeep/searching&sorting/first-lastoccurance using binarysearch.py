
def searchfirstBS(arr,start,end,x):
    while start<=end:
        mid=(start+end)//2 
        if arr[mid]==x:
            end=mid-1 
        else:
            start=mid+1 
    return start 

def searchlastBS(arr,start,end,x):
    while start<=end:
        mid=(start+end)//2 
        if arr[mid]==x:
            end=mid-1 
        else:
            start=mid+1 
    return end
    
def search(arr, first, last, x):
    while first <= last:
        mid = (first + last) // 2
        
        if arr[mid] == x:
            first = searchFirst(arr, l, mid, x)
            last = searchLast(arr, mid, r, x)
            return [first, last]
        elif arr[mid] > x:
            last = mid - 1
        else:
            first = mid + 1
    
    return [-1]
for _ in range(int(input())):
    n,x = map(int,input().split())
    
    arr = list(map(int,input().split()))
    
    print(*search(arr,0,n-1,x))