def search_in_rotated(arr,n,x):
    
    low=0
    high=n-1 
    while low<=high:
        mid=(low+high)//2 
        if arr[mid]==x:
            return mid
        if arr[low]<=arr[mid]:
            if x>arr[mid] or x<arr[low]:
                low=mid+1 
            else:
                high=mid-1 
        else:
            if x<arr[mid] or x>arr[high]:
                high=mid-1
            else:
                low=mid+1 
            

    return -1
n = int(input())
arr = list(map(int,input().split()))
x=int(input())
print(search_in_rotated(arr,n,x))