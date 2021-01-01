#User function Template for python3
from collections import defaultdict
class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        dic = defaultdict(set)
        
        for i in range(n):
            dic[arr[i]].add(i)
        
        c=0
        for i in range(n):
            if k-arr[i] in dic:
                for j in dic[k-arr[i]]:
                    if j>i:
                        c+=1
        return c


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends