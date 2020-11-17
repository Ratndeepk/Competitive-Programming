#3 Find Kth smallest element in O(N)
n = 6
arr = [7,10,4,3,20,15]
k = 1

def quicksort(arr,l,r,k):
    if l<=r:
        pos = partition(arr,l,r)
        if pos+1 == k:
            return arr[pos]
        
        if pos+1 > k:
            return quicksort(arr,l,pos-1,k)
        else:
            return quicksort(arr,pos + 1,r,k)
        
def partition(arr,l,r):
    pivot = arr[l]
    i,j = l,r
    while(i < j):
        while(i < r and arr[i]<=pivot):
            i += 1
        while(0<=j and arr[j] > pivot):
            j -= 1
        if i < j:
            arr[i],arr[j] = arr[j],arr[i]
    arr[l],arr[j]  = arr[j],arr[l]
    return j

quicksort(arr,0,n-1,k)