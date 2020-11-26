from heapq import heapify,heappop,heappush
def kthSmallest(arr, l, r, k):
    heapify(arr) 
    for i in range(k): 
        a=heappop(arr)
    return a


arr=list(map(int,input().split()))
k=int(input())
print(kthSmallest(arr,0,len(arr)-1,k))