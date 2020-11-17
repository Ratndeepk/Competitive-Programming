#7 Largest sum subarray
def maxSubArraySum(a,size):
    gs,ls,n = float('-inf'),0,len(a)
    for i in range(n):
        ls += a[i]
        gs = max(ls,gs)
        if ls <0:
            ls = 0
    return gs if gs > -1 else -1

arr = [1,2,3,-2,5]
N = len(arr)
maxSubArraySum(arr,N)