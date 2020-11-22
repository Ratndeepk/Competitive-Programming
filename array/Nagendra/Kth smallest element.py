#link https://practice.geeksforgeeks.org/problems/kth-smallest-element5635/1#


def kthSmallest(arr, l, r, k):
    '''
    arr : given array
    l : starting index of the array i.e 0
    r : ending index of the array i.e size-1
    k : find kth smallest element and return using this function
    '''
    arr.sort()
    return(arr[k-1])


#{
#  Driver Code Starts
#Initial Template for Python 3
#contributed by RavinderSinghPB
if __name__ == '__main__':
    import random
    t = int(input())
    for tcs in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        print(kthSmallest(arr, 0, n-1, k))

# } Driver Code Ends
