#link https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays5135/1#
#incomplete

class Solution:
    def merge(self, arr1, arr2, n, m):
        # code here
        i = 0
        j = 0
        while i < n:
            if arr1[i] > arr2[i]:
                arr1pop = arr1.pop()
                arr2pop = arr2.pop(j)
                arr1.insert(i, arr2pop)
                arr2.insert(0, arr1pop)
                j += 1


#{
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        n, m = map(int, (input().strip().split()))
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.merge(arr1, arr2, n, m)
        for x in arr1:
            print(x, end=" ")
        for x in arr2:
            print(x, end=" ")
        print()
        tc = tc-1
# } Driver Code Ends
