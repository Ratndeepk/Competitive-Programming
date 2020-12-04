#link https://practice.geeksforgeeks.org/problems/count-squares3649/1
import math


class Solution:
    def countSquares(self, N):
        # code here
        sqr = math.floor(math.sqrt(N))
        if sqr**2 == N:
            return int(sqr)-1
        else:
            return int(sqr)


#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.countSquares(N))
# } Driver Code Ends
