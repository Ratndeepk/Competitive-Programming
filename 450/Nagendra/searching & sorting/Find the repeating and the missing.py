#link https://practice.geeksforgeeks.org/problems/find-missing-and-repeating2512/1#
from collections import defaultdict


class Solution:
    def findTwoElement(self, arr, n):
        # code here
        dic = defaultdict(int)
        lis = []
        for i in arr:
            dic[i] += 1
            if dic[i] == 2:
                lis.append(i)

        for i in range(1, n+1):
            if dic[i] <= 0:
                lis.append(i)
                break
        return lis


#{
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc = tc-1
# } Driver Code Ends
