#2 find minimum and mzximum element in array

#! By Linear Search
def linear(arr):
    return (min(arr),max(arr))

#by pair compresion
def paircmp(arr,n):
    if n %2:
        mn,mx = arr[0],arr[0]
    else:
        mn,mx = min(arr[0],arr[1]),max(arr[0],arr[1])
    i = 1 if n%2 else 2
    while(i < n-1):
        if arr[i] < arr[i + 1]:
            mx = max(mx,arr[i + 1])
            mn = min(mn,arr[i])
        else:
            mx = max(mx,arr[i])
            mn = min(mn,arr[i+1])
        i += 2
    return (mn,mx)
        
arr = [100, 15, 45, 1, 320, 400]
print("Linear Search :",linear(arr))
print("Pair Comperision:",paircmp(arr,len(arr)))